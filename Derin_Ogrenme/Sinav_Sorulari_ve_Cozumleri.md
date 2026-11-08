# Derin Öğrenme Vize ve Final Sınavına Hazırlık: İnteraktif Soru Bankası ve Çözümleri

Bu doküman, Derin Öğrenme dersinin tüm transkriptleri, hocanın derste bizzat tahtaya yazıp çözdüğü quiz soruları, vize sınavında geleceğini açıkça duyurduğu sayısal soru kalıpları ve klasik yazılı soruları tek bir kaynakta toplamaktadır.

> [!TIP]
> **Çalışma Yöntemi (Self-Testing):**
> Tüm soruların cevapları ve çözümleri **açılır-kapanır (toggle / `<details>`)** kutular içerisine gizlenmiştir. Çalışırken önce soruyu okuyup kendi çözümünüzü bir kağıda yazınız veya zihninizde tahmin ediniz; ardından **"🔍 Çözümü ve Detaylı Anlatımı Gör"** butonuna tıklayarak adımlarınızı kontrol ediniz.

---

## İÇİNDEKİLER

1. [BÖLÜM 1: Derste Yapılan Gerçek Quiz Soruları ve Çözümleri](#bölüm-1-derste-yapılan-gerçek-quiz-soruları-ve-çözümleri)
   - [Quiz 1 (26 Ekim): Mobil Uygulamalar İçin Hafif Model Seçimi](#quiz-1-26-ekim-mobil-uygulamalar-i̇çin-hafif-model-seçimi)
   - [Quiz 2 (2 Kasım): Tahtadaki CNN Mimarisinde Flatten Eleman Sayısı Hesabı](#quiz-2-2-kasım-tahtadaki-cnn-mimarisinde-flatten-eleman-sayısı-hesabı)
   - [Quiz 3 (2 Kasım Telafi): Temel CNN Katmanları ve Görevleri](#quiz-3-2-kasım-telafi-temel-cnn-katmanları-ve-görevleri)
2. [BÖLÜM 2: CNN Katman Boyutları ve Parametre Hesaplama Soruları (Garanti Sınav Sorusu)](#bölüm-2-cnn-katman-boyutları-ve-parametre-hesaplama-soruları)
   - [Soru 1: $128 \times 128 \times 3$ Girdili CNN Boyut ve Tensör Akışı Analizi](#soru-1-128-times-128-times-3-girdili-cnn-boyut-ve-tensör-akışı-analizi)
   - [Soru 2: Conv2D ve Dense Katmanlarında Eğitilebilir Parametre (Ağırlık + Bias) Hesabı](#soru-2-conv2d-ve-dense-katmanlarında-eğitilebilir-parametre-hesabı)
   - [Soru 3: Stride ve Padding'in Boyuta Etkisi ($W_{out}$ Formülü)](#soru-3-stride-ve-paddingin-boyuta-etkisi-w_out-formülü)
   - [Soru 4: Flatten vs. Global Average Pooling (GAP) Parametre Karşılaştırması](#soru-4-flatten-vs-global-average-pooling-gap-parametre-karşılaştırması)
3. [BÖLÜM 3: Nesne Tespiti (YOLO), IoU ve Metrik Hesaplama Soruları (Garanti Sınav Sorusu)](#bölüm-3-nesne-tespiti-yolo-iou-ve-metrik-hesaplama-soruları)
   - [Soru 5: İki Sınırlayıcı Kutunun Koordinatlarıyla Adım Adım Sayısal IoU Hesabı](#soru-5-i̇ki-sınırlayıcı-kutunun-koordinatlarıyla-adım-adım-sayısal-iou-hesabı)
   - [Soru 6: Otonom Araç Senaryosunda TP, FP, FN, Precision, Recall ve F1-Score Hesabı](#soru-6-otonom-araç-senaryosunda-tp-fp-fn-precision-recall-ve-f1-score-hesabı)
   - [Soru 7: YOLO Normalize Koordinat Dönüşümü ($x_c, y_c, w, h$)](#soru-7-yolo-normalize-koordinat-dönüşümü-x_c-y_c-w-h)
   - [Soru 8: mAP@0.5 ve mAP@0.5:0.95 Metriklerinin Matematiksel Anlamı](#soru-8-map05-ve-map05095-metriklerinin-matematiksel-anlamı)
4. [BÖLÜM 4: Modern CNN Mimarileri ve Tasarım Felsefesi Klasik Yazılı Soruları](#bölüm-4-modern-cnn-mimarileri-ve-tasarım-felsefesi-klasik-yazılı-soruları)
   - [Soru 9: VGG Felsefesi: İki Adet $3 \times 3$ Filtre vs. Bir Adet $5 \times 5$ Filtre (%28 Tasarruf İspatı)](#soru-9-vgg-felsefesi-i̇ki-adet-3-times-3-filtre-vs-bir-adet-5-times-5-filtre)
   - [Soru 10: ResNet Residual Block ve Skip Connection Matematiksel Kurtarma Mekanizması](#soru-10-resnet-residual-block-ve-skip-connection-matematiksel-kurtarma-mekanizması)
   - [Soru 11: MobileNet Derinlik Ayrıştırılabilir Evrişim (Depthwise Separable Conv) Tasarrufu](#soru-11-mobilenet-derinlik-ayrıştırılabilir-evrişim-tasarrufu)
   - [Soru 12: Mimari Eşleştirme ve Donanım Kısıtları Senaryo Analizi](#soru-12-mimari-eşleştirme-ve-donanım-kısıtları-senaryo-analizi)
5. [BÖLÜM 5: Sinir Ağlarının Eğitimi, Aktivasyonlar ve Optimizasyon Soruları](#bölüm-5-sinir-ağlarının-eğitimi-aktivasyonlar-ve-optimizasyon-soruları)
   - [Soru 13: Tek Nöronun Matematiksel Modeli ($Z = W \cdot X + b$) ve Bias Analojisi](#soru-13-tek-nöronun-matematiksel-modeli-z--w-cdot-x--b-ve-bias-analojisi)
   - [Soru 14: Aktivasyon Fonksiyonları Karşılaştırmalı Tablosu ve Yok Olan Gradyan](#soru-14-aktivasyon-fonksiyonları-karşılaştırmalı-tablosu-ve-yok-olan-gradyan)
   - [Soru 15: Epoch, Batch Size ve İterasyon Sayısal Hesaplaması](#soru-15-epoch-batch-size-ve-iterasyon-sayısal-hesaplaması)
   - [Soru 16: Transfer Learning Stratejileri: Feature Extraction vs. Fine-Tuning](#soru-16-transfer-learning-stratejileri-feature-extraction-vs-fine-tuning)
6. [BÖLÜM 6: Hata Analizi ve Mühendislik Vakaları Soruları](#bölüm-6-hata-analizi-ve-mühendislik-vakaları-soruları)
   - [Soru 17: "Kediye Kurbağa Dedi!" Vakası (Arka Plan Yanlılığı ve Çözümleri)](#soru-17-kediye-kurbağa-dedi-vakası-arka-plan-yanlılığı-ve-çözümleri)
   - [Soru 18: 1B Ses Sinyalleri Neden ve Nasıl 2B CNN ile Sınıflandırılır? (Spektrogram)](#soru-18-1b-ses-sinyalleri-neden-ve-nasıl-2b-cnn-ile-sınıflandırılır)
   - [Soru 19: GAN Minimax Oyunu: Kalpazan (G) ve Polis (D) Amaç Fonksiyonu](#soru-19-gan-minimax-oyunu-kalpazan-g-ve-polis-d-amaç-fonksiyonu)

---

## BÖLÜM 1: Derste Yapılan Gerçek Quiz Soruları ve Çözümleri

### Quiz 1 (26 Ekim): Mobil Uygulamalar İçin Hafif Model Seçimi

**SORU METNİ:**
> *"Bir öğrenci, rüyasında cep telefonunda çok hafif ve hızlı çalışan bir görüntü sınıflandırma uygulaması geliştirdiğini görmektedir. Uyandığında bu uygulama için derste gördüğümüz **LeNet, VGG, ResNet, MobileNet ve EfficientNet** modellerinden hangisini seçmelidir?"*

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### DETAYLI ÇÖZÜM:
* **Doğru Cevap:** **MobileNet** (Hoca, modern ve verimli bir mimari olduğu için EfficientNet yazanları da kabul etmiştir; ancak akıllı telefon ve hafiflik denince birinci cevap **MobileNet**'tir).
* **Neden MobileNet?**
  * Klasik evrişim (Convolution) işlemi hem pikselleri hem de renk kanallarını aynı anda çarparak devasa bir hesaplama yükü üretir.
  * MobileNet mimarisi, standart evrişimi **Depthwise Separable Convolution (Derinlik Ayrıştırılabilir Evrişim)** adı verilen iki ayrı aşamaya böler:
    1. *Depthwise Conv:* Her kanal sadece kendi içinde $3 \times 3$ filtrelenir.
    2. *Pointwise Conv ($1 \times 1$):* Kanallar birbirine bağlanır.
  * Bu yöntem işlem yükünü ve parametre sayısını yaklaşık **$\frac{1}{9}$ oranına (%88-%89 tasarruf)** indirir. Telefonların sınırlı bataryası, ısınma problemi ve zayıf işlemcileri için en uygun mimaridir.
* **Diğerleri Neden Seçilmez?**
  * **VGG:** 138 milyon parametreye sahiptir, cep telefonunun RAM'ini kilitler ve telefonu aşırı ısıtır.
  * **LeNet:** 1998 yapımıdır; sadece $28 \times 28$ tek kanallı gri rakamları tanır, renkli modern görüntülerde yetersizdir.
  * **ResNet:** Güçlüdür ancak MobileNet kadar uç cihazlar için hafifletilmemiştir.

</details>

---

### Quiz 2 (2 Kasım): Tahtadaki CNN Mimarisinde Flatten Eleman Sayısı Hesabı

> [!IMPORTANT]
> Bu soru hocanın tahtaya bizzat yazdığı, sınıfa 5 dakika süre verdiği ve 4 Kasım dersinde çözümünü formülleriyle tahtada anlattığı **en önemli sınav sorusudur**.

**SORU METNİ:**
> Bir derin öğrenme modeline **$64 \times 64$ boyutunda, 3 kanallı (RGB)** bir görüntü girdi olarak verilmektedir ($64 \times 64 \times 3$).
> Model aşağıdaki katmanlardan oluşmaktadır:
> 1. Katman: `Conv2D(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)`
> 2. Katman: `MaxPool2D(kernel_size=2, stride=2)`
> 3. Katman: `Conv2D(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)`
> 4. Katman: `MaxPool2D(kernel_size=2, stride=2)`
> 5. Katman: `Flatten`
> 
> **Soru:** *Flatten katmanından sonra elde edilen toplam özellik (feature) sayısı kaçtır?*

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ADIM ADIM ÖĞRETİCİ ÇÖZÜM:

##### 1. Adım: Temel Formülü Hatırlayalım
Evrişim katmanı (Conv2D) için çıkış boyutu formülü:
$$W_{out} = \left\lfloor \frac{W_{in} - K + 2P}{S} \right\rfloor + 1$$
Havuzlama katmanı (MaxPool2D) $K=2, S=2$ için çıkış boyutu:
$$W_{out} = \frac{W_{in}}{2}$$

##### 2. Adım: Altın Kısayolumuzu Kullanalım
Hocanın tahtada belirttiği kural:
Filtre boyutu $K = 3$, adım $S = 1$ ve dolgu $P = 1$ olduğunda:
$$W_{out} = \frac{W_{in} - 3 + 2(1)}{1} + 1 = W_{in} - 3 + 2 + 1 = W_{in}$$
> **PÜF NOKTASI:** $3 \times 3$ filtrede `Stride = 1` ve `Padding = 1` varsa **uzamsal boyut asla değişmez, aynen korunur!**

##### 3. Adım: Katman Katman Tensör Boyutlarını Takip Edelim

1. **Başlangıç Girdisi:**
   $$\text{Tensör: } 64 \times 64 \times 3 \quad (\text{Yükseklik } H=64, \text{Genişlik } W=64, \text{Kanal } C=3)$$

2. **1. Katman: Conv2D ($K=3, S=1, P=1, \text{out\_channels}=16$):**
   * $K=3, S=1, P=1$ olduğu için boyut korunur: $64 \times 64$.
   * Çıkış kanal sayısı 16'ya yükselir.
   * **Çıktı Tensörü:** $\mathbf{64 \times 64 \times 16}$

3. **2. Katman: MaxPool2D ($K=2, S=2$):**
   * Havuzlama boyutu tam yarıya indirir: $\frac{64}{2} = 32$.
   * Havuzlama kanal sayısını ($C$) asla DEĞİŞTİRMEZ! 16 olarak kalır.
   * **Çıktı Tensörü:** $\mathbf{32 \times 32 \times 16}$

4. **3. Katman: Conv2D ($K=3, S=1, P=1, \text{out\_channels}=32$):**
   * $K=3, S=1, P=1$ olduğu için boyut yine korunur: $32 \times 32$.
   * Çıkış kanal sayısı 32'ye yükselir.
   * **Çıktı Tensörü:** $\mathbf{32 \times 32 \times 32}$

5. **4. Katman: MaxPool2D ($K=2, S=2$):**
   * Havuzlama boyutu tekrar yarıya indirir: $\frac{32}{2} = 16$.
   * Kanal sayısı 32 olarak kalır.
   * **Çıktı Tensörü:** $\mathbf{16 \times 16 \times 32}$

6. **5. Katman: Flatten:**
   * Flatten katmanı bu $16 \times 16 \times 32$ boyutundaki üç boyutlu tensörü tek bir düz vektör olarak açar.
   * Toplam eleman sayısı tüm boyutların birbiriyle çarpımıdır:
     $$\text{Toplam Eleman Sayısı} = H \times W \times C$$
     $$\text{Toplam Eleman Sayısı} = 16 \times 16 \times 32$$
   * İşlemi yapalım:
     $$16 \times 16 = 256$$
     $$256 \times 32 = \mathbf{8192}$$

**NİHAİ CEVAP:** **8192**

</details>

---

### Quiz 3 (2 Kasım Telafi): Temel CNN Katmanları ve Görevleri

**SORU METNİ:**
> *"Ödevinizde ve projelerinizde kullanmış olduğunuz temel CNN katmanlarını yazınız ve görevlerini kısaca açıklayınız."*

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### DOĞRU VE TAM CEVAP:
*(Hoca sınavda katman yerine MobileNet, ResNet gibi mimari isimleri yazanları dersten çıkarmıştır. Doğru cevap katman isimleridir).*

1. **Evrişim Katmanı (Convolutional Layer / Conv2D):**
   * Görüntü üzerinde küçük filtreler (çekirdekler) kaydırarak kenar, köşe, doku gibi yerel öznitelikleri (Feature Map) matematiksel iç çarpım ile çıkaran ana katmandır.
2. **Aktivasyon Katmanı (Activation Layer - Genellikle ReLU):**
   * Modele doğrusallık dışılık (Non-Linearity) kazandırır. Negatif değerleri sıfırlayarak ($f(z) = \max(0, z)$) modelin karmaşık nesne sınırlarını öğrenmesini sağlar ve gradyan akışını hızlandırır.
3. **Havuzlama Katmanı (Pooling Layer - MaxPool2D):**
   * Öznitelik haritasının uzamsal boyutunu ($H$ ve $W$) küçülterek hesaplama yükünü azaltır, gereksiz arka plan gürültüsünü eler ve nesnenin görüntüdeki konum değişimlerine karşı direnç (Translation Invariance) kazandırır.
4. **Düzleştirme Katmanı (Flatten Layer):**
   * Çok boyutlu öznitelik haritalarını ($H \times W \times C$) tek boyutlu bir vektöre dönüştürerek sınıflandırma katmanına hazırlar.
5. **Tam Bağlantılı Katman (Fully Connected / Dense Layer):**
   * Flatten'dan gelen tüm öznitelikleri birbirine bağlar ve yüksek seviyeli özellik kombinasyonlarını değerlendirerek sınıflandırma kararını verir.
6. **Dropout Katmanı (Düzenlileştirme):**
   * Eğitim sırasında rastgele nöronları kapatarak modelin aşırı ezberlemesini (Overfitting) engeller.
7. **Softmax Katmanı (Çıkış):**
   * Son katmanda üretilen ham skorları toplamı $\%100$ ($1.0$) olan sınıf olasılıklarına dönüştürür.

</details>

---

## BÖLÜM 2: CNN Katman Boyutları ve Parametre Hesaplama Soruları

### Soru 1: $128 \times 128 \times 3$ Girdili CNN Boyut ve Tensör Akışı Analizi

**SORU:**
Bir otonom robotun kamerası $128 \times 128$ piksel çözünürlüğünde 3 kanallı (RGB) renkli görüntüler almaktadır. Görüntü sırasıyla şu katmanlardan geçer:
1. `Conv2D(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)`
2. `MaxPool2D(kernel_size=2, stride=2)`
3. `Conv2D(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2)`
4. `MaxPool2D(kernel_size=2, stride=2)`
5. `Conv2D(in_channels=64, out_channels=128, kernel_size=3, stride=2, padding=1)`
6. `Flatten`

**İstenenler:**
a) Her katmandan sonra elde edilen tensör boyutlarını ($H \times W \times C$) adım adım yazınız.
b) Flatten katmanından sonra elde edilen toplam özellik sayısını hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ADIM ADIM ÇÖZÜM:

##### Adım 1: Formülü Hatırlayalım
$$W_{out} = \left\lfloor \frac{W_{in} - K + 2P}{S} \right\rfloor + 1$$

##### Adım 2: Katman Katman Hesaplayalım

* **Girdi:** $128 \times 128 \times 3$

* **1. Katman: Conv2D ($K=3, S=1, P=1, C_{out}=32$):**
  * $K=3, S=1, P=1$ altın kısayolu $\implies$ Boyut korunur: $128 \times 128$.
  * Çıkış kanalı: $32$.
  * **Tensör: $128 \times 128 \times 32$**

* **2. Katman: MaxPool2D ($K=2, S=2$):**
  * Boyut yarıya iner: $\frac{128}{2} = 64$.
  * Kanal sayısı değişmez: $32$.
  * **Tensör: $64 \times 64 \times 32$**

* **3. Katman: Conv2D ($K=5, S=1, P=2, C_{out}=64$):**
  * Dikkat! Filtre boyutu $K=5$, dolgu $P=2$, adım $S=1$.
  * Formülü uygulayalım:
    $$W_{out} = \frac{64 - 5 + 2(2)}{1} + 1 = \frac{64 - 5 + 4}{1} + 1 = 63 + 1 = 64$$
  * Gördüğünüz gibi $K=5, P=2, S=1$ olduğunda da boyut korunur!
  * Çıkış kanalı: $64$.
  * **Tensör: $64 \times 64 \times 64$**

* **4. Katman: MaxPool2D ($K=2, S=2$):**
  * Boyut yarıya iner: $\frac{64}{2} = 32$.
  * Kanal sayısı değişmez: $64$.
  * **Tensör: $32 \times 32 \times 64$**

* **5. Katman: Conv2D ($K=3, S=2, P=1, C_{out}=128$):**
  * Dikkat! Burada adım `stride = 2` olarak verilmiştir.
  * Formülü uygulayalım:
    $$W_{out} = \left\lfloor \frac{32 - 3 + 2(1)}{2} \right\rfloor + 1 = \left\lfloor \frac{32 - 3 + 2}{2} \right\rfloor + 1 = \left\lfloor \frac{31}{2} \right\rfloor + 1 = 15 + 1 = 16$$
  * Adım 2 olduğu için uzamsal boyut 16'ya düşer!
  * Çıkış kanalı: $128$.
  * **Tensör: $16 \times 16 \times 128$**

* **6. Katman: Flatten:**
  * Toplam Özellik Sayısı $= 16 \times 16 \times 128$
  * $16 \times 16 = 256$
  * $256 \times 128 = 256 \times 2^7 = 32.768$

**NİHAİ CEVAP:**
a) Tensör Akışı:
$128 \times 128 \times 3 \to 128 \times 128 \times 32 \to 64 \times 64 \times 32 \to 64 \times 64 \times 64 \to 32 \times 32 \times 64 \to 16 \times 16 \times 128$
b) Flatten Sonrası Özellik Sayısı: **32.768**

</details>

---

### Soru 2: Conv2D ve Dense Katmanlarında Eğitilebilir Parametre Hesabı

**SORU:**
Aşağıdaki iki katman için ayrı ayrı modelin öğrenmesi gereken **toplam eğitilebilir parametre (Ağırlıklar + Bias)** sayılarını formülleriyle hesaplayınız:

a) Bir Evrişim Katmanı: `Conv2D(in_channels=16, out_channels=64, kernel_size=3)` (Bias kullanıldığı varsayılmaktadır).
b) Bir Tam Bağlantılı Katman: `Dense(in_features=2048, out_features=128)` (Bias kullanıldığı varsayılmaktadır).

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ADIM ADIM ÇÖZÜM:

##### a) Conv2D Katmanı Parametre Sayısı:
* **Formül:**
  Bir evrişim katmanında her bir filtre, tüm girdi kanallarını kapsar. Dolayısıyla tek bir filtrenin ağırlık sayısı:
  $$\text{Tek Filtre Ağırlıkları} = K_h \times K_w \times C_{in}$$
  Bu katmanda $C_{out}$ adet filtre vardır ve her filtrenin $1$ adet bias terimi bulunur:
  $$\text{Toplam Parametre} = \Big( (K_h \times K_w \times C_{in}) + 1 \Big) \times C_{out}$$

* **Sayıları Yerine Koyalım:**
  * $K_h = 3, K_w = 3$
  * $C_{in} = 16$
  * $C_{out} = 64$
  * Tek filtrenin ağırlık sayısı: $3 \times 3 \times 16 = 144$
  * Tek filtrenin bias'ı: $+1 \implies 145$ parametre
  * 64 adet filtre için:
    $$\text{Toplam Conv Parametresi} = 145 \times 64 = \mathbf{9280}$$

##### b) Dense (Tam Bağlantılı) Katman Parametre Sayısı:
* **Formül:**
  Girdi nöron sayısı $N_{in}$, çıktı nöron sayısı $N_{out}$ ise her girdi her çıktıya bağlanır:
  $$\text{Ağırlık Sayısı} = N_{in} \times N_{out}$$
  Her çıktı nöronunun $1$ adet bias terimi vardır:
  $$\text{Bias Sayısı} = N_{out}$$
  $$\text{Toplam Parametre} = (N_{in} + 1) \times N_{out}$$

* **Sayıları Yerine Koyalım:**
  * $N_{in} = 2048$
  * $N_{out} = 128$
  * $\text{Ağırlık Sayısı} = 2048 \times 128 = 262.144$
  * $\text{Bias Sayısı} = 128$
  * $\text{Toplam Dense Parametresi} = 262.144 + 128 = \mathbf{262.272}$

</details>

---

### Soru 3: Stride ve Padding'in Boyuta Etkisi ($W_{out}$ Formülü)

**SORU:**
Girdi boyutu $W_{in} = 100 \times 100$ olan tek kanallı bir matrise $7 \times 7$ boyutunda bir evrişim filtresi uygulanacaktır ($K = 7$).
Aşağıdaki durumlar için çıkış boyutlarını hesaplayınız:
a) `Stride = 1, Padding = 0 (Valid Padding)`
b) `Stride = 2, Padding = 3 (Same Padding)`
c) `Stride = 3, Padding = 1`

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
Formülümüz: $W_{out} = \lfloor \frac{W_{in} - K + 2P}{S} \rfloor + 1$

* **a) $S = 1, P = 0$:**
  $$W_{out} = \frac{100 - 7 + 0}{1} + 1 = 93 + 1 = \mathbf{94 \times 94}$$

* **b) $S = 2, P = 3$:**
  $$W_{out} = \left\lfloor \frac{100 - 7 + 2(3)}{2} \right\rfloor + 1 = \left\lfloor \frac{100 - 7 + 6}{2} \right\rfloor + 1 = \left\lfloor \frac{99}{2} \right\rfloor + 1 = 49 + 1 = \mathbf{50 \times 50}$$

* **c) $S = 3, P = 1$:**
  $$W_{out} = \left\lfloor \frac{100 - 7 + 2(1)}{3} \right\rfloor + 1 = \left\lfloor \frac{100 - 7 + 2}{3} \right\rfloor + 1 = \left\lfloor \frac{95}{3} \right\rfloor + 1 = 31 + 1 = \mathbf{32 \times 32}$$

</details>

---

### Soru 4: Flatten vs. Global Average Pooling (GAP) Parametre Karşılaştırması

**SORU:**
Bir CNN modelinin son evrişim katmanından çıkan öznitelik haritasının boyutu **$7 \times 7 \times 512$**'dir. Model 10 sınıflı bir sınıflandırma yapacaktır ($N_{out} = 10$).
a) Bu aşamada klasik **Flatten** katmanı kullanılır ve doğrudan 10 nöronlu çıkış katmanına bağlanırsa kaç adet eğitilebilir parametre üretilir?
b) Flatten yerine modern **Global Average Pooling (GAP)** kullanılırsa kaç adet eğitilebilir parametre üretilir?
c) Aradaki parametre farkını ve GAP'in derin öğrenmedeki mühendislik avantajını açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:

##### a) Flatten Kullanıldığında:
* $7 \times 7 \times 512 = 25.088$ elemanlı tek bir vektör oluşur ($N_{in} = 25.088$).
* Bu vektör 10 nöronlu çıkış katmanına bağlanırsa:
  $$\text{Parametre Sayısı} = (N_{in} + 1) \times N_{out} = (25.088 + 1) \times 10 = \mathbf{250.890 \text{ parametre}}$$

##### b) Global Average Pooling (GAP) Kullanıldığında:
* GAP, her bir $7 \times 7$'lik kanalın doğrudan ortalamasını alır. Tensör boyutu $1 \times 1 \times 512$'ye iner ($N_{in} = 512$).
* GAP katmanının kendisinin parametresi sıfırdır.
* 512 elemanlı vektör 10 nöronlu çıkış katmanına bağlanırsa:
  $$\text{Parametre Sayısı} = (N_{in} + 1) \times N_{out} = (512 + 1) \times 10 = \mathbf{5.130 \text{ parametre}}$$

##### c) Mühendislik Yorumu:
* Parametre sayısı $250.890$'dan $5.130$'a düşmüştür; yani **yaklaşık %98 oranında azalmıştır!**
* **Avantajı:** Model boyutunu devasa ölçüde küçültür, GPU belleğini rahatlatır ve en önemlisi son katmandaki aşırı ezberlemeyi (Overfitting) neredeyse tamamen ortadan kaldırır. ResNet ve EfficientNet gibi modern mimarilerin başarısının arkasındaki temel sırlardan biridir.

</details>

---

## BÖLÜM 3: Nesne Tespiti (YOLO), IoU ve Metrik Hesaplama Soruları

### Soru 5: İki Sınırlayıcı Kutunun Koordinatlarıyla Adım Adım Sayısal IoU Hesabı

> [!IMPORTANT]
> **VİZE İÇİN GARANTİ SORU TİPİ:**
> Hoca koordinat verip IoU hesabı soracağını belirtmiştir.

**SORU METNİ:**
Bir görüntü üzerinde etiketlenmiş Gerçek Kutu (Ground Truth - $A$) ve modelin tahmin ettiği Kutu (Prediction - $B$) koordinatları $[x_{min}, y_{min}, x_{max}, y_{max}]$ formatında piksel cinsinden verilmiştir:
* **Gerçek Kutu ($A$):** $[50, 50, 150, 150]$
* **Tahmin Kutusu ($B$):** $[100, 100, 200, 200]$

**İstenenler:**
a) Gerçek Kutunun Alanını ($\text{Area}(A)$) hesaplayınız.
b) Tahmin Kutusunun Alanını ($\text{Area}(B)$) hesaplayınız.
c) Kesişim Kutusunun koordinatlarını ve Kesişim Alanını ($\text{Area}(A \cap B)$) hesaplayınız.
d) Birleşim Alanını ($\text{Area}(A \cup B)$) hesaplayınız.
e) $\text{IoU}$ değerini hesaplayınız ve $\tau = 0.50$ eşiğine göre bu tespitin **True Positive (TP)** mi yoksa **False Positive (FP)** mi olduğunu belirtiniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ADIM ADIM ÖĞRETİCİ ÇÖZÜM:

##### 1. Adım: Bireysel Kutu Alanlarının Hesabı
Bir kutunun alanı: $\text{Alan} = (x_{max} - x_{min}) \times (y_{max} - y_{min})$
* **Gerçek Kutu ($A$):**
  * Genişlik $= 150 - 50 = 100$
  * Yükseklik $= 150 - 50 = 100$
  * $\text{Area}(A) = 100 \times 100 = \mathbf{10.000}$
* **Tahmin Kutusu ($B$):**
  * Genişlik $= 200 - 100 = 100$
  * Yükseklik $= 200 - 100 = 100$
  * $\text{Area}(B) = 100 \times 100 = \mathbf{10.000}$

##### 2. Adım: Kesişim Kutusunun (Intersection) Koordinatları ve Alanı
İki kutunun kesişim koordinatları şu formülle bulunur:
$$x_{min}^{\text{kesişim}} = \max(x_{min}^A, x_{min}^B) = \max(50, 100) = 100$$
$$y_{min}^{\text{kesişim}} = \max(y_{min}^A, y_{min}^B) = \max(50, 100) = 100$$
$$x_{max}^{\text{kesişim}} = \min(x_{max}^A, x_{max}^B) = \min(150, 200) = 150$$
$$y_{max}^{\text{kesişim}} = \min(y_{max}^A, y_{max}^B) = \min(150, 200) = 150$$

* Kesişim Kutusunun Genişliği $= 150 - 100 = 50$
* Kesişim Kutusunun Yüksekliği $= 150 - 100 = 50$
* $\text{Area}(A \cap B) = 50 \times 50 = \mathbf{2.500}$

##### 3. Adım: Birleşim Alanının (Union) Hesabı
$$\text{Area}(A \cup B) = \text{Area}(A) + \text{Area}(B) - \text{Area}(A \cap B)$$
$$\text{Area}(A \cup B) = 10.000 + 10.000 - 2.500 = \mathbf{17.500}$$

##### 4. Adım: IoU Hesabı ve Karar
$$\text{IoU} = \frac{\text{Area}(A \cap B)}{\text{Area}(A \cup B)} = \frac{2.500}{17.500} = \frac{25}{175} = \frac{1}{7} \approx \mathbf{0.1428} \quad (\%14.28)$$

* **Karar:**
  Belirlenen eşik değer $\tau = 0.50$'dir.
  $$\text{IoU} = 0.1428 < 0.50$$
  Bu tespit **yetersiz örtüşme nedeniyle FALSE POSITIVE (FP - Hatalı Tespit)** olarak değerlendirilir!

</details>

---

### Soru 6: Otonom Araç Senaryosunda TP, FP, FN, Precision, Recall ve F1-Score Hesabı

**SORU METNİ:**
Bir otonom araç projesi kapsamında geliştirilen YOLO nesne tespit modeli, test pistinde 100 metrelik bir sürüş boyunca yayaları tespit etmek üzere çalıştırılmıştır. Test verileri ve model çıktıları şöyledir:
* Pistte toplamda **80 adet gerçek yaya** bulunmaktadır.
* Model toplamda **70 adet yaya kutusu** tahmin etmiştir.
* Bu 70 kutudan **56 tanesi** doğru bir yayayı $\text{IoU} \ge 0.50$ şartıyla yakalamıştır.
* Kalan **14 kutu** yol kenarındaki trafik levhalarına ve çöp kutularına yaya denilerek yanlış çizilmiştir.

**İstenenler:**
a) $\text{TP}$ (True Positive), $\text{FP}$ (False Positive) ve $\text{FN}$ (False Negative) sayılarını belirleyiniz.
b) Modelin **Kesinlik (Precision)** değerini formülüyle hesaplayınız.
c) Modelin **Duyarlılık (Recall)** değerini formülüyle hesaplayınız.
d) Modelin **F1-Skorunu** hesaplayınız.
e) Otonom sürüş güvenliği açısından Precision mı yoksa Recall mu daha kritiktir? Neden?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ADIM ADIM ÇÖZÜM:

##### a) Metrik Bileşenleri:
* **$\text{TP}$ (Doğru Tespit):** Doğru sınıf ve $\text{IoU} \ge 0.5$ olan kutu sayısı $\implies \mathbf{TP = 56}$
* **$\text{FP}$ (Yanlış Alarm):** Çöp kutularına ve tabelalara yaya denilen kutu sayısı $\implies \mathbf{FP = 14}$
* **$\text{FN}$ (Kaçırılan Hedef):** Modelin hiç kutu çizemediği, görmezden geldiği gerçek yaya sayısı:
  $$\text{FN} = \text{Toplam Gerçek Yaya} - \text{TP} = 80 - 56 = \mathbf{24}$$

##### b) Kesinlik (Precision) Hesabı:
$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} = \frac{56}{56 + 14} = \frac{56}{70} = \mathbf{0.80} \quad (\%80)$$
* *Anlamı:* Modelin *"Yaya buldum"* dediği her 100 kutudan 80'i gerçekten yayadır.

##### c) Duyarlılık (Recall) Hesabı:
$$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} = \frac{56}{56 + 24} = \frac{56}{80} = \mathbf{0.70} \quad (\%70)$$
* *Anlamı:* Pistteki gerçek yayaların $\%70$'i yakalanmış, $\%30$'u ($24$ yaya) kaçırılmıştır.

##### d) F1-Skoru Hesabı:
$$\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \cdot \frac{0.80 \cdot 0.70}{0.80 + 0.70} = 2 \cdot \frac{0.56}{1.50} = \frac{1.12}{1.50} \approx \mathbf{0.7467}$$

##### e) Mühendislik Yorumu (Otonom Sürüş Güvenliği):
* Otonom sürüşte **RECALL çok daha hayatidir!**
* Düşük Precision durumunda (FP yüksek) araç bazen boş yere fren yapar veya yavaşlar (konfor bozulur).
* Ancak düşük Recall durumunda (FN yüksek), araç önündeki gerçek bir yayayı hiç algılayamaz ve yayaya çarpar! İnsan hayatı söz konusu olduğunda hiçbir yaya kaçırılmamalıdır ($\text{Recall} \to 1.0$ olmalıdır).

</details>

---

### Soru 7: YOLO Normalize Koordinat Dönüşümü ($x_c, y_c, w, h$)

**SORU:**
$1920 \times 1080$ piksel çözünürlüğündeki Full HD bir güvenlik kamerası görüntüsünde bir otomobilin köşe koordinatları piksel olarak şöyledir:
* $x_{min} = 480$, $y_{min} = 270$
* $x_{max} = 960$, $y_{max} = 810$

Bu nesnenin sınıf kimliği `Araba` için `class_id = 0` olduğuna göre; YOLO etiket dosyasında (`.txt`) yer alması gereken satırı normalize değerleri adım adım hesaplayarak yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* Görüntü Boyutları: $W_{\text{resim}} = 1920$, $H_{\text{resim}} = 1080$

1. **Kutunun Piksel Genişlik ve Yüksekliği:**
   $$W_{\text{kutu}} = x_{max} - x_{min} = 960 - 480 = 480$$
   $$H_{\text{kutu}} = y_{max} - y_{min} = 810 - 270 = 540$$

2. **Kutunun Piksel Merkez Koordinatları:**
   $$X_{\text{merkez}} = x_{min} + \frac{W_{\text{kutu}}}{2} = 480 + \frac{480}{2} = 480 + 240 = 720$$
   $$Y_{\text{merkez}} = y_{min} + \frac{H_{\text{kutu}}}{2} = 270 + \frac{540}{2} = 270 + 270 = 540$$

3. **Normalize Değerler ($[0.0, 1.0]$):**
   $$x_c = \frac{X_{\text{merkez}}}{W_{\text{resim}}} = \frac{720}{1920} = \mathbf{0.375000}$$
   $$y_c = \frac{Y_{\text{merkez}}}{H_{\text{resim}}} = \frac{540}{1080} = \mathbf{0.500000}$$
   $$w = \frac{W_{\text{kutu}}}{W_{\text{resim}}} = \frac{480}{1920} = \mathbf{0.250000}$$
   $$h = \frac{H_{\text{kutu}}}{H_{\text{resim}}} = \frac{540}{1080} = \mathbf{0.500000}$$

**YOLO Dosyasına Yazılacak Satır:**
```text
0 0.375000 0.500000 0.250000 0.500000
```

</details>

---

### Soru 8: mAP@0.5 ve mAP@0.5:0.95 Metriklerinin Matematiksel Anlamı

**SORU:**
Akademik bir yayında Model A'nın $\text{mAP@0.5} = 0.85$, $\text{mAP@0.5:0.95} = 0.42$ aldığı; Model B'nin ise $\text{mAP@0.5} = 0.80$, $\text{mAP@0.5:0.95} = 0.65$ aldığı belirtilmektedir.
a) $\text{mAP@0.5}$ ile $\text{mAP@0.5:0.95}$ arasındaki fark nedir?
b) Bu iki modelin güçlü ve zayıf yönlerini kıyaslayınız. Hassas robotik cerrahi için hangisini seçersiniz?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* **a) Tanım Farkı:**
  * $\text{mAP@0.5}$: Tahmin kutusunun gerçek kutuyla en az $\%50$ örtüşmesini ($\text{IoU} \ge 0.50$) yeterli kabul eder. Kutunun sınırlarının tam oturup oturmadığına çok bakmaz, kaba tespiti ödüllendirir.
  * $\text{mAP@0.5:0.95}$: IoU eşiğini $0.50$'den $0.95$'e kadar $0.05$'lik adımlarla ($0.50, 0.55, 0.60, \dots, 0.95$) 10 farklı seviyede test eder ve ortalamasını alır. Modelin kutu sınırlarını milimetrik çizme hassasiyetini ölçer.
