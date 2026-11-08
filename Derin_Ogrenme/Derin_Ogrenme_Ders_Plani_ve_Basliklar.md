# Derin Öğrenme Dersi: Konu Başlıkları ve Öğrenme Sırası Müfredatı

Bu doküman, ders transkriptinde işlenen tüm teorik ve uygulamalı konuların mantıksal, pedagojik bir öğrenme sırasına göre düzenlenmiş başlık ve alt başlık iskeletidir.

---

## 1. Giriş ve Temel Kavramlar
### 1.1. Yapay Zekanın Temel Alanları ve Hiyerarşisi
- Yapay Zeka (AI), Makine Öğrenmesi (ML) ve Derin Öğrenme (DL) Tanımları
- Kural Tabanlı Programlama vs. Veriden Öğrenen Sistemler (Örnek Vaka: Spam / Phishing Tespiti)
### 1.2. Makine Öğrenmesi Türleri ve Problem Tipleri
- Denetimli Öğrenme (Supervised Learning): Sınıflandırma (Classification) vs. Regresyon (Regression)
- Denetimsiz Öğrenme (Unsupervised Learning): Kümeleme (Clustering)
- Pekiştirmeli Öğrenme (Reinforcement Learning) Kavramı
### 1.3. Derin Öğrenmenin Tarihsel Gelişimi ve Yükseliş Nedenleri
- YSA'nın Tarihçesi ve "Yapay Zeka Kışları"
- Yükselişi Tetikleyen Üç Temel Unsur: Büyük Veri (Big Data), Paralel Hesaplama (GPU) ve Algoritmik Gelişmeler
### 1.4. Veri Seti Bölümleme ve Değerlendirme Esasları
- Eğitim (Train), Doğrulama (Validation) ve Test Kümelerinin Rolleri

---

## 2. Matematiksel Altyapı ve Veri Temsili
### 2.1. Çok Boyutlu Veri Temsili ve Lineer Cebir Temelleri
- Skaler (0D), Vektör (1D), Matris (2D) ve Tensör (ND) Kavramları
- Öznitelik (Feature) Vektörü Mantığı
### 2.2. Bilgisayarlı Görüde Görüntü Temsili ve Renk Kanalları
- Piksel Değerleri ve Matris Karşılığı ($0 - 255$)
- Grayscale ($H \times W \times 1$) vs. RGB ($H \times W \times 3$) Temsili ve Biyolojik Altyapı
### 2.3. Matris İşlemleri ve Tensör Manipülasyonları
- Matris Toplaması, Skalerle Çarpım ve Matris Çarpımı Kuralları
### 2.4. Temel İstatistiksel Ölçütler
- Aritmetik Ortalama, Varyans ve Standart Sapma

---

## 3. Yapay Sinir Ağlarının (YSA / ANN) Temelleri ve Nöron Mimarisi
### 3.1. Biyolojik Nörondan Yapay Nörona (Perceptron)
- Biyolojik Nöron Yapısı (Dendrit, Akson, Sinaps) ile Yapay Karşılıkları
### 3.2. Tek Bir Nöronun Matematiksel Modeli
- Girdi Vektörü ($X$), Ağırlık Vektörü ($W$) ve Lineer Kombinasyon ($Z = \sum w_i x_i + b = W \cdot X + b$)
- Ağırlıkların (Weights) Anlamı ve Önemi (Ev Fiyatı / Kredi Tahmini Örneği)
- Sapma / Öteleme (Bias) Parametresinin Mantığı ve Gerekliliği (Bisiklet / Yokuş Analojisi)
### 3.3. Aktivasyon Fonksiyonları ve Doğrusallık Dışılık (Non-Linearity)
- Doğrusal Olmayan Dönüşümlerin Neden Zorunlu Olduğu
- Sigmoid Fonksiyonu: Formülü, Çıkış Aralığı ($0, 1$) ve Doygunluk Problemi
- Hiperbolik Tanjant (Tanh): Formülü ve Sıfır Merkezli (Zero-Centered) Yapısı ($-1, 1$)
- ReLU (Rectified Linear Unit): Formülü, Hesaplama Avantajı ve "Ölü Nöron" Sorunu
- Leaky ReLU: Negatif Eğim Çözümü
- Softmax Fonksiyonu: Çok Sınıflı Çıktılarda Olasılık Dağılımına Dönüştürme Mantığı

