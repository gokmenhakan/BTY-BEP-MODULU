# Bilişim Teknolojileri ve Yazılım Dersi BEP Modülü

MEB Bilişim Teknolojileri ve Yazılım Dersi Öğretim Programı'na uygun, istemci taraflı Bireyselleştirilmiş Eğitim Programı (BEP) hazırlama aracı.

## Özellikler
- **Modüller:**
  - Programlamaya Giriş ve Algoritma
  - Programlama Dilleri (Python)
  - Robotik Kodlama
  - Mobil Uygulama Geliştirme
  - Yapay Zekâ Uygulamaları
- **Pedagojik UDA ve KDA Yapısı:** MEB ve RAM standartlarına uygun, ünite adları yerine öğrenci merkezli Uzun Dönemli Amaç (UDA) cümleleri ve basamaklandırılmış Kısa Dönemli Amaç (KDA) kazanımları.
- **Düzenlenebilir UDA Alanı:** Seçilen uzun dönemli amacı öğrencinin bireysel performans düzeyine göre düzenleyebilme.
- **Çoklu Kazanım Seçimi:** Açılır menü üzerinden birden fazla kazanım seçebilme.
- **Yazdırma ve PDF:** MEB standart BEP planı şablonunda doğrudan yazdırma veya PDF olarak kaydetme.
- **Excel Dışa Aktarma:** xlsx-js-style kütüphanesi ile tablo hücre çizgileri (borders), başlık dolguları, metin kaydırma (wrapText), hücre birleştirmeleri ve resmi imza bloklarıyla tam formatlı MEB uyumlu `.xlsx` Excel dosyası indirme.

## Yerel Sunucuda Çalıştırma (Local Server)

### Windows'ta:
1. **Pratik Yol:** Klasör içerisindeki `sunucuyu_baslat.bat` dosyasına çift tıklayın. Sunucu otomatik başlar ve varsayılan tarayıcınızda açılır.
2. **Terminal ile:** Klasörde PowerShell veya Komut İstemi açıp şu komutu çalıştırın:
   ```bash
   python -m http.server 8000
   ```
   Ardından tarayıcınızda `http://localhost:8000` adresine gidin.

### Pardus / Linux'ta:
```bash
python3 -m http.server 8000
```
Ardından tarayıcınızda `http://localhost:8000` adresine gidin.