* **b) Model Kıyası ve Seçim:**
  * **Model A:** Nesneleri genel olarak yakalamada başarılıdır ($\text{mAP@0.5} = 0.85$), ancak kutuları kaba çizer, örtüşme eşiği $0.80-0.90$'a çıktığında başarısı çökmektedir ($\text{mAP@0.5:0.95} = 0.42$).
  * **Model B:** Nesnelerin sınırlarını son derece hassas ve kusursuz çizmektedir ($\text{mAP@0.5:0.95} = 0.65$).
  * **Tercih:** Hassas robotik cerrahi veya fabrika mikro-montajında milimetrik hata bile kabul edilemeyeceği için kesinlikle **Model B** seçilmelidir.

</details>

---

## BÖLÜM 4: Modern CNN Mimarileri ve Tasarım Felsefesi Klasik Yazılı Soruları

### Soru 9: VGG Felsefesi: İki Adet $3 \times 3$ Filtre vs. Bir Adet $5 \times 5$ Filtre

**SORU:**
VGG mimarisinde büyük filtreler ($5 \times 5$ veya $7 \times 7$) yerine ardışık iki adet $3 \times 3$ filtre kullanılmıştır.
a) Bu iki tasarımın Alıcı Alanlarını (Effective Receptive Field) karşılaştırınız.
b) Girdi kanal sayısı $C$ ve çıkış kanal sayısı $C$ olan bir katman için her iki tasarımın parametre sayılarını formülle çıkarıp tasarruf oranını matematiksel olarak ispatlayınız.
c) Doğrusallık dışılık (Non-Linearity) açısından avantajı nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### İSPAT VE ÇÖZÜM:

##### a) Alıcı Alan (Receptive Field) Eşitliği:
* $1.$ Katman ($3 \times 3$ filtre): Girdi üzerindeki $3 \times 3$'lük alanı görür.
* $2.$ Katman ($3 \times 3$ filtre): Birinci katmandan çıkan $3 \times 3$'lük alanın üzerine oturur. Bu alanın en dış pikselleri orijinal girdide $1$ piksel daha dışarı taşar.
* Toplam görülen alan: $3 + (3 - 1) = \mathbf{5 \times 5}$.
* Yani ardışık iki adet $3 \times 3$ filtre, girdi üzerinde **tam olarak tek bir $5 \times 5$ filtrenin gördüğü alanı görür!**

##### b) Parametre Tasarrufu İspatı:
Girdi ve çıktı kanal sayısına $C$ diyelim (bias'ları ihmal edip ağırlıklara odaklanalım):
* **Tasarım 1 (Tek bir $5 \times 5$ Katmanı):**
  $$\text{Parametre}_1 = 5 \times 5 \times C \times C = \mathbf{25 C^2}$$
* **Tasarım 2 (Ardışık iki adet $3 \times 3$ Katmanı):**
  * 1. Katman: $3 \times 3 \times C \times C = 9 C^2$
  * 2. Katman: $3 \times 3 \times C \times C = 9 C^2$
  * Toplam: $9 C^2 + 9 C^2 = \mathbf{18 C^2}$
* **Tasarruf Oranı:**
  $$\text{Oran} = \frac{18 C^2}{25 C^2} = \frac{18}{25} = 0.72 \implies \mathbf{\%28 \text{ Tasarruf!}}$$
* İki adet $3 \times 3$ filtre kullanıldığında aynı görsel bilgi **%28 daha az parametreyle** hesaplanır!

##### c) Doğrusallık Dışılık Avantajı:
Tek bir $5 \times 5$ katmanda sadece $1$ adet aktivasyon (ReLU) fonksiyonu varken; iki adet $3 \times 3$ mimarisinde araya ve sona olmak üzere **$2$ adet ReLU** girer. Bu durum ağın karar fonksiyonunu iki kat daha zengin ve doğrusal olmayan hale getirir.

</details>

---

### Soru 10: ResNet Residual Block ve Skip Connection Matematiksel Kurtarma Mekanizması

**SORU:**
ResNet mimarisinden önce çok derin ağlar (20+ katman) eğitilemiyordu ve katman sayısı arttıkça hata azalmıyor, aksine artıyordu (Degradation Problem).
a) ResNet bu sorunu hangi matematiksel blok tasarımıyla çözmüştür? Şemasını çizip formülünü yazınız.
b) Geri yayılımda (Backpropagation) türev alındığında bu kısayolun (Skip connection) yok olan gradyanı (Vanishing gradient) nasıl engellediğini matematiksel olarak gösteriniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:

##### a) Artık Blok (Residual Block) Mimarisi:
Klasik ağlar doğrudan $H(x)$ hedef fonksiyonunu öğrenmeye çalışırken; ResNet katmana aradaki farkı (artığı) öğrenme görevi verir:
$$F(x) = H(x) - x$$
Katman çıktısına girdinin kendisi ($x$) doğrudan kimlik bağlantısıyla (Identity Shortcut / Skip Connection) eklenir:
$$H(x) = F(x) + x$$

##### b) Gradyan Kurtarma Matematiği:
Geri yayılım yapılırken hata fonksiyonunun ($\mathcal{L}$) girdiye ($x$) göre türevi zincir kuralıyla alınır:
$$\frac{\partial \mathcal{L}}{\partial x} = \frac{\partial \mathcal{L}}{\partial H} \cdot \frac{\partial H}{\partial x}$$

Burada $\frac{\partial H}{\partial x}$ terimini açalım:
$$\frac{\partial H}{\partial x} = \frac{\partial}{\partial x} \Big( F(x) + x \Big) = \frac{\partial F}{\partial x} + 1$$

Bu ifadeyi yerine koyduğumuzda:
$$\frac{\partial \mathcal{L}}{\partial x} = \frac{\partial \mathcal{L}}{\partial H} \cdot \left( \frac{\partial F}{\partial x} + 1 \right) = \frac{\partial \mathcal{L}}{\partial H} \cdot \frac{\partial F}{\partial x} + \mathbf{\frac{\partial \mathcal{L}}{\partial H}}$$

