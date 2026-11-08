# Derin Öğrenme Dersi – Kapsamlı ve Modüler Ders Notları

Bu dizin, Derin Öğrenme dersinin tüm transkriptleri, teorik anlatımları, hocanın vurguladığı sınav ipuçları, analojiler ve matematiksel hesaplamalar taranarak pedagojik bir öğrenme sırasına göre hazırlanmış modüler ders notlarını içermektedir.

Tüm matematiksel formüller KaTeX / LaTeX standartlarında hazırlanmış, `assets/` klasöründeki yüksek çözünürlüklü şemalar ve grafiklerle desteklenmiş; yardımcı Python scriptleri ise `tools/` klasöründe toplanmıştır.

---

## 📚 Müfredat ve Bölüm İndeksi

| Bölüm No | Konu Başlığı | Dosya Bağlantısı | Ana İçerikler ve Sınav Odakları |
| :---: | :--- | :--- | :--- |
| **01** | **Giriş ve Temel Kavramlar** | [01_Giris_ve_Temel_Kavramlar.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/01_Giris_ve_Temel_Kavramlar.md) | AI-ML-DL Hiyerarşisi, Denetimli/Denetimsiz Öğrenme, Sınıflandırma vs. Regresyon, Spam/Phishing vakası, İHA ile Kenevir Tespiti, Train/Val/Test bölümlemesi. |
| **02** | **Matematiksel Altyapı ve Veri Temsili** | [02_Matematiksel_Altyapi_ve_Veri_Temsili.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/02_Matematiksel_Altyapi_ve_Veri_Temsili.md) | Skaler (0D), Vektör (1D), Matris (2D), Tensör (ND), Grayscale vs. RGB ($H \times W \times C$), Piksel değerleri, Matris Çarpımı boyutu, Ortalama/Varyans/Normalizasyon ($Z$). |
| **03** | **YSA ve Nöron Mimarisi** | [03_Yapay_Sinir_Aglari_ve_Noron_Mimarisi.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/03_Yapay_Sinir_Aglari_ve_Noron_Mimarisi.md) | Biyolojik vs. Yapay Nöron, $Z = W \cdot X + b$, Ağırlıkların önemi (Ev fiyatı örneği), Bias ve Bisiklet analojisi, Doğrusallık dışılık zorunluluğu, Sigmoid, Tanh, ReLU, Leaky ReLU, Softmax. |
| **04** | **Model Eğitimi, Kayıp ve Optimizasyon** | [04_Model_Egitimi_Kayip_ve_Optimizasyon.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/04_Model_Egitimi_Kayip_ve_Optimizasyon.md) | İleri ve Geri Yayılım (Backprop), MSE, Binary & Categorical Cross-Entropy, Gradyan İnişi, Öğrenme Oranı ($\alpha$), Epoch, Batch Size ve İterasyon ilişkisi, SGD ve Adam. |
| **05** | **Model Başarımı ve Aşırı Öğrenme** | [05_Model_Basarimi_ve_Asiri_Ogrenme.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/05_Model_Basarimi_ve_Asiri_Ogrenme.md) | Accuracy limitleri, Genelleme (Generalization), Overfitting vs. Underfitting (Çıkmış soru ezberleyen öğrenci analojisi), Dropout katmanı (Unutma mekanizması), Veri Artırma kuralları, Early Stopping, Ablasyon. |
| **06** | **CNN Mimarisi ve Hesaplamalar** | [06_CNN_Mimarisi_ve_Hesaplamalar.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/06_CNN_Mimarisi_ve_Hesaplamalar.md) | **[SINAVIN MERKEZİ]** Dense ağların resimlerde çöküşü, Conv2D, MaxPool (24 saat analojisi), Flatten, Parametre sayısı formülleri, $W_{out} = \lfloor \frac{W-K+2P}{S} \rfloor + 1$, Altın Kısayol ($3 \times 3, S=1, P=1$), Tahtadaki Quiz sorusu çözümü (8192). |
| **07** | **Klasik ve Modern CNN Mimarileri** | [07_Klasik_ve_Modern_CNN_Mimarileri.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/07_Klasik_ve_Modern_CNN_Mimarileri.md) | LeNet-5 (1998, MNIST), AlexNet (2012, ReLU, Dropout, GPU), VGGNet (İki $3 \times 3$ vs bir $5 \times 5$), ResNet (Skip Connection, Asansör analojisi), MobileNet (Depthwise Separable Conv, Quiz sorusu), EfficientNet (Compound Scaling). |
| **08** | **Transfer Öğrenme ve İnce Ayar** | [08_Transfer_Ogrenme_ve_Ince_Ayar.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/08_Transfer_Ogrenme_ve_Ince_Ayar.md) | Pre-trained model nedir? ("Sizler de birer pre-trained modelsiniz" analojisi), Katman dondurma (`requires_grad = False`), Fine-Tuning kuralları, Felaket Unutması (Catastrophic Forgetting), Etiketleme araçları (Roboflow). |
| **09** | **Nesne Tespiti ve YOLO Mimarisi** | [09_Nesne_Tespiti_ve_YOLO_Mimarisi.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/09_Nesne_Tespiti_ve_YOLO_Mimarisi.md) | Sınıflandırma vs. Konumlandırma vs. Nesne Tespiti vs. Segmentasyon, Bounding Box $(x_c, y_c, w, h)$ normalizasyonu, İki aşamalı vs. Tek aşamalı modeller, YOLO $S \times S$ ızgara ve sorumlu hücre mantığı, Otonom sürüş (Tesla/TOGG). |
| **10** | **Nesne Tespiti Metrikleri ve Analizi** | [10_Nesne_Tespiti_Metrikleri_ve_Matematiksel_Analizi.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/10_Nesne_Tespiti_Metrikleri_ve_Matematiksel_Analizi.md) | **[SINAV UYARISI]** IoU (Kesişim / Birleşim) formülü ve hesabı, TP, FP, FN durumları, Precision, Recall, F1-Score, PR Eğrisi, AP ve mAP (mAP@0.5 vs. mAP@0.5:0.95), Sayısal örnek vaka çözümü. |
| **11** | **Üretken Modeller: GAN ve Halüsinasyon** | [11_Uretken_Modeller_GAN_ve_Halusinasyon.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/11_Uretken_Modeller_GAN_ve_Halusinasyon.md) | Ayırt Edici vs. Üretici modeller, Minimax oyunu, Üreteç (Kalpazan) vs. Ayırt Edici (Polis), Nash Dengesi, DCGAN, CycleGAN, StyleGAN, Halüsinasyon kavramı ve tıbbi/mühendislik riskleri. |
| **12** | **Pratik Uygulamalar ve Hata Analizi** | [12_Pratik_Muhendislik_Uygulamalari_ve_Hata_Analizi.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Derin_Ogrenme/notlar/12_Pratik_Muhendislik_Uygulamalari_ve_Hata_Analizi.md) | Arka Plan Yanlılığı ("Kediye Kurbağa Dedi!" laboratuvar vakası), Ses sinyallerinin Spektrogram ile 2D CNN'e aktarılması, GPU VRAM ve OOM yönetimi, Model budama ve nicemleme (Quantization). |

