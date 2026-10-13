# -*- coding: utf-8 -*-
"""
MEB Türkiye Yüzyılı Maarif Modeli (TYMM) Müfredat Çıkarıcı ve BEP Havuz Oluşturucu
Bu betik 'GoogleScriptveTablolar/müfredat' klasöründeki tüm PDF müfredatlarını okur,
öğrenme çıktıları (UDA) ve süreç bileşenlerini (KDA) çıkarıp özel eğitime uyarlanmış
BEP havuzu satırlarına dönüştürür.
"""

import os
import re
import csv
import pymupdf

PDF_FOLDER = os.path.join(os.path.dirname(__file__), "müfredat")
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "csv")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

HEADERS = [
    "Mufredat_Turu", "Ders_Adi", "Sinif_Duzeyi", "Modul_Tema", "Unite_Konu",
    "UDA_Kodu", "UDA_Metni", "BEP_UDA_Metni", "KDA_Kodu", "KDA_Metni",
    "KDA_Tipi", "Onerilen_Olcut", "Onerilen_Yontemler", "Onerilen_Materyaller", "Aktif_Mi"
]

# PDF Dosyası -> Ders Yapılandırması
SUBJECT_CONFIGS = [
    {
        "file_keyword": "biyoloji",
        "ders_adi": "Biyoloji",
        "kod_prefix": "BİY",
        "varsayilan_sinif": "9",
        "csv_name": "Biyoloji_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "fizik",
        "ders_adi": "Fizik",
        "kod_prefix": "FİZ",
        "varsayilan_sinif": "9",
        "csv_name": "Fizik_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "kimya",
        "ders_adi": "Kimya",
        "kod_prefix": "KİM",
        "varsayilan_sinif": "9",
        "csv_name": "Kimya_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "tarihdöp",
        "ders_adi": "Tarih",
        "kod_prefix": "TAR",
        "varsayilan_sinif": "9",
        "csv_name": "Tarih_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "laptarihi",
        "ders_adi": "T.C. İnkılap Tarihi ve Atatürkçülük",
        "kod_prefix": "İTA",
        "varsayilan_sinif": "12",
        "csv_name": "Inkilap_Tarihi_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "cogdöp",
        "ders_adi": "Coğrafya",
        "kod_prefix": "COĞ",
        "varsayilan_sinif": "10",
        "csv_name": "Cografya_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "felsefe",
        "ders_adi": "Felsefe",
        "kod_prefix": "FEL",
        "varsayilan_sinif": "10",
        "csv_name": "Felsefe_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "dkab",
        "ders_adi": "Din Kültürü ve Ahlak Bilgisi",
        "kod_prefix": "DKAB",
        "varsayilan_sinif": "9",
        "csv_name": "DKAB_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "ph912",
        "ders_adi": "Peygamberimizin Hayatı",
        "kod_prefix": "PH",
        "varsayilan_sinif": "9",
        "csv_name": "Peygamberimizin_Hayati_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "görsel",
        "ders_adi": "Görsel Sanatlar",
        "kod_prefix": "GS",
        "varsayilan_sinif": "9",
        "csv_name": "Gorsel_Sanatlar_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Saglıkbiltrafik",
        "ders_adi": "Sağlık Bilgisi ve Trafik Kültürü",
        "kod_prefix": "SBTK",
        "varsayilan_sinif": "9",
        "csv_name": "Saglik_Bilgisi_Trafik_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Temel Matematik",
        "ders_adi": "Temel Matematik",
        "kod_prefix": "MAT",
        "varsayilan_sinif": "11",
        "csv_name": "Temel_Matematik_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Matematik Uygulamaları",
        "ders_adi": "Matematik Uygulamaları",
        "kod_prefix": "MAT.U",
        "varsayilan_sinif": "11",
        "csv_name": "Matematik_Uygulamalari_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Sosyoloji",
        "ders_adi": "Sosyoloji",
        "kod_prefix": "SOS",
        "varsayilan_sinif": "11",
        "csv_name": "Sosyoloji_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Psikoloji",
        "ders_adi": "Psikoloji",
        "kod_prefix": "PSK",
        "varsayilan_sinif": "11",
        "csv_name": "Psikoloji_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Mantık",
        "ders_adi": "Mantık",
        "kod_prefix": "MAN",
        "varsayilan_sinif": "11",
        "csv_name": "Mantik_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Türk Kültür",
        "ders_adi": "Türk Kültür ve Medeniyet Tarihi",
        "kod_prefix": "TKMT",
        "varsayilan_sinif": "11",
        "csv_name": "Turk_Kultur_Medeniyet_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Çağdaş Türk",
        "ders_adi": "Çağdaş Türk ve Dünya Tarihi",
        "kod_prefix": "ÇTDT",
        "varsayilan_sinif": "12",
        "csv_name": "Cagdas_Turk_Dunya_Tarihi_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Demokrasi",
        "ders_adi": "Demokrasi ve İnsan Hakları",
        "kod_prefix": "DİH",
        "varsayilan_sinif": "10",
        "csv_name": "Demokrasi_Insan_Haklari_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "temeldini",
        "ders_adi": "Temel Dini Bilgiler",
        "kod_prefix": "TDB",
        "varsayilan_sinif": "9",
        "csv_name": "Temel_Dini_Bilgiler_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "İslam Bilim Tarihi",
        "ders_adi": "İslam Bilim Tarihi",
        "kod_prefix": "İBT",
        "varsayilan_sinif": "11",
        "csv_name": "Islam_Bilim_Tarihi_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "İklim, Çevre",
        "ders_adi": "İklim, Çevre ve Yenilikçi Çözümler",
        "kod_prefix": "İÇYÇ",
        "varsayilan_sinif": "11",
        "csv_name": "Iklim_Cevre_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "Sosyal Bilim",
        "ders_adi": "Sosyal Bilim Çalışmaları",
        "kod_prefix": "SBÇ",
        "varsayilan_sinif": "10",
        "csv_name": "Sosyal_Bilim_Calismalari_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "edebiyat",
        "ders_adi": "Türk Dili ve Edebiyatı",
        "kod_prefix": "TDE",
        "varsayilan_sinif": "9",
        "csv_name": "Turk_Dili_Edebiyati_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "ingilizce912",
        "ders_adi": "İngilizce",
        "kod_prefix": "ENG",
        "varsayilan_sinif": "9",
        "csv_name": "Ingilizce_TYMM_BEP_Havuzu.csv"
    },
    {
        "file_keyword": "hazırlıkingilizce",
        "ders_adi": "Hazırlık İngilizce",
        "kod_prefix": "EENG",
        "varsayilan_sinif": "Hazırlık",
        "csv_name": "Hazirlik_Ingilizce_TYMM_BEP_Havuzu.csv"
    }
]

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def adapt_to_bep_uda(ders_adi, uda_text):
    """
    Öğrenme çıktısı metninden özel eğitim öğrencisine uygun BEP Uzak Hedef metni üretir.
    """
    clean_uda = clean_text(uda_text)
    # Baştaki kodları temizle (örn: BİY.9.1.1. )
    clean_uda = re.sub(r'^[A-ZÇĞİÖŞÜ0-9\.\s]+\.\s*', '', clean_uda)
    # Sondaki fiil köklerini dönüştür (sorgulayabilme -> temel özelliklerini açıklar ve günlük hayatla ilişkilendirir)
    core = re.sub(r'(sorgulayabilme|yapılandırabilme|sınıflandırabilme|çözümleyebilme|karşılaştırabilme|değerlendirebilme|yorumlayabilme|ilişkilendirebilme|çözebilme|tümevarımsal akıl yürütebilme|özetleyebilme|çıkarım yapabilme|öngörüde bulunabilme|ayırt edebilme|analiz edebilme|uygulayabilme|tanımlayabilme|belirleyebilme)$', '', clean_uda, flags=re.IGNORECASE).strip()
    
    if len(core) < 10:
        core = clean_uda
        
    return f"Öğrenci, dönem sonunda {core} ile ilgili temel kavram ve özellikleri görsel kartlar ve modeller üzerinden tanır, adlandırır ve söyler."

