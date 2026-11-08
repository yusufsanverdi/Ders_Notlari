# Derin Öğrenme Vize ve Final Sınavına Hazırlık: Kapsamlı ve İnteraktif Soru Bankası

Bu doküman, Derin Öğrenme dersinin tüm transkriptleri taranarak ders müfredatının **birebir öğrenme sırasına göre (Bölüm 1'den Bölüm 12'ye)** yapılandırılmış kapsamlı sınav soru bankasıdır.

İçerisinde:
- Derste yapılan **tüm gerçek quizler ve tahtada çözülen sınav soruları**,
- Vizede garanti çıkacak **adım adım öğretici sayısal hesaplama soruları**,
- Mimarilerin arkasındaki mantığı ölçen **ispat ve türetim soruları**,
- Hocanın derste vurguladığı **sözel, teorik ve analoji odaklı klasik yazılı soruları** yer almaktadır.

> [!TIP]
> **Çalışma Yöntemi (Self-Testing):**
> Tüm soruların cevapları ve ayrıntılı çözüm adımları **açılır-kapanır (toggle / `<details>`)** kutular içerisine gizlenmiştir. Çalışırken önce soruyu okuyup kendi çözümünüzü bir kağıda yazınız veya zihninizde yanıtlayınız; ardından **"🔍 Çözümü ve Detaylı Anlatımı Gör"** butonuna tıklayarak adımlarınızı ve gerekçelerinizi kontrol ediniz.

---

## 📑 İÇİNDEKİLER VE MÜFREDAT SIRASI

