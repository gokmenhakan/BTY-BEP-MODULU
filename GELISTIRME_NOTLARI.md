# BTY BEP Modülü - Geliştirme Notları ve Yol Haritası

Bu belge, **Bilişim Teknolojileri ve Yazılım Dersi BEP Modülü**'nün Google Apps Script (GAS) ortamında canlıya alınması, dağıtımı ve gelecekte eklenebilecek bulut tabanlı geliştirme önerilerini içermektedir.

---

## 📌 1. Bölüm: Google Apps Script (GAS) ile Web Uygulaması Olarak Yayınlama

Yerel sunucu (`python3 -m http.server`) ihtiyacını tamamen ortadan kaldırmak ve uygulamayı internet bağlantısı olan her cihazdan (okul, ev, telefon, tablet) erişilebilir kılmak için izlenecek adımlar:

### Adım 1: Proje Açma
1. Tarayıcıdan [script.google.com](https://script.google.com) adresine gidin (veya Google Drive'da **Yeni > Diğer > Google Apps Script** seçeneğini kullanın).
2. Proje adını `BTY BEP Modülü` olarak belirleyin.

### Adım 2: Sunucu Kodunu (`Code.gs`) Yazma
Varsayılan `Code.gs` dosyasının içine aşağıdaki kodu ekleyin:

```javascript
function doGet() {
  return HtmlService.createHtmlOutputFromFile('index3')
    .setTitle('BTY BEP Modülü (Temel / Uygulamalı Düzey)')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}
```

### Adım 3: Arayüz Dosyasını (`index3.html`) Ekleme
1. Sol menüde **Dosyalar** yanındaki `+` butonuna tıklayıp **HTML** seçin.
2. Adını `index3` olarak kaydedin.
3. Yerel projedeki `index3.html` dosyasının tüm kodunu kopyalayıp buraya yapıştırın.
   *(Word kütüphanesi CDN yedeği ile çalıştığı için Google Apps Script ortamında da çevrim içi sorunsuz yüklenir).*

### Adım 4: Yayına Alma (Deploy)
1. Sağ üstteki mavi **Dağıt (Deploy)** butonuna tıklayın -> **Yeni Dağıtım (New deployment)** seçin.
2. Tür olarak **Web Uygulaması (Web app)** seçin.
3. Parametreler:
   - **Açıklama:** `BEP Modülü v1.0`
   - **Farklı yürüt (Execute as):** `Ben (kendi e-postanız)`
   - **Erişimi olanlar (Who has access):** `Herkes (Anyone)` *(veya sadece siz kullanacaksanız: Yalnızca ben)*
4. **Dağıt** butonuna basın ve Google hesabınızla gerekli izinleri onaylayın.
5. Verilen Web Uygulaması URL'sini (`https://script.google.com/macros/s/.../exec`) kaydedip kullanmaya başlayın.

---

## 🚀 2. Bölüm: Gelecek Geliştirme Önerileri (Yol Haritası)

Sistemi daha işlevsel, pratik ve kurumsal hale getirmek için planlanan özellikler:

### 1. Google Drive'a Otomatik Arşivleme
- **Açıklama:** Öğretmen Word veya Excel çıktısı aldığı anda, dosya yalnızca bilgisayara indirilmekle kalmaz; arka planda öğretmenin Google Drive'ında otomatik oluşturulacak `2026-2027 BEP Planları` klasörüne de yedeklenir.
- **Fayda:** Dosya kaybetme riski sıfırlanır, istenen cihaza anında Google Drive üzerinden ulaşılır.

### 2. Google E-Tablo (Sheets) Öğrenci Veritabanı Entegrasyonu
- **Açıklama:** Okuldaki kaynaştırma öğrencilerinin listesi (Ad, Soyad, TC No, Sınıf, Veli Adı, BEP Geliştirme Birimi Üyeleri vb.) tek bir Google E-Tablosunda tutulur.
- **Fayda:** Formdaki "Öğrenci Adı" kutusundan öğrenci seçildiğinde sınıfı, numarası ve veli bilgileri forma otomatik dolar. Tek tek elle veri girme zahmeti ortadan kalkar.

### 3. Hazırlanan Planları Kaydetme ve Geri Yükleme (Taslak Sistemi)
- **Açıklama:** Hazırlanan bir BEP planı tek tıkla buluta kaydedilebilir. Dönem ortasında veya 2. dönem başında aynı öğrencinin planı listeden seçilerek kaldığı yerden düzenlenebilir.
- **Fayda:** Her dönem sıfırdan plan hazırlamak yerine mevcut plan üzerinden hızlı güncelleme yapılır.

### 4. Çoklu Öğretmen / Zümre Paylaşım Modülü
- **Açıklama:** Aynı okuldaki diğer branş öğretmenleri veya rehberlik servisi (RAM koordinatörleri) için yetkilendirilmiş erişim linki.
- **Fayda:** Tüm okulun BEP hazırlama süreci tek bir standart MEB formatında birleştirilir.

---

## 🛠️ 3. Bölüm: Tamamlanan Son Arayüz Güncellemeleri
- **Satır Düzeni:** 
  - 4 sütunlu satır: *Öğretim Yöntem ve Teknikleri, Kullanılacak Materyaller, Başlama Tarihi, Bitiş Tarihi*
  - 3 sütunlu satır: *Değ. Yöntem ve Teknikleri, Değerlendirme Tarihleri, Performans*
- **Rehber Öğretmen Alanı:** 
  - Özel açılır menü (Combobox) yapısına geçirildi (`Mehmet Ünal MEMOĞLU` ve `Nermin KUMRU`).
  - Seçim yapıldıktan sonra bile her iki isim her zaman menüde görünür ve değiştirilebilir.
  - Serbest isim yazma desteği ve tek tıkla temizleme (`✕`) butonu eklendi.