---

## 4. Model Eğitimi, Kayıp Fonksiyonları ve Optimizasyon
### 4.1. İleri Yayılım (Forward Propagation) Süreci
- Katmanlar Boyunca Bilgi Akışı ve Tahmin Üretimi
### 4.2. Kayıp / Maliyet Fonksiyonları (Loss / Cost Functions)
- Regresyon İçin: Ortalama Kare Hata (MSE)
- Sınıflandırma İçin: Çapraz Entropi (Cross-Entropy Loss / Binary & Categorical)
### 4.3. Geri Yayılım (Backpropagation) ve Gradyan İnişi (Gradient Descent)
- Hatanın Geri Dağıtılması ve Zincir Kuralı (Chain Rule) Sezgisi
- Gradyan Vektörü ve Ağırlık Güncelleme Mantığı
### 4.4. Öğrenme Oranı (Learning Rate - $\alpha$)
- Küçük vs. Büyük Öğrenme Oranlarının Riskleri ve Yerel Minimum Sorunu
### 4.5. Eğitim Döngüsü Hiperparametreleri
- Epoch, Batch Size ve İterasyon İlişkisi ve Farkları
### 4.6. Modern Optimizasyon Algoritmaları
- Standart Gradyan İnişi (GD), Stokastik Gradyan İnişi (SGD) ve Adam Optimizer

---

## 5. Model Başarımı, Genelleme ve Aşırı Öğrenme ile Mücadele
### 5.1. Performans Kriterleri ve Değerlendirme
- Doğruluk (Accuracy) Tanımı ve Dengesiz Veri Kümelerindeki Yanıltıcılığı
- Genelleme Yeteneği (Generalization) ve Gerçek Dünya Senaryoları
### 5.2. Aşırı Öğrenme (Overfitting) ve Eksik Öğrenme (Underfitting)
- Overfitting Belirtileri (Eğitim Kaybı Düşerken Doğrulama Kaybının Artması)
- Underfitting Nedenleri ve Çözümleri
### 5.3. Düzenlileştirme (Regularization) Teknikleri
- Dropout Katmanı: Rastgele Nöron Devre Dışı Bırakma, Unutma Mekanizması ve Topluluk (Ensemble) Etkisi
- Ağırlık Cezalandırma (Weight Decay / L1 - L2 Regularization)
- Veri Artırma (Data Augmentation): Döndürme, Kırpma, Parlaklık vb. İşlemlerin Sadece Train Kümesine Uygulanma İlkesi
- Erken Durdurma (Early Stopping)
- Ablasyon (Ablation) Çalışması: Bileşenlerin Modele Katkısının Test Edilmesi

---

## 6. Evrişimsel Sinir Ağları (CNN) Mimarisi ve Matematiksel Hesaplamalar
### 6.1. Görüntülerde Neden Tam Bağlantılı (Dense) Ağlar Yetersizdir?
- Boyut Patlaması, Parametre Çokluğu ve Uzamsal (Spatial) Bilginin Kaybı
### 6.2. Temel CNN Katmanları ve Çalışma Prensipleri
- **Evrişim Katmanı (Conv2D):** Filtre / Çekirdek (Kernel), Kaydırma (Stride), Dolgu (Padding - Valid vs. Same), Öznitelik Haritası (Feature Map)
- **Havuzlama Katmanı (Pooling):** Max Pooling, Average Pooling; Boyut İndirgeme ve Translasyonel Değişmezlik
- **Düzleştirme Katmanı (Flatten):** 3B/Çok Boyutlu Tensörden 1B Özellik Vektörüne Geçiş
- **Tam Bağlantılı Katman (Dense / Fully Connected):** Üst Düzey Sınıflandırma
- **Global Average Pooling (GAP):** Parametre Sayısını Azaltmada Modern Alternatif (Flatten vs. GAP)
### 6.3. CNN Matematiksel Boyut ve Parametre Hesaplamaları (Sınav Odaklı)
- Katman Çıkış Boyutu Hesaplama Formülü:
  $$W_{out} = \left\lfloor \frac{W_{in} - K + 2P}{S} \right\rfloor + 1$$