1. [BÖLÜM 1: Giriş ve Temel Kavramlar (Soru 1 – 5)](#bölüm-1-giriş-ve-temel-kavramlar)
2. [BÖLÜM 2: Matematiksel Altyapı ve Veri Temsili (Soru 6 – 9)](#bölüm-2-matematiksel-altyapı-ve-veri-temsili)
3. [BÖLÜM 3: Yapay Sinir Ağları ve Nöron Mimarisi (Soru 10 – 14)](#bölüm-3-yapay-sinir-ağları-ve-nöron-mimarisi)
4. [BÖLÜM 4: Model Eğitimi, Kayıp ve Optimizasyon (Soru 15 – 18)](#bölüm-4-model-eğitimi-kayıp-ve-optimizasyon)
5. [BÖLÜM 5: Model Başarımı ve Aşırı Öğrenme (Soru 19 – 22)](#bölüm-5-model-başarımı-ve-aşırı-öğrenme)
6. [BÖLÜM 6: CNN Mimarisi ve Hesaplamalar (Soru 23 – 28 - GERÇEK QUİZLER DAHİL)](#bölüm-6-cnn-mimarisi-ve-hesaplamalar)
7. [BÖLÜM 7: Klasik ve Modern CNN Mimarileri (Soru 29 – 34 - GERÇEK QUİZ DAHİL)](#bölüm-7-klasik-ve-modern-cnn-mimarileri)
8. [BÖLÜM 8: Transfer Öğrenme ve İnce Ayar (Soru 35 – 36)](#bölüm-8-transfer-öğrenme-ve-i̇nce-ayar)
9. [BÖLÜM 9: Nesne Tespiti ve YOLO Mimarisi (Soru 37 – 39)](#bölüm-9-nesne-tespiti-ve-yolo-mimarisi)
10. [BÖLÜM 10: Nesne Tespiti Metrikleri ve Matematiksel Analizi (Soru 40 – 42)](#bölüm-10-nesne-tespiti-metrikleri-ve-matematiksel-analizi)
11. [BÖLÜM 11: Üretken Modeller: GAN ve Halüsinasyon (Soru 43 – 45)](#bölüm-11-üretken-modeller-gan-ve-halüsinasyon)
12. [BÖLÜM 12: Pratik Mühendislik Uygulamaları ve Hata Analizi (Soru 46 – 48)](#bölüm-12-pratik-mühendislik-uygulamaları-ve-hata-analizi)

---

## BÖLÜM 1: Giriş ve Temel Kavramlar

### Soru 1 (Sözel / Teorik): AI, ML ve DL Farkı ve Kural Tabanlı Programlamanın Sınırları
**Soru:**
Geleneksel kural tabanlı yazılım geliştirme yaklaşımı ile Makine Öğrenmesi (ML) ve Derin Öğrenme (DL) arasındaki temel felsefe farkını açıklayınız. Neden spam filtresi gibi sistemlerde kural tabanlı if-else kodları başarısızlığa uğramıştır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Paradigma Farkı:**
   * **Geleneksel Yazılım:** $Kurallar (Kod) + Girdi\ Verisi \implies Çıktı$. Mühendis bütün kuralları tek tek zihninde öngörüp elle kodlamak zorundadır.
   * **Makine Öğrenmesi (ML):** $Girdi\ Verisi + Doğru\ Çıktılar \implies Model (Kurallar)$. Kuralları insan yazmaz; algoritma verideki istatistiksel örüntüleri (patterns) kendisi öğrenir.
   * **Derin Öğrenme (DL):** ML'nin çok katmanlı yapay sinir ağlarını kullanan alt dalıdır. Klasik ML'den farkı, özniteliklerin (kulak açısı, renk dağılımı vb.) insan mühendis tarafından elle çıkarılmasına gerek kalmadan, ham piksellerden modelin kendi kendine katman katman öznitelik öğrenmesidir (Feature Learning).
2. **Kural Tabanlı Yaklaşımın Tıkanma Nedeni (Spam Örneği):**
   * Mühendisler *"Eğer metinde 'ikramiye', 'bedava', 'tıkla' geçiyorsa spam yap"* diye kural yazdığında dolandırıcılar kelimeleri değiştirdi (`i.k.r.a.m.i.y.e`), eş anlamlı kullandı veya harf ekledi.
   * İnsan dilindeki trilyonlarca permütasyonu `if-else` ile yazmak imkansızdır. ML/DL modelleri ise kelime olasılık dağılımlarını, alan adı kalıplarını ve gönderici itibarını bütüncül bir vektör olarak incelediği için kuralların etrafından dolanılmasına izin vermez.

</details>

---

### Soru 2 (Senaryo / Sözel): Sınıflandırma mı, Regresyon mu?
**Soru:**
Aşağıdaki 5 problem için modelin üreteceği çıktının tipini inceleyerek problemin **Sınıflandırma (Classification)** mı yoksa **Regresyon (Regression)** mu olduğunu belirtiniz:
1. Bir otonom aracın ön kamerasından gelen görüntüye bakarak trafik ışığının rengini (Kırmızı, Sarı, Yeşil) tespit etmesi.
2. Bir ikinci el araç satış platformunda aracın kilometresi, yaşı, hasar kaydı ve motor gücü verilerek piyasa satış fiyatının tahmin edilmesi.
3. Bir öğrencinin derse devam yüzdesi, haftalık çalışma saati ve laboratuvar quiz notlarına bakarak vize sınavından alacağı puanın tahmin edilmesi.
4. Çekilen bir akciğer röntgeni (X-ray) görüntüsüne bakarak hastada zatürre (Pnömoni) olup olmadığının (Var / Yok) belirlenmesi.
5. Bir banka müşterisinin kredi kartı harcamasının şüpheli bir dolandırıcılık (Fraud) işlemi olup olmadığının belirlenmesi.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Temel İlke:**
  * Çıktı kesikli (ayrık / kategorik / sınıflı) etiketlerden oluşuyorsa $\implies$ **Sınıflandırma**
  * Çıktı reel (sürekli / sayısal) bir sayı değeri alıyorsa $\implies$ **Regresyon**

1. **Trafik ışığı rengi:** Kesikli 3 kategori $\implies$ **Sınıflandırma (Classification)**
2. **Araç piyasa fiyatı:** Sürekli sayısal para değeri ($850.000\text{ TL}$) $\implies$ **Regresyon (Regression)**
3. **Sınav puanı tahmini:** Sürekli sayısal not değeri ($74.5$) $\implies$ **Regresyon (Regression)**
4. **Zatürre teşhisi:** İkili kesikli durum ($0$ veya $1$) $\implies$ **Sınıflandırma (Binary Classification)**
5. **Dolandırıcılık tespiti:** İkili etiket (Normal / Şüpheli) $\implies$ **Sınıflandırma (Classification)**

</details>

---

### Soru 3 (Vaka Analizi / Sözel): PTT Oltalama (Phishing) Dolandırıcılığı Vakası
**Soru:**
Hocanın derste anlattığı PTT Kargo oltalama (Phishing) vakasında dolandırıcılar sistemi nasıl kurmuştur? Bir makine öğrenmesi modeli arayüzü birebir resmi siteye benzeyen bu tuzağı nasıl teşhis eder?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Olayın İşleyişi:**
   * Kullanıcıya *"Kargonuz adres yetersizliği nedeniyle teslim edilemedi, linke tıklayıp adresinizi güncelleyin"* mesajı atılır.
   * Tıklanan web sitesi resmi PTT sitesinin CSS, logo ve tasarımını birebir taklit eder ve kredi kartı bilgilerini ister.
   * Ancak URL dikkatle incelendiğinde harfler arasında fazladan karakter veya benzer harfler olduğu görülür (Örn: `ptt-kargo-guncelle.com` veya `pttt.gov.tr` benzeri sahte alan adları).
2. **Modelin Tespiti:**
   * Model yalnızca görsel arayüze aldanmaz.
   * Alan adı yaşı (yeni mi açılmış?), SSL sertifikası otoritesi, URL karakter uzunluğu ve entropisi, IP adresi geçmişi ve sitedeki yönlendirme scriptlerini girdi olarak alır.
   * Bu özellikler üzerinden kurumsal PTT ile uyuşmayan anomalileri saptayarak kullanıcıyı *"Zararlı / Sahte Bağlantı"* olarak uyarır.

</details>

---

### Soru 4 (Kavramsal): Derin Öğrenmenin 2010 Sonrası Yükselişini Sağlayan 3 Temel Unsur
**Soru:**
Yapay sinir ağlarının temelleri 1950'lere dayanmasına rağmen neden 2010'lu yıllara kadar beklemek zorunda kalmıştır? Derin öğrenme devrimini başlatan 3 temel sacayağını maddeler halinde açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Büyük Veri (Big Data):**
   * Derin sinir ağları milyonlarca parametreye sahiptir. Az veriyle beslenirlerse ezberlerler (Overfitting).
   * İnternet, akıllı telefonlar, sosyal medya ve dijital kameralar sayesinde milyonlarca etiketli görüntü (ImageNet) toplanabilmiştir.
2. **Donanım ve Paralel Hesaplama (GPU / TPU):**
   * Sinir ağları trilyonlarca matris çarpımından ibarettir.
   * Standart işlemciler (CPU) işlemleri sırayla yaparken; Grafik İşlemcileri (GPU - NVIDIA CUDA) binlerce çekirdeğiyle matrisleri paralel işleyerek aylarca sürecek eğitimi birkaç güne indirmiştir.
3. **Algoritmik İlerlemeler:**
   * Sigmoid yerine **ReLU** aktivasyon fonksiyonunun kullanılmasıyla yok olan gradyan (Vanishing gradient) çözülmüştür.
   * **Dropout** ile ezberleme engellenmiş; **Adam optimizer** ile hızlı yakınsama sağlanmış; **ResNet** artık bağlantılarıyla derin katmanlar stabil eğitilebilir hale gelmiştir.

</details>

---

### Soru 5 (Sınav Kuralı / Metodoloji): Veri Seti Bölümleme ve Veri Sızıntısı (Data Leakage)
**Soru:**
Bir derin öğrenme projesinde ham veri kümesi hangi oranlarda hangi alt kümelere bölünür? Test kümesine Veri Artırma (Data Augmentation) uygulamak neden büyük bir bilimsel ve metodolojik hatadır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Bölümleme Oranları:**
   * **Eğitim Seti (Train Set - %70 - %80):** Modelin ağırlıklarını güncellemek için doğrudan gördüğü küme.
   * **Doğrulama Seti (Validation Set - %10 - %15):** Eğitim devam ederken hiperparametreleri (öğrenme oranı vb.) ayarlamak ve aşırı öğrenmeyi izlemek için kullanılan küme.
   * **Test Seti (Test Set - %10 - %15):** Modelin eğitim sırasında kesinlikle hiç görmediği, nihai genelleme başarısını ölçen bağımsız hakem küme.
2. **Test Kümesine Neden Veri Artırma Yapılamaz?**
   * Test seti, modelin sokakta karşılaşacağı tarafsız gerçek dünyayı temsil eder.
   * Eğer test setine döndürme, kırpma veya yapay filtreler uygularsanız test verisinin doğal dağılımını bozarsınız.
   * Veri Artırma (Data Augmentation) **YALNIZCA EĞİTİM (TRAIN) KÜMESİNE** uygulanır. Test setinin bozulması veya eğitime sızdırılması (**Veri Sızıntısı / Data Leakage**) modelin gerçek dünya başarısını sahte şekilde yüksek gösterir ve projeyi geçersiz kılar.

</details>

---

## BÖLÜM 2: Matematiksel Altyapı ve Veri Temsili

### Soru 6 (Kavramsal): Skaler, Vektör, Matris ve Tensör Tanımları
**Soru:**
Derin öğrenmede kullanılan 0D, 1D, 2D ve ND tensör kavramlarını tanımlayınız ve derin öğrenme eğitim sürecinden birer somut örnek veriniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Skaler (0D Tensör):** Sıfır boyutlu, tek bir sayıdır.
  * *Örnek:* Bir epoch sonundaki anlık Kayıp değeri ($Loss = 0.245$) veya anlık öğrenme oranı ($\alpha = 0.001$).
* **Vektör (1D Tensör):** Sayıların tek bir eksen boyunca dizildiği 1 boyutlu listedir.
  * *Örnek:* Bir evin özelliklerini tutan Öznitelik Vektörü ($[m^2, \text{oda}, \text{bina yaşı}]$) veya modelin ürettiği sınıf olasılık vektörü.
* **Matris (2D Tensör):** Satır ve sütunlardan oluşan iki eksenli tablodur ($H \times W$).
  * *Örnek:* Siyah-beyaz (Grayscale) tek kanallı bir fotoğraf matrisi veya iki katman arasındaki Ağırlık Matrisi ($W$).
* **Tensör (3D / 4D / ND):** İkiden fazla eksene sahip genelleştirilmiş çok boyutlu veri yapılarıdır.
  * *Örnek (3D):* Renkli tek bir RGB görüntü ($H \times W \times 3$).
  * *Örnek (4D):* Modele tek bir adımda paket halinde verilen Batch renkli görüntüler ($B \times H \times W \times C$, örn: $32 \times 224 \times 224 \times 3$).

</details>

---

### Soru 7 (Sayısal / Boyut): Görüntü Tensör Boyutları ve Bellek Hesabı
**Soru:**
$256 \times 256$ piksel çözünürlüğünde renkli (RGB) fotoğraflardan oluşan bir veri setinde model eğitimi için `Batch Size = 32` seçilmiştir.
a) Modele her adımda verilen 4 boyutlu girdi tensörünün şeklini ($Shape$) yazınız.
b) Piksel değerleri 8-bit işaretsiz tamsayı (`uint8` - 1 bayt) olarak tutulursa, tek bir batch görüntünün bellekte kapladığı ham boyutu Megabayt (MB) cinsinden hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Tensör Şekli ($Shape$):**
  $$Shape = [B, H, W, C] = \mathbf{[32, 256, 256, 3]}$$
  *(PyTorch formatında $[B, C, H, W] = [32, 3, 256, 256]$).*

* **b) Bellek Hesabı:**
  * Toplam Piksel Sayısı $= 32 \times 256 \times 256 \times 3$
  * $256 \times 256 = 65.536$
  * $65.536 \times 3 = 196.608$ piksel (Tek resim)
  * $196.608 \times 32 = 6.291.456$ toplam piksel baytı.
  * Her piksel 1 bayt olduğuna göre:
    $$\text{Toplam Bayt} = 6.291.456 \text{ Bayt}$$
    $$\text{Kilobayt (KB)} = \frac{6.291.456}{1024} = 6144 \text{ KB}$$
    $$\text{Megabayt (MB)} = \frac{6144}{1024} = \mathbf{6.0 \text{ MB}}$$
  * Tek bir batch görüntü bellekte tam **$6\text{ MB}$** yer kaplar.

</details>

---

### Soru 8 (Sayısal): Matris Çarpımı Boyut Kuralı ve Hesaplama
**Soru:**
$A$ matrisi $2 \times 3$ ve $B$ matrisi $3 \times 2$ boyutundadır:
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}, \quad B = \begin{bmatrix} 7 & 8 \\ 9 & 1 \\ 2 & 3 \end{bmatrix}$$
a) Bu iki matrisin çarpımı ($C = A \cdot B$) tanımlı mıdır? Sonuç matrisinin boyutu ne olur?
b) $C$ matrisinin tüm elemanlarını adım adım çarparak hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Boyut Kuralı:**
  * $A$'nın boyutu: $2 \times \mathbf{3}$
  * $B$'nin boyutu: $\mathbf{3} \times 2$
  * Birinci matrisin sütun sayısı ($3$), ikinci matrisin satır sayısına ($3$) eşit olduğu için çarpım **tanımlıdır**.
  * Sonuç matrisinin boyutu: $\mathbf{2 \times 2}$ olacaktır.

* **b) Adım Adım Hesaplama:**
  $$c_{11} = (1 \cdot 7) + (2 \cdot 9) + (3 \cdot 2) = 7 + 18 + 6 = 31$$
  $$c_{12} = (1 \cdot 8) + (2 \cdot 1) + (3 \cdot 3) = 8 + 2 + 9 = 19$$
  $$c_{21} = (4 \cdot 7) + (5 \cdot 9) + (6 \cdot 2) = 28 + 45 + 12 = 85$$
  $$c_{22} = (4 \cdot 8) + (5 \cdot 1) + (6 \cdot 3) = 32 + 5 + 18 = 55$$

  $$C = A \cdot B = \begin{bmatrix} 31 & 19 \\ 85 & 55 \end{bmatrix}_{2 \times 2}$$

</details>

---

### Soru 9 (Teorik / Sayısal): Normalizasyon ve Z-Score Standardizasyonu
**Soru:**
Bir veri kümesinde evin metrekaresi $X_1 \in [50, 300]$, oda sayısı ise $X_2 \in [1, 5]$ aralığındadır.
a) Bu veriler normalize edilmeden doğrudan bir sinir ağına verilirse optimizasyon sürecinde ne gibi sorunlar yaşanır?
b) Ortalaması $\mu = 150$, standart sapması $\sigma = 50$ olan bir veri setinde $X = 250\text{ m}^2$ değerinin Z-Score standardizasyonunu ($Z = \frac{X - \mu}{\sigma}$) hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Yaşanacak Sorunlar:**
  * $X_1$ (Metrekare) sayısal olarak oda sayısından yüzlerce kat büyüktür.
  * Ağırlıklı toplamda ($Z = w_1 X_1 + w_2 X_2 + b$), $X_1$'in gradyanları devasa olurken $X_2$'nin gradyanları mikroskobik kalır.
  * Hata yüzeyi aşırı eliptik ve dar bir vadiye dönüşür; gradyan inişi iki duvar arasında sert zig-zaglar çizer ve öğrenme aşırı yavaşlar veya patlar.
  * Normalizasyon tüm öznitelikleri benzer ölçeğe (ortalama 0, varyans 1 veya $[0, 1]$ aralığına) getirerek hatanın simetrik bir çanakta hızla tabana inmesini sağlar.
* **b) Z-Score Hesabı:**
  $$Z = \frac{X - \mu}{\sigma} = \frac{250 - 150}{50} = \frac{100}{50} = \mathbf{+2.0}$$
  * Bu evin metrekaresi, veri kümesi ortalamasının tam $2$ standart sapma üzerindedir.

</details>

---

## BÖLÜM 3: Yapay Sinir Ağları ve Nöron Mimarisi

### Soru 10 (Sayısal): Tek Bir Nöronun Matematiksel Çıktısı ($Z = W \cdot X + b$)
**Soru:**
3 öznitelikli bir yapay nöron için şu değerler verilmiştir:
* Girdiler: $X = [x_1 = 3.0, x_2 = -2.0, x_3 = 1.0]^T$
* Ağırlıklar: $W = [w_1 = 0.4, w_2 = 1.5, w_3 = -2.0]^T$
* Bias: $b = 0.8$
a) Lineer kombinasyon ($Z$) değerini hesaplayınız.
b) Nöronun aktivasyon fonksiyonu $\text{ReLU}(z)$ ise çıktısını hesaplayınız.
c) Nöronun aktivasyon fonksiyonu $\text{Sigmoid}(\sigma(z))$ olsaydı çıktı ne olurdu? (Formülü yazıp hesaplayınız: $e^{-z}$ cinsinden).

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) $Z$ Hesabı:**
  $$Z = (w_1 x_1 + w_2 x_2 + w_3 x_3) + b$$
  $$Z = (0.4 \cdot 3.0) + (1.5 \cdot -2.0) + (-2.0 \cdot 1.0) + 0.8$$
  $$Z = 1.2 - 3.0 - 2.0 + 0.8 = \mathbf{-3.0}$$

