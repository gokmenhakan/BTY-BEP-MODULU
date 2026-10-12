/**
 * T.C. MİLLÎ EĞİTİM BAKANLIĞI - BEP DİNAMİK VERİTABANI MODÜLÜ
 * Google Apps Script Sunucu Kodu (Code.gs)
 * 
 * Bu betik:
 * 1. Web arayüzünü (index.html) yayınlar.
 * 2. Bağlı Google E-Tablo'dan (Spreadsheet) ders, modül, UDA ve KDA verilerini dinamik çeker.
 * 3. Hızlı çalışması ve kota tasarrufu için Google CacheService (Önbellek) kullanır.
 * 4. Yeni ders/müfredat eklendiğinde kod değişikliğine gerek kalmadan anında yansıtır.
 */

// Varsayılan / Yedek E-Tablo ID'si (Buraya kendi oluşturacağınız Google E-Tablo ID'nizi yazabilirsiniz)
var DEFAULT_SPREADSHEET_ID = "";

/**
 * Web uygulaması GET isteklerini karşılar
 */
function doGet(e) {
  var template = HtmlService.createTemplateFromFile('index');
  try {
    template.scriptUrl = ScriptApp.getService().getUrl();
  } catch (err) {
    template.scriptUrl = "";
  }
  
  return template.evaluate()
    .setTitle('Dinamik BEP Modülü (Google E-Tablolar Destekli)')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

/**
 * Google E-Tablo ID'sini bulur (Script Properties, Aktif Tablo veya Varsayılan)
 */
function getTargetSpreadsheetId() {
  var props = PropertiesService.getScriptProperties();
  var savedId = props.getProperty('SPREADSHEET_ID');
  if (savedId && savedId.trim() !== '') {
    return savedId.trim();
  }
  
  // Eğer container-bound script ise (yani E-Tablo içinden Araçlar > Apps Script ile açıldıysa)
  try {
    var activeSheet = SpreadsheetApp.getActiveSpreadsheet();
    if (activeSheet) {
      return activeSheet.getId();
    }
  } catch (e) {
    // Bağımsız (standalone) script modunda çalışıyor olabilir
  }
  
  return DEFAULT_SPREADSHEET_ID;
}

/**
 * Kullanıcının E-Tablo ID'sini kaydetmesini sağlar
 */
function saveSpreadsheetId(sheetId) {
  if (!sheetId) return { success: false, message: "Geçersiz E-Tablo ID'si!" };
  
  // Eğer tam URL girildiyse içinden ID'yi ayıkla
  var extractedId = extractSheetIdFromUrl(sheetId);
  
  try {
    // Tabloya erişimi test et
    var ss = SpreadsheetApp.openById(extractedId);
    PropertiesService.getScriptProperties().setProperty('SPREADSHEET_ID', extractedId);
    clearBepCache(); // Eski önbelleği temizle
    return { 
      success: true, 
      message: "E-Tablo başarıyla bağlandı: " + ss.getName(),
      sheetName: ss.getName(),
      id: extractedId
    };
  } catch (err) {
    return { success: false, message: "E-Tablo açılamadı! Lütfen paylaşım izinlerini veya ID'yi kontrol ediniz. Hata: " + err.message };
  }
}

/**
 * URL'den Spreadsheet ID'sini ayıklar
 */
function extractSheetIdFromUrl(urlOrId) {
  if (!urlOrId) return "";
  var trimmed = urlOrId.trim();
  var match = trimmed.match(/\/spreadsheets\/d\/([a-zA-Z0-9-_]+)/);
  if (match && match[1]) {
    return match[1];
  }
  return trimmed;
}

/**
 * Önbelleği (Cache) temizler - Yeni kazanımlar eklendiğinde hemen güncellenmesi için
 */
function clearBepCache() {
  var cache = CacheService.getScriptCache();
  cache.remove("BEP_DATA_TREE");
  cache.remove("BEP_DATA_META");
  return { success: true, message: "Önbellek temizlendi, yeni veriler E-Tablo'dan okunacak." };
}

/**
 * Google E-Tablo'dan tüm BEP verilerini okur, hiyerarşik yapıya çevirir ve döner.
 * CacheService ile 30 dakika hafızada tutarak hızlı açılmasını sağlar.
 */
function getBepDataFromSheet(forceRefresh) {
  var cache = CacheService.getScriptCache();
  
  if (!forceRefresh) {
    var cachedTree = cache.get("BEP_DATA_TREE");
    var cachedMeta = cache.get("BEP_DATA_META");
    if (cachedTree && cachedMeta) {
      try {
        return {
          success: true,
          fromCache: true,
          tree: JSON.parse(cachedTree),
          meta: JSON.parse(cachedMeta)
        };
      } catch (e) {
        // Cache parse hatası olursa yeniden okumaya devam et
      }
    }
  }
  
  var sheetId = getTargetSpreadsheetId();
  if (!sheetId) {
    return {
      success: false,
      isConfigured: false,
      message: "Henüz bir Google E-Tablo bağlanmadı. Lütfen Ayarlar bölümünden E-Tablo bağlantısını yapınız."
    };
  }
  
  try {
    var ss = SpreadsheetApp.openById(sheetId);
    var sheet = ss.getSheetByName("BEP_HAVUZU") || ss.getSheets()[0];
    
    var data = sheet.getDataRange().getValues();
    if (!data || data.length < 2) {
      return {
        success: false,
        message: "E-Tablo boş veya başlık satırı dışında veri içermiyor!"
      };
    }
    
    // Başlık satırını oku
    var headers = data[0].map(function(h) { return h.toString().trim(); });
    
    // Sütun indekslerini bul
    var colMap = {};
    headers.forEach(function(h, idx) {
      colMap[h.toUpperCase()] = idx;
    });
    
    // Gerekli kolonları tespit et (esnek isim eşleştirme)
    var idxMufredat = findColIndex(colMap, ['MUFREDAT_TURU', 'MÜFREDAT_TÜRÜ', 'MUFREDAT', 'PROGRAM']);
    var idxDers = findColIndex(colMap, ['DERS_ADI', 'DERS', 'DERS ADI']);
    var idxSinif = findColIndex(colMap, ['SINIF_DUZEYI', 'SINIF', 'DÜZEY']);
    var idxModul = findColIndex(colMap, ['MODUL_TEMA', 'MODÜL_TEMA', 'MODUL', 'TEMA', 'OGRENME_ALANI']);
    var idxUnite = findColIndex(colMap, ['UNITE_KONU', 'ÜNİTE_KONU', 'UNITE', 'KONU']);
    var idxUdaKod = findColIndex(colMap, ['UDA_KODU', 'UDA_KOD', 'KOD', 'CIKTI_KODU']);
    var idxUdaMetin = findColIndex(colMap, ['UDA_METNI', 'UDA_METNİ', 'UDA', 'OGRENME_CIKTISI']);
    var idxBepUda = findColIndex(colMap, ['BEP_UDA_METNI', 'BEP_UDA', 'BEP_UYARLAMASI']);
    var idxKdaKod = findColIndex(colMap, ['KDA_KODU', 'KDA_KOD', 'SUREC_KODU']);
    var idxKdaMetin = findColIndex(colMap, ['KDA_METNI', 'KDA_METNİ', 'KDA', 'SUREC_BILESENI', 'KAZANIM']);
    var idxKdaTipi = findColIndex(colMap, ['KDA_TIPI', 'KDA_TİPİ', 'KAZANIM_TIPI', 'DURUM']);
    var idxOlcut = findColIndex(colMap, ['ONERILEN_OLCUT', 'ÖNERİLEN_ÖLÇÜT', 'OLCUT', 'ÖLÇÜT']);
    var idxYontem = findColIndex(colMap, ['ONERILEN_YONTEMLER', 'YONTEM', 'YÖNTEMLER']);
    var idxMateryal = findColIndex(colMap, ['ONERILEN_MATERYALLER', 'MATERYAL', 'MATERYALLER']);
    var idxAktif = findColIndex(colMap, ['AKTIF_MI', 'AKTİF_Mİ', 'AKTIF', 'DURUM_AKTIF']);
    
    // Ağaç (Hierarchical Tree) Yapısı:
    // tree[mufredat][ders][modul] = [ { uda_kodu, uda_metni, bep_uda_metni, unite, kda_listesi: [...] } ]
    var tree = {};
    var dersListesi = [];
    var mufredatListesi = [];
    var totalRecords = 0;
    
    for (var r = 1; r < data.length; r++) {
      var row = data[r];
      
      // Aktiflik kontrolü (Eğer aktif kolonu varsa ve 'HAYIR' veya 'PASIF' ise atla)
      if (idxAktif !== -1) {
        var aktifVal = (row[idxAktif] || '').toString().trim().toUpperCase();
        if (aktifVal === 'HAYIR' || aktifVal === 'PASİF' || aktifVal === 'FALSE' || aktifVal === '0') {
          continue;
        }
      }
      
      var mufredat = (idxMufredat !== -1 ? row[idxMufredat] : 'TYMM') || 'TYMM';
      var ders = (idxDers !== -1 ? row[idxDers] : 'Bilişim Teknolojileri ve Yazılım') || 'Genel Ders';
      var modul = (idxModul !== -1 ? row[idxModul] : 'Genel Modül') || 'Genel Modül';
      var unite = idxUnite !== -1 ? (row[idxUnite] || '') : '';
      var udaKod = idxUdaKod !== -1 ? (row[idxUdaKod] || '') : '';
      var udaMetin = idxUdaMetin !== -1 ? (row[idxUdaMetin] || '') : '';
      var bepUda = idxBepUda !== -1 ? (row[idxBepUda] || udaMetin) : udaMetin;
      var kdaKod = idxKdaKod !== -1 ? (row[idxKdaKod] || '') : '';
      var kdaMetin = idxKdaMetin !== -1 ? (row[idxKdaMetin] || '') : '';
      var kdaTipi = idxKdaTipi !== -1 ? (row[idxKdaTipi] || 'MEB_Resmi') : 'MEB_Resmi';
      var olcut = idxOlcut !== -1 ? (row[idxOlcut] || '%70 Başarı ile') : '%70 Başarı ile';
      var yontem = idxYontem !== -1 ? (row[idxYontem] || '') : '';
      var materyal = idxMateryal !== -1 ? (row[idxMateryal] || '') : '';
      
      // Boş satırları atla
      if (!kdaMetin && !udaMetin) continue;
      
      // Ağaç dallarını oluştur
      if (!tree[mufredat]) tree[mufredat] = {};
      if (!tree[mufredat][ders]) tree[mufredat][ders] = {};
      if (!tree[mufredat][ders][modul]) tree[mufredat][ders][modul] = [];
      
      if (mufredatListesi.indexOf(mufredat) === -1) mufredatListesi.push(mufredat);
      if (dersListesi.indexOf(ders) === -1) dersListesi.push(ders);
      
      // Modül altındaki UDA'yı bul ya da ekle
      var modulItems = tree[mufredat][ders][modul];
      var udaItem = null;
      for (var u = 0; u < modulItems.length; u++) {
        if ((udaKod && modulItems[u].kod === udaKod) || (!udaKod && modulItems[u].uda === udaMetin)) {
          udaItem = modulItems[u];
          break;
        }
      }
      
      if (!udaItem) {
        udaItem = {
          unite: unite,
          kod: udaKod,
          uda: udaMetin,
          bep_uda: bepUda,
          kda_listesi: []
        };
        modulItems.push(udaItem);
      }
      
      // KDA'yı listeye ekle
      if (kdaMetin) {
        udaItem.kda_listesi.push({
          kod: kdaKod,
          metin: kdaMetin,
          tip: kdaTipi,
          olcut: olcut,
          yontem: yontem,
          materyal: materyal
        });
      }
      
      totalRecords++;
    }
    
    var meta = {
      sheetName: ss.getName(),
      totalRows: totalRecords,
      mufredatListesi: mufredatListesi,
      dersListesi: dersListesi,
      lastUpdated: new Date().toLocaleString('tr-TR')
    };
    
    // Önbelleğe yaz (1500 saniye = 25 dakika)
    try {
      var serializedTree = JSON.stringify(tree);
      // CacheService tek parça max 100KB kabul ettiği için çok büyükse güvenli bloklama yapılır
      if (serializedTree.length < 95000) {
        cache.put("BEP_DATA_TREE", serializedTree, 1500);
        cache.put("BEP_DATA_META", JSON.stringify(meta), 1500);
      }
    } catch (cacheErr) {
      // Önbellek yazma hatası normal çalışmayı engellemesin
    }
    
    return {
      success: true,
      fromCache: false,
      tree: tree,
      meta: meta
    };
    
  } catch (err) {
    return {
      success: false,
      message: "Veri okuma hatası: " + err.message
    };
  }
}

/**
 * Kolon başlığını esnek arayan yardımcı fonksiyon
 */
function findColIndex(colMap, possibleNames) {
  for (var i = 0; i < possibleNames.length; i++) {
    var key = possibleNames[i].toUpperCase();
    if (typeof colMap[key] !== 'undefined') {
      return colMap[key];
    }
  }
  return -1;
}

/**
 * Bağlanan boş bir Google E-Tabloya anında şablon başlıklarını ve örnek BTY satırlarını yükler
 */
function setupSampleSpreadsheet(targetSheetId) {
  var id = targetSheetId ? extractSheetIdFromUrl(targetSheetId) : getTargetSpreadsheetId();
  if (!id) return { success: false, message: "E-Tablo ID'si belirtilmedi!" };
  
  try {
    var ss = SpreadsheetApp.openById(id);
    var sheet = ss.getSheetByName("BEP_HAVUZU");
    if (!sheet) {
      sheet = ss.insertSheet("BEP_HAVUZU");
    }
    
    // Başlıklar
    var headers = [
      "Mufredat_Turu", "Ders_Adi", "Sinif_Duzeyi", "Modul_Tema", "Unite_Konu",
      "UDA_Kodu", "UDA_Metni", "BEP_UDA_Metni", "KDA_Kodu", "KDA_Metni",
      "KDA_Tipi", "Onerilen_Olcut", "Onerilen_Yontemler", "Onerilen_Materyaller", "Aktif_Mi"
    ];
    
    // Örnek BTY Satırları
    var sampleRows = [
      [
        "TYMM", "Bilişim Teknolojileri ve Yazılım 9.Sınıf", "9", "Programlamaya Giriş ve Algoritma", "1. ÜNİTE: BİLİŞİM TEKNOLOJİLERİNİN PROGRAMLAMADAKİ YERİ",
        "BTY.9.1.1", "BTY.9.1.1. Bilişim teknolojilerine ilişkin temel kavramları ve bilişim araçlarını sınıflandırabilme",
        "Öğrenci, dönem sonunda bilişim teknolojilerine ilişkin temel kavramları ve yaygın bilişim araçlarını eşleştirir, gösterir ve kullanım amacını söyler.",
        "KDA 1.1", "Temel bilişim kavramlarını (bilgisayar, yazılım, veri, donanım) temsil eden kartlardan adı söyleneni seçip gösterir.",
        "Revize_Temel", "%70 Başarı ile", "Doğrudan Öğretim, Gösterip Yaptırma, Model Olma", "Bilgisayar, Görsel Kartlar, Çalışma Yaprakları", "EVET"
      ],
      [
        "TYMM", "Bilişim Teknolojileri ve Yazılım 9.Sınıf", "9", "Programlamaya Giriş ve Algoritma", "1. ÜNİTE: BİLİŞİM TEKNOLOJİLERİNİN PROGRAMLAMADAKİ YERİ",
        "BTY.9.1.1", "BTY.9.1.1. Bilişim teknolojilerine ilişkin temel kavramları ve bilişim araçlarını sınıflandırabilme",
        "Öğrenci, dönem sonunda bilişim teknolojilerine ilişkin temel kavramları ve yaygın bilişim araçlarını eşleştirir, gösterir ve kullanım amacını söyler.",
        "1.1", "Bilişim teknolojilerine ilişkin temel kavramları tanımlar.",
        "MEB_Resmi", "%75 Başarı ile", "Anlatım, Soru-Cevap, Gösterip Yaptırma", "Ders Kitabı, EBA İçerikleri, Bilgisayar", "EVET"
      ],
      [
        "TYMM", "Bilişim Teknolojileri ve Yazılım 9.Sınıf", "9", "Programlamaya Giriş ve Algoritma", "2. ÜNİTE: ALGORİTMA İLE PROBLEM ÇÖZME VE AKIŞ DİYAGRAMI",
        "BTY.9.2.1", "BTY.9.2.1. Problem çözme sürecinde girdi-işlem-çıktı bileşenlerini ilişkilendirerek algoritmik düşünebilme ve çözüm algoritması geliştirebilme",
        "Öğrenci, dönem sonunda önüne konulan 3-4 adımlı günlük yaşam probleminin girdi-çıktılarını belirler; işlem adımı kartlarını oluş sırasına göre soldan sağa hatasız dizer ve sıralar.",
        "KDA 2.1", "Basit bir problem durumunu dinleyerek problemin ne olduğunu söyler.",
        "Revize_Temel", "3/4 Oranında", "Model Olma, İpuçlarının Geri Çekilmesi", "Görsel Sıralama Kartları, Bloklar", "EVET"
      ],
      [
        "TYMM", "Bilişim Teknolojileri ve Yazılım 9.Sınıf", "9", "Programlamaya Giriş ve Algoritma", "2. ÜNİTE: ALGORİTMA İLE PROBLEM ÇÖZME VE AKIŞ DİYAGRAMI",
        "BTY.9.2.1", "BTY.9.2.1. Problem çözme sürecinde girdi-işlem-çıktı bileşenlerini ilişkilendirerek algoritmik düşünebilme ve çözüm algoritması geliştirebilme",
        "Öğrenci, dönem sonunda önüne konulan 3-4 adımlı günlük yaşam probleminin girdi-çıktılarını belirler; işlem adımı kartlarını oluş sırasına göre soldan sağa hatasız dizer ve sıralar.",
        "2.5", "Bir problemin çözümü için en doğru algoritmayı geliştirir.",
        "MEB_Resmi", "%80 Başarı ile", "Gösterip Yaptırma, Problem Çözme", "Akış Şeması Şablonları, Bilgisayar", "EVET"
      ],
      [
        "KLASIK", "Bilişim Teknolojileri ve Yazılım 10.Sınıf", "10", "Programlama Dilleri (Python)", "Python ile Temel Programlama",
        "BTY.10.1", "Python dilinde temel değişkenleri ve veri tiplerini kavrar.",
        "Öğrenci, Python ortamında sayısal ve metinsel veri tiplerini öğretmen rehberliğinde ekrana yazdırır.",
        "KDA 1.1", "print() komutunu kullanarak kendi adını ve okulunu ekrana yazdırır.",
        "Revize_Temel", "%70 Başarı ile", "Doğrudan Öğretim, Birebir Öğretim", "IDLE / VS Code, Kod Kartları", "EVET"
      ]
    ];
    
    sheet.clear();
    sheet.appendRow(headers);
    sampleRows.forEach(function(row) {
      sheet.appendRow(row);
    });
    
    // Başlık stilini güzelleştir (Mavi dolgu, beyaz kalın yazı, sabitleme)
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#0284c7");
    headerRange.setFontColor("#ffffff");
    headerRange.setFontWeight("bold");
    headerRange.setHorizontalAlignment("center");
    sheet.setFrozenRows(1);
    
    // Sütun genişliklerini otomatik ayarla
    for (var c = 1; c <= headers.length; c++) {
      sheet.autoResizeColumn(c);
    }
    
    clearBepCache();
    return { success: true, message: "Şablon ve örnek BTY verileri E-Tabloya başarıyla yüklendi!" };
  } catch (err) {
    return { success: false, message: "Şablon oluşturulamadı: " + err.message };
  }
}
