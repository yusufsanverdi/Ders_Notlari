# Yapay Zekâya Giriş – Kapsamlı ve Modüler Ders Notları (Vize Müfredatı: 1–9. Haftalar)

Bu dizin, **Dr. Seda Bayat Tosun** tarafından yürütülen **Yapay Zekâya Giriş** dersinin tüm transkriptleri, ders içi soru-cevap oturumları, tahta analizleri, haftalık sunum slaytları (`Hafta01`–`Hafta09`) ve Colab defterleri taranarak pedagojik bir öğrenme sırasına göre yapılandırılmış modüler ders notlarını içermektedir.

Tüm konu anlatımları `assets/` klasöründeki yüksek çözünürlüklü teknik şemalar ve grafiklerle desteklenmiş; yardımcı Python çizim scriptleri ise `tools/` klasöründe toplanmıştır.

> [!IMPORTANT]
> **VİZE SINAVI KAPSAMI VE FORMATI:**
> * **Kapsam:** Yalnızca **ilk 8-9 haftanın** konuları dahildir (Hafta 10–14 vizeye dahil değildir).
> * **Format:** Test (çoktan seçmeli) formatında yaklaşık **20 soru** sorulacaktır. Kod yazımı kesinlikle sorulmayacaktır.
> * **İçerik:** Temel kavramlar, mimari karşılaştırmalar, hocanın derste vurguladığı 16 vize sorusu ve **garanti bir adet matris/boyut hesaplama sorusu** yer alacaktır.

---

## 📚 Müfredat ve Modül İndeksi

