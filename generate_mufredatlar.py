# -*- coding: utf-8 -*-
import subprocess, re, os

# PDF Metnini Çıkar
out = subprocess.check_output(['pdftotext', '2024930135238340-Bilişim.pdf', '-']).decode('utf-8', errors='ignore')
lines = out.split('\n')

module_specs = [
    {
        'file': '01_Programlamaya_Giris_ve_Algoritma.txt',
        'id': '9_algoritma',
        'title': 'PROGRAMLAMAYA GİRİŞ VE ALGORİTMA',
        'start': 933,
        'end': 1288,
        'sinif': '9. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, temel bilgisayar donanım parçalarını (monitör, klavye, fare, kasa) ve yaygın bilişim araçlarını gösterir ve kullanım amaçlarını söyler.",
                'kda': [
                    "KDA 1.1: Öğrenci, masada bulunan temel donanım birimlerinden (kasa, monitör, klavye, fare) adı söylenen parçayı 4 denemenin en az 3'ünde parmağıyla gösterir.",
                    "KDA 1.2: Öğrenci, kendisine gösterilen bilişim araçlarının (bilgisayar, telefon, tablet) ne amaçla kullanıldığını istendiğinde söyler.",
                    "KDA 1.3: Öğrenci, bilgisayarı kurallara uygun olarak açma/kapama butonuna basarak açar ve güvenli şekilde kapatır.",
                    "KDA 1.4: Öğrenci, bilişim araçlarının günlük yaşamdaki faydalarına dair en az iki örnek verir."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, günlük hayattaki olayların işlem adımlarını oluş sırasına göre resimli kartlarla masaya dizer ve temel akış şeması şekillerini (başla/bitir, işlem) eşleştirir.",
                'kda': [
                    "KDA 2.1: Öğrenci, önüne konulan 3 adımlı resimli günlük yaşam kartlarını (ör. el yıkama, çay yapma, uyanma) doğru oluş sırasına göre soldan sağa dizer.",
                    "KDA 2.2: Öğrenci, verilen bir akış diyagramındaki 'Başla/Bitir' elips sembolü ile 'İşlem' dikdörtgen sembolünü doğru adıyla gösterir.",
                    "KDA 2.3: Öğrenci, 2 adımlı basit bir yönergeyi (ör. 1. Adım: Butona bas, 2. Adım: Ekrana bak) sırasıyla hatasız uygular.",
                    "KDA 2.4: Öğrenci, öğretmenin anlattığı basit bir problem durumunu dinleyerek ilk yapılacak adımı söyler."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, kodlama ekranındaki başlatma ve durdurma butonlarını fareyle tıklar; sayı ve metin veri türlerini ilgili kutucuklara yazar.",
                'kda': [
                    "KDA 3.1: Öğrenci, ekrandaki yeşil bayrak / başlat butonunu ve kırmızı durdur butonunu fareyle tıklar.",
                    "KDA 3.2: Öğrenci, kendisine verilen örnek verilerden sayıyı sayı kutusuna, kelimeyi metin kutusuna klavye kullanarak yazar.",
                    "KDA 3.3: Öğrenci, 'Eğer / Değilse' (karar) mantığını içeren basit bir şartlı yönergeyi ('Hava yağmurluysa şemsiye al') doğru davranışla açıklar.",
                    "KDA 3.4: Öğrenci, döngü yapısı ile tekrarlanan basit bir hareketi (3 kez zıpla / 3 kez tıkla) komuta göre uygular."
                ]
            },
            {
                'unite_no': 4,
                'uda': "Öğrenci, sırası karışmış 3 işlem adımı içerisindeki hatalı adımı parmağıyla gösterir ve öğretmenin rehberliğinde doğru sırasına koyar.",
                'kda': [
                    "KDA 4.1: Öğrenci, sırası ters verilmiş 3 adımlı akış sıralamasında hata olan basamağı işaret eder.",
                    "KDA 4.2: Öğrenci, öğretmenin yönlendirmesiyle programdaki basit bir komut sırasını düzelterek kodu yeniden çalıştırır.",
                    "KDA 4.3: Öğrenci, hatalı çalışan bir program çıktısı ile doğru çalışan çıktıyı ekranda karşılaştırır."
                ]
            },
            {
                'unite_no': 5,
                'uda': "Öğrenci, üzerinde 1'den 5'e kadar rakamlar yazan kartları küçükten büyüğe sırayla yan yana dizer ve aranan kartı bulup gösterir.",
                'kda': [
                    "KDA 5.1: Öğrenci, karışık verilen 5 adet rakam kartını masada soldan sağa küçükten büyüğe doğru dizer.",
                    "KDA 5.2: Öğrenci, önüne konulan kartlar arasından öğretmenin söylediği hedef sayıyı en fazla 2 denemede seçip gösterir.",
                    "KDA 5.3: Öğrenci, sıralama ve arama işlemlerinin günlük hayatta (ör. rehberden isim arama, boy sırasına girme) nerede kullanıldığını söyler."
                ]
            }
        ]
    },
    {
        'file': '02_Robotik_Kodlama.txt',
        'id': 'robotik_kodlama',
        'title': 'ROBOTİK KODLAMA',
        'start': 1288,
        'end': 1562,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, robotik set kutusundaki temel parçaları (kart, motor, tekerlek, kablo) gösterir, adını söyler ve robotların kullanım alanlarına 2 örnek verir.",
                'kda': [
                    "KDA 1.1: Öğrenci, robotik set kutusundan adı söylenen parçayı (kart, tekerlek, motor) 4 denemenin en az 3'ünde bulup çıkarır.",
                    "KDA 1.2: Öğrenci, robotların temizlik, üretim veya sağlık alanındaki kullanımını gösteren resimleri doğru adlandırır.",
                    "KDA 1.3: Öğrenci, otomatik çalışan cihazlar ile uzaktan kumandalı cihazlar arasındaki farkı basit örnekle söyler."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, USB bağlantı kablosunu karta ve bilgisayara takıp çıkarır; devre kartı üzerindeki LED lamba ve butonu gösterir.",
                'kda': [
                    "KDA 2.1: Öğrenci, USB kablosunu bilgisayar girişine ve karta doğru yönde zarar vermeden takar ve çıkarır.",
                    "KDA 2.2: Öğrenci, devre tahtası veya kart üzerindeki LED lambayı ve buton anahtarı parmağıyla gösterir.",
                    "KDA 2.3: Öğrenci, basit bir bağlantı kablosunun iki ucunu karta takarak öğretmenin rehberliğinde devreyi tamamlar."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, hazır kodlanmış devre kartındaki butona basarak LED ışığı yakar ve robot tekerleğinin döndüğünü gözlemleyerek gösterir.",
                'kda': [
                    "KDA 3.1: Öğrenci, devre kartındaki başlat butonuna basarak LED lambanın yandığını işaret eder.",
                    "KDA 3.2: Öğrenci, motora bağlı tekerleğin döndüğünü fark edip açma/kapama düğmesinden robotu durdurur.",
                    "KDA 3.3: Öğrenci, ışık sensörüne elini yaklaştırdığında meydana gelen değişimi (ses veya ışık) gözlemler ve söyler."
                ]
            }
        ]
    },
    {
        'file': '03_Mobil_Uygulama_Gelistirme.txt',
        'id': 'mobil_uygulama',
        'title': 'MOBİL UYGULAMA GELİŞTİRME',
        'start': 1562,
        'end': 1733,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, tablet/telefon ekranındaki temel uygulama simgelerine (kamera, galeri, ayarlar) dokunarak açar ve kapatır.",
                'kda': [
                    "KDA 1.1: Öğrenci, tablet ekranındaki kamera uygulamasının simgesini bulup dokunarak açar.",
                    "KDA 1.2: Öğrenci, açtığı uygulamayı 'ana ekran' veya 'geri' tuşuna basarak kapatır.",
                    "KDA 1.3: Öğrenci, dokunmatik ekranda parmağıyla sağa/sola kaydırma hareketini amacına uygun yapar."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, mobil geliştirme programında buton veya resim simgesini fareyle tutup ekrana sürükleyip bırakır.",
                'kda': [
                    "KDA 2.1: Öğrenci, sol araç panelindeki 'Button' (Düğme) bileşenini fareyle tutup mobil tasarım ekranına bırakır.",
                    "KDA 2.2: Öğrenci, ekrana eklenen butonun rengini veya üzerindeki yazıyı öğretmenin yardımıyla değiştirir.",
                    "KDA 2.3: Öğrenci, mobil ekran tasarımına bir resim kutusu (Image) ekler."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, hazırlanan basit uygulamadaki butona tıkladığında ekranda çıkan resmi veya yazıyı parmağıyla gösterir.",
                'kda': [
                    "KDA 3.1: Öğrenci, 'Tıkla ve Dinle' butonuna basarak çıkan sesi dinler ve ne sesi olduğunu söyler.",
                    "KDA 3.2: Öğrenci, iki ekranlı basit bir uygulamada 'İleri' butonuna basarak diğer sayfaya geçer.",
                    "KDA 3.3: Öğrenci, ekrandaki butona her bastığında rengin değiştiğini gözlemler ve açıklar."
                ]
            }
        ]
    },
    {
        'file': '04_Programlama_Dilleri_Java.txt',
        'id': 'java',
        'title': 'PROGRAMLAMA DİLLERİ (JAVA)',
        'start': 1733,
        'end': 1944,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, Java geliştirme ortamını bilgisayarda açar ve hazır kod projesini 'Run' butonuna basarak konsolda çalıştırır.",
                'kda': [
                    "KDA 1.1: Masaüstündeki Java IDE simgesine çift tıklayarak programı açar.",
                    "KDA 1.2: Ekranda görünen yeşil üçgen 'Run / Çalıştır' butonuna fareyle tıklar.",
                    "KDA 1.3: Konsol ekranında beliren yazıyı fareyle işaret eder."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, tamsayı (int) ve metin (String) türündeki basit değerleri klavyeden kod içerisindeki ilgili alanlara yazar.",
                'kda': [
                    "KDA 2.1: Tırnak işaretleri arasına klavyeden kendi adını yazar.",
                    "KDA 2.2: Sayı değişkeninin karşısına klavyeden kendi yaşını yazar.",
                    "KDA 2.3: Yazılan değerlerin konsolda ekrana geldiğini kontrol eder."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, kodlama ekranındaki hazır nesneye ait özellikleri (renk, boyut) listeden seçerek değiştirir.",
                'kda': [
                    "KDA 3.1: Hazır araba/öğrenci nesnesinin adını kodda bulup değiştirir.",
                    "KDA 3.2: Nesne oluşturma butonuna tıklayarak yeni nesnenin oluştuğunu gözlemler."
                ]
            },
            {
                'unite_no': 4,
                'uda': "Öğrenci, ekrandaki iki sayıdan büyük olanı şartlı ifadeyle (if-else) karşılaştırıp sonucu konsolda gösterir.",
                'kda': [
                    "KDA 4.1: Kod satırındaki sayıları değiştirerek sonucu konsolda gözlemler.",
                    "KDA 4.2: 'Doğru' veya 'Yanlış' çıktısını konsolda parmağıyla işaret eder."
                ]
            },
            {
                'unite_no': 5,
                'uda': "Öğrenci, döngü komutuyla ekranda 1'den 5'e kadar sayıların sıralandığını konsol ekranında gösterir.",
                'kda': [
                    "KDA 5.1: Döngü sayısını 3 yaparak ekranda 3 kez tekrar eden yazıyı parmağıyla gösterir.",
                    "KDA 5.2: Döngünün başladığı ve bittiği anı öğretmenin rehberliğinde takip eder."
                ]
            },
            {
                'unite_no': 6,
                'uda': "Öğrenci, liste (Array) içerisindeki 3 elemandan ilk elemanı fareyle veya klavyeyle seçip görüntüler.",
                'kda': [
                    "KDA 6.1: Hazır listeye yeni bir kelime ekleme alanına klavyeden yazı yazar.",
                    "KDA 6.2: Listenin 1. sırasındaki meyve/öğrenci adını konsoldan okur."
                ]
            },
            {
                'unite_no': 7,
                'uda': "Öğrenci, üst sınıf ve alt sınıf kavramını resimli hayvan/araç şemaları üzerinden eşleştirir.",
                'kda': [
                    "KDA 7.1: Taşıt üst sınıfının altına araba ve uçak kartlarını yerleştirir.",
                    "KDA 7.2: Anne-baba ve çocuk benzetmesiyle kalıtım mantığını söyler."
                ]
            },
            {
                'unite_no': 8,
                'uda': "Öğrenci, kendini tekrar eden basit bir geri sayım işlemini (3-2-1-Bitti) ekranda gözlemler ve söyler.",
                'kda': [
                    "KDA 8.1: Sayacın sıfıra ulaştığında durduğunu belirtir.",
                    "KDA 8.2: Başlangıç sayısını 5 yaparak geri sayımı yeniden başlatır."
                ]
            }
        ]
    },
    {
        'file': '05_Programlama_Dilleri_C_Plus_Plus.txt',
        'id': 'cpp',
        'title': 'PROGRAMLAMA DİLLERİ (C++)',
        'start': 1944,
        'end': 2118,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, C++ editörünü açar ve 'cout' komutu içerisine kendi adını yazarak programı derleyip çalıştırır.",
                'kda': [
                    "KDA 1.1: C++ editörünün masaüstü simgesine tıklar.",
                    "KDA 1.2: Ekrana 'Merhaba' yazdıran hazır kod satırını bulur.",
                    "KDA 1.3: Derle ve Çalıştır (F9 / Run) butonuna basarak siyah konsol penceresini açar."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, şartlı durumda (if) girilen sayının pozitif veya negatif olduğunu konsol ekranında kontrol eder.",
                'kda': [
                    "KDA 2.1: Klavyeden bir rakam girip Enter tuşuna basar.",
                    "KDA 2.2: Ekranda çıkan sonucu okur veya parmağıyla gösterir."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, toplama işlemi yapan hazır fonksiyonu çağırıp iki sayının sonucunu konsolda görüntüler.",
                'kda': [
                    "KDA 3.1: Fonksiyon parantezi içerisindeki sayıları klavyeden değiştirir.",
                    "KDA 3.2: Ekranda çıkan toplam sonucunu söyler."
                ]
            },
            {
                'unite_no': 4,
                'uda': "Öğrenci, grafik arayüz form penceresine bir etiket (label) ve metin kutusu ekler.",
                'kda': [
                    "KDA 4.1: Araç kutusundan butonu forma sürükler.",
                    "KDA 4.2: Butonun başlığını klavyeden 'Giriş' olarak düzenler."
                ]
            },
            {
                'unite_no': 5,
                'uda': "Öğrenci, hazır veri listesindeki isimleri ekranda listeler ve kendi adını yeni kayıt kutusuna yazar.",
                'kda': [
                    "KDA 5.1: 'Kayıtları Göster' butonuna basarak listeyi ekrana getirir.",
                    "KDA 5.2: Metin kutusuna adını yazıp 'Ekle' butonuna tıklar."
                ]
            }
        ]
    },
    {
        'file': '06_Programlama_Dilleri_C_Sharp.txt',
        'id': 'csharp',
        'title': 'PROGRAMLAMA DİLLERİ (C#)',
        'start': 2118,
        'end': 2375,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, Visual Studio ortamını açar, yeni bir Windows Form projesi başlatır ve 'Başlat' butonuna tıklar.",
                'kda': [
                    "KDA 1.1: Visual Studio programını masaüstünden açar.",
                    "KDA 1.2: Yeşil 'Başlat' (Start) butonuna basarak form penceresini görüntüler.",
                    "KDA 1.3: Açılan form penceresini 'X' butonuna basarak kapatır."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, form üzerindeki metin kutusuna girilen sayıya göre buton renginin yeşil veya kırmızı olduğunu gözlemler.",
                'kda': [
                    "KDA 2.1: Metin kutusuna fareyle tıklayıp klavyeden sayı yazar.",
                    "KDA 2.2: Butona basarak buton renginin değiştiğini işaret eder."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, hazır araba sınıfından nesne üreterek rengini ve modelini form üzerindeki etiketlerde görüntüler.",
                'kda': [
                    "KDA 3.1: Kod ekranında renk yazan kısmı 'Mavi' olarak günceller.",
                    "KDA 3.2: Ekranda oluşan araba görselini gösterir."
                ]
            },
            {
                'unite_no': 4,
                'uda': "Öğrenci, liste kutusuna (ListBox) 3 öğrenci ismi ekler ve listeden istediği ismi fareyle seçer.",
                'kda': [
                    "KDA 4.1: Kutucuğa arkadaşının adını yazıp 'Listeye Ekle'ye tıklar.",
                    "KDA 4.2: Listeden kendi adını fareyle işaretler."
                ]
            },
            {
                'unite_no': 5,
                'uda': "Öğrenci, buton, metin kutusu ve onay kutusunu form üzerine hizalayarak yerleştirir.",
                'kda': [
                    "KDA 5.1: Form üzerine araç kutusundan CheckBox (onay kutusu) sürükler.",
                    "KDA 5.2: Kutucuğu işaretleyip işaretini kaldırır."
                ]
            },
            {
                'unite_no': 6,
                'uda': "Öğrenci, veri tablosundaki (DataGridView) satırları fareyle seçer ve 'Kaydet' butonuna tıklar.",
                'kda': [
                    "KDA 6.1: Tablodaki ilk satırı fareyle tıklar.",
                    "KDA 6.2: 'Kaydet' butonuna basarak onay mesajını görür."
                ]
            }
        ]
    },
    {
        'file': '07_Programlama_Dilleri_Dart.txt',
        'id': 'dart',
        'title': 'PROGRAMLAMA DİLLERİ (DART)',
        'start': 2375,
        'end': 2547,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, çevrim içi DartPad editörünü tarayıcıda açar, `print()` fonksiyonu içerisine adını yazar ve çalıştırır.",
                'kda': [
                    "KDA 1.1: Web tarayıcısında DartPad sayfasını açar.",
                    "KDA 1.2: Kod satırına klavyeden adını tırnak içinde yazar.",
                    "KDA 1.3: Mavi 'Run' butonuna tıklar ve konsoldaki çıktıyı gösterir."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, ekranda beliren yükleniyor simgesi sonrasında gelen metni konsol ekranında gösterir.",
                'kda': [
                    "KDA 2.1: Veri getirme butonuna basar ve bekleme süresini takip eder.",
                    "KDA 2.2: Gelen mesajı ekranda okur."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, hazır listedeki şehir isimlerini konsola yazdırır ve listeden bir şehri seçer.",
                'kda': [
                    "KDA 3.1: Şehirler listesine yeni bir şehir adı ekler.",
                    "KDA 3.2: Listenin kaç elemandan oluştuğunu konsol çıktısından söyler."
                ]
            }
        ]
    },
    {
        'file': '08_Programlama_Dilleri_PHP.txt',
        'id': 'php',
        'title': 'PROGRAMLAMA DİLLERİ (PHP)',
        'start': 2547,
        'end': 2665,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, yerel web sunucusunu (XAMPP/Apache) başlatır ve tarayıcıda 'localhost' adresini açar.",
                'kda': [
                    "KDA 1.1: Masaüstündeki XAMPP simgesine tıklar.",
                    "KDA 1.2: Apache servisinin yanındaki 'Start' butonuna basar.",
                    "KDA 1.3: Tarayıcı adres çubuğuna 'localhost' yazar ve sayfayı açar."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, `echo` komutu ile web tarayıcısı sayfasına 'Merhaba Dünya' metnini yazdırıp sayfayı yeniler.",
                'kda': [
                    "KDA 2.1: Kod editöründe `echo` yazan yeri bulur.",
                    "KDA 2.2: Tarayıcıda 'Yenile' butonuna basarak yazının geldiğini görür."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, web sayfasındaki form kutusuna yazdığı adın 'Gönder' butonuna basınca ekranda görüntülendiğini gösterir.",
                'kda': [
                    "KDA 3.1: Form kutusuna klavyeden adını yazar.",
                    "KDA 3.2: 'Gönder' butonuna tıklar ve karşı sayfadaki selamlama yazısını gösterir."
                ]
            },
            {
                'unite_no': 4,
                'uda': "Öğrenci, web sayfasında listelenen tablodan bir satırı seçer ve 'Sil' butonuna tıklar.",
                'kda': [
                    "KDA 4.1: Tablodaki ilk kayıt satırını gösterir.",
                    "KDA 4.2: Silme butonuna basarak kaydın ekrandan çıktığını doğrular."
                ]
            }
        ]
    },
    {
        'file': '09_Programlama_Dilleri_JavaScript.txt',
        'id': 'javascript',
        'title': 'PROGRAMLAMA DİLLERİ (JAVASCRIPT)',
        'start': 2665,
        'end': 2873,
        'sinif': '10. / 11. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, web tarayıcısında 'alert' uyarı penceresi açan butona tıklar ve açılan kutudaki 'Tamam' düğmesine basar.",
                'kda': [
                    "KDA 1.1: Web sayfasındaki mavi butona fareyle tıklar.",
                    "KDA 1.2: Ekranda açılan uyarı penceresini okur veya gösterir.",
                    "KDA 1.3: 'Tamam' butonuna basarak pencereyi kapatır."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, butona her tıklandığında ekrandaki sayacın 1 arttığını takip eder ve ekrandaki sayıyı söyler.",
                'kda': [
                    "KDA 2.1: 'Arttır' butonuna 3 kez tıklar.",
                    "KDA 2.2: Ekranda beliren güncel sayıyı (1, 2, 3) söyler.",
                    "KDA 2.3: 'Sıfırla' butonuna basarak sayacı sıfıra döndürür."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, butona tıkladığında web sayfasının arka plan renginin veya yazı boyutunun değiştiğini gösterir.",
                'kda': [
                    "KDA 3.1: 'Karanlık Mod' butonuna tıklar ve sayfanın siyah olduğunu görür.",
                    "KDA 3.2: 'Aydınlık Mod' butonuna basarak sayfayı beyaz yapar.",
                    "KDA 3.3: 'Yazıyı Büyüt' butonuna basarak metnin büyüdüğünü işaret eder."
                ]
            }
        ]
    },
    {
        'file': '10_Programlama_Dilleri_Python.txt',
        'id': '10_python',
        'title': 'PROGRAMLAMA DİLLERİ (PYTHON)',
        'start': 2873,
        'end': 3167,
        'sinif': '10. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, Python geliştirme ortamını açar, `print()` fonksiyonu içerisine adını yazar ve 'Run' butonuna basarak konsolda görüntüler.",
                'kda': [
                    "KDA 1.1: Masaüstündeki Python IDE (Thonny/IDLE/VS Code) simgesine çift tıklayarak programı açar.",
                    "KDA 1.2: Klavyeden `print('...')` fonksiyonunun tırnakları içerisine kendi adını yazar.",
                    "KDA 1.3: Yeşil 'Çalıştır / Run' butonuna basar ve alt konsolda kendi adını parmağıyla gösterir.",
                    "KDA 1.4: Klavyeden iki sayıyı (ör. 5 ve 3) yazıp `+` işareti koyarak sonucu konsolda kontrol eder."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, klavyeden girilen sayıya göre çalışan hazır şartlı programı (if-else) çalıştırır ve ekrandaki doğru sonucu işaret eder.",
                'kda': [
                    "KDA 2.1: Konsoldan yaşını yazıp Enter tuşuna basar.",
                    "KDA 2.2: Ekranda 'Geçtiniz' veya 'Kaldınız' mesajını fareyle işaret eder.",
                    "KDA 2.3: 3 kez tekrar eden basit bir for döngüsünün çıktısını ekranda sayar."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, grafik pencereli veya basit listeli Python uygulamasında butonlara tıklayarak ekrandaki veriyi değiştirir.",
                'kda': [
                    "KDA 3.1: Hazır listedeki 3 meyve isminden birincisini konsolda gösterir.",
                    "KDA 3.2: Ekranda açılan basit arayüzdeki butona tıklar.",
                    "KDA 3.3: Programın ürettiği sonucu ekrandan takip eder."
                ]
            }
        ]
    },
    {
        'file': '11_Yapay_Zeka_Uygulamalari.txt',
        'id': 'yapay_zeka',
        'title': 'YAPAY ZEKÂ UYGULAMALARI',
        'start': 3167,
        'end': len(lines),
        'sinif': '11. / 12. Sınıf',
        'bep_data': [
            {
                'unite_no': 1,
                'uda': "Öğrenci, klavyeden sayıları ve metinleri kullanarak basit veri giriş kutusuna adını ve numarasını yazar.",
                'kda': [
                    "KDA 1.1: Metin kutusuna klavyeden adını ve soyadını yazar.",
                    "KDA 1.2: Sayı kutusuna öğrenci numarasını yazar.",
                    "KDA 1.3: Veri tablosundaki satır ve sütunları parmağıyla gösterir."
                ]
            },
            {
                'unite_no': 2,
                'uda': "Öğrenci, ekranda verilen 3 farklı sayıdan en büyüğünü veya en küçüğünü parmağıyla gösterir.",
                'kda': [
                    "KDA 2.1: Ekranda görünen sayılardan en büyük olanı söyler.",
                    "KDA 2.2: İki sayının ortalamasını hazır hesaplama butonuyla bulup gösterir."
                ]
            },
            {
                'unite_no': 3,
                'uda': "Öğrenci, ekrandaki veri tablosunda ad ve numara yazan kutucukları fareyle tıklar.",
                'kda': [
                    "KDA 3.1: Tablodaki ilk öğrencinin adını okur.",
                    "KDA 3.2: Tabloya yeni bir satır eklendiğini fark edip işaret eder."
                ]
            },
            {
                'unite_no': 4,
                'uda': "Öğrenci, ekranda beliren renkli sütun veya pasta grafiğini gösterir ve en uzun çubuğu işaret eder.",
                'kda': [
                    "KDA 4.1: Sütun grafiğindeki en yüksek renkli sütunu parmağıyla gösterir.",
                    "KDA 4.2: Pasta grafiğindeki en büyük dilimi söyler."
                ]
            },
            {
                'unite_no': 5,
                'uda': "Öğrenci, grafikte yukarı doğru çıkan çizgiyi parmağıyla takip ederek gösterir.",
                'kda': [
                    "KDA 5.1: Çizgi grafiğindeki artış ve azalış yönünü parmağıyla takip eder.",
                    "KDA 5.2: Grafikteki en yüksek noktayı işaretler."
                ]
            },
            {
                'unite_no': 6,
                'uda': "Öğrenci, veri tablosundaki boş veya hatalı kutucuğu fareyle tıklar ve silme (backspace) tuşuyla düzeltir.",
                'kda': [
                    "KDA 6.1: Boş kalan hücreyi gösterir.",
                    "KDA 6.2: Klavyeden doğru harfi yazarak kutuyu tamamlar."
                ]
            },
            {
                'unite_no': 7,
                'uda': "Öğrenci, öğretmenin gösterdiği hazır veri uygulamasında 'Yükle' ve 'Başlat' butonlarına tıklar.",
                'kda': [
                    "KDA 7.1: 'Dosya Yükle' butonuna tıklar.",
                    "KDA 7.2: 'Analizi Başlat' butonuna basarak sonucu bekler."
                ]
            },
            {
                'unite_no': 8,
                'uda': "Öğrenci, yapay zekâ kamera/çizim uygulamasına bir nesne gösterir ve ekranda ne tanıdığını söyler.",
                'kda': [
                    "KDA 8.1: Kameraya kalemi gösterir ve ekranda beliren 'Kalem' yazısını okur.",
                    "KDA 8.2: Yapay zekâ çizim aracına bir daire çizer ve yapay zekânın tahminini seçer."
                ]
            },
            {
                'unite_no': 9,
                'uda': "Öğrenci, sohbet botunun (Chatbot) metin kutusuna 'Merhaba' yazar, 'Gönder' tuşuna tıklar ve gelen cevabı okur.",
                'kda': [
                    "KDA 9.1: Sohbet kutusuna klavyeden bir soru veya selamlama yazar.",
                    "KDA 9.2: Gönder (uçak simgesi veya Enter) tuşuna tıklar.",
                    "KDA 9.3: Sohbet botunun verdiği cevabı seslendirir veya okur."
                ]
            }
        ]
    }
]