* **b) ReLU Çıktısı:**
  $$\hat{y} = \text{ReLU}(-3.0) = \max(0, -3.0) = \mathbf{0.0}$$

* **c) Sigmoid Çıktısı:**
  $$\sigma(z) = \frac{1}{1 + e^{-z}} = \frac{1}{1 + e^{-(-3.0)}} = \frac{1}{1 + e^{3.0}}$$
  * $e^3 \approx 20.0855$ olduğuna göre:
    $$\sigma(-3.0) = \frac{1}{1 + 20.0855} = \frac{1}{21.0855} \approx \mathbf{0.0474} \quad (\%4.74)$$

</details>

---

### Soru 11 (Teorik / Analoji): Bias Teriminin Anlamı ve Bisiklet Analojisi
**Soru:**
Sinir hücresi formülünde neden yalnızca $W \cdot X$ yetmez de bir $+b$ terimi eklenir? Formülde $b=0$ olursa ağ geometrik olarak neye zorlanır? Hocanın derste anlattığı bisiklet analojisiyle açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Geometrik Gerekçe:**
   * Eğer $b = 0$ olursa, bütün girdiler sıfır olduğunda ($X=0$) çıktı daima $Z=0$ olur.
   * Çizilen hiper-düzlem / karar sınırı **daima orijinden $(0, 0)$ geçmek zorunda kalır**. Veri kümesi orijinden uzakta bir yerdeyse model o veriyi asla doğru ayıramaz. Bias, karar doğrusunu eksen üzerinde serbestçe yukarı-aşağı ötelememizi sağlar.
2. **Hocanın Bisiklet Analojisi:**
   * Düz bir yolda bisiklet sürerken pedal basmazsanız (Girdi $X=0$), bisiklet durur.
   * Eğer yol **yokuş aşağı** ise, hiç pedal çevirmeseniz bile bisiklet kendiliğinden hızlanır ve akar. Bu **pozitif biastır ($+b$)**.
   * Eğer yol **dik bir yokuş yukarı** ise, bisikletin durmaması ve ilerleyebilmesi için belirli bir eşik kuvvetinden fazla pedal basmanız gerekir. Bu da **negatif biastır ($-b$)**.
   * Bias, nöronun ateşlenme eşiğini (threshold) belirler.

</details>

---

### Soru 12 (İspat / Teorik): Doğrusallık Dışılık (Non-Linearity) Zorunluluğu
**Soru:**
*"Eğer katmanlar arasına aktivasyon fonksiyonu koymazsak ne olur?"* sorusunun cevabını iki katmanlı bir yapay sinir ağı üzerinden matematiksel olarak ispatlayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm ve İspat:
Aktivasyon fonksiyonu olmadığını varsayalım:
* 1. Katman Çıktısı: $Z_1 = W_1 X + b_1$
* 2. Katman Çıktısı: $Z_2 = W_2 Z_1 + b_2$

$Z_1$ ifadesini ikinci katmanda yerine koyalım:
$$Z_2 = W_2 (W_1 X + b_1) + b_2$$
Parantezi dağıtalım:
$$Z_2 = (W_2 W_1) X + (W_2 b_1 + b_2)$$

Burada:
* $W' = W_2 W_1$ (İki matrisin çarpımı yine tek bir matristir).
* $b' = W_2 b_1 + b_2$ (Bir vektör ile skalerin toplamı yine tek bir vektördür).

İfade şuna dönüşür:
$$Z_2 = W' X + b'$$

> **İSPAT SONUCU:**
> Katmanlar arasına doğrusal olmayan aktivasyon fonksiyonu koymazsanız, ardı ardına 1000 adet gizli katman koysanız bile bütün ağ matematiksel olarak **tek bir lineer katmana çöker!** Ağ XOR problemini dahi çözemez, eğrisel sınırları öğrenemez.

</details>

---