---

## 🛠️ Klasör ve Dosya Organizasyonu

```text
Derin_Ogrenme/
├── assets/                                          # Yüksek çözünürlüklü grafikler ve şemalar
│   ├── ai_ml_dl_hierarchy.png
│   ├── ml_types.png
│   ├── tensors_overview.png
│   ├── rgb_channels_breakdown.png
│   ├── activation_functions.png
│   ├── single_neuron_math.png
│   ├── learning_rate_comparison.png
│   ├── overfitting_curve.png
│   ├── dropout_mechanism.png
│   ├── cnn_architecture_flow.png
│   ├── convolution_stride_padding.png
│   ├── resnet_skip_connection.png
│   ├── cnn_models_timeline.png
│   ├── transfer_learning_finetuning.png
│   ├── cv_tasks_comparison.png
│   ├── yolo_grid_bounding_box.png
│   ├── iou_mathematical_diagram.png
│   ├── precision_recall_map_curve.png
│   ├── gan_architecture_diagram.png
│   ├── audio_spectrogram_2d_cnn.png
│   └── background_bias_cat_frog.png
├── tools/                                           # Diyagramları üreten Python scriptleri
│   ├── plot_ai_hierarchy.py
│   ├── plot_tensors_and_channels.py
│   ├── plot_activations_and_neuron.py
│   ├── plot_gradient_descent.py
│   ├── plot_overfitting_dropout.py
│   ├── plot_cnn_architecture.py
│   ├── plot_architectures_resnet.py
│   ├── plot_transfer_learning.py
│   ├── plot_object_detection_tasks.py
│   ├── plot_iou_and_metrics.py
│   ├── plot_gan_architecture.py
│   └── plot_audio_spectrogram.py
└── notlar/                                          # Modüler ders notları
    ├── README.md                                    # İndeks ve Müfredat Rehberi (Bu dosya)
    ├── 01_Giris_ve_Temel_Kavramlar.md
    ├── 02_Matematiksel_Altyapi_ve_Veri_Temsili.md
    ├── 03_Yapay_Sinir_Aglari_ve_Noron_Mimarisi.md
    ├── 04_Model_Egitimi_Kayip_ve_Optimizasyon.md
    ├── 05_Model_Basarimi_ve_Asiri_Ogrenme.md
    ├── 06_CNN_Mimarisi_ve_Hesaplamalar.md
    ├── 07_Klasik_ve_Modern_CNN_Mimarileri.md
    ├── 08_Transfer_Ogrenme_ve_Ince_Ayar.md
    ├── 09_Nesne_Tespiti_ve_YOLO_Mimarisi.md
    ├── 10_Nesne_Tespiti_Metrikleri_ve_Matematiksel_Analizi.md
    ├── 11_Uretken_Modeller_GAN_ve_Halusinasyon.md
    └── 12_Pratik_Muhendislik_Uygulamalari_ve_Hata_Analizi.md
```