def adapt_to_bep_kda(ders_adi, comp_text, step_no):
    """
    Resmî süreç bileşeninden özel eğitim öğrencisi için somut, ölçülebilir Revize KDA üretir.
    """
    clean_comp = clean_text(comp_text)
    # Fiilleri uyarlayarak somut eyleme dönüştür
    action = "gösterilen seçenekler arasından doğru seçip işaretler." if step_no % 2 == 1 else "resimli kartlar yardımıyla adlandırır/söyler."
    
    # Basitleştirilmiş cümle oluştur
    words = clean_comp.split()
    short_topic = " ".join(words[:8]) if len(words) > 8 else clean_comp
    short_topic = re.sub(r'[\.\,\;]$', '', short_topic)
    
    return f"{short_topic} konusundaki temel ögeleri {action}"

def process_subject(config):
    # İlgili PDF dosyasını bul
    matching_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf") and config["file_keyword"].lower() in f.lower()]
    if not matching_files:
        print(f"[-] Bulunamadı: {config['ders_adi']} ({config['file_keyword']})")
        return []

    pdf_filename = matching_files[0]
    pdf_path = os.path.join(PDF_FOLDER, pdf_filename)
    print(f"[+] İşleniyor: {config['ders_adi']} -> {pdf_filename}")
    
    try:
        doc = pymupdf.open(pdf_path)
    except Exception as e:
        print(f"Hata: {pdf_filename} açılamadı: {e}")
        return []

    prefix = config["kod_prefix"]
    ders_adi_base = config["ders_adi"]
    default_grade = config["varsayilan_sinif"]
    
    udas = {}
    current_unit = "1. Ünite"
    
    for page_idx in range(len(doc)):
        text = doc[page_idx].get_text()
        
        # Ünite/Tema başlığı tespiti
        unit_match = re.search(r'(\d+)\.\s*(?:TEMA|ÜNİTE)\s*:\s*([^\n\r]+)', text, re.IGNORECASE)
        if unit_match:
            u_num = unit_match.group(1)
            u_name = clean_text(unit_match.group(2))
            current_unit = f"{u_num}. ÜNİTE: {u_name}"
            
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # UDA Kodu tespiti (Örn: BİY.9.1.1 veya TDE1.1 veya SBTK.1.1)
            # Regex: prefix + (.) + grade/unit + (.) + num
            pattern_full = rf'^({re.escape(prefix)}\s*(?:\.\s*)?(\d{{1,2}})?\s*(?:\.\s*)?(\d{{1,2}})?\s*(?:\.\s*)?(\d{{1,2}})?)\s*\.\s*(.*)$'
            m = re.match(pattern_full, line)
            if m:
                raw_code = re.sub(r'\s+', '', m.group(1))
                # Sınıf düzeyi çıkarımı
                g_extracted = m.group(2)
                if g_extracted and g_extracted in ["9", "10", "11", "12"]:
                    grade = g_extracted
                else:
                    grade = default_grade
                    
                uda_text = m.group(5).strip()
                # Çok satırlı UDA metnini topla
                j = i + 1
                while j < len(lines) and not re.match(r'^[a-zçğıöşü]\)\s*', lines[j].strip()) and not re.match(rf'^{re.escape(prefix)}', lines[j].strip()) and len(lines[j].strip()) > 0:
                    uda_text += " " + lines[j].strip()
                    if any(lines[j].strip().endswith(end) for end in ['ebilme', 'abilme', 'bilme']):
                        i = j
                        break
                    if j - i > 3:
                        break
                    j += 1
                    
                uda_text = clean_text(uda_text)
                if len(uda_text) > 10 and raw_code not in udas:
                    udas[raw_code] = {
                        "code": raw_code,
                        "grade": grade,
                        "unit": current_unit,
                        "modul": current_unit.split(":")[-1].strip() if ":" in current_unit else current_unit,
                        "text": uda_text,
                        "components": {}
                    }
                    
            # Süreç bileşeni tespiti (a), b), c)...)
            comp_m = re.match(r'^([a-zçğıöşü])\)\s*(.*)$', line)
            if comp_m and udas:
                last_code = list(udas.keys())[-1]
                letter = comp_m.group(1)
                comp_text = comp_m.group(2).strip()
                j = i + 1
                while j < len(lines) and not re.match(r'^[a-zçğıöşü]\)\s*', lines[j].strip()) and not re.match(rf'^{re.escape(prefix)}', lines[j].strip()) and len(lines[j].strip()) > 0:
                    comp_text += " " + lines[j].strip()
                    if j - i > 3:
                        break
                    j += 1
                comp_text = clean_text(comp_text)
                if len(comp_text) > 5:
                    udas[last_code]["components"][letter] = comp_text
            i += 1
            
    # Eğer UDA tespit edilemediyse, sayfalardan genel tema ve kazanımları toparla
    if not udas:
        print(f"  [!] Standart kod formatı bulunamadı, temalar taranıyor...")
        for p in range(len(doc)):
            t = doc[p].get_text()
            matches = re.findall(rf'({re.escape(prefix)}[0-9\.\s]+)', t)
            for m in matches:
                c = re.sub(r'\s+', '', m).rstrip('.')
                if c not in udas:
                    udas[c] = {
                        "code": c,
                        "grade": default_grade,
                        "unit": current_unit,
                        "modul": "Genel Modül",
                        "text": f"{c} Öğrenme Çıktısı",
                        "components": {"a": "Temel kavramları açıklar.", "b": "Örnek olayları çözümler."}
                    }

    print(f"  --> {len(udas)} UDA elde edildi.")
    
    # 15 sütunluk veritabanı satırlarını oluştur
    rows = []
    for code, uda in udas.items():
        grade = uda["grade"]
        if grade in ["9", "10", "11", "12"]:
            ders_tam_adi = f"{ders_adi_base} {grade}.Sınıf"
        else:
            ders_tam_adi = f"{ders_adi_base} {default_grade}.Sınıf"
            
        uda_metni_full = f"{code}. {uda['text']}" if not uda['text'].startswith(code) else uda['text']
        bep_uda_metni = adapt_to_bep_uda(ders_adi_base, uda['text'])
        
        comps = uda["components"]
        if not comps:
            comps = {
                "a": f"{uda['text']} ile ilgili temel kuralları/kavramları tanımlar.",
                "b": f"{uda['text']} ile ilgili örnekleri sınıflandırır."
            }
            
        step_idx = 1
        for letter, c_text in comps.items():
            # 1. Resmî MEB Satırı
            rows.append([
                "TYMM",
                ders_tam_adi,
                grade,
                uda["modul"],
                uda["unit"],
                code,
                uda_metni_full,
                bep_uda_metni,
                f"1.{step_idx}",
                c_text,
                "MEB_Resmi",
                "%75 Başarı ile",
                "Anlatım, Soru-Cevap, Görsel İnceleme",
                "Ders Kitabı, Şemalar, Akıllı Tahta",
                "EVET"
            ])
            
            # 2. Revize BEP Satırı
            revize_text = adapt_to_bep_kda(ders_adi_base, c_text, step_idx)
            rows.append([
                "TYMM",
                ders_tam_adi,
                grade,
                uda["modul"],
                uda["unit"],
                code,
                uda_metni_full,
                bep_uda_metni,
                f"KDA 1.{step_idx}",
                revize_text,
                "Revize_Temel",
                "%70 Başarı ile",
                "Doğrudan Öğretim, Gösterip Yaptırma, Model Olma",
                "Görsel Kartlar, Resimli Çalışma Yaprakları, Model/Maket",
                "EVET"
            ])
            step_idx += 1
            
    # Bireysel CSV dosyasını kaydet
    csv_file_path = os.path.join(OUTPUT_FOLDER, config["csv_name"])
    with open(csv_file_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows(rows)
        
    print(f"  [OK] {len(rows)} satır yazıldı: {config['csv_name']}")
    return rows

def main():
    print("=== TÜM MÜFREDATLAR İÇİN BEP HAVUZU OLUŞTURMA BAŞLATILDI ===")
    all_master_rows = []
    
    for cfg in SUBJECT_CONFIGS:
        subject_rows = process_subject(cfg)
        all_master_rows.extend(subject_rows)
        
    # Tüm dersleri birleştiren Genel Master CSV
    master_csv_path = os.path.join(OUTPUT_FOLDER, "Tum_Dersler_TYMM_BEP_Havuzu.csv")
    with open(master_csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows(all_master_rows)
        
    print("===========================================================")
    print(f"TÜM DERSLER TAMAMLANDI! Toplam {len(all_master_rows)} satır oluşturuldu.")
    print(f"Master CSV Dosyası: {master_csv_path}")

if __name__ == "__main__":
    main()