> **HAYATİ İSPAT:**
> Parantez içindeki **$+1$** terimine dikkat ediniz!
> Katmandaki ağırlıklar ne kadar kötü olursa olsun veya $\frac{\partial F}{\partial x}$ türevi sıfıra yaklaşsa bile (Vanishing gradient durumu); formüldeki $+1$ sayesinde hata sinyali ($\frac{\partial \mathcal{L}}{\partial H}$) **hiçbir kayba uğramadan bir önceki katmana doğrudan iletilir.**
> Bu kısayol, hata sinyali için bir "otoban" görevi görür ve ağın 152 hatta 1000 katmana kadar çökmeden eğitilmesini sağlar.

</details>

---

### Soru 11: MobileNet Derinlik Ayrıştırılabilir Evrişim (Depthwise Separable Conv) Tasarrufu

**SORU:**
Girdi boyutu $D_F \times D_F \times M$ ve çıktı boyutu $D_F \times D_F \times N$ olan bir evrişim katmanında $D_K \times D_K$ boyutunda filtreler kullanılacaktır ($D_K = 3$).
a) Standart evrişimin hesaplama maliyetini formüle ediniz.
b) Depthwise Separable Convolution yönteminin hesaplama maliyetini formüle ediniz.
c) Bu iki maliyetin oranını hesaplayınız. $3 \times 3$ filtre ve $N=128$ için yaklaşık tasarruf çarpanı kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* **a) Standart Evrişim Maliyeti:**
  Her çıkış noktası için $D_K \times D_K \times M$ çarpım yapılır. Toplam çıkış noktası $D_F \times D_F$ ve $N$ kanal olduğuna göre:
  $$\text{Maliyet}_{\text{standart}} = D_K \times D_K \times M \times N \times D_F \times D_F$$