### Soru 13 (Kavramsal Karşılaştırma): Temel Aktivasyon Fonksiyonları
**Soru:**
Sigmoid, Tanh ve ReLU fonksiyonlarını çıkış aralıkları, sıfır merkezlilik durumları ve yok olan gradyan riski açısından karşılaştırınız. Neden modern derin CNN mimarilerinde ara katmanlarda Sigmoid yerine ReLU tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Sigmoid:** Çıkış aralığı $(0, 1)$'dir. Sıfır merkezli değildir. Uç noktalarda ($|z| > 4$) türevi sıfıra gittiği için **Vanishing Gradient** problemi çok yüksektir.
2. **Tanh:** Çıkış aralığı $(-1, 1)$'dir. **Sıfır merkezlidir** (Ortalaması 0'a yakındır). Ancak yine uç noktalarda doygunluğa ulaşır ve gradyan yok olur.
3. **ReLU ($\max(0, z)$):** Çıkış aralığı $[0, \infty)$'dur. Pozitif bölgede türevi sabit $1$'dir; dolayısıyla ağ ne kadar derin olursa olsun gradyan zayıflamadan geriye akar.
4. **Neden ReLU Tercih Edilir?**
   * **Yok Olan Gradyanı Çözmesi:** $z > 0$ için türev daima 1'dir.
   * **Hesaplama Hızı:** Sigmoid ve Tanh üstel işlem ($e^z$) yaparken, ReLU sadece basit bir `if z > 0` karşılaştırmasıdır; GPU'larda 6 kat daha hızlı çalışır.

</details>

---

### Soru 14 (Sayısal / Teorik): Softmax Fonksiyonu ve Olasılık Hesabı
**Soru:**
3 sınıflı bir hayvan sınıflandırma modelinin son katmanından çıkan ham skorlar (Logits):
$z_1 = 2.0$ (Zürafa), $z_2 = 1.0$ (At), $z_3 = 0.0$ (Köpek)
a) Softmax fonksiyonunun formülünü yazınız.
b) Bu skorları Softmax'tan geçirerek her bir sınıfın olasılık değerlerini hesaplayınız. ($e^2 \approx 7.39, e^1 \approx 2.72, e^0 = 1.00$).

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Formül:**
  $$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^C e^{z_j}}$$

* **b) Adım Adım Hesaplama:**
  1. Üstel Değerlerin Hesabı:
     * $e^{z_1} = e^{2.0} \approx 7.39$
     * $e^{z_2} = e^{1.0} \approx 2.72$
     * $e^{z_3} = e^{0.0} = 1.00$
  2. Paydaların Toplamı:
     $$\text{Toplam} = 7.39 + 2.72 + 1.00 = 11.11$$
  3. Olasılıklar:
     * $P(\text{Zürafa}) = \frac{7.39}{11.11} \approx \mathbf{0.665} \quad (\%66.5)$
     * $P(\text{At}) = \frac{2.72}{11.11} \approx \mathbf{0.245} \quad (\%24.5)$
     * $P(\text{Köpek}) = \frac{1.00}{11.11} \approx \mathbf{0.090} \quad (\%9.0)$
  * Toplam: $0.665 + 0.245 + 0.090 = 1.000$ (%100). Model $\%66.5$ güvenle zürafa tahmininde bulunur.

</details>

---

## BÖLÜM 4: Model Eğitimi, Kayıp ve Optimizasyon

### Soru 15 (Kavramsal): Kayıp Fonksiyonları (Loss Functions) Seçimi
**Soru:**
MSE, Binary Cross-Entropy ve Categorical Cross-Entropy kayıp fonksiyonlarının hangi problem türlerinde kullanıldığını ve çıktı katmanında hangi aktivasyon fonksiyonuyla eşleştiklerini yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Ortalama Kare Hata (MSE - Mean Squared Error):**
   * *Problem:* Regresyon (Sürekli sayı tahmini, ev fiyatı, sıcaklık vb.).
   * *Çıkış Aktivasyonu:* Linear (Hiçbir aktivasyon konmaz veya identity).
2. **İkili Çapraz Entropi (Binary Cross-Entropy - BCE):**
   * *Problem:* İkili sınıflandırma (Kedi/Köpek, Spam/Normal, 0 veya 1).
   * *Çıkış Aktivasyonu:* **Sigmoid** (Çıktıyı $0-1$ arası tek bir olasılığa dönüştürür).
3. **Kategorik Çapraz Entropi (Categorical Cross-Entropy - CCE):**
   * *Problem:* Çok sınıflı sınıflandırma ($C > 2$, ImageNet 1000 sınıf, MNIST 10 sınıf).
   * *Çıkış Aktivasyonu:* **Softmax** (Tüm sınıfların toplamı 1 olan olasılık dağılımı).

</details>

---

### Soru 16 (Teorik / Çizim): Öğrenme Oranı ($\alpha$) Dinamikleri
**Soru:**
Gradyan inişinde öğrenme oranının ($\alpha$) çok büyük veya çok küçük seçilmesinin optimizasyon sürecine etkilerini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Öğrenme Oranı Çok Küçükse ($\alpha = 10^{-6}$):**
  * Atılan adımlar mikroskobiktir.
  * Modelin minimum noktaya ulaşması haftalar/aylar sürebilir.
  * Model eyer noktalarına (Saddle Points) veya sığ yerel çukurlara takılıp kalır.
* **Öğrenme Oranı Çok Büyükse ($\alpha = 1.0$ veya $5.0$):**
  * Adım minimum çukurun genişliğini aşar. Karşı duvara çarpar, vadinin üzerinden atlar.
  * Kayıp değeri azalmak yerine patlar ($Loss \to \infty$ veya `NaN` hatası). Model tamamen ıraksar (Divergence).
* **Optimal Öğrenme Oranı ($\alpha \approx 10^{-3}$ veya $3 \times 10^{-4}$):**
  * Hızlı, kararlı ve salınım yapmadan minimum kayıp noktasına yakınsar.

</details>

---

### Soru 17 (Sayısal): Epoch, Batch Size ve İterasyon Hesabı
**Soru:**
$60.000$ adet görüntüden oluşan bir veri seti `Batch Size = 64` ile `20 Epoch` boyunca eğitilecektir.
a) 1 Epoch'ta kaç adet iterasyon (ağırlık güncellemesi) gerçekleşir?
b) 20 Epoch tamamlandığında toplam kaç güncelleme yapılmış olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) 1 Epoch İterasyon Sayısı:**
  $$\text{İterasyon} = \left\lceil \frac{\text{Toplam Veri}}{\text{Batch Size}} \right\rceil = \left\lceil \frac{60.000}{64} \right\rceil = \lceil 937.5 \rceil = \mathbf{938 \text{ İterasyon}}$$
* **b) 20 Epoch Toplam Güncelleme:**
  $$\text{Toplam Güncelleme} = 20 \times 938 = \mathbf{18.760 \text{ Kez}}$$

</details>

---

### Soru 18 (Kavramsal): SGD, Momentum ve Adam Optimizer Karşılaştırması
**Soru:**
Stokastik Gradyan İnişi (SGD), Momentum ve Adam algoritmalarını çalışma prensipleri ve hızları açısından karşılaştırınız. Neden Adam günümüzde en çok tercih edilen optimizasyon algoritmasıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **SGD (Stochastic Gradient Descent):** Her adımda rastgele küçük bir paketle (Mini-batch) yön tayin eder. Basittir ancak eyer noktalarında ve gürültülü vadilerde yavaş ilerler.
2. **Momentum:** Fizikteki eylemsizlik ilkesini gradyana ekler. Geçmiş adımların yönünü hatırlar; sürekli aynı yönde gidiyorsa hızlanır, yön değiştiriyorsa yavaşlar.
3. **Adam (Adaptive Moment Estimation):**
   * Hem Momentum (gradyanların hareketli ortalaması) hem de RMSProp (gradyan karelerinin hareketli ortalaması) algoritmalarını birleştirir.
   * **Neden En Popüler?** Her bir parametre için öğrenme oranını ayrı ayrı ve adaptif olarak ayarlar. Sık güncellenen ağırlıkların adımını küçültür, nadir güncellenen ağırlıkların adımını büyütür. Hiperparametre hassasiyeti çok düşüktür; varsayılan $\alpha = 0.001$ değeriyle neredeyse tüm problemlerde mükemmel yakınsar.

</details>

---

## BÖLÜM 5: Model Başarımı ve Aşırı Öğrenme

