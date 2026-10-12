/**
 * T.C. MİLLÎ EĞİTİM BAKANLIĞI
 * Bilişim Teknolojileri ve Yazılım Dersi BEP Modülü
 * Google Apps Script Sunucu Kodu (Code.gs)
 *
 * Bu dosya, web uygulaması olarak dağıtıldığında gelen GET isteklerini karşılar
 * ve ?page= parametresine göre index, index2 veya index3 sayfalarını sunar.
 */

function doGet(e) {
  // 1. URL'deki ?page= parametresini oku (Varsayılan: index3 - Maarif Modeli 2.0)
  var page = (e && e.parameter && e.parameter.page) ? e.parameter.page.toString().toLowerCase() : 'index3';
  
  // 2. Güvenlik: Sadece projede bulunan geçerli HTML dosyalarına izin ver
  var izinVerilenSayfalar = ['index', 'index2', 'index3'];
  if (izinVerilenSayfalar.indexOf(page) === -1) {
    page = 'index3';
  }
  
  // 3. HTML dosyasını şablon olarak derle ve yayınla
  return HtmlService.createTemplateFromFile(page)
    .evaluate()
    .setTitle(sayfaBasligiGetir(page))
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

/**
 * Sayfa türüne göre tarayıcı sekme başlığını belirler
 */
function sayfaBasligiGetir(page) {
  switch (page) {
    case 'index':
      return 'BTY BEP Modülü (v1 Standart / Akademik)';
    case 'index2':
      return 'BTY BEP Modülü (v2 Temel / Uygulamalı)';
    case 'index3':
      return 'BTY BEP Modülü (v3 Maarif Modeli & UDA)';
    default:
      return 'Bilişim Teknolojileri ve Yazılım BEP Modülü';
  }
}

/**
 * Web uygulamasının yayınlanan güncel URL adresini döndürür
 */
function getScriptUrl() {
  return ScriptApp.getService().getUrl();
}

