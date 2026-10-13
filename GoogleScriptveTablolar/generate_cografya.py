# -*- coding: utf-8 -*-
import csv

cografya_data = [
    # =========================================================================
    # 10. SINIF COĞRAFYA (TYMM)
    # =========================================================================
    # 1. Ünite: Coğrafyanın Doğası
    {
        "sinif": "10", "modul": "Coğrafyanın Doğası", "unite": "1. ÜNİTE: COĞRAFYANIN DOĞASI (Coğrafi Bakış)",
        "uda_kod": "COĞ.10.1.1",
        "uda_metin": "COĞ.10.1.1. Örnek olay, olgu ve/veya mekânı coğrafyanın temel kavramları ile ilişkilendirebilme",
        "bep_uda": "Öğrenci, dönem sonunda yakın çevresindeki veya Türkiye'deki bir coğrafi olayı/mekânı harita üzerinde gösterir ve temel özelliklerini söyler.",
        "kda_list": [
            ("1.1", "Örnek olay, olgu ve/veya mekânın harita üzerindeki konumunu algılar.", "MEB_Resmi"),
            ("1.2", "Örnek olay, olgu ve/veya mekânın temel coğrafi koşullarını tanımlar.", "MEB_Resmi"),
            ("KDA 1.1", "Türkiye dilsiz haritası üzerinde yaşadığı ili ve komşu illeri gösterir.", "Revize_Temel"),
            ("KDA 1.2", "Verilen resimlerdeki coğrafi ortamları (dağ, deniz, orman) doğru adlandırır.", "Revize_Temel")
        ]
    },
    # 2. Ünite: Mekânsal Bilgi Teknolojileri
    {
        "sinif": "10", "modul": "Mekânsal Bilgi Teknolojileri", "unite": "2. ÜNİTE: MEKÂNSAL BİLGİ TEKNOLOJİLERİ (CBS ve Haritalar)",
        "uda_kod": "COĞ.10.2.1",
        "uda_metin": "COĞ.10.2.1. Örnek uygulamalar üzerinden CBS ve uzaktan algılamanın kullanım alanlarını özetleyebilme",
        "bep_uda": "Öğrenci, dönem sonunda dijital harita ve navigasyon araçlarının günlük hayattaki kullanım amaçlarını listeler ve gösterir.",
        "kda_list": [
            ("2.1", "Örnek uygulamalar üzerinden CBS ve uzaktan algılamanın kullanım alanlarını çözümler.", "MEB_Resmi"),
            ("2.2", "CBS ve uzaktan algılamanın kullanım alanlarını sınıflandırır.", "MEB_Resmi"),
            ("KDA 2.1", "Akıllı telefonda veya bilgisayarda navigasyon/harita uygulamasını açıp okulun yerini gösterir.", "Revize_Temel"),
            ("KDA 2.2", "Uydu görüntüsü ile çizim harita arasındaki farkı resimlere bakarak söyler.", "Revize_Temel")
        ]
    },
    {
        "sinif": "10", "modul": "Mekânsal Bilgi Teknolojileri", "unite": "2. ÜNİTE: MEKÂNSAL BİLGİ TEKNOLOJİLERİ (Vektör Veri ve Kroki)",
        "uda_kod": "COĞ.10.2.2",
        "uda_metin": "COĞ.10.2.2. Mekânsal bilgi teknolojilerini kullanarak altlık haritalar üzerinde mekânsal veriler oluşturabilme",
        "bep_uda": "Öğrenci, dönem sonunda okulun veya sınıfın krokisi üzerinde önemli noktaları sembollerle işaretler.",
        "kda_list": [
            ("2.3", "Oluşturacağı haritanın amacını belirler ve verileri haritaya işler.", "MEB_Resmi"),
            ("KDA 2.3", "Basit bir kroki üzerinde okul binasını ve bahçesini gösterilen sembollerle işaretler.", "Revize_Temel")
        ]
    },
    # 3. Ünite: Doğal Sistemler ve Süreçler
    {
        "sinif": "10", "modul": "Doğal Sistemler ve Süreçler", "unite": "3. ÜNİTE: DOĞAL SİSTEMLER VE SÜREÇLER (Tektonik Yapı ve Depremler)",
        "uda_kod": "COĞ.10.3.1",
        "uda_metin": "COĞ.10.3.1. Yerkürenin tektonik yapısını çözümleyebilme",
        "bep_uda": "Öğrenci, dönem sonunda yerin katmanlarını model üzerinde gösterir ve Türkiye'deki önemli deprem bölgelerini dilsiz haritada ayırt eder.",
        "kda_list": [
            ("3.1", "Levha tektoniğine neden olan süreçleri belirler.", "MEB_Resmi"),
            ("3.2", "Yeryüzü şekilleri ile levha tektoniği arasındaki ilişkiyi belirler.", "MEB_Resmi"),
            ("KDA 3.1", "Yerin katmanlarını (yer kabuğu, manto, çekirdek) temsil eden şema üzerinde doğru yerleri gösterir.", "Revize_Temel"),
            ("KDA 3.2", "Fay hattı ve deprem kavramlarını eşleştirilmiş resimli kartlar arasından seçer.", "Revize_Temel")
        ]
    },
    {
        "sinif": "10", "modul": "Doğal Sistemler ve Süreçler", "unite": "3. ÜNİTE: DOĞAL SİSTEMLER VE SÜREÇLER (Yeryüzü Şekilleri ve Aşınım)",
        "uda_kod": "COĞ.10.3.3",
        "uda_metin": "COĞ.10.3.3. Yeryüzü şekillerinin oluşumunu aşınım ve birikim süreçleri açısından çözümleyebilme",
        "bep_uda": "Öğrenci, dönem sonunda akarsu, rüzgâr ve dalgaların oluşturduğu yaygın yer şekillerini (vadi, delta, peri bacası, kumsal) görsel kartlardan tanır.",
        "kda_list": [
            ("3.3", "Aşınım ve birikim süreçlerinde ortaya çıkan yeryüzü şekillerini belirler.", "MEB_Resmi"),
            ("KDA 3.3", "Verilen yer şekli fotoğraflarından dağ, ova, plato ve vadiyi doğru eşleştirir.", "Revize_Temel"),
            ("KDA 3.4", "Peri bacası ve kumsal görsellerini gösterip hangi dış kuvvetin etkisiyle oluştuğunu söyler.", "Revize_Temel")
        ]
    },
    # 4. Ünite: Beşerî Sistemler ve Süreçler
    {
        "sinif": "10", "modul": "Beşerî Sistemler ve Süreçler", "unite": "4. ÜNİTE: BEŞERÎ SİSTEMLER VE SÜREÇLER (Yerleşmeler)",
        "uda_kod": "COĞ.10.4.1",
        "uda_metin": "COĞ.10.4.1. Yerleşme yeri seçiminde ve yerleşmelerin gelişiminde etkili olan coğrafi faktörleri sorgulayabilme",
        "bep_uda": "Öğrenci, dönem sonunda insanların yerleşmek için su kenarlarını ve ılıman iklimleri tercih etme nedenlerini açıklar.",
        "kda_list": [
            ("4.1", "Yerleşme yeri seçiminde ve gelişiminde etkili olan coğrafi faktörleri belirler.", "MEB_Resmi"),
            ("KDA 4.1", "İnsanların yaşamak için su kaynaklarına ve düz arazilere ihtiyaç duyduğunu söyler.", "Revize_Temel"),
            ("KDA 4.2", "Köy ve şehir yerleşmelerini gösteren fotoğrafları özelliklerine göre ayırır.", "Revize_Temel")
        ]
    },
    # 5. Ünite: Ekonomik Faaliyetler ve Etkileri
    {
        "sinif": "10", "modul": "Ekonomik Faaliyetler ve Etkileri", "unite": "5. ÜNİTE: EKONOMİK FAALİYETLER VE ETKİLERİ (Ekonomik Sektörler)",
        "uda_kod": "COĞ.10.5.1",
        "uda_metin": "COĞ.10.5.1. Ekonomik faaliyetleri sektörlere göre sınıflandırabilme",
        "bep_uda": "Öğrenci, dönem sonunda meslekleri tarım, sanayi ve hizmet sektörleri kartlarıyla hatasız eşleştirir.",
        "kda_list": [
            ("5.1", "Ekonomik faaliyetlerin sınıflandırılmasındaki ölçütleri belirler.", "MEB_Resmi"),
            ("5.2", "Ekonomik faaliyetleri birincil, ikincil, üçüncül sektörlere göre ayırır.", "MEB_Resmi"),
            ("KDA 5.1", "Çiftçi, balıkçı (tarım); işçi, mühendis (sanayi); doktor, öğretmen (hizmet) meslek kartlarını doğru kutulara koyar.", "Revize_Temel"),
            ("KDA 5.2", "Yaşadığı çevrede en çok hangi ekonomik faaliyetin yapıldığını söyler.", "Revize_Temel")
        ]
    },
    # 6. Ünite: Afetler ve Sürdürülebilir Çevre
    {
        "sinif": "10", "modul": "Afetler ve Sürdürülebilir Çevre", "unite": "6. ÜNİTE: AFETLER VE SÜRDÜRÜLEBİLİR ÇEVRE (Afet Bilinci ve Korunma)",
        "uda_kod": "COĞ.10.6.3",
        "uda_metin": "COĞ.10.6.3. Mekânın özelliklerine göre afetlerden korunma uygulamalarına karar verebilme",
        "bep_uda": "Öğrenci, dönem sonunda deprem anında yapılması gereken 'Çök-Kapan-Tutun' hareketini ve afet çantası malzemelerini eksiksiz uygular/sayar.",
        "kda_list": [
            ("6.1", "Afetlerden korunma uygulamalarına alternatif seçenekler oluşturur ve karar verir.", "MEB_Resmi"),
            ("KDA 6.1", "Deprem tatbikatında uyarı verildiğinde 'Çök-Kapan-Tutun' pozisyonunu hatasız alır.", "Revize_Temel"),
            ("KDA 6.2", "Deprem çantasında bulunması gereken malzemeleri (su, fener, düdük, ilk yardım seti) resimler arasından seçer.", "Revize_Temel")
        ]
    },
    # 7. Ünite: Bölgeler, Ülkeler ve Küresel Bağlantılar
    {
        "sinif": "10", "modul": "Bölgeler, Ülkeler ve Küresel Bağlantılar", "unite": "7. ÜNİTE: BÖLGELER, ÜLKELER VE KÜRESEL BAĞLANTILAR (Türk Dünyası)",
        "uda_kod": "COĞ.10.7.1",
        "uda_metin": "COĞ.10.7.1. Türk dünyasının ortak kültürel özellikleri hakkında analojik çıkarım yapabilme",
        "bep_uda": "Öğrenci, dönem sonunda Türk dünyası haritasında Türkiye ile dost ve kardeş Türk cumhuriyetlerinin (Azerbaycan, Kazakistan, Özbekistan) bayraklarını eşleştirir.",
        "kda_list": [
            ("7.1", "Türk kültürünün yayıldığı alanlardaki kültürel özellikleri tespit eder.", "MEB_Resmi"),
            ("KDA 7.1", "Harita üzerinde Türkiye ve komşularını gösterip isimlerini söyler.", "Revize_Temel"),
            ("KDA 7.2", "Azerbaycan bayrağı ile Türk bayrağını tanır ve kardeş ülke olduklarını ifade eder.", "Revize_Temel")
        ]
    },

    # =========================================================================
    # 11. SINIF COĞRAFYA (TYMM)
    # =========================================================================
    # 1. Ünite: Coğrafyanın Doğası
    {
        "sinif": "11", "modul": "Coğrafyanın Doğası", "unite": "1. ÜNİTE: COĞRAFYANIN DOĞASI (Mekânsal Sorunlar)",
        "uda_kod": "COĞ.11.1.1",
        "uda_metin": "COĞ.11.1.1. Mekânsal sorunların çözümünde coğrafya biliminin katkılarını yapılandırabilme",
        "bep_uda": "Öğrenci, dönem sonunda çevre kirliliği ve plansız kentleşmenin zararlarını resimler üzerinden açıklar ve çözüm önerisi söyler.",
        "kda_list": [
            ("1.1", "Coğrafya biliminin mekânsal sorunların çözümüne sunduğu katkıları inceler.", "MEB_Resmi"),
            ("KDA 1.1", "Hava, su ve toprak kirliliğini gösteren görselleri doğru çevre sorunuyla eşleştirir.", "Revize_Temel"),
            ("KDA 1.2", "Çevreyi temiz tutmak için yere çöp atmama ve geri dönüşüm kurallarını söyler.", "Revize_Temel")
        ]
    },
    # 2. Ünite: Mekânsal Bilgi Teknolojileri
    {
        "sinif": "11", "modul": "Mekânsal Bilgi Teknolojileri", "unite": "2. ÜNİTE: MEKÂNSAL BİLGİ TEKNOLOJİLERİ (Web CBS)",
        "uda_kod": "COĞ.11.2.1",
        "uda_metin": "COĞ.11.2.1. Web tabanlı CBS aracılığı ile harita uygulamaları yapabilme",
        "bep_uda": "Öğrenci, dönem sonunda bilgisayarda açık olan dijital harita üzerinde Türkiye'nin denizlerini ve komşularını fareyle tıklayarak gösterir.",
        "kda_list": [
            ("2.1", "Web tabanlı CBS uygulamasını kullanarak harita okur ve basit harita oluşturur.", "MEB_Resmi"),
            ("KDA 2.1", "Google Haritalar üzerinde Karadeniz, Akdeniz ve Ege Denizi'ni gösterip söyler.", "Revize_Temel")
        ]
    },
    # 3. Ünite: Doğal Sistemler ve Süreçler
    {
        "sinif": "11", "modul": "Doğal Sistemler ve Süreçler", "unite": "3. ÜNİTE: DOĞAL SİSTEMLER VE SÜREÇLER (Su Kaynakları)",
        "uda_kod": "COĞ.11.3.1",
        "uda_metin": "COĞ.11.3.1. Yeryüzündeki su kaynaklarını sınıflandırabilme",
        "bep_uda": "Öğrenci, dönem sonunda tatlı ve tuzlu su kaynaklarını (okyanus, deniz, göl, akarsu, yer altı suyu) kartlar üzerinden gruplandırır.",
        "kda_list": [
            ("3.1", "Yeryüzündeki su kaynaklarını sınıflandırabilmek için gerekli olan ölçütleri belirler.", "MEB_Resmi"),
            ("KDA 3.1", "Deniz suyunun tuzlu, akarsu ve göllerin tatlı su olduğunu söyler.", "Revize_Temel"),
            ("KDA 3.2", "Türkiye'nin en büyük gölünün Van Gölü olduğunu haritada gösterir.", "Revize_Temel")
        ]
    },
    {
        "sinif": "11", "modul": "Doğal Sistemler ve Süreçler", "unite": "3. ÜNİTE: DOĞAL SİSTEMLER VE SÜREÇLER (Türkiye'nin Suları ve Mavi Vatan)",
        "uda_kod": "COĞ.11.3.2",
        "uda_metin": "COĞ.11.3.2. Türkiye’deki su kaynaklarının çevresel, ekonomik, politik ve sosyokültürel etkilerini sorgulayabilme",
        "bep_uda": "Öğrenci, dönem sonunda Türkiye'yi çevreleyen denizleri (Karadeniz, Marmara, Ege, Akdeniz - Mavi Vatan) haritada gösterir.",
        "kda_list": [
            ("3.2", "Türkiye’deki su kaynaklarının çevresel ve ekonomik etkilerini çözümler.", "MEB_Resmi"),
            ("KDA 3.3", "Türkiye'nin üç tarafının denizlerle çevrili olduğunu dilsiz haritada gösterir.", "Revize_Temel"),
            ("KDA 3.4", "Suyun tarımda sulama ve enerji üretimindeki önemine birer örnek verir.", "Revize_Temel")
        ]
    },
    # 5. Ünite: Ekonomik Faaliyetler ve Etkileri
    {
        "sinif": "11", "modul": "Ekonomik Faaliyetler ve Etkileri", "unite": "5. ÜNİTE: EKONOMİK FAALİYETLER VE ETKİLERİ (Tarım ve Madenler)",
        "uda_kod": "COĞ.11.5.1",
        "uda_metin": "COĞ.11.5.1. Tarımsal faaliyetleri gıda güvencesi açısından sorgulayabilme",
        "bep_uda": "Öğrenci, dönem sonunda temel tarım ürünlerini (buğday, mısır, zeytin, çay) ve yetiştirildikleri bölgeleri eşleştirir.",
        "kda_list": [
            ("5.1", "Tarımsal faaliyetler ve gıda güvencesi ile ilgili bilgileri çözümler.", "MEB_Resmi"),
            ("KDA 5.1", "Ekmek yapımında buğdayın kullanıldığını ve unun buğdaydan elde edildiğini söyler.", "Revize_Temel"),
            ("KDA 5.2", "Rize'de çay, Akdeniz'de turunçgil yetiştiğini görsel eşleştirme kartıyla gösterir.", "Revize_Temel")
        ]
    },
    {
        "sinif": "11", "modul": "Ekonomik Faaliyetler ve Etkileri", "unite": "5. ÜNİTE: EKONOMİK FAALİYETLER VE ETKİLERİ (Enerji Kaynakları)",
        "uda_kod": "COĞ.11.5.4",
        "uda_metin": "COĞ.11.5.4. Dünya ve Türkiye’deki enerji kaynaklarının kullanımında meydana gelen değişim ve sürekliliği algılayabilme",
        "bep_uda": "Öğrenci, dönem sonunda yenilenebilir temiz enerji kaynaklarını (güneş paneli, rüzgâr gülü) fosil yakıtlardan (kömür, petrol) ayırt eder.",
        "kda_list": [
            ("5.2", "Enerji kaynaklarının kullanımındaki değişim sürecini sentezler.", "MEB_Resmi"),
            ("KDA 5.3", "Güneş ve rüzgâr enerjisinin çevreye zarar vermeyen temiz enerji olduğunu söyler.", "Revize_Temel"),
            ("KDA 5.4", "Evde elektrik ve su tasarrufu için yapılabilecek 2 kuralı sıralar.", "Revize_Temel")
        ]
    },
    # 6. Ünite: Afetler ve Sürdürülebilir Çevre
    {
        "sinif": "11", "modul": "Afetler ve Sürdürülebilir Çevre", "unite": "6. ÜNİTE: AFETLER VE SÜRDÜRÜLEBİLİR ÇEVRE (Su Tasarrufu ve İklim)",
        "uda_kod": "COĞ.11.6.3",
        "uda_metin": "COĞ.11.6.3. Türkiye’de bulunan su kaynaklarının sürdürülebilir kullanımını sorgulayabilme",
        "bep_uda": "Öğrenci, dönem sonunda su israfını önlemeye yönelik davranışları (diş fırçalarken musluğu kapatma vb.) açıklar.",
        "kda_list": [
            ("6.2", "Türkiye'de su kaynaklarının sürdürülebilir kullanımına ilişkin çözümler sunar.", "MEB_Resmi"),
            ("KDA 6.1", "Musluğu açık bırakmanın su israfı olduğunu söyler ve gereksiz akan musluğu kapatır.", "Revize_Temel")
        ]
    },

    # =========================================================================
    # 12. SINIF COĞRAFYA (TYMM)
    # =========================================================================
    # 1. Ünite: Coğrafyanın Doğası
    {
        "sinif": "12", "modul": "Coğrafyanın Doğası", "unite": "1. ÜNİTE: COĞRAFYANIN DOĞASI (Geleceğin Dünyası)",
        "uda_kod": "COĞ.12.1.1",
        "uda_metin": "COĞ.12.1.1. Geleceğin dünyasında coğrafya biliminin etkilerine ilişkin öngörüde bulunabilme",
        "bep_uda": "Öğrenci, dönem sonunda geleceğin akıllı şehirlerinde teknolojinin doğayla uyumlu kullanımına bir örnek verir.",
        "kda_list": [
            ("1.1", "Coğrafya bilimiyle ilgili kanıtları ve gelecekteki etkilerini ilişkilendirir.", "MEB_Resmi"),
            ("KDA 1.1", "Akıllı şehirlerde güneş enerjisi ve elektrikli toplu taşıma araçlarının kullanımını resimden seçer.", "Revize_Temel")
        ]
    },
    # 2. Ünite: Mekânsal Bilgi Teknolojileri
    {
        "sinif": "12", "modul": "Mekânsal Bilgi Teknolojileri", "unite": "2. ÜNİTE: MEKÂNSAL BİLGİ TEKNOLOJİLERİ (Tematik Haritalar)",
        "uda_kod": "COĞ.12.2.1",
        "uda_metin": "COĞ.12.2.1. Web tabanlı CBS ile oluşturulan tematik haritaları kullanarak uygulamalar yapabilme",
        "bep_uda": "Öğrenci, dönem sonunda hava durumu haritasında yağmurlu ve güneşli bölgeleri sembollerine göre okur.",
        "kda_list": [
            ("2.1", "Web tabanlı CBS ile oluşturulan tematik haritaları okur ve çözümler.", "MEB_Resmi"),
            ("KDA 2.1", "Hava durumu haritasındaki bulut, güneş ve kar simgelerini anlamlarıyla eşleştirir.", "Revize_Temel")
        ]
    },
    # 3. Ünite: Doğal Sistemler ve Süreçler
    {
        "sinif": "12", "modul": "Doğal Sistemler ve Süreçler", "unite": "3. ÜNİTE: DOĞAL SİSTEMLER VE SÜREÇLER (Toprak ve Bitki Örtüsü)",
        "uda_kod": "COĞ.12.3.1",
        "uda_metin": "COĞ.12.3.1. Toprak oluşum sürecini toprak türleri açısından yapılandırabilme",
        "bep_uda": "Öğrenci, dönem sonunda toprağın bitkiler ve tarım için önemini söyler; erozyonu önlemek için ağaç dikilmesi gerektiğini belirtir.",
        "kda_list": [
            ("3.1", "Toprak oluşumunu etkileyen faktörlerle toprak grupları arasındaki ilişkiyi açıklar.", "MEB_Resmi"),
            ("KDA 3.1", "Ağaç dikmenin toprağın kaymasını (erozyonu) önlediğini resimli afiş üzerinden açıklar.", "Revize_Temel")
        ]
    },
    {
        "sinif": "12", "modul": "Doğal Sistemler ve Süreçler", "unite": "3. ÜNİTE: DOĞAL SİSTEMLER VE SÜREÇLER (Türkiye'nin Bitki Örtüsü)",
        "uda_kod": "COĞ.12.3.3",
        "uda_metin": "COĞ.12.3.3. Coğrafi faktörlerin dünya ve Türkiye’deki bitki örtüsünün çeşitliliği ve dağılışı üzerindeki etkisi hakkında haritalardan çıkarım yapabilme",
        "bep_uda": "Öğrenci, dönem sonunda Türkiye'deki ana bitki örtüsü türlerini (orman, maki, bozkır) harita ve görsellerden tanır.",
        "kda_list": [
            ("3.2", "Bitki örtüsü dağılış haritalarını karşılaştırarak çıkarımlar yapar.", "MEB_Resmi"),
            ("KDA 3.2", "Karadeniz'de orman, Akdeniz'de maki, İç Anadolu'da bozkır olduğunu görsel eşleştirme kartıyla gösterir.", "Revize_Temel")
        ]
    },
    # 5. Ünite: Ekonomik Faaliyetler ve Etkileri
    {
        "sinif": "12", "modul": "Ekonomik Faaliyetler ve Etkileri", "unite": "5. ÜNİTE: EKONOMİK FAALİYETLER VE ETKİLERİ (Ulaşım, Ticaret ve Turizm)",
        "uda_kod": "COĞ.12.5.1",
        "uda_metin": "COĞ.12.5.1. Dünya ve Türkiye’deki ulaşım sistemlerinin gelişim sürecinde meydana gelen değişim ve sürekliliği algılayabilme",
        "bep_uda": "Öğrenci, dönem sonunda ulaşım türlerini (kara yolu, demir yolu, deniz yolu, hava yolu) araçlarıyla eşleştirir ve en hızlı olanı belirtir.",
        "kda_list": [
            ("5.1", "Ulaşım sistemlerinin gelişim sürecindeki değişimleri sıralar ve açıklar.", "MEB_Resmi"),
            ("KDA 5.1", "Otobüs (kara), tren (demir), gemi (deniz), uçak (hava) araçlarını doğru ulaşım yolu kartına yerleştirir.", "Revize_Temel"),
            ("KDA 5.2", "Uçağın en hızlı ulaşım aracı olduğunu söyler.", "Revize_Temel")
        ]
    },
    {
        "sinif": "12", "modul": "Ekonomik Faaliyetler ve Etkileri", "unite": "5. ÜNİTE: EKONOMİK FAALİYETLER VE ETKİLERİ (Türkiye'de Turizm)",
        "uda_kod": "COĞ.12.5.3",
        "uda_metin": "COĞ.12.5.3. Turizm faaliyetlerinin dünya ve Türkiye’deki sosyal, kültürel, ekonomik, politik ve çevresel etkilerini sorgulayabilme",
        "bep_uda": "Öğrenci, dönem sonunda Türkiye'nin tarihi ve doğal turizm mekanlarından (Ayasofya, Peri Bacaları, Pamukkale Travertenleri) en az ikisini fotoğraftan tanır.",
        "kda_list": [
            ("5.2", "Turizm faaliyetlerinin ekonomik ve kültürel etkilerini çözümler.", "MEB_Resmi"),
            ("KDA 5.3", "Pamukkale travertenleri ve Peri Bacaları fotoğraflarını gösterip isimlerini söyler.", "Revize_Temel"),
            ("KDA 5.4", "Turistlerin ülkemize döviz kazandırdığını ve tarihi eserlerin korunması gerektiğini söyler.", "Revize_Temel")
        ]
    },
    # 6. Ünite: Afetler ve Sürdürülebilir Çevre
    {
        "sinif": "12", "modul": "Afetler ve Sürdürülebilir Çevre", "unite": "6. ÜNİTE: AFETLER VE SÜRDÜRÜLEBİLİR ÇEVRE (Doğal Mirasın Korunması)",
        "uda_kod": "COĞ.12.6.6",
        "uda_metin": "COĞ.12.6.6. Doğal ve kültürel mirasa yönelik tehditleri ortadan kaldırmak için ihtiyaç duyulan uygulamalara karar verebilme",
        "bep_uda": "Öğrenci, dönem sonunda milli parkları ve tarihi eserleri korumanın bir vatandaşlık görevi olduğunu ifade eder.",
        "kda_list": [
            ("6.1", "Doğal ve kültürel mirasa yönelik tehditleri ortadan kaldırmak için çözümler üretir.", "MEB_Resmi"),
            ("KDA 6.1", "Tarihi eserlerin ve ormanların kirletilmemesi gerektiğini afiş üzerinde gösterir.", "Revize_Temel")
        ]
    }
]