def extract_units_raw(start_line, end_line):
    chunk = lines[start_line:end_line]
    units = []
    current_unit = None
    current_desc = []
    current_kazanimlar = []
    in_desc = False
    
    for l in chunk:
        l_str = l.strip()
        m_unit = re.match(r'^([1-9]\d*\.\s*ÜNİTE:\s*.+)', l_str)
        if m_unit:
            if current_unit:
                units.append({
                    'unit': current_unit,
                    'desc': ' '.join(current_desc).strip(),
                    'kazanimlar': current_kazanimlar
                })
            current_unit = m_unit.group(1)
            current_desc = []
            current_kazanimlar = []
            in_desc = False
            continue
        
        if 'Ünite Açıklaması' in l_str:
            in_desc = True
            continue
        if 'Kazanım ve Açıklamaları' in l_str:
            in_desc = False
            continue
            
        m_kaz = re.match(r'^([1-9]\d*\.[1-9]\d*\.\s*.+)', l_str)
        if m_kaz and current_unit:
            in_desc = False
            current_kazanimlar.append(m_kaz.group(1))
            continue
            
        if in_desc and current_unit and l_str:
            current_desc.append(l_str)
            
    if current_unit:
        units.append({
            'unit': current_unit,
            'desc': ' '.join(current_desc).strip(),
            'kazanimlar': current_kazanimlar
        })
    return units