* **b) Depthwise Separable Conv Maliyeti:**
  İki aşamadan oluşur:
  1. *Depthwise Conv:* Her girdi kanalı için $D_K \times D_K$ filtre uygulanır $\implies D_K \times D_K \times M \times D_F \times D_F$
  2. *Pointwise Conv ($1 \times 1$):* Kanalları birleştirmek için $1 \times 1 \times M \times N$ evrişim yapılır $\implies M \times N \times D_F \times D_F$
  $$\text{Maliyet}_{\text{ayrıştırılmış}} = (D_K \cdot D_K \cdot M \cdot D_F \cdot D_F) + (M \cdot N \cdot D_F \cdot D_F)$$

* **c) Oran ve Tasarruf:**
  $$\text{Maliyet Oranı} = \frac{D_K^2 \cdot M \cdot D_F^2 + M \cdot N \cdot D_F^2}{D_K^2 \cdot M \cdot N \cdot D_F^2} = \frac{D_K^2 + N}{D_K^2 \cdot N} = \frac{1}{N} + \frac{1}{D_K^2}$$
  * $D_K = 3$ ve $N = 128$ için:
    $$\text{Oran} = \frac{1}{128} + \frac{1}{3^2} = 0.0078 + \frac{1}{9} \approx 0.0078 + 0.1111 \approx \mathbf{0.1189} \approx \mathbf{\frac{1}{8.4}}$$
  * **Sonuç:** MobileNet, standart evrişime göre **yaklaşık 8.4 kat daha az hesaplama yapar**; bu da akıllı telefonlarda saniyede 60 FPS'e ulaşılmasını sağlar.

</details>

---

### Soru 12: Mimari Eşleştirme ve Donanım Kısıtları Senaryo Analizi

**SORU:**
Aşağıdaki 4 mühendislik senaryosu için **LeNet-5, VGG-16, ResNet-50, MobileNetV2, EfficientNet-B0** modellerinden en uygun olanını seçiniz ve gerekçenizi yazınız:

1. **Senaryo 1:** Bir İnsansız Hava Aracı (İHA) Raspberry Pi 4 üzerinde çalışacak ve gerçek zamanlı kenevir tespiti yapacaktır. Batarya ve işlemci kısıtlıdır.
2. **Senaryo 2:** Bulut sunucusunda çalışacak, GPU kaynağı bol, tıp hekimlerine kanser teşhisinde yardımcı olacak maksimum doğruluk hedefleyen bir hastane sistemi.
3. **Senaryo 3:** Bir bankanın ATM'sindeki çek okuyucusunda çalışan, sadece siyah-beyaz rakamları tanıması gereken ultra hafif sistem.
4. **Senaryo 4:** Endüstriyel bir fabrikada konveyör banttaki hatalı parçaları ayıran, hem yüksek doğruluk isteyen hem de aşırı hantal olmayan standart omurga.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜMLER:
1. **Senaryo 1 $\implies$ MobileNetV2:** Sınırlı donanım, düşük enerji tüketimi ve yüksek FPS gerektiren uç cihazlar için özel olarak optimize edilmiştir.
2. **Senaryo 2 $\implies$ EfficientNet-B0 (veya ResNet / EfficientNet üst serisi):** Kaynak kısıtı yoktur, en yüksek doğruluk ve hassasiyet aranmaktadır.
3. **Senaryo 3 $\implies$ LeNet-5:** Problem $28 \times 28$ tek kanallı rakam tanımadır; modern devasa ağlara gerek yoktur, LeNet mikrosaniye hızında çözer.
4. **Senaryo 4 $\implies$ ResNet-50:** Endüstride en çok test edilmiş, artık bağlantıları sayesinde stabil eğitilen, güçlü ve güvenilir genel amaçlı omurgadır.

</details>

---

## BÖLÜM 5: Sinir Ağlarının Eğitimi, Aktivasyonlar ve Optimizasyon Soruları

### Soru 13: Tek Nöronun Matematiksel Modeli ($Z = W \cdot X + b$) ve Bias Analojisi

**SORU:**
3 girdili bir yapay nöron için:
* Girdiler: $X = [x_1 = 2.0, x_2 = -1.0, x_3 = 3.0]^T$
* Ağırlıklar: $W = [w_1 = 0.5, w_2 = 2.0, w_3 = -0.5]^T$
* Bias: $b = 1.5$
* Aktivasyon Fonksiyonu: $\text{ReLU}(z)$

a) Lineer kombinasyon ($Z$) değerini hesaplayınız.
b) Nöronun nihai çıktısını ($\hat{y}$) hesaplayınız.
c) Formülde $+b$ terimi olmasaydı ne olurdu? Hocanın bisiklet analojisiyle açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* **a) $Z$ Hesabı:**
  $$Z = \sum w_i x_i + b = (w_1 x_1 + w_2 x_2 + w_3 x_3) + b$$
  $$Z = (0.5 \cdot 2.0) + (2.0 \cdot -1.0) + (-0.5 \cdot 3.0) + 1.5$$
  $$Z = 1.0 - 2.0 - 1.5 + 1.5 = \mathbf{-1.0}$$

* **b) Çıktı ($\hat{y}$) Hesabı:**
  $$\hat{y} = \text{ReLU}(Z) = \max(0, Z) = \max(0, -1.0) = \mathbf{0.0}$$
  * Negatif değer ReLU tarafından sıfırlanmış, nöron ateşlenmemiştir.

* **c) Bias Analojisi:**
  * Eğer $b = 0$ olsaydı, girdiler sıfır olduğunda ($X = 0$) çıktı her zaman sıfır olurdu; karar düzlemi orijine kilitlenirdi.
  * **Bisiklet Analojisi:** Düz yolda pedal basmazsanız ($X=0$) durursunuz. Yokuş aşağı bir yoldaysanız (pozitif bias), hiç pedal basmasanız bile bisiklet kendiliğinden hareket eder. Dik bir yokuştaysanız (negatif bias), bisikletin hareket etmesi için belirli bir eşikten fazla pedal kuvveti üretmeniz gerekir. Bias nöronun uyarılma eşiğini serbestçe kaydırır.

</details>

---

### Soru 14: Aktivasyon Fonksiyonları Karşılaştırmalı Tablosu ve Yok Olan Gradyan

**SORU:**
Sigmoid, Tanh, ReLU ve Leaky ReLU aktivasyon fonksiyonlarını formül, değer aralığı, sıfır merkezlilik ve yok olan gradyan riski kriterlerine göre karşılaştırınız. Yok Olan Gradyan (Vanishing Gradient) nedir ve ReLU bunu nasıl çözer?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:

| Kriter | Sigmoid | Tanh | ReLU | Leaky ReLU |
| :--- | :---: | :---: | :---: | :---: |
| **Matematiksel Formül** | $\frac{1}{1 + e^{-z}}$ | $\frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $\max(0, z)$ | $\max(\alpha z, z)$ |
| **Çıkış Değer Aralığı** | $(0, 1)$ | $(-1, 1)$ | $[0, \infty)$ | $(-\infty, \infty)$ |
| **Sıfır Merkezli mi?** | Hayır (Daima pozitif) | **Evet** | Hayır | Hayır / Kısmen |
| **Yok Olan Gradyan Riski** | **Çok Yüksek** | Yüksek | **Yok (Pozitif bölgede)** | **Yok** |
| **Hesaplama Maliyeti** | Yüksek ($e^{-z}$) | Yüksek ($e^z$) | **Çok Düşük (Sadece if-else)** | Çok Düşük |
| **Tipik Kullanım Yeri** | İkili sınıflandırma çıkışı | Bazı RNN hücreleri | **Gizli katman varsayılanı** | Ölü nöron riski olan katmanlar |

* **Yok Olan Gradyan (Vanishing Gradient) ve ReLU Çözümü:**
  * Sigmoid ve Tanh fonksiyonlarında $|z| > 4$ olduğunda eğri tamamen yataylaşır ve türevi sıfıra yaklaşır ($\sigma'(z) \approx 0$). Geri yayılımda zincir kuralı gereği bu sıfıra yakın türevler birbiriyle çarpıldığında ilk katmanlara hata sinyali $10^{-10}$ seviyesinde ulaşır; ilk katmanların ağırlıkları güncellenemez ve eğitim kilitlenir.
  * **ReLU Çözümü:** ReLU fonksiyonunun türevi pozitif bölgede ($z > 0$) **sabit 1'dir** ($f'(z) = 1$). Ağ 100 katman bile olsa $1 \times 1 \times 1 \dots = 1$ kaldığı için gradyan ilk katmanlara kayıpsız akar.

</details>

---

### Soru 15: Epoch, Batch Size ve İterasyon Sayısal Hesaplaması

**SORU:**
Bir derin öğrenme mühendisi, $50.000$ adet renkli görüntüden oluşan bir veri setini eğitecektir.
* Batch Size: $64$
* Toplam Epoch: $25$

a) Tek bir epoch tamamlandığında model kaç adet **iterasyon (ağırlık güncellemesi)** gerçekleştirmiş olur?
b) 25 epoch'luk tüm eğitim tamamlandığında toplam kaç kez ağırlık güncellemesi yapılmış olur?
c) Batch Size $50.000$ (tüm veri) seçilirse ne olur? Neden küçük batch size tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* **a) 1 Epoch İçin İterasyon Sayısı:**
  $$\text{İterasyon} = \left\lceil \frac{\text{Toplam Veri}}{\text{Batch Size}} \right\rceil = \left\lceil \frac{50.000}{64} \right\rceil = \lceil 781.25 \rceil = \mathbf{782 \text{ İterasyon}}$$

* **b) Tüm Eğitim İçin Toplam Güncelleme:**
  $$\text{Toplam Güncelleme} = 25 \times 782 = \mathbf{19.550 \text{ Kez}}$$

* **c) Büyük vs. Küçük Batch Size Mühendislik Farkı:**
  * Eğer Batch Size $50.000$ seçilirse (Full Batch Gradient Descent):
    1. $50.000$ renkli resim GPU belleğine sığmaz $\implies$ **CUDA Out of Memory (OOM)** çöküşü yaşanır.
    2. Model 1 epoch boyunca sadece $1$ kez ağırlık günceller; öğrenme aşırı yavaşlar.
  * Küçük Batch Size ($32, 64$):
    1. Belleğe kolayca sığar.
    2. Gradyana faydalı bir stokastik gürültü ekler; bu sayede model sığ yerel çukurlardan (Local Minima) kurtulup genelleme yeteneği kazanır.

