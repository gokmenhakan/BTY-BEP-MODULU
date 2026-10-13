# 📊 Google E-Tablolar & Dinamik BEP Modülü

Bu klasör, BEP kazanımlarını doğrudan **Google E-Tablolar (Spreadsheet)** üzerinden dinamik olarak çeken bağımsız modüldür.

---

## 📁 Klasör İçeriği

1. **`index.html`**:
   * Google E-Tablo'dan dinamik olarak çekilen verilerle çalışan BEP arayüzüdür.
   * `Müfredat Türü` $\rightarrow$ `Ders` $\rightarrow$ `Modül` $\rightarrow$ `UDA` $\rightarrow$ `KDA` kademeli açılır listelerini tablodan besler.
   * Çift yönlü çalışır:
     * **Canlı Mod:** Google Apps Script üzerinde yayınlandığında E-Tablonuzdaki güncel satırları okur.
     * **Yerel / Offline Mod:** İnternetsiz veya doğrudan çift tıklanarak açıldığında dahili BTY havuzunu kullanır, asla çökmez.
   * Word (.docx), Excel (.xlsx) ve MEB A4 Yatay Yazdırma desteğine sahiptir.

2. **`Code.gs`**:
   * Google Apps Script sunucu tarafı kodudur.
   * `CacheService` kullanarak E-Tablo verilerini 25-30 dakika hafızada tutar (sayfaların anında, 100ms altında açılmasını sağlar).
   * E-Tablo ID'sini Script Properties üzerinde saklar.
   * `setupSampleSpreadsheet()` fonksiyonu ile boş bir tabloya şablon başlıklarını ve BTY satırlarını tek tıkla yükleyebilir.

3. **`Tablo_Sablonu.csv`**:
   * Google E-Tablo için hazır içe aktarılabilir şablon dosyasıdır.
   * Google Drive'da yeni bir E-Tablo açıp **Dosya > İçe Aktar (Import)** diyerek bu CSV'yi yükleyebilirsiniz.

4. **`docx.umd.js`**:
   * İnternetsiz (çevrimdışı) ortamda Word (.docx) belgeleri üretebilmek için yerel kütüphanedir.

---

## 🚀 Hızlı Başlangıç & Kurulum

### 1. Adım: Google E-Tablo'yu Oluşturma
1. [Google E-Tablolar](https://sheets.google.com)'a gidin ve yeni boş bir tablo oluşturun.
2. Adını `BEP_HAVUZU` yapın.
3. Bu klasördeki `Tablo_Sablonu.csv` dosyasını içe aktarın (veya E-Tablo bağlantısından sonra arayüzdeki *"Şablonu E-Tabloya Yükle"* butonuna basın).
4. Tablonun sağ üstündeki **Paylaş** butonuna basarak **"Bağlantıya sahip olan herkes görüntüleyebilir"** yapın.

### 2. Adım: Google Apps Script Yayını
1. Google Apps Script projesi açın (veya E-Tablonuzun içinden **Uzantılar > Apps Script** seçin).
2. Bu klasördeki `Code.gs` ve `index.html` kodlarını yapıştırın.
3. Sağ üstteki **Dağıt (Deploy) > Yeni Dağıtım > Web Uygulaması** seçeneğini seçin.
4. Erişim iznini **"Herkes (Anyone)"** yapıp yayınlayın.

