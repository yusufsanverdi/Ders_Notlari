# Python script to build the complete 200-question comprehensive bank
import os

output_file = "Yapay_Zekaya_Giris/Sinav_Sorulari_ve_Cozumleri.md"

def build_bank():
    # We will assemble the bank in well-structured sections
    parts = []
    
    parts.append("""# Yapay Zekâya Giriş Vize Sınavına Hazırlık: 200 Soruluk Kapsamlı ve İnteraktif Soru Bankası

Bu doküman, **Dr. Seda Bayat Tosun** tarafından yürütülen **Yapay Zekâya Giriş** dersinin tüm transkriptleri, ders içi soru-cevap oturumları, haftalık sunum slaytları (`Hafta01`–`Hafta09`) ve Colab defterleri taranarak **sadece vize kapsamındaki ilk 8-9 haftanın** konularını kapsayacak şekilde hazırlanmış resmi soru bankasıdır.

İçerisinde:
- **Çoktan Seçmeli (Test) Soruları:** Kavramsal, mimari, model karşılaştırmalı,
- **Sayısal ve Matris Hesaplama Soruları:** 2D evrişim matris çarpımları, çıktı boyut formülleri, parametre hesapları, bellek hesabı, gradyan güncellemesi, normalizasyon ve metrik türetimleri,
- **Doğru / Yanlış (Gerekçeli) Soruları:** Sınavda şaşırtmaca yaratabilecek ince teknik detaylar,
- **Senaryo ve Vaka Analizi Soruları:** Gerçek hayat mühendislik problemleri, aşırı öğrenme teşhisi, gürültü temizleme ve metrik seçimi,
- **Hocanın Derste Bizzat Sorduğu 16 Vize Sorusu ve Gerçek Sınav Uyarıları**,
- **20 Soruluk Gerçek Formatlı Vize Deneme Sınavı** yer almaktadır.

> [!TIP]
> **Çalışma Yöntemi (Self-Testing):**
> Tüm soruların cevapları ve ayrıntılı çözüm adımları **açılır-kapanır (toggle / `<details>`)** kutular içerisine gizlenmiştir. Çalışırken önce soruyu okuyup kendi cevabınızı bir kağıda yazınız; ardından **"🔍 Çözümü ve Detaylı Anlatımı Gör"** butonuna tıklayarak cevabınızı ve gerekçenizi kontrol ediniz.

---

## 📑 İÇİNDEKİLER VE MÜFREDAT SIRASI

1. [BÖLÜM 1: Hafta 01 – Yapay Zekâya Giriş, Tarihçe, Turing Testi ve Paradigmalar (Soru 1 – 18)](#bölüm-1-hafta-01--yapay-zekâya-giriş-tarihçe-turing-testi-ve-paradigmalar)
2. [BÖLÜM 2: Hafta 02 – Makine Öğrenmesinin Temelleri, Yaşam Döngüsü ve Veri Ön İşleme (Soru 19 – 36)](#bölüm-2-hafta-02--makine-öğrenmesinin-temelleri-yaşam-döngüsü-ve-veri-ön-i̇şleme)
3. [BÖLÜM 3: Hafta 03 – Doğrusal Regresyon, Kayıp Fonksiyonları ve Gradyan İnişi (Soru 37 – 54)](#bölüm-3-hafta-03--doğrusal-regresyon-kayıp-fonksiyonları-ve-gradyan-i̇nişi)
4. [BÖLÜM 4: Hafta 04 – Sınıflandırma Yöntemleri (Lojistik Regresyon, k-NN, Ağaçlar, Naive Bayes, SVM) (Soru 55 – 74)](#bölüm-4-hafta-04--sınıflandırma-yöntemleri)
5. [BÖLÜM 5: Hafta 05 – Model Değerlendirme, Karışıklık Matrisi, ROC/AUC ve Kümeleme (Soru 75 – 94)](#bölüm-5-hafta-05--model-değerlendirme-karışıklık-matrisi-rocauc-ve-kümeleme)
6. [BÖLÜM 6: Hafta 06 – Yapay Sinir Ağları (YSA), Perceptron, XOR ve MLP Mimarisi (Soru 95 – 114)](#bölüm-6-hafta-06--yapay-sinir-ağları-ysa-perceptron-xor-ve-mlp-mimarisi)
7. [BÖLÜM 7: Hafta 07 – Derin Ağların Eğitimi, Geri Yayılım ve Optimizasyon (Soru 115 – 134)](#bölüm-7-hafta-07--derin-ağların-eğitimi-geri-yayılım-ve-optimizasyon)
8. [BÖLÜM 8: Hafta 08 – Görüntü İşlemenin Temelleri, Filtreler ve 2D Evrişim (Soru 135 – 154)](#bölüm-8-hafta-08--görüntü-i̇şlemenin-temelleri-filtreler-ve-2d-evrişim)
9. [BÖLÜM 9: Hafta 09 – Evrişimli Sinir Ağları (CNN), Katmanlar ve Boyut Hesaplamaları (Soru 155 – 180)](#bölüm-9-hafta-09--evrişimli-sinir-ağları-cnn-katmanlar-ve-boyut-hesaplamaları)
10. [BÖLÜM 10: Hocanın Formatında 20 Soruluk Tam Kapsamlı Vize Deneme Sınavı (Soru 181 – 200)](#bölüm-10-hocanın-formatında-20-soruluk-tam-kapsamlı-vize-deneme-sınavı)

---
""")
    return parts

def main():
    import sys
    sys.path.append('Yapay_Zekaya_Giris/tools')
    import qbank_sections_1_to_3 as s13
    import qbank_sections_4_to_6 as s46
    import qbank_sections_7_to_10 as s710

    parts = build_bank()
    parts.append(s13.get_section_1())
    parts.append(s13.get_section_2())
    parts.append(s13.get_section_3())
    parts.append(s46.get_section_4())
    parts.append(s46.get_section_5())
    parts.append(s46.get_section_6())
    parts.append(s710.get_section_7())
    parts.append(s710.get_section_8())
    parts.append(s710.get_section_8_and_beyond())

    full_content = "\n\n".join(parts) + "\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"Successfully generated {output_file} ({len(full_content)} bytes)")

if __name__ == "__main__":
    main()