| Modül No | Konu Başlığı | Dosya Bağlantısı | Ana İçerikler ve Vize Sınavı Odakları |
| :---: | :--- | :--- | :--- |
| **01** | **Yapay Zekâya Giriş, Tarihçe ve Temel Paradigmalar** | [01_Yapay_Zekaya_Giris_ve_Tarihce.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/01_Yapay_Zekaya_Giris_ve_Tarihce.md) | Alan Turing ve Turing Testi (Taklit Oyunu), Dar/Genel/Süper YZ, $YZ \supset ML \supset DL \supset Üretken\ YZ$ hiyerarşisi, Geleneksel Programlama vs ML paradigması, Mitchell'in $T, E, P$ tanımı, PEAS modeli, Derin Öğrenmeyi başlatan 3 etken, Veri gizliliği ve insan faktörü. |
| **02** | **Makine Öğrenmesinin Temelleri ve Veri Ön İşleme** | [02_Makine_Ogrenmesinin_Temelleri_ve_Veri_On_Isleme.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/02_Makine_Ogrenmesinin_Temelleri_ve_Veri_On_Isleme.md) | Denetimli (Sınıflandırma/Regresyon), Denetimsiz (Kümeleme/Boyut İndirgeme) ve Pekiştirmeli (RL/RLHF) öğrenme, Train (%70) / Val (%15) / Test (%15) bölümleme, **Veri Sızıntısı (Data Leakage) tehlikesi**, Overfitting vs Underfitting, Eksik veri (medyan/mod), Min-Maks normalizasyonu ($x'$ hesabı), Z-skoru, Label vs One-Hot Encoding yapay sıralama tuzağı. |
| **03** | **Doğrusal Regresyon, Kayıp Fonksiyonları ve Gradyan İnişi** | [03_Regresyon_ve_Gradyan_Inis.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/03_Regresyon_ve_Gradyan_Inis.md) | Basit Doğrusal Regresyon ($\hat{y} = wx + b$), Artıklar ($e_i$), MSE, RMSE ve MAE kayıp fonksiyonları, $R^2$ Belirlilik Katsayısı ($R^2=0$ ortalama tahmini anlamı), **Gradyan İnişi güncelleme kuralı ($w_{t+1} = w_t - \eta \frac{\partial L}{\partial w}$ sayısal adımı)**, Öğrenme Oranı ($\eta$) davranışları (yavaş, ideal, ıraksama), Batch vs SGD vs Mini-Batch GD. |
| **04** | **Sınıflandırma Yöntemleri ve Karar Sınırları** | [04_Siniflandirma_Yontemleri.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/04_Siniflandirma_Yontemleri.md) | Karar Sınırı, Lojistik Regresyon ve Sigmoid Fonksiyonu ($\sigma(z)$), İkili Çapraz Entropi (Log-Loss) sayısal hesabı, k-NN algoritması, **$k=1$ aşırı öğrenme tuzağı**, k-NN'de ölçekleme zorunluluğu, Karar Ağaçları (Entropi, Gini Kirliliği, Bilgi Kazancı), Naive Bayes koşullu bağımsızlık varsayımı, Destek Vektör Makineleri (SVM) ve Marj maksimizasyonu. |
| **05** | **Model Değerlendirme Metrikleri, ROC/AUC ve Kümeleme** | [05_Model_Degerlendirme_ve_Kumeleme.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/05_Model_Degerlendirme_ve_Kumeleme.md) | Karışıklık Matrisi (TP, TN, FP, FN), Doğruluk, Kesinlik (Precision), Duyarlılık (Recall), F1-Skoru formülleri ve sayısal soru çözümü, Kanser teşhisinde Recall vs Spam filtresinde Precision önceliği, **ROC Eğrisi ve AUC (AUC=0.5 rastgele tahmin anlamı)**, k-Katlı Çapraz Doğrulama, Yanlılık-Varyans dengesi, L1 (Lasso) vs L2 (Ridge), K-Means Kümeleme ve Dirsek Yöntemi. |
| **06** | **Yapay Sinir Ağları (YSA), Perceptron ve MLP** | [06_Yapay_Sinir_Aglari_ve_MLP.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/06_Yapay_Sinir_Aglari_ve_MLP.md) | Biyolojik vs Yapay Nöron eşleşmesi, Tek nöron çıktısı sayısal hesabı ($z = w^Tx + b$ ve ReLU), Frank Rosenblatt Perceptron'u, **Minsky-Papert XOR çıkmazı ve 1. YZ Kışı**, Çok Katmanlı Algılayıcı (MLP) ve Gizli Katman, Doğrusal olmayan aktivasyonların zorunluluğu, Aktivasyonlar (Sigmoid, Tanh, ReLU, Leaky ReLU), **Tam Bağlantılı katman parametre sayısı formülü ($(N_{in}\times N_{out})+N_{out}$)**, Çıkış katmanı seçim tablosu. |
| **07** | **Derin Ağların Eğitimi, Geri Yayılım ve Optimizasyon** | [07_Derin_Ogrenme_Aglarin_Egitimi_ve_Optimizasyon.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/07_Derin_Ogrenme_Aglarin_Egitimi_ve_Optimizasyon.md) | Softmax formülü ve Kategorik Çapraz Entropi sayısal hesabı, Eğitim döngüsünün 4 adımı, **Epoch vs Batch Size vs İterasyon**, Geri Yayılım (Backpropagation) ve Zincir Kuralı, Geri yayılımda ReLU türevinin $z<0$ iken gradyanı sıfırlaması, Kaybolan Gradyan sorunu ve ReLU çözümü, Optimizasyon algoritmaları (SGD, Momentum, RMSProp, Adam), **Aşırı Öğrenme Karşıtı Savunma (Dropout, Erken Durdurma, Batch Normalization)**. |
| **08** | **Görüntü İşlemenin Temelleri, Filtreler ve 2D Evrişim** | [08_Goruntu_Islemenin_Temelleri_ve_Evrisim.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/08_Goruntu_Islemenin_Temelleri_ve_Evrisim.md) | Dijital görüntü piksel matrisi yapısı, Gri ton vs RGB (3 kanal) vs HSV, **Sıkıştırılmamış RGB görüntü bellek hesabı ($W \times H \times 3\text{ B}$)**, Histogram Eşitleme (kontrast düşüklüğü çözümü), Otsu Eşikleme, 2D Kayan pencere evrişimi, **Tuz-Biber gürültüsünde Medyan Filtresi tercihi**, Sobel Kenar Operatörleri ($G_x, G_y$), Canny kenar algoritmasının 4 adımı, Morfolojik işlemler (Aşınma/Genişleme), Geleneksel CV'den CNN'e köprü. |
| **09** | **Evrişimli Sinir Ağları (CNN) Mimarisi ve Hesaplamalar** | [09_Evrisimli_Sinir_Aglari_CNN_Mimarisi.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/notlar/09_Evrisimli_Sinir_Aglari_CNN_Mimarisi.md) | **Neden MLP değil de CNN? (Parametre patlaması, uzamsal kayıp, yerel bağlantı, ağırlık paylaşımı, öteleme değişmezliği)**, **Çıktı boyutu formülü ($\lfloor\frac{W-K+2P}{S}\rfloor+1$)**, Conv parametre sayısı formülü, **Pooling katmanının kaldırılması sonucu (parametre patlaması)**, Max vs Average Pooling (0 parametre), **Flatten quiz hesabı ($32\times32\times16=16.384$ / $8.192$)**, LeNet-5 mimarisi katman analizi, Öznitelik hiyerarşisi, CNN'in ses spektrogramlarında kullanımı. |

---

## 🛠️ Klasör ve Dosya Organizasyonu

```text
Yapay_Zekaya_Giris/
├── notlar/                                           # 1-9. Hafta modüler ders notları
│   ├── 01_Yapay_Zekaya_Giris_ve_Tarihce.md
│   ├── 02_Makine_Ogrenmesinin_Temelleri_ve_Veri_On_Isleme.md
│   ├── 03_Regresyon_ve_Gradyan_Inis.md
│   ├── 04_Siniflandirma_Yontemleri.md
│   ├── 05_Model_Degerlendirme_ve_Kumeleme.md
│   ├── 06_Yapay_Sinir_Aglari_ve_MLP.md
│   ├── 07_Derin_Ogrenme_Aglarin_Egitimi_ve_Optimizasyon.md
│   ├── 08_Goruntu_Islemenin_Temelleri_ve_Evrisim.md
│   ├── 09_Evrisimli_Sinir_Aglari_CNN_Mimarisi.md
│   └── README.md                                     # Ana dizin rehberi (Bu dosya)
├── assets/                                           # Yüksek çözünürlüklü teknik şemalar
│   ├── ai_hierarchy_and_programming_paradigms.png
│   ├── ml_workflow_data_split_leakage.png
│   ├── classification_metrics_roc_curve.png
│   ├── gradient_descent_learning_rate.png
│   ├── perceptron_xor_mlp_decision_boundary.png
│   ├── convolution_stride_padding_matrix.png
│   ├── pooling_max_vs_average_flatten.png
│   └── cnn_full_architecture_lenet5.png
├── tools/                                            # Çizim ve soru bankası üretim scriptleri
│   ├── plot_ai_hierarchy_and_programming.py
│   ├── plot_ml_workflow_and_metrics.py
│   ├── plot_gradient_and_perceptron.py
│   ├── plot_convolution_and_pooling.py
│   ├── plot_cnn_architecture.py
│   ├── generate_question_bank.py
│   ├── qbank_sections_1_to_3.py
│   ├── qbank_sections_4_to_6.py
│   └── qbank_sections_7_to_10.py
├── Sinav_Sorulari_ve_Cozumleri.md                    # 200 soruluk kapsamlı interaktif toggle soru bankası
├── Yapay Zekaya Giriş 401a7e1cf07380b898c0dabb749c4775.md # Ham ders transkripti
└── Yapay_Zekaya_Giris_Haftalik/                      # Orijinal PPTX ve Colab defterleri
    ├── slaytlar/ (Hafta01 - Hafta14)
    └── colab_defterleri/ (Hafta01 - Hafta14)
```

---

## 💡 Vize Sınavına Hazırlık ve Çalışma Stratejisi

1. **Modülleri Sırayla Okuyun:** Her modülün başındaki **🚨 HOCANIN VİZE SINAVI UYARILARI** kutucuklarını mutlaka ezberleyin.
2. **Görselleri İnceleyin:** `assets/` klasöründeki şemaları gözünüzde canlandırın (Özellikle 2D evrişim matrisi, Max/Avg pooling ve CNN mimari akışı).
3. **İnteraktif Soru Bankasını Çözün:** [Sinav_Sorulari_ve_Cozumleri.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Yapay_Zekaya_Giris/Sinav_Sorulari_ve_Cozumleri.md) dosyasındaki 200 soruyu önce cevabı açmadan bir kağıda elle çözün, ardından `<details>` toggle'ına tıklayarak cevabınızı karşılaştırın.
4. **Deneme Sınavını Çözün:** Dokümanın 10. bölümündeki 20 soruluk deneme sınavını 30 dakikalık süre tutarak gerçek sınav simülasyonu şeklinde tamamlayın.