out_dir = 'mufredatlar'
os.makedirs(out_dir, exist_ok=True)

# Generate Module Files
for mod in module_specs:
    fpath = os.path.join(out_dir, mod['file'])
    raw_units = extract_units_raw(mod['start'], mod['end'])
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write('='*80 + '\n')
        f.write('T.C. MİLLÎ EĞİTİM BAKANLIĞI - BİLİŞİM TEKNOLOJİLERİ VE YAZILIM DERSİ\n')
        f.write(f"MODÜL: {mod['title']} ({mod['sinif']})\n")
        f.write('BEP (BİREYSELLEŞTİRİLMİŞ EĞİTİM PROGRAMI) UYARLAMA VE MÜFREDAT KILAVUZU\n')
        f.write('='*80 + '\n\n')
        
        f.write('[BEP HEDEF YAZIM İLKELERİ VE AÇIKLAMA]\n')
        f.write('1. UZUN DÖNEMLİ AMAÇ (UDA / Uzak Hedef):\n')
        f.write('   Öğrencinin dönem veya öğretim yılı sonunda kazanması beklenen genel ve kalıcı davranıştır.\n')
        f.write('   Soyut fiiller ("anlar", "kavrar", "özümser") yerine doğrudan gözlenebilir ve ölçülebilir\n')
        f.write('   eylem bildiren fiillerle ("yazar", "söyler", "gösterir", "tıklar", "eşleştirir") formüle edilmiştir.\n\n')
        f.write('2. KISA DÖNEMLİ AMAÇLAR (KDA / Kısa Hedefler - Görev Analizi):\n')
        f.write('   UDA\'ya ulaştıran küçük, basamaklandırılmış ara adımlardır.\n')
        f.write('   Her bir KDA; Birey (Öğrenci), Koşul (şartlar/araçlar), Davranış (somut eylem) ve Ölçüt\n')
        f.write('   bileşenlerini barındıracak şekilde yapılandırılmıştır.\n\n')
        f.write('3. MEB ORİJİNAL MÜFREDAT KAZANIMLARI:\n')
        f.write('   Dersin resmî öğretim programında yer alan akademik kazanımların tam listesidir.\n')
        f.write('-'*80 + '\n\n')
        
        for idx, u_bep in enumerate(mod['bep_data']):
            u_raw = raw_units[idx] if idx < len(raw_units) else {'unit': f"{idx+1}. Ünite", 'desc': '', 'kazanimlar': []}
            
            f.write(f"################################################################################\n")
            f.write(f"{u_raw['unit']}\n")
            f.write(f"################################################################################\n\n")
            
            if u_raw['desc']:
                f.write(f"[Ünite Özeti/Kapsamı]:\n{u_raw['desc']}\n\n")
                
            f.write(f"A) REVİZE EDİLMİŞ UZUN DÖNEMLİ AMAÇ (UDA / Uzak Hedef):\n")
            f.write(f"   >>> {u_bep['uda']}\n\n")
            
            f.write(f"B) REVİZE EDİLMİŞ KISA DÖNEMLİ AMAÇLAR (KDA / Kısa Hedefler - Görev Analizi):\n")
            for k_item in u_bep['kda']:
                f.write(f"   * {k_item}\n")
            f.write("\n")
            
            f.write(f"C) MEB ORİJİNAL MÜFREDAT KAZANIMLARI (Referans):\n")
            if u_raw['kazanimlar']:
                for kaz in u_raw['kazanimlar']:
                    f.write(f"   - {kaz}\n")
            else:
                f.write("   - (Kazanım bilgisi ünite başlığı altında yer almaktadır)\n")
            f.write("\n" + "-"*80 + "\n\n")

print('All 11 module text files generated successfully in mufredatlar/')