- Havuzlama Sonrası Çıkış Boyutu Hesabı
- Flatten Katmanı Sonrası Toplam Eleman / Özellik Sayısı Hesabı ($H \times W \times C$)
- Conv2D Katmanı Eğitilebilir Parametre Sayısı Hesabı:
  $$\text{Parametre Sayısı} = (K_h \times K_w \times C_{in} + 1) \times C_{out}$$
- Fully Connected (Dense) Katmanı Parametre Sayısı Hesabı:
  $$\text{Parametre Sayısı} = (N_{in} + 1) \times N_{out}$$
### 6.4. Öznitelik Çıkarımının Hiyerarşik Yapısı
- İlk Katmanlar (Kenar, Köşe, Çizgi) $\rightarrow$ Orta Katmanlar (Doku, Şekil) $\rightarrow$ Derin Katmanlar (Nesne Parçaları ve Bütünsel Nesne)

---

## 7. Klasik ve Modern CNN Mimarileri (Karşılaştırmalı Analiz)
### 7.1. LeNet-5 (1998)
- MNIST Rakam Tanıma Problemi, Mimari Yapısı ve Tarihsel Önemi
### 7.2. AlexNet (2012)
- ImageNet Zaferi, ReLU ve Dropout Kullanımı, Çift GPU Mimarisi
### 7.3. VGGNet (VGG16 / VGG19 - 2014)
- Küçük $3 \times 3$ Filtrelerin Bloklar Halinde Ardışık Kullanımı, Mimari Sadeliği ve Yüksek Hesaplama Yükü
### 7.4. ResNet (Residual Networks - 2015)
- Derin Ağlarda "Yok Olan Gradyan" (Vanishing Gradient) Problemi
- Artık Blok (Residual Block) ve Kısayol Bağlantıları (Skip / Identity Connections)
### 7.5. MobileNet (2017)
- Mobil ve Gömülü Sistemler İçin Tasarım Felsefesi
- Derinlik Ayrıştırılabilir Evrişim (Depthwise Separable Convolution) Mantığı ve Standart Evrişime Göre Hesaplama Kazancı
### 7.6. EfficientNet (2019)
- Bileşik Ölçekleme (Compound Scaling) Prensibi (Derinlik, Genişlik ve Çözünürlüğün Birlikte Ölçeklenmesi)
- AutoML ve MBConv Blokları
### 7.7. Mimari Seçim Kriterleri
- Hangi Problemde, Hangi Donanım Kısıtında Hangi Mimari Seçilmelidir? (Doğruluk vs. Model Boyutu vs. Hız Kıyası)

---

## 8. Transfer Öğrenme (Transfer Learning) ve İnce Ayar (Fine-Tuning)
### 8.1. Transfer Öğrenmenin Temel Mantığı
- Önceden Eğitilmiş (Pre-Trained) Modellerin Kullanımı (ImageNet Ağırlıkları)
- Küçük Veri Setlerinde Aşırı Öğrenmeyi Engelleme ve Eğitim Süresini Kısaltma
### 8.2. İnce Ayar (Fine-Tuning) Stratejileri
- Katmanları Dondurma (Freezing) ve Sadece Sınıflandırıcı Başlığı (Classifier Head) Eğitme
- Katman Kilidi Açma (Unfreezing) ve Düşük Öğrenme Oranı ile Yeniden Eğitim
### 8.3. Veri Seti Uyarlama ve Etiketleme
- Kendi Veri Setine Göre Son Katman Nöron Sayısını Ayarlama
- Veri Etiketleme (Annotation / Labeling) Araçları (Roboflow, LabelImg)

---