</details>

---

### Soru 16: Transfer Learning Stratejileri: Feature Extraction vs. Fine-Tuning

**SORU:**
Elinizde 500 fotoğraftan oluşan domates yaprağı hastalık veri seti vardır. ImageNet ile önceden eğitilmiş ResNet-50 modelini transfer edeceksiniz.
a) Katman dondurma (Feature extraction) nasıl uygulanır? Kod mantığını yazınız.
b) Fine-Tuning yaparken öğrenme oranı neden standart eğitimden 10-100 kat daha küçük ($\alpha \approx 10^{-5}$) seçilmelidir? Büyük seçilirse ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* **a) Katman Dondurma Mantığı:**
  ResNet-50 omurgasındaki tüm evrişim katmanlarının gradyan takibi kapatılır:
  ```python
  for param in resnet50.parameters():
      param.requires_grad = False  # Ağırlıklar donduruldu
  # Sadece son katman değiştirilir ve eğitilir
  resnet50.fc = nn.Linear(in_features=2048, out_features=4)
  ```
  Böylece 25 milyon parametreden sadece son katmandaki küçük ağırlıklar eğitilir; 500 resimle aşırı öğrenme engellenir.

* **b) Küçük Öğrenme Oranı Zorunluluğu:**
  * ImageNet üzerinde haftalarca eğitilmiş ağırlıklar zaten evrensel görsel özellikleri mükemmel öğrenmiştir.
  * Eğer Fine-Tuning yaparken büyük bir öğrenme oranı ($\alpha = 0.01$ veya $0.001$) kullanılırsa; rastgele başlayan yeni katmandan gelen devasa gradyan dalgası önceden öğrenilmiş bu hassas ağırlıkları siler ve ezer.
  * Bu duruma literatürde **Felaket Unutması (Catastrophic Forgetting)** denir. Ağırlıkları bozmadan sadece hafifçe kendi verimize uyarlamak için mikroskobik adımlar ($\alpha = 10^{-5}$) atılmalıdır.

</details>

---

## BÖLÜM 6: Hata Analizi ve Mühendislik Vakaları Soruları

### Soru 17: "Kediye Kurbağa Dedi!" Vakası (Arka Plan Yanlılığı ve Çözümleri)

**SORU:**
Laboratuvar uygulamasında bir öğrencinin eğittiği kedi-kurbağa sınıflandırma modeli, yeşil çimen üzerinde duran bir kediye $\%94$ güvenle "Kurbağa" demiştir.
a) Bu hatanın temel sebebi nedir? Literatürdeki adı nedir?
b) Bu modelin eğitim setindeki muhtemel hata nedir?
c) Bir mühendis olarak bu problemi çözmek için 3 somut önlem öneriniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* **a) Temel Sebep ve Adı:**
  * Problem **Arka Plan Yanlılığıdır (Background Bias / Kestirme Öğrenme - Shortcut Learning)**. Model kedinin anatomik formunu değil, arka plandaki piksel renklerini ezberlemiştir.
* **b) Eğitim Setindeki Hata:**
  * Öğrencinin indirdiği veri setinde kurbağaların tamamı yeşil çimen, nilüfer yaprağı ve sazlıktadır; kediler ise ev içinde parke/halı üzerindedir. Model kediyi değil, yeşil rengi sınıflandırmıştır.
* **c) Mühendislik Çözümleri:**
  1. **Veri Dağılımını Dengelemek:** Yeşil çimende kedi, karlı zeminde kedi, beyaz arka planda kurbağa fotoğrafları ekleyerek arka plan ile sınıf arasındaki yapay korelasyonu kırmak.
  2. **Veri Artırma (Data Augmentation):** Renk tonu ve parlaklık değişimleri (Color Jitter), gri tonlama dönüşümleri uygulamak.
  3. **Açıklanabilir Yapay Zeka (Grad-CAM):** Modelin karar verirken resmin neresine baktığını ısı haritasıyla inceleyip, arka plana bakan modelleri eğitime kabul etmemek.

</details>

---

### Soru 18: 1B Ses Sinyalleri Neden ve Nasıl 2B CNN ile Sınıflandırılır?

**SORU:**
Bir otomotiv fabrikasında motorlardan gelen sesler dinlenerek arıza tespiti yapılacaktır. Ses bir boyutlu ($1\text{D}$) bir sinyal olmasına rağmen neden doğrudan $1\text{D}$ modeller yerine $2\text{D}$ CNN modelleri tercih edilir? Dönüşüm sürecini anlatınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
1. **Dönüşüm Süreci (Spektrogram / STFT):**
   * Ham ses sinyali zamana bağlı basınç genliğidir ($1\text{D}$).
   * Sinyale **Kısa Zamanlı Fourier Dönüşümü (STFT)** uygulanarak küçük pencerelere bölünür.
   * Her penceredeki ses frekanslarının enerjisi (desibel) hesaplanır.
   * Ortaya $X$ ekseni zaman, $Y$ ekseni frekans ve piksel parlaklığı ses şiddeti olan iki boyutlu bir **Spektrogram görüntüsü** çıkar.
2. **Neden 2B CNN Tercih Edilir?**
   * İki boyutlu bilgisayarlı görü alanı (ResNet, EfficientNet vb.) trilyonlarca dolarlık yatırımla ve ImageNet ile çok üst düzey bir olgunluğa ulaşmıştır.
   * Sesi bir kez görüntü haline getirdiğinizde; ses alanında sıfırdan model geliştirmek yerine, kendini ispatlamış devasa 2D CNN omurgalarını ve Transfer Learning gücünü doğrudan kullanabilirsiniz.

</details>

---

### Soru 19: GAN Minimax Oyunu: Kalpazan (G) ve Polis (D) Amaç Fonksiyonu

**SORU:**
Çekişmeli Üretici Ağların (GAN) amaç fonksiyonu şöyledir:
$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}} [\log D(x)] + \mathbb{E}_{z \sim p_z} [\log (1 - D(G(z)))]$$

a) Buradaki $G$, $D$, $x$ ve $z$ terimlerini açıklayınız.
b) Ayırt Edici ($D$) neden bu fonksiyonu maksimize etmeye çalışır?
c) Üreteç ($G$) neden bu fonksiyonu minimize etmeye çalışır?
d) Nash Dengesi (Nash Equilibrium) sağlandığında $D(G(z))$ değeri ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### ÇÖZÜM:
* **a) Terimler:**
  * $x$: Gerçek veri setinden gelen orijinal fotoğraf.
  * $z$: Rastgele gürültü vektörü.
  * $G(z)$: Üreteç'in ürettiği sahte fotoğraf.
  * $D(\cdot)$: Ayırt Edici'nin bir görsele verdiği "gerçeklik olasılığı" ($0$ ile $1$ arası).
  * $G$: Kalpazan, $D$: Polis.

* **b) $D$'nin Maksimizasyon Hedefi:**
  * Gerçek resim verildiğinde $D(x) \to 1$ olmalıdır $\implies \log(1) = 0$ (Maksimum).
  * Sahte resim verildiğinde $D(G(z)) \to 0$ olmalıdır $\implies \log(1 - 0) = \log(1) = 0$ (Maksimum).
  * Polis gerçeğe 1, sahteye 0 vererek fonksiyonu en büyük değere ulaştırmak ister.

* **c) $G$'nin Minimizasyon Hedefi:**
  * Kalpazan $G$, bastığı sahte parayı polise gerçekmiş gibi yedirmek ister ($D(G(z)) \to 1$).
  * $D(G(z)) \to 1$ olduğunda $\log(1 - 1) = \log(0) \to -\infty$ (Minimum).
  * Yani kalpazan polisi kandırarak fonksiyonu en küçük değere çekmek ister.

* **d) Nash Dengesi:**
  * İki model de mükemmelleştiğinde polis artık gerçeği sahteden ayırt edemez.
  * Önüne gelen her resme $\%50$ ihtimalle gerçek der:
    $$D(G(z)) = \mathbf{0.50}$$

</details>