### Soru 19 (Teorik / Vaka): Doğruluk (Accuracy) Sınırı ve Dengesiz Veri Kümeleri
**Soru:**
10.000 kişilik bir kanser tarama testinde sadece 20 kişi kanserdir ($y=1$), 9.980 kişi sağlıklıdır ($y=0$). Modelin herkese "Sağlıklısın" dediği bir senaryoda:
a) Modelin Doğruluk (Accuracy) oranını hesaplayınız.
b) Bu model neden tıbbi olarak tamamen kullanışsız ve felakettir? Bir mühendis bu durumda hangi metrikleri incelemelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Accuracy Hesabı:**
  $$\text{Accuracy} = \frac{\text{Doğru Tahmin}}{\text{Toplam Veri}} = \frac{9.980}{10.000} = \mathbf{\%99.8}$$
* **b) Değerlendirme:**
  * Model kağıt üzerinde $\%99.8$ başarı göstermektedir; ancak kanserli 20 hastanın tamamını kaçırmıştır ($\text{Recall} = 0$).
  * Dengesiz veri setlerinde Accuracy yanıltıcı bir illüzyondur.
  * Bir mühendis kesinlikle **Precision, Recall, F1-Score ve Confusion Matrix** incelemelidir.

</details>

---

### Soru 20 (Kavramsal): Genelleme (Generalization), Overfitting ve Underfitting
**Soru:**
Genelleme (Generalization) nedir? Overfitting ile Underfitting arasındaki farkı eğitim/doğrulama kaybı grafiği ve hocanın sınav analojisiyle açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Genelleme (Generalization):** Modelin eğitimde hiç görmediği yeni ve gürültülü gerçek dünya verileri üzerinde doğru tahmin üretebilme kabiliyetidir.
* **Underfitting (Eksik Öğrenme):** Model problemi kavrayamamıştır. Hem Train kaybı hem Val kaybı yüksektir. Model çok basittir veya az eğitilmiştir.
* **Overfitting (Aşırı Öğrenme / Ezberleme):**
  * Train kaybı sıfıra yaklaşırken ($Loss_{train} \to 0$), Validation kaybı yükselmeye başlar ($Loss_{val} \uparrow$).
  * **Hocanın Öğrenci Analojisi:** Eski çıkmış soruların soru numarasını, şıklarını ve virgülünü ezberleyen bir öğrenci düşünün. Eski testten 100 alır; fakat sınavda hoca sorudaki rakamları veya bir iki kelimeyi değiştirdiğinde mantığı bilmediği için 0 alır.

</details>

---

### Soru 21 (Teorik / Analoji): Dropout Katmanı ve Unutma Mekanizması
**Soru:**
Dropout katmanı eğitim sırasında nasıl çalışır? Test (Inference) anında neden kapatılır? İnsan beyninin unutma mekanizmasıyla benzerliğini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Çalışma Şekli:** Eğitim sırasında her adımda o katmandaki nöronlar belirlenen bir olasılıkla ($p=0.5$) rastgele kapatılır ve çıktıları sıfırlanır. Nöronlar birbirine güvenemez ve bağımsız güçlü özellikler öğrenmek zorunda kalır.
2. **Test Anındaki Durumu:** Test anında **Dropout tamamen kapatılır**, tüm nöronlar aktiftir. Ancak eğitimdeki sinyal dengesini korumak için çıktılar $(1-p)$ ile ölçeklenir.
3. **Beyin ve Unutma Analojisi:** İnsan beyni gün boyu binlerce araba plakası ve önemsiz detay görür. Gece uykuda beyin önemsiz sinaps bağlantılarını budar (unutur). Eğer her şeyi ezberleseydik yeni ve genel kavramları öğrenemezdik. Nöronların unutması zekanın ve genellemenin temel şartıdır.

</details>

---

### Soru 22 (Metodolojik): Ablasyon (Ablation) Çalışması
**Soru:**
Derin öğrenme literatüründe "Ablasyon Çalışması (Ablation Study)" nedir? Neden bir modelin başarısını ispatlamak için sadece nihai doğruluk puanı yeterli değildir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Tanım:** Geliştirilen bir mimarideki bileşenlerin (Dropout, Veri artırma, artık bağlantı vb.) tek tek sistemden çıkarılarak veya değiştirilerek modele olan bireysel katkısının ölçüldüğü kontrollü deney serisidir.
* **Önemi:** *"Modelim %95 doğruluk verdi"* demek bilimsel olarak yetersizdir. *"Bu modele Dropout eklediğimde doğruluk %91'den %95'e çıktı; Dropout'u çıkardığımda %91'e düştü"* diyerek o bileşenin gerçek başarısını ablasyon ile ispatlamak zorundasınız.

</details>

---

## BÖLÜM 6: CNN Mimarisi ve Hesaplamalar

### Soru 23 (Teorik): Görüntülerde Dense Ağların Çöküşü
**Soru:**
$1000 \times 1000$ piksel boyutunda 3 kanallı renkli bir görüntü neden doğrudan klasik Tam Bağlantılı (Dense) bir ağa verilemez? CNN bu iki büyük sorunu hangi iki prensiple çözer?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Çöküş Nedenleri:**
   * **Parametre Patlaması:** $1000 \times 1000 \times 3 = 3.000.000$ piksel. Sadece 1.000 nöronlu tek bir gizli katmana bağlarsanız $3.000.000 \times 1.000 = 3\text{ Milyar Parametre}$ gerekir. Bellek anında çöker ve model aşırı ezberler.
   * **Uzamsal Bilgi Kaybı:** Resim tek bir vektöre açıldığında piksellerin 2 boyutlu komşuluk ve mesafe ilişkisi yok olur.
2. **CNN Çözümü:**
   * **Yerel Alıcı Alan (Local Receptive Field):** Tüm resme aynı anda bağlanmak yerine küçük pencerelerle ($3 \times 3$) yerel bölgelere bağlanır.
   * **Ağırlık Paylaşımı (Parameter Sharing):** Aynı $3 \times 3$ filtre tüm resim üzerinde kaydırılarak parametre sayısı milyonlardan birkaç bine indirilir.

</details>

---

### Soru 24 (GERÇEK QUİZ 3 - 2 Kasım Telafi): Temel CNN Katmanları
**Soru:**
*"Ödevinizde ve projelerinizde kullanmış olduğunuz temel CNN katmanlarını yazınız ve görevlerini kısaca açıklayınız."* (Hocanın telafi quiz sorusudur).

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Conv2D (Evrişim):** Görüntü üzerinde filtreler kaydırarak kenar, köşe ve doku öznitelik haritalarını çıkarır.
2. **Aktivasyon (ReLU):** Negatif değerleri sıfırlayarak ağa doğrusallık dışılık kazandırır ve gradyan akışını hızlandırır.
3. **MaxPool2D (Havuzlama):** Uzamsal boyutu yarıya indirerek hesaplama yükünü azaltır, baskın özellikleri özetler (Parametresi sıfırdır).
4. **Flatten (Düzleştirme):** Çok boyutlu öznitelik haritasını tek boyutlu vektöre açar (Parametresi sıfırdır).
5. **Dense (Tam Bağlantılı):** Çıkarılan öznitelikleri birleştirip nihai sınıflandırmayı yapar.
6. **Dropout:** Eğitimde rastgele nöron kapatarak ezberlemeyi önler.
7. **Softmax:** Çıkış skorlarını toplamı %100 olan olasılık dağılımına dönüştürür.

</details>

---

### Soru 25 (GERÇEK QUİZ 2 - 2 Kasım Part 1): Tahtadaki Mimari Boyut Hesabı
**Soru:**
Girdi: $64 \times 64 \times 3$ (RGB görüntü).
* 1. Katman: `Conv2D(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)`
* 2. Katman: `MaxPool2D(kernel_size=2, stride=2)`
* 3. Katman: `Conv2D(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)`
* 4. Katman: `MaxPool2D(kernel_size=2, stride=2)`
* 5. Katman: `Flatten`
* **Soru:** *Flatten katmanından sonra elde edilen toplam özellik sayısı kaçtır?*

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Adım Adım Çözüm:
1. **1. Conv2D:** $K=3, S=1, P=1 \implies$ Boyut korunur: **$64 \times 64 \times 16$**
2. **1. MaxPool2D:** $K=2, S=2 \implies$ Boyut yarıya iner: **$32 \times 32 \times 16$**
3. **2. Conv2D:** $K=3, S=1, P=1 \implies$ Boyut korunur: **$32 \times 32 \times 32$**
4. **2. MaxPool2D:** $K=2, S=2 \implies$ Boyut yarıya iner: **$16 \times 16 \times 32$**
5. **Flatten Katmanı:**
   $$\text{Toplam Eleman} = 16 \times 16 \times 32 = 256 \times 32 = \mathbf{8192}$$