output_rows = []
headers = [
    "Mufredat_Turu", "Ders_Adi", "Sinif_Duzeyi", "Modul_Tema", "Unite_Konu",
    "UDA_Kodu", "UDA_Metni", "BEP_UDA_Metni", "KDA_Kodu", "KDA_Metni",
    "KDA_Tipi", "Onerilen_Olcut", "Onerilen_Yontemler", "Onerilen_Materyaller", "Aktif_Mi"
]

for item in cografya_data:
    ders_adi = f"Coğrafya {item['sinif']}.Sınıf"
    for kda_kod, kda_metin, kda_tipi in item["kda_list"]:
        olcut = "%70 Başarı ile" if kda_tipi == "Revize_Temel" else "%75 Başarı ile"
        yontem = "Doğrudan Öğretim, Gösterip Yaptırma, Model Olma" if kda_tipi == "Revize_Temel" else "Anlatım, Soru-Cevap, Harita İnceleme"
        materyal = "Harita, Küre, Resimli Kartlar, Akıllı Tahta"
        row = [
            "TYMM", ders_adi, item["sinif"], item["modul"], item["unite"],
            item["uda_kod"], item["uda_metin"], item["bep_uda"],
            kda_kod, kda_metin, kda_tipi, olcut, yontem, materyal, "EVET"
        ]
        output_rows.append(row)

csv_path = "c:\\Users\\HAKAN\\Desktop\\BEP script\\GoogleScriptveTablolar\\Cografya_10_11_12_TYMM_BEP_Havuzu.csv"
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(output_rows)

print(f"Toplam {len(output_rows)} adet Coğrafya satırı oluşturuldu: {csv_path}")