## 9. Nesne Tespiti (Object Detection) ve YOLO Mimarisi
### 9.1. Bilgisayarlı Görü Görevlerinin Karşılaştırılması
- Görüntü Sınıflandırma vs. Konumlandırma vs. Nesne Tespiti vs. Semantik / Örnek Segmentasyon
### 9.2. Sınırlayıcı Kutu (Bounding Box) Temsili
- Koordinat Parametreleri: Merkez Koordinatları ($x, y$), Genişlik ($w$), Yükseklik ($h$) ve Köşe Temsilleri
- Koordinatların Normalize Edilmesi ($0 - 1$ Aralığı)
### 9.3. Nesne Tespit Modelleri Yaklaşımları
- İki Aşamalı Dedektörler (Two-Stage Detectors: R-CNN, Fast R-CNN, Faster R-CNN)
- Tek Aşamalı Dedektörler (Single-Stage Detectors: YOLO, SSD)
### 9.4. YOLO (You Only Look Once) Mimarisi ve Çalışma Prensibi
- Görüntünün Izgara (Grid) Hücrelerine Bölünmesi
- Çapa Kutuları (Anchor Boxes) ve Gerçek Zamanlı (Real-Time) Hız Avantajı
- YOLO Veri Seti Formatı (`<class_id> <x_center> <y_center> <width> <height>`)

---

## 10. Nesne Tespiti Değerlendirme Metrikleri ve Matematiksel Analizi
### 10.1. Kesişim / Birleşim Oranı (IoU - Intersection over Union)
- Matematiksel Formülü:
  $$\text{IoU} = \frac{\text{Kesişim Alanı}}{\text{Birleşim Alanı}} = \frac{\text{Area of Overlap}}{\text{Area of Union}}$$
- Pozitif Tespit Eşiği (Genellikle $\text{IoU} \ge 0.5$)
### 10.2. Karışıklık Matrisi (Confusion Matrix) Bileşenleri
- True Positive (TP), False Positive (FP), False Negative (FN), True Negative (TN)
- Güven Skoru (Confidence Score) ve Eşik Değeri Seçiminin Sonuçlara Etkisi
### 10.3. Kesinlik (Precision) ve Duyarlılık (Recall)
- Precision Formülü:
  $$\text{Precision} = \frac{TP}{TP + FP}$$
- Recall Formülü:
  $$\text{Recall} = \frac{TP}{TP + FN}$$
- Precision-Recall Takası (Trade-off)
### 10.4. Ortalama Kesinlik (AP) ve mAP (mean Average Precision)
- Precision-Recall Eğrisi Altındaki Alan (AUC)
- Sınıf Bazlı AP ve Tüm Sınıfların Ortalaması (mAP)
- mAP@0.5 ve mAP@0.5:0.95 Metriklerinin Anlamı

---

## 11. Üretken Modeller: Çekişmeli Üretici Ağlar (GAN)
### 11.1. GAN Temel Felsefesi ve Minimax Oyunu
- Üreteç (Generator - Sahte Para Basan Kalpazan) vs. Ayırt Edici (Discriminator - Polis) Analojisi
- Karşılıklı Eğitim Dinamiği ve Yakınsama Mantığı
### 11.2. GAN Türleri ve Kullanım Alanları
- DCGAN, CycleGAN, StyleGAN
### 11.3. Halüsinasyon (Hallucination) Kavramı
- Üretici Derin Öğrenme Modellerinde Halüsinasyonun Nedenleri ve Riskleri

---

## 12. Pratik Mühendislik Uygulamaları, Hata Analizi ve Donanım
### 12.1. Model Hata Analizi ve Veri Kümesi Sorunları
- Arka Plan Yanlılığı (Background Bias) ve "Kediye Kurbağa Dedi" Vakası
- Dağılım Dışı Veri (Out-of-Distribution Data) Problemi
### 12.2. Farklı Veri Modaliteleri ile Çalışma
- 1B Sinyaller vs. 2B Matrisler
- Ses Verilerinin Spektrogram (Zaman-Frekans Görüntüsü) Haline Getirilerek 2D CNN ile Sınıflandırılması
### 12.3. Donanım ve Hesaplama Kısıtları
- GPU Bellek (VRAM) Yönetimi, Batch Size Dengesi ve Çıkarım (Inference) Hızı