**NİHAİ CEVAP:** **8192**

</details>

---

### Soru 26 (Sayısal / Boyut): $128 \times 128 \times 3$ Mimarisi Boyut Akışı
**Soru:**
Girdi: $128 \times 128 \times 3$.
1. `Conv2D(in=3, out=32, K=3, S=1, P=1)`
2. `MaxPool2D(K=2, S=2)`
3. `Conv2D(in=32, out=64, K=5, S=1, P=2)`
4. `MaxPool2D(K=2, S=2)`
5. `Conv2D(in=64, out=128, K=3, S=2, P=1)`
6. `Flatten`
Katman tensör boyutlarını ve Flatten eleman sayısını hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. Conv2D ($K=3, S=1, P=1$): **$128 \times 128 \times 32$**
2. MaxPool2D: **$64 \times 64 \times 32$**
3. Conv2D ($K=5, S=1, P=2$): $W_{out} = \frac{64 - 5 + 4}{1} + 1 = 64 \implies \mathbf{64 \times 64 \times 64}$
4. MaxPool2D: **$32 \times 32 \times 64$**
5. Conv2D ($K=3, S=2, P=1$): $W_{out} = \lfloor \frac{32 - 3 + 2}{2} \rfloor + 1 = 15 + 1 = 16 \implies \mathbf{16 \times 16 \times 128}$
6. Flatten: $16 \times 16 \times 128 = 256 \times 128 = \mathbf{32.768}$

</details>

---

### Soru 27 (Sayısal / Parametre): Eğitilebilir Parametre Sayısı Hesabı
**Soru:**
a) `Conv2D(in_channels=16, out_channels=64, kernel_size=3)` katmanının parametre sayısını hesaplayınız (Bias dahil).
b) `Dense(in_features=2048, out_features=128)` katmanının parametre sayısını hesaplayınız (Bias dahil).

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Conv2D Parametre Sayısı:**
  $$\text{Parametre} = \Big( (K_h \times K_w \times C_{in}) + 1 \Big) \times C_{out}$$
  $$\text{Parametre} = \Big( (3 \times 3 \times 16) + 1 \Big) \times 64 = (144 + 1) \times 64 = 145 \times 64 = \mathbf{9280}$$
* **b) Dense Parametre Sayısı:**
  $$\text{Parametre} = (N_{in} + 1) \times N_{out} = (2048 + 1) \times 128 = 2049 \times 128 = \mathbf{262.272}$$

</details>

---

### Soru 28 (Sayısal / Mimari): Flatten vs. GAP Parametre Tasarrufu
**Soru:**
Son katman tensörü $7 \times 7 \times 512$ ve sınıf sayısı 10'dur.
a) Flatten kullanılıp 10 nörona bağlanırsa kaç parametre oluşur?
b) GAP kullanılıp 10 nörona bağlanırsa kaç parametre oluşur? Tasarruf oranını hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Flatten:**
  $N_{in} = 7 \times 7 \times 512 = 25.088$.
  $$\text{Parametre} = (25.088 + 1) \times 10 = \mathbf{250.890}$$
* **b) GAP:**
  Tensör $1 \times 1 \times 512$'ye iner ($N_{in} = 512$).
  $$\text{Parametre} = (512 + 1) \times 10 = \mathbf{5.130}$$
* **Tasarruf:** Parametre sayısı $\%98$ azalır, aşırı ezberleme engellenir.

</details>

---

## BÖLÜM 7: Klasik ve Modern CNN Mimarileri

### Soru 29 (Tarihsel / Kavramsal): LeNet-5'ten AlexNet'e 4 Büyük Devrim
**Soru:**
AlexNet'in 2012 ImageNet yarışmasında hata oranını %26'dan %15'e düşürerek derin öğrenme devrimini başlatmasını sağlayan 4 temel mimari yeniliği yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **ReLU Aktivasyonu:** Sigmoid yerine ReLU kullanarak ağın 6 kat daha hızlı eğitilmesini sağlamış ve vanishing gradient'i çözmüştür.
2. **Dropout ($p=0.5$):** 60 milyon parametreli bu devasa ağın aşırı ezberlemesini önlemek için ilk kez tam bağlantılı katmanlarda Dropout kullanılmıştır.
3. **Çift GPU Paralel Eğitimi:** Ağ ikiye bölünerek dönemin iki NVIDIA GTX 580 GPU'su üzerinde paralel eğitilmiştir.
4. **Yoğun Veri Artırma (Data Augmentation):** Görüntüler rastgele aynalanmış, kırpılmış ve renk değişimlerine tabi tutulmuştur.

</details>

---

### Soru 30 (İspat / Matematiksel): VGG %28 Filtre Tasarrufu İspatı
**Soru:**
Neden bir adet $5 \times 5$ filtre yerine iki adet ardışık $3 \times 3$ filtre tercih edilir? Alıcı alan eşitliğini ve %28 parametre tasarrufunu matematiksel olarak ispatlayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### İspat:
1. **Alıcı Alan:** İki adet $3 \times 3$ katman ardışık uygulandığında girdi üzerinde $3 + (3-1) = 5 \times 5$'lik alanı görür; bilgi kaybı olmaz.
2. **Parametre Hesabı ($C$ girdi ve çıktı kanalı):**
   * Tek $5 \times 5$ katman: $5 \times 5 \times C \times C = \mathbf{25 C^2}$
   * İki adet $3 \times 3$ katman: $2 \times (3 \times 3 \times C \times C) = \mathbf{18 C^2}$
   * Oran: $\frac{18 C^2}{25 C^2} = 0.72 \implies \mathbf{\%28 \text{ Tasarruf!}}$
3. **Ekstra Avantaj:** Araya bir ReLU daha girdiği için model daha zengin karar sınırları çizer.

</details>

---

### Soru 31 (Teorik / İspat): ResNet Skip Connection ve Gradyan Kurtarma
**Soru:**
ResNet mimarisinde artık blok formülü $H(x) = F(x) + x$ olarak tanımlanmıştır. Geri yayılımda türev alındığında bu $+x$ bağlantısının yok olan gradyanı nasıl engellediğini matematiksel olarak gösteriniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### İspat:
Hata fonksiyonu $\mathcal{L}$ olsun. Girdiye göre türev:
$$\frac{\partial \mathcal{L}}{\partial x} = \frac{\partial \mathcal{L}}{\partial H} \cdot \frac{\partial H}{\partial x}$$
Burada $H(x) = F(x) + x$ türevi:
$$\frac{\partial H}{\partial x} = \frac{\partial F}{\partial x} + 1$$
Yerine koyarsak:
$$\frac{\partial \mathcal{L}}{\partial x} = \frac{\partial \mathcal{L}}{\partial H} \cdot \frac{\partial F}{\partial x} + \mathbf{\frac{\partial \mathcal{L}}{\partial H}}$$

> **SONUÇ:** Katman ağırlıkları çok kötü olsa veya $\frac{\partial F}{\partial x} \approx 0$ olsa dahi formüldeki **$+1$** sayesinde gradyan sinyali ($\frac{\partial \mathcal{L}}{\partial H}$) kayıpsız olarak bir önceki katmana akar. Bu sayede 152 katmanlı ağlar çökmeden eğitilebilir.

</details>

---

### Soru 32 (GERÇEK QUİZ 1 - 26 Ekim): Cep Telefonu İçin Hafif Model Seçimi
**Soru:**
*"Bir öğrenci cep telefonunda çok hafif ve hızlı çalışan bir sınıflandırma modeli geliştirmek istiyor. LeNet, VGG, ResNet, MobileNet, EfficientNet modellerinden hangisini seçmelidir?"*

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Cevap:** **MobileNet**
* **Gerekçe:** Depthwise Separable Convolution kullanarak standart evrişime göre hesaplama yükünü yaklaşık $\frac{1}{9}$'a düşürür. Cep telefonlarının düşük batarya ve zayıf işlemci ortamında yüksek FPS ile çalışabilen en optimize modeldir.

</details>

---

### Soru 33 (Sayısal / İspat): MobileNet Hesaplama Tasarrufu İspatı
**Soru:**
Standart evrişim maliyeti ile MobileNet Depthwise Separable Conv maliyetini formüle edip oranlayınız. $3 \times 3$ filtre ve 128 kanal için yaklaşık tasarruf çarpanı kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### İspat:
* Standart Maliyet: $D_K^2 \cdot M \cdot N \cdot D_F^2$
* MobileNet Maliyeti: $(D_K^2 \cdot M \cdot D_F^2) + (M \cdot N \cdot D_F^2)$
* Oran:
  $$\text{Oran} = \frac{1}{N} + \frac{1}{D_K^2}$$
* $D_K = 3, N = 128$ için:
  $$\text{Oran} = \frac{1}{128} + \frac{1}{9} \approx 0.0078 + 0.1111 = 0.1189 \approx \mathbf{\frac{1}{8.4}}$$
* MobileNet standart evrişime kıyasla **8.4 kat daha az hesaplama** yapar!

</details>

---

### Soru 34 (Kavramsal): EfficientNet Compound Scaling
**Soru:**
EfficientNet'in literatüre getirdiği Bileşik Ölçekleme (Compound Scaling) prensibi nedir? Eski rastgele ölçekleme yöntemlerinden farkını açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Eski yöntemlerde araştırmacılar modeli büyütmek için sadece derinliği (daha çok katman), sadece genişliği (daha çok kanal) veya sadece çözünürlüğü artırıyordu. Tek bir boyutu aşırı artırmak hızla doygunluğa yol açar.
* EfficientNet bu 3 ekseni sabit bir bileşik katsayı ($\phi$) ile matematiksel dengede birlikte büyütür:
  $$d = \alpha^\phi, \quad w = \beta^\phi, \quad r = \gamma^\phi$$
* Böylece model boyutu orantılı büyür ve çok daha az parametreyle en yüksek doğruluk elde edilir.

</details>

---

## BÖLÜM 8: Transfer Öğrenme ve İnce Ayar

### Soru 35 (Kavramsal / Analoji): Pre-Trained Model ve İnsan Analojisi
**Soru:**
Önceden eğitilmiş (Pre-trained) model nedir? Hocanın *"Sizler de birer pre-trained modelsiniz"* analojisini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Pre-trained Model:** Milyonlarca resim (ImageNet) üzerinde önceden eğitilerek görsel dünyanın temel çizgilerini, dokularını ve formlarını öğrenmiş modeldir.
* **Hocanın Analojisi:** Bir üniversite öğrencisi derin öğrenme dersine geldiğinde zihni sıfır değildir; 12 yıl boyunca ilkokul ve lisede okuma-yazma, matematik ve mantık öğrenmiştir (Pre-training). Derin öğrenmeyi öğrenirken anaokuluna geri dönmez; var olan güçlü temeli üzerine yeni uzmanlığı ekler (Fine-Tuning).

</details>

---

### Soru 36 (Metodolojik / Kod): Feature Extraction vs. Fine-Tuning
**Soru:**
Transfer öğrenmede Katman Dondurma (Feature Extraction) ile İnce Ayar (Fine-Tuning) arasındaki fark nedir? Fine-Tuning yaparken öğrenme oranı neden çok küçük ($\alpha = 10^{-5}$) seçilmelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Feature Extraction:** Modelin evrişim omurgası tamamen dondurulur (`requires_grad = False`). Sadece en sondaki yeni sınıflandırma başlığı eğitilir. Çok az veri olduğunda tercih edilir.
2. **Fine-Tuning:** Son katman eğitildikten sonra omurganın üst katmanlarının da kilidi açılır (`requires_grad = True`) ve model kendi verimizle birlikte yeniden eğitilir.
3. **Küçük Öğrenme Oranı Zorunluluğu:** Büyük bir öğrenme oranı kullanılırsa, yeni veriden gelen sert gradyanlar önceden öğrenilmiş hassas ağırlıkları siler (**Felaket Unutması / Catastrophic Forgetting**). Ağırlıkları incelikle korumak için öğrenme oranı en az 10-100 kat küçültülür ($\alpha = 10^{-5}$).

</details>

---

## BÖLÜM 9: Nesne Tespiti ve YOLO Mimarisi

### Soru 37 (Kavramsal): Bilgisayarlı Görü Görevleri Hiyerarşisi
**Soru:**
Classification, Localization, Object Detection ve Segmentation görevlerinin çıktılarını ve farklarını yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Classification:** Resimde ne var? $\implies$ Tek bir sınıf etiketi ("Kedi").
2. **Localization:** Resimde ne var ve nerede? $\implies$ Tek nesne için sınıf + 1 sınırlayıcı kutu ($[x, y, w, h]$).
3. **Object Detection:** Resimde hangi nesneler nerede? $\implies$ Çoklu nesneler için sınıf etiketleri + çoklu sınırlayıcı kutular.
4. **Segmentation:** Hangi piksel hangi nesneye ait? $\implies$ Kutu yerine nesnenin piksel düzeyinde sınır maskeleri boyanır.

</details>

---

### Soru 38 (Sayısal): YOLO Normalize Koordinat Dönüşümü
**Soru:**
$1920 \times 1080$ piksel resimde köşe koordinatları $x_{min}=480, y_{min}=270, x_{max}=960, y_{max}=810$ olan nesnenin YOLO normalize koordinatlarını ($x_c, y_c, w, h$) hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. $W_{\text{kutu}} = 960 - 480 = 480 \implies w = \frac{480}{1920} = \mathbf{0.250000}$
2. $H_{\text{kutu}} = 810 - 270 = 540 \implies h = \frac{540}{1080} = \mathbf{0.500000}$
3. $X_{\text{merkez}} = 480 + 240 = 720 \implies x_c = \frac{720}{1920} = \mathbf{0.375000}$
4. $Y_{\text{merkez}} = 270 + 270 = 540 \implies y_c = \frac{540}{1080} = \mathbf{0.500000}$

**YOLO Formatı:** `class_id 0.375000 0.500000 0.250000 0.500000`

</details>

---

### Soru 39 (Teorik): YOLO Izgara Yapısı ve Hız Avantajı
**Soru:**
YOLO algoritmasında nesnenin tespitinden hangi ızgara (grid) hücresi sorumludur? Faster R-CNN gibi iki aşamalı modellere göre nasıl gerçek zamanlı (Real-Time 60+ FPS) hız sağlar?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Sorumlu Hücre Kuralı:** Görüntü $S \times S$ ızgaraya bölünür. Nesnenin tam **merkez noktası ($x_c, y_c$)** hangi hücrenin sınırları içine düşüyorsa, o nesneyi tespit etmekten sadece o hücre sorumludur.
2. **Hız Avantajı:** İki aşamalı modeller önce binlerce aday bölge önerisi üretip her birini tek tek sınıflandırırken; YOLO görüntünün tamamını tek bir sinir ağından tek bir ileri yayılımda (Forward pass) geçirir. Kutuları ve sınıfları aynı anda tahmin ederek saniyede 60-140 kare işleyebilir.

</details>

---

## BÖLÜM 10: Nesne Tespiti Metrikleri ve Matematiksel Analizi

### Soru 40 (Sayısal): Adım Adım IoU Hesabı ve Karar Eşiği
**Soru:**
* Gerçek Kutu ($A$): $[50, 50, 150, 150]$
* Tahmin Kutusu ($B$): $[100, 100, 200, 200]$
$\text{Area}(A)$, $\text{Area}(B)$, Kesişim Alanı, Birleşim Alanı ve $\text{IoU}$ değerini hesaplayınız. $\tau = 0.50$ eşiğinde bu tespit TP midir FP midir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Adım Adım Çözüm:
1. $\text{Area}(A) = (150-50) \times (150-50) = 100 \times 100 = \mathbf{10.000}$
2. $\text{Area}(B) = (200-100) \times (200-100) = 100 \times 100 = \mathbf{10.000}$
3. Kesişim Koordinatları: $[\max(50,100), \max(50,100), \min(150,200), \min(150,200)] = [100, 100, 150, 150]$
   * $\text{Kesişim Alanı} = (150-100) \times (150-100) = 50 \times 50 = \mathbf{2.500}$
4. $\text{Birleşim Alanı} = 10.000 + 10.000 - 2.500 = \mathbf{17.500}$
5. $\text{IoU} = \frac{2.500}{17.500} = \frac{1}{7} \approx \mathbf{0.1428} \quad (\%14.28)$
* Karar: $0.1428 < 0.50$ olduğundan bu tespit **FALSE POSITIVE (FP)** olarak değerlendirilir!

</details>

---

### Soru 41 (Sayısal / Senaryo): Otonom Araç Yaya Tespit Metrikleri
**Soru:**
Test pistinde 80 gerçek yaya vardır. Model 70 yaya kutusu tahmin etmiştir. Bu kutulardan 56 tanesi doğru yayayı $\text{IoU} \ge 0.50$ ile yakalamış, 14 kutu çöp kutularına çizilmiştir.
a) TP, FP ve FN sayılarını bulunuz.
b) Precision, Recall ve F1-Skorunu hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) Bileşenler:**
  * $\text{TP} = \mathbf{56}$
  * $\text{FP} = \mathbf{14}$
  * $\text{FN} = 80 - 56 = \mathbf{24}$
* **b) Metrikler:**
  * $\text{Precision} = \frac{56}{56 + 14} = \frac{56}{70} = \mathbf{0.80} \quad (\%80)$
  * $\text{Recall} = \frac{56}{56 + 24} = \frac{56}{80} = \mathbf{0.70} \quad (\%70)$
  * $\text{F1} = 2 \cdot \frac{0.80 \cdot 0.70}{0.80 + 0.70} = \frac{1.12}{1.50} \approx \mathbf{0.7467}$

</details>

---

### Soru 42 (Teorik): mAP@0.5 vs. mAP@0.5:0.95
**Soru:**
$\text{mAP@0.5}$ ile $\text{mAP@0.5:0.95}$ metriklerinin farkını açıklayınız. Hassas robotik cerrahide neden mAP@0.5:0.95 metriğine bakılır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* $\text{mAP@0.5}$, kutunun gerçek kutuyla en az %50 örtüşmesini yeterli sayar; kaba tespiti ölçer.
* $\text{mAP@0.5:0.95}$ (COCO standardı), IoU eşiğini 0.50'den 0.95'e kadar 10 farklı seviyede test edip ortalamasını alır; kutu sınırlarının milimetrik çizilme hassasiyetini ölçer. Robotik cerrahide milimetrik hata bile kabul edilemeyeceği için yüksek $\text{mAP@0.5:0.95}$ aranır.

</details>

---

## BÖLÜM 11: Üretken Modeller: GAN ve Halüsinasyon

### Soru 43 (Kavramsal): Discriminative vs. Generative Modeller
**Soru:**
Ayırt Edici (Discriminative) modeller ile Üretici (Generative) modeller arasındaki olasılıksal ve işlevsel farkı yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Ayırt Edici ($P(Y \mid X)$):** Girdinin hangi sınıfa ait olduğunu bulur, karar sınırını öğrenir (Örn: Resim kedi mi köpek mi?).
* **Üretici ($P(X)$ veya $P(X \mid Y)$):** Verinin dağılımını öğrenir ve bu dağılımdan dünyada daha önce var olmamış sıfırdan sentetik görüntüler üretir (Örn: GAN, Stable Diffusion).

</details>

---

### Soru 44 (Teorik / Analoji): GAN Minimax Oyunu ve Nash Dengesi
**Soru:**
GAN mimarisinde Üreteç (G) ve Ayırt Edici (D) arasındaki ilişkiyi kalpazan ve polis analojisiyle açıklayınız. Nash Dengesi sağlandığında $D(G(z))$ değeri ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Kalpazan (G):** Rastgele sayılardan sahte paralar basar; amacı polisi kandırmaktır.
2. **Polis (D):** Önüne gelen paranın gerçek mi sahte mi olduğunu ayırt etmeye çalışır.
3. **Nash Dengesi:** İkisi birbirini eğittikçe Üreteç kusursuz sahteler üretir; polis artık gerçeği sahteden ayırt edemez ve rastgele yazı-tura atar:
   $$D(G(z)) = \mathbf{0.50} \quad (\%50)$$

</details>

---

### Soru 45 (Vaka / Teorik): Derin Öğrenmede Halüsinasyon ve Tıbbi Riskleri
**Soru:**
Derin öğrenmede "Halüsinasyon (Hallucination)" nedir? Neden ortaya çıkar ve tıbbi görüntülemede (MR / BT netleştirme) ne gibi ölümcül riskler doğurur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Tanım:** Modelin yüzeyde çok ikna edici ve net görünen; ancak gerçekte tamamen uydurma ve var olmayan pikseller/çıktılar üretmesidir.
* **Nedeni:** Modeller doğruları bilmez, sadece verideki istatistiksel olasılıkları taklit eder.
* **Tıbbi Riski:** Düşük çözünürlüklü bir beyin MR'ını netleştiren GAN modeli, eksik pikselleri tamamlarken gerçekte olmayan bir tümör lezyonu uydurabilir (Yanlış ameliyat riski) veya var olan gerçek bir mikro kanamayı gürültü sanıp silebilir (Ölümcül teşhis hatası).

</details>

---

## BÖLÜM 12: Pratik Mühendislik Uygulamaları ve Hata Analizi

### Soru 46 (Vaka / Laboratuvar): "Kediye Kurbağa Dedi!" Vakası ve Arka Plan Yanlılığı
**Soru:**
Laboratuvarda yeşil çimende oturan bir kediye %94 güvenle "Kurbağa" diyen modelin kök nedeni nedir? Bu problem nasıl çözülür?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Kök Neden (Arka Plan Yanlılığı / Shortcut Learning):** Eğitim setindeki kurbağaların tamamı yeşil çimendedir; kediler ise ev içindedir. Model kedinin kulaklarını veya bıyıklarını öğrenmek yerine *"Yeşil çimen yoğunluğu $\implies$ Kurbağa"* kestirmesini ezberlemiştir.
2. **Çözümler:**
   * Veri setini çeşitlendirmek (Çimende kedi, asfaltta kedi, beyaz arka planda kurbağa).
   * Veri Artırma ile arka plan renklerini değiştirmek.
   * Grad-CAM ısı haritası kullanarak modelin nesneye mi yoksa arka plana mı odaklandığını denetlemek.

</details>

---

### Soru 47 (Mühendislik / Ses): 1B Ses Sinyalleri Neden 2B CNN ile Sınıflandırılır?
**Soru:**
Fabrika motor arıza sesleri ($1\text{D}$ sinyal) neden doğrudan 1B modeller yerine Spektrogram ile 2B hale getirilerek 2D CNN (ResNet vb.) ile sınıflandırılır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Spektrogram Dönüşümü:** Ses sinyaline Fourier Dönüşümü (STFT) uygulanarak $X$ ekseni zaman, $Y$ ekseni frekans ve piksel renkleri ses enerjisi olan 2 boyutlu bir zaman-frekans resmi elde edilir.
2. **2D CNN Tercihi:** Bilgisayarlı görüdeki 2D CNN modelleri (ResNet, MobileNet vb.) ImageNet ile trilyonlarca parametre üzerinde eğitilmiş devasa bir güce sahiptir. Sesi bir kez resme dönüştürdükten sonra sıfırdan model yazmak yerine bu devasa Transfer Learning omurgalarını doğrudan kullanabilirsiniz.

</details>

---

### Soru 48 (Donanım / Optimizasyon): CUDA OOM, Budama (Pruning) ve Nicemleme (Quantization)
**Soru:**
a) Model eğitimi sırasında `CUDA Out of Memory (OOM)` hatası alan bir mühendis ilk olarak hangi iki hiperparametreyi değiştirmelidir?
b) Eğitilmiş bir derin öğrenme modelini cep telefonunda çalıştırmak için Model Budama (Pruning) ve Nicemleme (Quantization - INT8) teknikleri ne işe yarar?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **a) CUDA OOM Çözümü:**
  1. **Batch Size'ı düşürmek:** Örneğin 128'den 64'e veya 32'ye çekmek.
  2. **Girdi Çözünürlüğünü küçültmek:** Görüntüleri $1024 \times 1024$ yerine $224 \times 224$'e yeniden boyutlandırmak.
* **b) Uç Cihaz Optimizasyonu:**
  * **Budama (Pruning):** Ağdaki mutlak değeri sıfıra yakın önemsiz ağırlık bağlantılarını kalıcı olarak silip ağ yapısını seyrekleştirir.
  * **Nicemleme (Quantization - INT8):** 32-bit (`FP32`) ağırlıkları 8-bit (`INT8`) tamsayılara yuvarlar. Model boyutu **%75 küçülür (4 kat tasarruf)** ve mobil işlemcilerde çıkarım (Inference) hızı 3-4 kat artar.

</details>
