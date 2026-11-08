# Sections 7 to 10: Weeks 7 to 9 and Mock Exam (Questions 115 to 200)

def get_section_7():
    return r"""## BÖLÜM 7: Hafta 07 – Derin Ağların Eğitimi, Geri Yayılım ve Optimizasyon

### Soru 115 (Kavramsal): Softmax Fonksiyonu Özellikleri
Çok sınıflı sınıflandırma problemlerinde kullanılan Softmax fonksiyonunun formülünü yazınız ve ürettiği çıktıların temel iki özelliğini belirtiniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$\hat{p}_k = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}$$
2. **Temel Özellikleri:**
   * Her bir sınıf için üretilen olasılık $[0, 1]$ aralığındadır ($0 \le \hat{p}_k \le 1$).
   * Tüm sınıfların olasılıklarının toplamı **kesinlikle 1.0'a eşittir** ($\sum_{k=1}^K \hat{p}_k = 1.0$).

</details>

---

### Soru 116 (Kavramsal): Kategorik Çapraz Entropi (CCE)
Çok sınıflı problemlerde modelin ürettiği Softmax olasılıkları ile gerçek etiketler arasındaki farkı ölçen Kategorik Çapraz Entropi (CCE) kaybını formüle ediniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Formül:**
  $$L = - \sum_{k=1}^{K} y_k \ln(\hat{p}_k) = - \ln(\hat{p}_{doğru})$$
* Gerçek sınıf için $y_k = 1$, diğer tüm sınıflar için $y_k = 0$ olduğundan kayıp yalnızca doğru sınıfa verilen olasılığın negatif doğal logaritmasına indirgenir.

</details>

---

### Soru 117 (Sayısal Kayıp - SLAYTLARDAN): CCE Kayıp Hesabı
Doğru sınıfa $0.50$ olasılık veren bir derin öğrenme modelinin kategorik çapraz entropi kaybı yaklaşık kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$L = -\ln(\hat{p}_{doğru})$$
2. **Hesap:**
   $$L = -\ln(0.50) \approx \mathbf{0.693}$$

</details>

---

### Soru 118 (Sıralama): Eğitim Döngüsünün 4 Temel Adımı
Bir yapay sinir ağının eğitim döngüsündeki (Training Loop) 4 temel adımı doğru sıraya diziniz:
1. Optimizer ile ağırlıkları güncelleme (`optimizer.step()`)
2. İleri yayılım ile tahmin üretme (`forward pass`)
3. Geri yayılım ile gradyanları hesaplama (`loss.backward()`)
4. Kayıp fonksiyonu ile hatayı hesaplama (`compute loss`)

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Sıralama:** **2 $\rightarrow$ 4 $\rightarrow$ 3 $\rightarrow$ 1**
* İleri Yayılım (2) $\rightarrow$ Kayıp Hesabı (4) $\rightarrow$ Geri Yayılım (3) $\rightarrow$ Ağırlık Güncelleme (1).

</details>

---

### Soru 119 (Kavramsal - HOCANIN DERSTE SORDUĞU): Epoch Nedir?
Eğitim sürecinde belirlenen **Epoch (Epok)** değeri tam olarak neyi ifade eder?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Epoch:** Eğitim veri kümesindeki her bir örneğin yapay sinir ağı tarafından **tam olarak 1 kez** işlenmesi (ileri ve geri yayılımının tamamlanması) sürecidir.
* Örneğin model 100 epoch eğitildiğinde, veri kümesinin tamamı 100 kez ağdan geçirilmiş olur.

</details>

---

### Soru 120 (Kavramsal - HOCANIN DERSTE SORDUĞU): Batch Size Nedir?
Eğitimde **Batch Size (Yığın Boyutu)** neyi ifade eder ve neden donanım elveriyor diye 1024 gibi aşırı büyük seçilmemelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Tanım:** Modelin ağırlıklarını bir kez güncellemek (bir gradyan adımı atmak) için GPU'ya aynı anda verilen örnek sayısıdır.
2. **Aşırı Büyük Seçilirse Ne Olur?**
   * Model verideki yerel detayları atlar, çok kaba adımlar atar ve genelleme yeteneğini kaybederek **aşırı öğrenmeye (overfitting)** düşer.
   * 16, 32, 64 gibi dengeli yığınlar gradyana hafif stokastik gürültü ekleyerek modelin dar çukurlardan kurtulmasını sağlar.

</details>

---

### Soru 121 (Sayısal İterasyon Hesabı): Adım Sayısı
Bir veri setinde toplam 60.000 eğitim örneği bulunmaktadır. Batch Size = 120 olarak ayarlandığında 1 Epoch'ta toplam kaç iterasyon (adım) gerçekleşir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
$$\text{İterasyon Sayısı} = \frac{\text{Toplam Örnek}}{\text{Batch Size}} = \frac{60.000}{120} = \mathbf{500\text{ Adım}}$$
* Ağırlıklar bir epoch boyunca 500 kez güncellenir.

</details>

---

### Soru 122 (Kavramsal): Geri Yayılım ve Zincir Kuralı
Geri yayılım (*Backpropagation*) algoritmasının arkasındaki temel kalkülüs ilkesi nedir ve hata gradyanı ağda hangi yönde akar?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Kalkülüs İlkesi: Zincir Kuralı (Chain Rule):** Bileşke fonksiyonların türevi katman katman çarpılarak hesaplanır:
  $$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}$$
* **Akış Yönü:** İleri yayılımın tam tersine, hata sinyali **ağın sonundan (kayıp fonksiyonundan) başlar ve girdi katmanına doğru geriye akar**.

</details>

---

### Soru 123 (Sayısal Türev - SLAYTLARDAN): Geri Yayılımda ReLU Türevi
İleri yayılımda ön aktivasyonu $z = -1.3$ olan bir ReLU nöronuna geri yayılımda $0.8$ hata gradyanı gelmektedir. Bu nöronun girdisine iletilen gradyan nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* $z < 0$ olduğundan ReLU fonksiyonunun türevi $\mathbf{0}$'dır.
* İletilen gradyan:
  $$\text{Gradyan} = 0.8 \times \text{ReLU}'(-1.3) = 0.8 \times 0 = \mathbf{0}$$

</details>

---

### Soru 124 (Kavramsal): Kaybolan Gradyan ve ReLU Çözümü
Derin yapay sinir ağlarında Kaybolan Gradyan (*Vanishing Gradient*) sorunu neden ortaya çıkar ve ReLU aktivasyon fonksiyonu bunu nasıl çözer?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Sorunun Nedeni:** Sigmoid veya Tanh gibi fonksiyonların türevleri $0.25$'ten küçüktür. 20 katmanlı bir ağda geriye doğru gidildikçe bu küçük türevler birbiriyle çarpılır ($0.25^{20} \approx 10^{-12}$) ve ilk katmanlara ulaşıldığında gradyan sıfırlanır; ilk katmanlar hiçbir şey öğrenemez.
2. **ReLU Çözümü:** Pozitif bölgede ($z > 0$) ReLU'nun türevi **tam olarak $1.0$**'dır. 1 ile çarpılan sayı zayıflamaz; gradyan derinlik ne olursa olsun ilk katmanlara eksilmeden ulaşır.

</details>

---

### Soru 125 (Çoktan Seçmeli): Patlayan Gradyan ve Gradyan Kırpma
Ağırlıkların veya türevlerin aşırı büyümesiyle sayısal taşmaya (*NaN / Overflow*) yol açan Patlayan Gradyan (*Exploding Gradient*) problemine karşı en yaygın mühendislik çözümü hangisidir?
A) Veriyi silmek
B) Gradyan Kırpma (Gradient Clipping - gradyan normunu belirli bir eşikte sınırlama)
C) Katman sayısını artırmak
D) Öğrenme oranını iki katına çıkarmak
E) Sigmoid fonksiyonuna dönmek

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Gradyan Kırpma, hesaplanan gradyan vektörünün uzunluğu belirlenen bir eşiği (örneğin $1.0$ veya $5.0$) aştığında onu ölçekleyerek kırpar ve patlamayı engeller.

</details>

---

### Soru 126 (Kavramsal): Momentum Optimizasyonu Mantığı
Stokastik Gradyan İnişine (SGD) **Momentum** eklenmesinin fiziksel analojisi ve avantajı nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Fiziksel Analoji:** Vadiden aşağı yuvarlanan bir topun kütlesi ve hızı (momentum) vardır.
* **Avantajı:** Top dik yamaçlarda zikzak çizerken birbirini sıfırlayan yönlerdeki salınımlar sönümlenir; minimum çukuruna doğru olan ana yönde ise hızlanarak çok daha çabuk ve kararlı yakınsar.

</details>

---

### Soru 127 (Çoktan Seçmeli): Adam Optimizasyon Algoritması
Endüstride ve akademik çalışmalarda en yaygın kullanılan **Adam (Adaptive Moment Estimation)** algoritması hangi iki yöntemin üstün yönlerini birleştirir?
A) K-Means ve PCA
B) Momentum (1. Moment / Hız) ve RMSProp (2. Moment / Varyans)
C) Karar Ağacı ve Lojistik Regresyon
D) Sigmoid ve ReLU
E) L1 ve L2 Düzenlileştirme

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Adam, Momentum'un yön kararlılığı ile RMSProp'un parametreye özel adaptif adım boyu ölçeklemesini birleştirerek hiperparametre ayarını çok kolaylaştırır.

</details>

---

### Soru 128 (Çoktan Seçmeli): Toplu Normalizasyon (Batch Normalization)
Batch Normalization (BatchNorm) katmanının derin öğrenme mimarilerindeki temel işlevi nedir?
A) Resimleri siyah-beyaza çevirmek
B) Katmanlar arasındaki içsel ortak değişken kaymasını (*Internal Covariate Shift*) azaltmak, eğitimi hızlandırmak ve daha yüksek öğrenme oranlarının kullanılmasına izin vermek
C) Çıkış katmanındaki sınıf sayısını belirlemek
D) Kayıp fonksiyonunu sıfırlamak
E) GPU'nun sıcaklığını düşürmek

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** BatchNorm, her mini-yığının aktivasyonlarını ortalaması 0, varyansı 1 olacak şekilde normalize ederek katmanların sürekli değişen girdi dağılımlarına uyum sağlama zorunluluğunu ortadan kaldırır.

</details>

---

### Soru 129 (Kavramsal): Dropout Mekanizması
Dropout (Seyreltme) tekniği eğitim (*training*) aşamasında ve test (*inference*) aşamasında nasıl davranır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Eğitim Aşamasında:** Her adımda gizli katmandaki nöronların rastgele bir yüzdesi (örneğin %50'si) geçici olarak kapatılır. Nöronların birbirine bağımlı ezber yapması (*co-adaptation*) engellenir.
2. **Test Aşamasında:** Hiçbir nöron kapatılmaz; tüm nöronlar aktif olarak çalışır (çıktılar kapatma oranıyla dengelenir).

</details>

---

### Soru 130 (Kavramsal): Erken Durdurma (Early Stopping)
Erken Durdurma (*Early Stopping*) aşırı öğrenmeyi engellemek için hangi metriği izler ve nasıl karar verir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **İzlenen Metrik:** Doğrulama Kümesi Kaybı ($Loss_{val}$).
* **Karar Kuralı:** Eğitim kaybı düşmeye devam ederken, doğrulama kaybı $k$ epoch boyunca (sabır / patience parametresi) üst üste artmaya başladığı anda eğitim otomatik olarak durdurulur ve en iyi ağırlıklar geri yüklenir.

</details>

---

### Soru 131 (Çoktan Seçmeli): L2 Ağırlık Azaltımı (Weight Decay)
Ağırlık Azaltımı (*Weight Decay*), optimizasyon formülüne nasıl müdahale eder?
A) Ağırlıkları doğrudan iki katına çıkarır.
B) Her güncelleme adımında ağırlığı kendi büyüklüğüyle orantılı küçük bir katsayı kadar küçülterek sıfıra doğru çeker.
C) Öğrenme oranını sıfırlar.
D) Nöronları siler.
E) Veriyi çoğaltır.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $W_{t+1} = (1 - \lambda \eta) W_t - \eta \nabla L$. Ağırlık her adımda $(1 - \lambda \eta)$ çarpanıyla hafifçe eritilir; böylece katsayıların aşırı büyümesi engellenir.

</details>

---

### Soru 132 (Çoktan Seçmeli): Veri Artırma (Data Augmentation)
Aşağıdakilerden hangisi görüntü işlemede kullanılan bir Veri Artırma tekniği **DEĞİLDİR**?
A) Görselleri rastgele $\pm 15^\circ$ döndürmek
B) Görselleri yatay olarak aynalamak (*Horizontal Flip*)
C) Parlaklık ve kontrastla rastgele oynamak
D) Görselin boyutunu sıfırlayıp piksellerini silmek
E) Görüntünün rastgele bir bölgesini kırpmak (*Random Crop*)

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: D**
* **Açıklama:** Veri artırma görüntünün semantik anlamını bozmadan insan gözünün karşılaşabileceği doğal varyasyonları simüle eder. Pikselleri silip yok etmek veri artırma değildir.

</details>

---

### Soru 133 (Doğru / Yanlış - Gerekçeli): Test Aşamasında Dropout
**İfade:** *"Dropout katmanı test ve canlı kullanım aşamasında da nöronların %50'sini rastgele kapatmaya devam eder."*
Bu ifade Doğru mudur, Yanlış mıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** Test aşamasında tüm nöronlar aktif olmalıdır. Rastgele kapatma yalnızca modelin eğitim sırasında ezber yapmasını engellemek amacıyla uygulanır.

</details>

---

### Soru 134 (Kavramsal): Transfer Öğrenme (Transfer Learning)
Transfer Öğrenme (*Transfer Learning*) nedir ve veri seti çok küçük olan bir projede neden sıfırdan model eğitmek yerine tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Tanım:** ImageNet gibi milyonlarca görselle önceden eğitilmiş güçlü bir modelin (ResNet, VGG) ilk katmanlarındaki dondurulmuş ağırlıklarını alıp, son sınıflandırma katmanını kendi problemimize göre uyarlama işlemidir.
* **Avantajı:** Küçük veri setlerinde sıfırdan milyonlarca parametreyi eğitmek kaçınılmaz olarak aşırı öğrenmeye (overfitting) yol açar. Hazır model genel kenar, doku ve şekil filtrelerini zaten bildiği için az veriyle %95+ başarı yakalanabilir.

</details>

---
"""

def get_section_8():
    return r"""## BÖLÜM 8: Hafta 08 – Görüntü İşlemenin Temelleri, Filtreler ve 2D Evrişim

### Soru 135 (Kavramsal - HOCANIN DERSTE SORDUĞU): Bilgisayarın Görüntüyü Algılaması
Bilgisayarlar dijital bir görüntüyü nasıl algılarlar? Piksel, çözünürlük ve parlaklık değeri ilişkisini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Bilgisayarlar görüntüyü sayısal bir **2D veya 3D piksel matrisi** olarak algılarlar.
* Her bir piksel o noktadaki ışık şiddetini temsil eden 8-bitlik tamsayıdır ($0 = \text{Siyah}, 255 = \text{Beyaz}$).
* Çözünürlük matrisin satır ve sütun boyutunu ($H \times W$) gösterir.

</details>

---

### Soru 136 (Çoktan Seçmeli): Renk Kanalları
Gri tonlamalı (*Grayscale*) bir görüntü ile RGB renkli bir görüntünün tensör boyutları ($Yükseklik \times Genişlik \times Kanal$) açısından farkı nedir?
A) Gri: $H \times W \times 3$ ; RGB: $H \times W \times 1$
B) Gri: $H \times W \times 1$ ; RGB: $H \times W \times 3$
C) Gri tonlamalı görüntüler matris değildir.
D) RGB görüntülerde yalnızca 2 kanal bulunur.
E) Her ikisi de aynı boyuttadır.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Gri ton tek parlaklık kanalı taşır ($H \times W \times 1$). RGB ise Kırmızı, Yeşil ve Mavi olmak üzere 3 ayrı kanala sahiptir ($H \times W \times 3$).

</details>

---

### Soru 137 (Kavramsal): HSV Renk Modeli Üstünlüğü
Robotik görme ve nesne takibinde RGB yerine neden sıklıkla **HSV (Hue, Saturation, Value)** renk uzayı tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* RGB uzayında bir lambanın yanması veya gölge düşmesi Kırmızı, Yeşil ve Mavi kanallarının üçünü birden dramatik biçimde değiştirir; nesne rengi tanınamaz hale gelir.
* HSV uzayında ise rengin saf özü (**Hue - Ton**) parlaklıktan (**Value**) tamamen ayrılmıştır. Işık ve gölge değişse bile Hue değeri sabit kalır; bu yüzden nesne takibinde çok daha kararlıdır.

</details>

---

### Soru 138 (Sayısal Bellek Hesabı - SLAYTLARDAN): $640 \times 480$ RGB Bellek
$640 \times 480$ çözünürlüklü, kanal başına 8 bitlik sıkıştırılmamış bir RGB görüntü bellekte kaç bayt yer kaplar?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$\text{Bellek} = Genişlik \times Yükseklik \times Kanal \times 1\text{ Bayt}$$
2. **Hesap:**
   $$\text{Bellek} = 640 \times 480 \times 3 \times 1 = \mathbf{921.600\text{ Bayt}} \approx 900\text{ KB}$$

</details>

---

### Soru 139 (Sayısal Bellek Hesabı): Full HD Bellek
$1920 \times 1080$ Full HD çözünürlüğünde, 3 kanallı (RGB) 8-bitlik sıkıştırılmamış tek bir kare görüntünün bellek boyutu kaç megabayttır (MB)?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
$$\text{Bayt} = 1920 \times 1080 \times 3 = 6.220.800\text{ Bayt}$$
$$\text{Megabayt} = \frac{6.220.800}{1024 \times 1024} \approx \mathbf{5.93\text{ MB}} \quad (\text{veya } \frac{6.220.800}{10^6} \approx \mathbf{6.22\text{ MB}})$$

</details>

---

### Soru 140 (Kavramsal): uint8 Taşma Tuzağı (Overflow)
Görüntü işlemede pikseller 8-bit işaretsiz tamsayı (`uint8`) tipindedir. Parlaklığı artırmak için $250$ değerindeki bir piksele $10$ eklendiğinde sonuç neden $260$ yerine $4$ olur? Nasıl önlenir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Neden 4 Olur?**
   * `uint8` en fazla $255$ değerini tutabilir ($2^8 = 256$). $250 + 10 = 260 \implies 260 \pmod{256} = 4$. Beyaz olması gereken piksel aniden kapkara bir noktaya dönüşür (**Modüler Taşma**).
2. **Nasıl Önlenir?**
   * Doygunluk aritmetiği (`np.clip(değer, 0, 255)`) kullanılmalı veya işlem öncesi pikseller `float32` tipine dönüştürülüp $[0, 1]$ aralığına normalize edilmelidir.

</details>

---

### Soru 141 (Kavramsal): Görüntü Histogramı
Bir görüntünün histogramı nedir? Histogramdaki piksellerin sol tarafa (0'a yakın) yığılması ne anlama gelir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Histogram:** Görüntüdeki her bir parlaklık seviyesinin ($0..255$) kaç adet piksel tarafından paylaşıldığını gösteren frekans grafiğidir.
2. **Sola Yığılma:** Görüntünün **aşırı karanlık, az pozlanmış (underexposed)** olduğunu gösterir.

</details>

---

### Soru 142 (Kavramsal - SLAYTLARDAN): Histogram Sıkışması ve Eşitleme
Bir görüntünün histogramı 100–140 aralığına sıkışmıştır. Bu görüntü hakkında ne söylenebilir ve hangi işlem uygulanmalıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Yorum:** Görüntünün **kontrastı çok düşüktür (soluk, mat ve ayrıntıları belirsizdir)**.
* **Uygulanacak İşlem: Histogram Eşitleme (Histogram Equalization):** Kümülatif dağılım fonksiyonu (CDF) ile sıkışmış pikseller $[0, 255]$ spektrumunun tamamına yayılarak kontrast ve kenar belirginliği maksimuma çıkarılır.

</details>

---

### Soru 143 (Çoktan Seçmeli): Otsu Eşikleme Yöntemi
Görüntü eşiklemede Otsu algoritmasının temel çalışma prensibi nedir?
A) Eşiği rastgele bir sayı seçer.
B) Arka plan ile ön plan sınıfları arasındaki varyansı (*between-class variance*) maksimize eden en ideal eşik değerini histogramdan otomatik olarak hesaplar.
C) Görüntüyü döndürür.
D) Tüm pikselleri sıfır yapar.
E) Renk kanallarını siler.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Otsu yöntemi ikili sınıflandırmada nesne ile arka planı en net ayıran eşiği istatistiksel varyans analiziyle otomatik keşfeder.

</details>

---

### Soru 144 (Kavramsal): 2D Uzamsal Evrişim İşlemi
Görüntü işlemede 2D evrişim (*Spatial Convolution*) işlemi adım adım nasıl icra edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. Küçük bir çekirdek matris (kernel - örneğin $3\times3$) görüntünün sol üst köşesine yerleştirilir.
2. Kernelin elemanları ile altındaki piksel değerleri noktasal olarak birebir çarpılır.
3. Çarpım sonuçları toplanır ve tek bir skaler değer olarak çıktı matrisinin ilgili hücresine yazılır.
4. Kernel belirlenen adım boyuyla (*stride*) sağa ve aşağı kaydırılarak tüm görüntü taranır.

</details>

---

### Soru 145 (Çoktan Seçmeli): Ortalama vs. Gauss Filtresi
Gauss (Gaussian) filtresinin Ortalama (Box Blur) filtresine göre görüntü yumuşatmada daha doğal sonuç vermesinin sebebi nedir?
A) Daha hızlı çalışması
B) Merkeze yakın piksellere çan eğrisi ağırlığıyla daha yüksek, uzak piksellere daha düşük ağırlık vererek kenarları daha iyi koruması
C) Negatif sayılar üretmesi
D) Görüntüyü siyah-beyaz yapması
E) Çözünürlüğü iki katına çıkarması

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Ortalama filtresi tüm piksellere eşit $1/9$ ağırlık vererek kenarları sertçe bulanıklaştırır; Gauss filtresi ise merkeze ağırlık veren yumuşak bir geçiş sağlar.

</details>

---

### Soru 146 (Çoktan Seçmeli - BANKO): Tuz-Biber Gürültüsü ve Medyan Filtresi
Görüntüdeki rastgele beyaz ve siyah noktalardan oluşan **Tuz-Biber gürültüsünü** kenarları en iyi koruyarak temizleyen filtre hangisidir?
A) Ortalama Filtresi (Mean Filter)
B) Medyan Filtresi (Median Filter)
C) Keskinleştirme Filtresi
D) Sobel Filtresi
E) Laplasyen Filtresi

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Medyan filtresi doğrusal değildir; komşuluktaki pikselleri sıralayıp ortanca değeri seçtiği için 0 (biber) ve 255 (tuz) uç aykırı değerlerinden hiç etkilenmez ve kenarları bozmadan gürültüyü tamamen siler.

</details>

---

### Soru 147 (Kavramsal): Keskinleştirme (Sharpening) Filtresi
Keskinleştirme çekirdeği $\begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & -1 \\ 0 & -1 & 0 \end{bmatrix}$ görüntüyü nasıl keskinleştirir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Merkez piksele $+5$ gibi yüksek bir pozitif ağırlık verirken; komşu pikselleri eksi katsayılarla ($-1$) çıkarır.
* Bu durum pikseller arasındaki yerel farkı (uzamsal türevi / yüksek frekansları) abartarak kenarların ve hatların gözle görülür biçimde keskinleşmesini sağlar.

</details>

---

### Soru 148 (Kavramsal): Kenar Nedir?
Dijital görüntü işlemede matematiksel olarak **kenar (edge)** nasıl tanımlanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Kenar:** Görüntü üzerindeki piksellerin parlaklık şiddetinde meydana gelen **ani ve keskin sıçramalardır (yerel süreksizlikler)**.
* Matematiksel olarak görüntünün uzamsal türevinin (gradyanının) tepe noktası yaptığı sınırlardır.

</details>

---

### Soru 149 (Kavramsal): Sobel Operatörleri
Sobel $G_x$ ve $G_y$ çekirdekleri ne işe yarar?
$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \qquad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **$G_x$:** Yatay türevi hesaplar; parlaklığın sağ-sol yönünde değiştiği **DİKEY KENARLARI** tespit eder.
* **$G_y$:** Dikey türevi hesaplar; parlaklığın alt-üst yönünde değiştiği **YATAY KENARLARI** tespit eder.

</details>

---

### Soru 150 (Sayısal Hesaplama): Gradyan Büyüklüğü ve Açısı
Bir pikselde Sobel operatörleri $G_x = 3$ ve $G_y = 4$ sonuçlarını üretmiştir. O noktadaki kenar şiddeti (gradyan büyüklüğü) ve kenar yönü kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Gradyan Büyüklüğü ($G$):**
   $$G = \sqrt{G_x^2 + G_y^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = \mathbf{5.0}$$
2. **Gradyan Açısı ($\theta$):**
   $$\theta = \arctan\left(\frac{G_y}{G_x}\right) = \arctan\left(\frac{4}{3}\right) \approx \mathbf{53.13^\circ}$$

</details>

---

### Soru 151 (Sıralama): Canny Kenar Algoritmasının 4 Aşaması
Canny kenar tespit algoritmasının 4 temel aşamasını doğru uygulama sırasına diziniz:
1. Çift eşikleme ve Histerezis ile kenar takibi
2. Maksimum Olmayanları Bastırma (Non-Maximum Suppression - NMS)
3. Gauss filtresi ile gürültü yumuşatma
4. Sobel ile gradyan büyüklüğü ve yönü hesabı

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Sıralama:** **3 $\rightarrow$ 4 $\rightarrow$ 2 $\rightarrow$ 1**
* Gauss Yumuşatma (3) $\rightarrow$ Gradyan Hesabı (4) $\rightarrow$ NMS İnceltme (2) $\rightarrow$ Histerezis Çift Eşikleme (1).

</details>

---

### Soru 152 (Kavramsal): Non-Maximum Suppression (NMS)
Canny algoritmasındaki Maksimum Olmayanları Bastırma (*Non-Maximum Suppression - NMS*) adımının temel görevi nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Sobel filtreleri geniş ve kalın kenar şeritleri üretir.
* NMS, gradyan yönü boyunca pikselleri tarar ve yerel tepe noktası olmayan tüm pikselleri sıfırlar; böylece kalın kenarları **tam olarak 1 piksel kalınlığında jilet gibi ince çizgilere dönüştürür**.

</details>

---

### Soru 153 (Kavramsal): Morfolojik Aşınma vs. Genişleme
İkili görüntülerde Morfolojik Aşınma (*Erosion*) ve Genişleme (*Dilation*) işlemlerinin etkileri nelerdir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Aşınma (Erosion):** Nesne sınırlarını 1 piksel inceltir; küçük beyaz gürültü adacıklarını tamamen yok eder.
* **Genişleme (Dilation):** Nesne sınırlarını 1 piksel genişletir; nesne üzerindeki küçük delikleri ve çatlakları kapatarak nesneyi birleştirir.

</details>

---

### Soru 154 (Kavramsal): Klasik CV'den CNN'e Evrim
Geleneksel bilgisayarlı görü (CV) yöntemleri ile modern Evrişimli Sinir Ağları (CNN) arasındaki temel felsefe farkını çekirdeklerin tasarımı açısından açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Geleneksel CV:** Sobel, Gauss ve Laplasyen gibi filtre çekirdeklerinin katsayıları insan mühendisler tarafından matematiksel formüllerle **elle tasarlanır**.
* **CNN:** Çekirdek ağırlıkları rastgele başlatılır ve eğitim sırasında gradyan inişi ile **veriden kendi kendine otomatik olarak öğrenilir**. Model hangi filtreye ihtiyaç duyuyorsa onu kendisi keşfeder.

</details>

---
"""

def get_section_8_and_beyond():
    # Will return Section 9 (CNN) and Section 10 (Mock Exam)
    return r"""## BÖLÜM 9: Hafta 09 – Evrişimli Sinir Ağları (CNN), Katmanlar ve Boyut Hesaplamaları

### Soru 155 (Kavramsal - HOCANIN DERSTE SORDUĞU): Neden MLP Değil de CNN?
Renkli dijital görüntülerde klasik tam bağlantılı ağlar (MLP) neden yetersiz kalır ve CNN bu sorunu nasıl çözer?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Parametre Patlaması:** $224 \times 224 \times 3$ boyutundaki bir resmi sadece 1000 nörona bağlamak 150 milyon parametre gerektirir; donanım kilitlenir.
2. **Uzamsal Bilginin Kaybı:** MLP pikselleri tek boyuta açarak yan yana koyar; alt-üst ve sağ-sol 2D komşuluk geometrisini yok eder.
3. **CNN Çözümü:** Küçük filtreleri resim üzerinde kaydırarak **Ağırlık Paylaşımı (Weight Sharing)**, **Yerel Bağlantı (Local Receptive Field)** ve **Öteleme Değişmezliği (Translation Invariance)** sağlar; parametreleri binlere indirir.

</details>

---

### Soru 156 (Çoktan Seçmeli): CNN'in 3 Temel İlkesi
Aşağıdakilerden hangisi CNN mimarisinin parametre sayısını azaltırken uzamsal yapıyı korumasını sağlayan temel ilkelerden biri **DEĞİLDİR**?
A) Yerel Bağlantı (Local Receptive Field)
B) Ağırlık Paylaşımı (Weight Sharing)
C) Öteleme Eşdeğerliği / Değişmezliği (Translation Equivariance / Invariance)
D) Her piksel için bağımsız milyarlarca ağırlık tanımlanması
E) Çok katmanlı hiyerarşik öznitelik öğrenimi

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: D**
* **Açıklama:** CNN her piksele ayrı ağırlık atamaz; tam tersine küçük bir filtreyi (örneğin $3\times3=9$ parametre) tüm resim üzerinde gezdirerek parametreleri paylaşır.

</details>

---

### Soru 157 (Sayısal Boyut Hesabı - SLAYTLARDAN): Conv Katmanı Boyutu
$64 \times 64 \times 3$ boyutundaki renkli bir girdiye $3 \times 3$ boyutunda 16 adet filtre, dolgu $P = 1$ ve adım $S = 1$ ile uygulanırsa çıktı tensörünün boyutu ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$W_{out} = \left\lfloor \frac{W_{in} - K + 2P}{S} \right\rfloor + 1$$
2. **Hesap:**
   $$W_{out} = \frac{64 - 3 + 2(1)}{1} + 1 = \frac{63}{1} + 1 = \mathbf{64}$$
3. **Kanal Sayısı:** Uygulanan filtre sayısına eşittir $\implies \mathbf{16}$.
* **Çıktı Boyutu:** $\mathbf{64 \times 64 \times 16}$

</details>

---

### Soru 158 (Sayısal Boyut Hesabı): $224 \times 224$ İlk Katman Boyutu
$224 \times 224 \times 3$ boyutundaki bir girdiye (ImageNet boyutu), $7 \times 7$ boyutunda 64 filtre, dolgu $P = 3$ ve adım $S = 2$ ile uygulanırsa çıktı boyutu ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$W_{out} = \left\lfloor \frac{224 - 7 + 2(3)}{2} \right\rfloor + 1 = \left\lfloor \frac{223}{2} \right\rfloor + 1 = 111 + 1 = \mathbf{112}$$
2. **Kanal Sayısı:** 64 filtre uygulandığından $\implies \mathbf{64}$.
* **Çıktı Boyutu:** $\mathbf{112 \times 112 \times 64}$

</details>

---

### Soru 159 (Kavramsal): Valid vs. Same Padding
1. **Valid Padding ($P = 0$):** Çıktı boyutu nasıl hesaplanır?
2. **Same Padding:** $S=1$ iken çıktı boyutunun girdi boyutuna eşit kalması için gereken dolgu formülü nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Valid Padding ($P=0$):** Dolgu yapılmaz; matris her katmanda küçülür:
   $$W_{out} = W_{in} - K + 1$$
2. **Same Padding ($W_{out} = W_{in}$):**
   $$P = \frac{K - 1}{2}$$
   * $3\times3$ filtre için $P = 1$, $5\times5$ filtre için $P = 2$ eklenir.

</details>

---

### Soru 160 (Sayısal Parametre Hesabı): Conv2D Parametre Sayısı
Girdisi 3 kanallı (RGB) olan bir katmana 16 adet $3 \times 3$ boyutunda evrişim filtresi uygulanmaktadır. Bu katmanda bias terimleri dahil toplam kaç adet öğrenilebilir parametre vardır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$\text{Parametre Sayısı} = (K_w \times K_h \times C_{in} + 1) \times C_{out}$$
2. **Hesap:**
   $$\text{Parametre} = (3 \times 3 \times 3 + 1) \times 16 = (27 + 1) \times 16 = 28 \times 16 = \mathbf{448}$$

</details>

---

### Soru 161 (Sayısal Parametre Hesabı): Derin Conv2D Parametresi
Girdisi 16 kanallı olan bir ara katmana 64 adet $5 \times 5$ boyutunda filtre uygulanmaktadır. Bu katmandaki öğrenilebilir parametre sayısı kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$\text{Parametre} = (5 \times 5 \times 16 + 1) \times 64 = (400 + 1) \times 64 = 401 \times 64 = \mathbf{25.664}$$

</details>

---

### Soru 162 (Kavramsal - HOCANIN DERSTE SORDUĞU): Havuzlama Katmanı Ne İşe Yarar?
CNN mimarisindeki Havuzlama (*Pooling*) katmanının temel işlevini 3 madde halinde özetleyiniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Uzamsal Boyut İndirgeme:** Öznitelik haritasının enini ve boyunu küçülterek sonraki katmanlardaki hesaplama yükünü ve parametre sayısını azaltır.
2. **Baskın Öznitelikleri Koruma:** Max Pooling penceredeki en parlak pikseli alarak nesnenin belirgin hatlarını muhafaza eder.
3. **Kayma Dayanıklılığı (*Translation Invariance*):** Nesnenin piksel düzeyindeki küçük hareketlerine karşı modelin sağlamlığını artırır.

</details>

---

### Soru 163 (Kavramsal - HOCANIN DERSTE SORDUĞU): Pooling Kaldırılırsa Ne Olur?
Bir CNN mimarisinden Havuzlama katmanını tamamen kaldırırsak sistemde ne tür teknik sorunlar baş gösterir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Parametre Patlaması:** Boyut küçülmediği için Flatten katmanına devasa tensörler ulaşır; tam bağlantılı katmanın ağırlık sayısı milyonlara fırlar.
2. **Bellek Taşması:** GPU RAM kullanımı aşırı artar ve eğitim kilitlenir.
3. **Aşırı Öğrenme (Overfitting):** Parametreler aşırı arttığı için model eğitim verisini ezberler, testte başarısız olur.

</details>

---

### Soru 164 (Çoktan Seçmeli - BANKO TUZAK): Pooling Parametre Sayısı
$2 \times 2$ boyutunda ve adım $S = 2$ olan bir Max Pooling katmanında kaç adet öğrenilebilir ağırlık ($W$) ve bias ($b$) parametresi vardır?
A) 4
B) 8
C) 0
D) 16
E) Kanal sayısı kadar

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: C**
* **Açıklama:** Havuzlama katmanı sabit bir matematiksel kuraldır (en büyüğü alma veya ortalama alma). **Hiçbir öğrenilebilir parametresi YOKTUR (Parametre = 0)**.

</details>

---

### Soru 165 (Çoktan Seçmeli - BANKO TUZAK): Pooling Kanal Sayısı
$32 \times 32 \times 64$ boyutundaki bir tensöre $2 \times 2$ Max Pooling uygulandığında çıktı tensörünün kanal sayısı kaç olur?
A) 32
B) 64
C) 128
D) 16
E) 0

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Havuzlama katmanı kanal sayısını **ASLA DEĞİŞTİRMEZ**. Her kanala bağımsız olarak uygulanır ($32 \times 32 \times 64 \implies 16 \times 16 \times \mathbf{64}$).

</details>

---

### Soru 166 (Sayısal Boyut Hesabı - SLAYTLARDAN): MaxPool Boyutu
$55 \times 55 \times 96$ boyutundaki bir öznitelik haritasına $3 \times 3$ pencere boyutu ($K=3$), adım $S = 2$ ve dolgu $P = 0$ ile maksimum havuzlama uygulanırsa çıktı boyutu ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$W_{out} = \left\lfloor \frac{55 - 3 + 0}{2} \right\rfloor + 1 = \left\lfloor \frac{52}{2} \right\rfloor + 1 = 26 + 1 = \mathbf{27}$$
2. **Kanal:** Sabit kalır $\implies \mathbf{96}$.
* **Çıktı Tensörü:** $\mathbf{27 \times 27 \times 96}$

</details>

---

### Soru 167 (Sayısal Boyut Hesabı): Standart MaxPool
$32 \times 32 \times 64$ boyutundaki öznitelik haritasına $2 \times 2$ pencere ve $S=2$ ile Max Pooling uygulanırsa çıktı boyutu ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
$$W_{out} = \frac{32 - 2}{2} + 1 = 15 + 1 = 16 \implies \mathbf{16 \times 16 \times 64}$$

</details>

---

### Soru 168 (Çoktan Seçmeli): Global Average Pooling (GAP)
Modern CNN mimarilerinde (ResNet vb.) Flatten katmanı yerine Global Average Pooling (GAP) kullanılmasının en büyük mühendislik avantajı nedir?
A) Görüntüyü büyütmesi
B) Her öznitelik haritasının doğrudan genel ortalamasını alarak 1 sayıya indirgemesi ve tam bağlantılı katmanların gerektirdiği milyonlarca parametreyi ortadan kaldırması
C) Çıktıyı ikili sınıflandırmaya zorlaması
D) Renk sayısını azaltması
E) GPU'ya gerek bırakmaması

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** GAP, örneğin $7 \times 7 \times 512$ tensörü doğrudan $1 \times 512$ vektöre indirger; böylece tam bağlantılı katman ağırlıkları sıfıra iner ve model aşırı öğrenmeye karşı çok dayanıklı hale gelir.

</details>

---

### Soru 169 (Sayısal Quiz Hesabı - HOCANIN DERSTEKİ QUİZİ): Flatten Eleman Sayısı
$64 \times 64$ RGB görüntü sırasıyla:
1. Conv2D (16 filtre, $3\times3$, $P=1, S=1$)
2. MaxPool2D ($2\times2, S=2$)
katmanlarından geçirildikten sonra Flatten uygulanırsa elde edilen tek boyutlu özellik sayısı kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Conv2D Çıktısı:** $64 \times 64 \times 16$
2. **MaxPool2D Çıktısı:** $32 \times 32 \times 16$
3. **Flatten Eleman Sayısı:**
   $$32 \times 32 \times 16 = \mathbf{16.384}$$
   *(Not: Derste hocanın belirttiği 8192 sayısı, filtre sayısının 8 olduğu veya havuzlamanın $S=4$ olduğu varyasyondur: $32 \times 32 \times 8 = 8192$ veya $16 \times 16 \times 32 = 8192$).*

</details>

---

### Soru 170 (Kavramsal - HOCANIN DERSTE SORDUĞU): Flatten Katmanı Görevi
Flatten katmanı tensör üzerinde ne yapar ve neden gereklidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Görevi:** Çok boyutlu öznitelik tensörünü ($H \times W \times C$) tek boyutlu bir sütun vektörüne dönüştürür.
* **Gerekliliği:** Evrişim katmanlarının çıkardığı öznitelikleri, yalnızca tek boyutlu girdilerle çalışan Dense (Tam Bağlantılı) sınıflandırma katmanlarına bağlayabilmek için bu düzleştirme zorunludur.

</details>

---

### Soru 171 (Kavramsal - HOCANIN DERSTE SORDUĞU): Neden Sadece Fully Connected Değil?
CNN mimarisinde neden tüm katmanlar Fully Connected yapılmaz da araya evrişim ve havuzlama katmanları konur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Sadece Fully Connected kullanıldığında her nöron tüm piksellere bağlanır; bu da devasa parametre maliyetine ve uzamsal bilginin yok olmasına neden olur.
* CNN ise küçük yerel filtrelerle tarama yaparak daha az parametreyle çok daha fazla öznitelik öğrenir.

</details>

---

### Soru 172 (Kavramsal - HOCANIN DERSTE SORDUĞU): Çok Sınıflı Çıkış Katmanı
10 sınıflı bir nesne tanıma CNN modelinde en son katmanda neden Softmax kullanılır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Modelin ürettiği 10 farklı sayıyı, toplamı **tam olarak 1.0 olan** bir olasılık dağılımına dönüştürür. Böylece "Bu resim %85 kedi, %10 köpek, %5 kuştur" şeklinde istatistiksel karar verilebilir.

</details>

---

### Soru 173 (Kavramsal - HOCANIN DERSTE SORDUĞU): Kedinin Farklı Açılardan Tanınması
CNN bir kediyi arkasından, sağından veya farklı duruşlarda nasıl yüksek başarıyla tanıyabilmektedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* CNN görüntüyü bir bütün olarak ezberlemez; kulak, bıyık, pati ve göz gibi öznitelikleri hiyerarşik olarak ayrı ayrı öğrenir.
* Kedi hangi açıda olursa olsun bu temel öznitelikler tespit edildiği anda nesnenin bir kedi olduğu sonucuna varır.

</details>

---

### Soru 174 (Kavramsal - HOCANIN DERSTE SORDUĞU): CNN Ses Tanımada Nasıl Çalışır?
CNN'ler ses sınıflandırmada (örneğin hayvan sesi tanıma) nasıl kullanılır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Ses sinyallerinin Fourier dönüşümüyle zaman-frekans grafiği olan **Mel-spektrogramları (Mel-Spectrogram)** çıkarılır.
* Ses bir nevi 2 boyutlu görsel ısı haritasına dönüştürülür ve standart bir 2D-CNN modeli üzerinden eğitilir.

</details>

---

### Soru 175 (Kavramsal): Alıcı Alan (Receptive Field)
CNN'de **Alıcı Alan (Receptive Field)** kavramı nedir? İlk katmanlar ile derin katmanların alıcı alanları nasıl farklılaşır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Tanım:** Ağdaki belirli bir katmandaki tek bir nöronun orijinal girdi görüntüsünde etkilendiği piksel bölgesinin büyüklüğüdür.
* **Fark:** İlk evrişim katmanında bir nöron yalnızca $3\times3$ piksellik minik bir alanı görürken; art arda gelen evrişim ve havuzlamalar sayesinde derin katmandaki tek bir nöron görüntünün neredeyse tamamını ($200\times200$ piksel) kapsayan geniş bir alıcı alana ulaşır.

</details>

---

### Soru 176 (Mimari Analiz): LeNet-5 (1998)
Yann LeCun tarafından geliştirilen LeNet-5 mimarisinin katman dizilimini sırasıyla yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Girdi:** $32 \times 32$ Gri ton el yazısı rakam
2. **C1 (Conv2D):** 6 adet $5\times5$ filtre $\implies 28 \times 28 \times 6$
3. **S2 (AvgPool):** $2\times2, S=2 \implies 14 \times 14 \times 6$
4. **C3 (Conv2D):** 16 adet $5\times5$ filtre $\implies 10 \times 10 \times 16$
5. **S4 (AvgPool):** $2\times2, S=2 \implies 5 \times 5 \times 16$
6. **Flatten / C5:** 120 tam bağlı nöron
7. **F6:** 84 tam bağlı nöron
8. **Çıktı:** 10 sınıf Softmax (0..9 rakamları)

</details>

---

### Soru 177 (Çoktan Seçmeli): $1 \times 1$ Evrişimin Rolü
GoogLeNet ve modern mimarilerde kullanılan $1 \times 1$ boyutundaki evrişim filtrelerinin temel mühendislik amacı nedir?
A) Resmin genişlik ve yüksekliğini küçültmek
B) Uzamsal boyutu değiştirmeden **kanal sayısını azaltarak (boyut indirgeme)** hesaplama maliyetini düşürmek
C) Renkleri tersine çevirmek
D) Pikselleri silmek
E) Dropout uygulamak

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $1\times1$ evrişim piksellerin enini ve boyunu bozmaz; kanallar arasında doğrusal kombinasyon yaparak örneğin 256 kanallı bir öznitelik haritasını 64 kanala indirger ve işlem maliyetini devasa oranda düşürür.

</details>

---

### Soru 178 (Kavramsal): CNN'de BatchNorm ve Dropout Yeri
Tipik bir CNN bloğunda katmanların sıralaması genellikle nasıldır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Standart Modern Blok:
  $$\text{Conv2D} \implies \text{BatchNormalization} \implies \text{ReLU} \implies \text{MaxPooling}$$
* Dropout ise genellikle öznitelik haritalarında değil; Flatten sonrasındaki **Tam Bağlantılı (Dense)** katmanların arasına yerleştirilir.

</details>

---

### Soru 179 (Doğru / Yanlış - Gerekçeli): Filtre Boyutu Simetrisi
**İfade:** *"CNN filtrelerinin boyutu kesinlikle tek sayı ($3\times3, 5\times5$) olmak zorundadır; çift sayılardan ($2\times2, 4\times4$) filtre yapılamaz."*
Bu ifade Doğru mudur, Yanlış mıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** Çift sayılardan da filtre yapılabilir (örneğin $2\times2$). Ancak tek sayılar tercih edilir; çünkü tek sayılı filtrelerin tam ortasında net ve simetrik bir merkez piksel bulunur ve Same Padding hesaplaması ($P = \frac{K-1}{2}$) simetrik olarak tam uygulanabilir.

</details>

---

### Soru 180 (Vaka Analizi): Benzer Sınıf Karışıklığı
Bir CNN modeli 3 rakamı ile 8 rakamını sürekli birbirine karıştırmaktadır. Bu hata nasıl analiz edilmeli ve model nasıl iyileştirilmelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Analiz:** Karışıklık Matrisine (*Confusion Matrix*) bakıldığında 3'ün 8 olarak, 8'in 3 olarak yanlış sınıflandırıldığı görülür. Her iki rakamın da kıvrımlı hatları birbirine çok yakındır; aradaki tek fark sol taraftaki kapanma çemberidir.
2. **İyileştirme:**
   * Sol kenardaki ince detayları yakalamak için daha küçük ($3\times3$) filtreler ve daha derin katmanlar eklemek.
   * Veri setine farklı el yazısıyla yazılmış 3 ve 8 örnekleri ekleyerek veri artırma yapmak.
   * Modelin odaklandığı bölgeleri Grad-CAM ile görselleştirip sol döngüye bakıp bakmadığını denetlemek.

</details>

---

## BÖLÜM 10: Hocanın Formatında 20 Soruluk Tam Kapsamlı Vize Deneme Sınavı

*(Sınav Süresi: 30 Dakika | Test Formatı)*

### Soru 181 (Deneme Sınavı): Alan Turing'in 1950 yılında önerdiği "Taklit Oyunu"na göre makine ne zaman testi geçmiş sayılır?
A) İnsan satranç şampiyonunu yendiğinde
B) İnsan sorgulayıcı, aldığı yazılı yanıtlara bakarak karşısındakinin insan mı makine mi olduğunu güvenilir biçimde ayırt edemediğinde
C) Tüm dünya dillerini tercüme ettiğinde
D) İnternetteki tüm verileri ezberlediğinde
E) Kendi kendine yeni bir donanım ürettiğinde

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Turing testinin temeli sorgulayıcının insan ile makineyi ayırt edememesidir.</details>

---

### Soru 182 (Deneme Sınavı): Kural tabanlı geleneksel programlama ile makine öğrenmesi arasındaki girdi-çıktı farkı hangisinde doğru verilmiştir?
A) Geleneksel: $Veri + Cevap \rightarrow Kural$ ; ML: $Veri + Kural \rightarrow Cevap$
B) Geleneksel: $Veri + Kural \rightarrow Cevap$ ; ML: $Veri + Cevap \rightarrow Kural$
C) Geleneksel programlama yalnızca GPU'da çalışır.
D) ML kuralları mühendis tarafından elle yazılır.
E) Her iki yaklaşım da birebir aynıdır.

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Geleneksel yazılımda kuralları insan kodlar; ML'de kuralları (modeli) veri ve etiketlerden algoritma öğrenir.</details>

---

### Soru 183 (Deneme Sınavı): Mitchell'in makine öğrenmesi tanımında bir spam filtresi için "Doğru sınıflandırılan e-postaların oranı" hangi bileşene karşılık gelir?
A) Görev ($T$)
B) Deneyim ($E$)
C) Performans Ölçütü ($P$)
D) Eyleyici
E) Ortam

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: C</b> — Başarımı ölçen nicelik performans ölçütüdür ($P$).</details>

---

### Soru 184 (Deneme Sınavı): Veri seti bölünmeden önce tüm veri üzerinden `StandardScaler` hesaplanıp uygulanması durumunda ortaya çıkan büyük mühendislik hatası nedir?
A) Eksik Öğrenme (Underfitting)
B) Veri Sızıntısı (Data Leakage)
C) Boyut Laneti
D) Kaybolan Gradyan
E) Gradyan Patlaması

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Test verisinin istatistikleri eğitime sızar ve model canlıda çöker.</details>

---

### Soru 185 (Deneme Sınavı): $x_{min} = 20, x_{max} = 80$ olan bir öznitelikte $x = 35$ değerinin Min-Maks normalizasyonu karşılığı kaçtır?
A) 0.15
B) 0.25
C) 0.35
D) 0.50
E) 0.75

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — $(35 - 20) / (80 - 20) = 15 / 60 = 0.25$.</details>

---

### Soru 186 (Deneme Sınavı): Araba markaları (BMW, Audi, Mercedes) gibi nominal değişkenlerde neden Label Encoding yerine One-Hot Encoding tercih edilir?
A) Bellek tasarrufu için
B) Modelin markalar arasında yapay bir sayısal büyüklük/sıralama ($2 > 0$) varsaymasını engellemek için
C) Modelin daha yavaş eğitilmesi için
D) Eksik verileri doldurmak için
E) Çıktı sayısını 1 yapmak için

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Sayısal etiketler modele yapay bir hiyerarşi öğretir; One-Hot Encoding ise her markaya bağımsız ikili sütun açar.</details>

---

### Soru 187 (Deneme Sınavı): Bir doğrusal regresyon modelinde $R^2 = 0$ bulunması ne anlama gelir?
A) Model kusursuzdur.
B) Model, her örnek için hedefin genel ortalamasını tahmin etmekten daha iyi bir tahmin yapamamaktadır.
C) MSE sıfırdır.
D) Model aşırı öğrenmiştir.
E) Verideki varyansın %100'ü açıklanmıştır.

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — $R^2 = 0$ modelin hiçbir bağıntı öğrenemediğini gösterir.</details>

---

### Soru 188 (Deneme Sınavı): $L(w) = w^2$ kayıp fonksiyonunda başlangıç ağırlığı $w_0 = 4$ ve $\eta = 0.25$ ise 1 gradyan iniş adımı sonra $w_1$ kaçtır?
A) 0
B) 1
C) 2
D) 3
E) 4

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: C</b> — $dL/dw = 2w = 8 \implies w_1 = 4 - (0.25 \times 8) = 2$.</details>

---

### Soru 189 (Deneme Sınavı): Lojistik regresyonda Sigmoid fonksiyonunun varsayılan karar eşiği $\tau$ kaçtır?
A) 0.0
B) 0.5
C) 1.0
D) -1.0
E) 0.1

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Standart sınıflandırmada $\hat{p} \ge 0.5$ pozitif, $\hat{p} < 0.5$ negatif kabul edilir.</details>

---

### Soru 190 (Deneme Sınavı): k-NN algoritmasında $k = 1$ seçildiğinde modelde ne gerçekleşir?
A) Model aşırı öğrenmeye (overfitting) düşer, eğitimdeki tüm gürültüyü ezberler.
B) Model genelleme yeteneğini maksimuma çıkarır.
C) Model eksik öğrenmeye (underfitting) düşer.
D) Karar sınırı tamamen düz bir çizgi olur.
E) Tahmin hızı yüz katına çıkar.

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: A</b> — $k=1$ her eğitim noktasını ezberler; gürültüye aşırı duyarlı hale gelir.</details>

---

### Soru 191 (Deneme Sınavı): $TP = 30, FP = 10, FN = 20, TN = 140$ olan bir modelin Kesinlik (*Precision*) ve Duyarlılık (*Recall*) değerleri sırasıyla nedir?
A) 0.75 ve 0.60
B) 0.60 ve 0.75
C) 0.85 ve 0.60
D) 0.75 ve 0.85
E) 0.50 ve 0.50

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: A</b> — $Precision = 30/40 = 0.75$ ; $Recall = 30/50 = 0.60$.</details>

---

### Soru 192 (Deneme Sınavı): Kanser tarama testinde hastayı kaçırmamak (Yanlış Negatifi sıfıra indirmek) için öncelikli olarak maksimize edilmesi gereken metrik hangisidir?
A) Kesinlik (Precision)
B) Duyarlılık (Recall)
C) Özgüllük (Specificity)
D) Doğruluk (Accuracy)
E) Siluet Skoru

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Gerçek pozitifleri kaçırmamak için Duyarlılık (Recall) maksimize edilir.</details>

---

### Soru 193 (Deneme Sınavı): Bir modelin ROC eğrisi altındaki alan $AUC = 0.5$ olarak ölçülmüştür. Bu model hakkında ne söylenebilir?
A) Model mükemmeldir.
B) Model sınıfları rastgele tahminden daha iyi ayıramamaktadır.
C) Model %50 doğruluk vermektedir.
D) Kesinlik ve duyarlılık eşittir.
E) Model aşırı öğrenmiştir.

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — AUC = 0.5 rastgele tahmin köşegenidir.</details>

---

### Soru 194 (Deneme Sınavı): Tek katmanlı Perceptron'un mantıksal XOR problemini çözememesi tarihte neye yol açmıştır?
A) İnternetin icadına
B) 1. Yapay Zekâ Kışı'na (AI Winter)
C) GPU'ların keşfedilmesine
D) ResNet mimarisinin yazılmasına
E) C dilinin icadına

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Minsky ve Papert'in 1969 tarihli kitabı fonların kesilmesine ve 1. YZ Kışı'na neden olmuştur.</details>

---

### Soru 195 (Deneme Sınavı): Yapay sinir ağlarında gizli katmanlarda doğrusal olmayan aktivasyon fonksiyonu (ReLU) kullanılmazsa ne olur?
A) Model çok hızlı öğrenir.
B) 100 katman da eklense ağ tek bir doğrusal regresyon katmanına çöker.
C) Model aşırı öğrenmeye düşer.
D) Ağırlıklar tersine döner.
E) Hiçbir matris çarpımı yapılamaz.

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Doğrusal dönüşümlerin bileşimi yine doğrusal bir matristir.</details>

---

### Soru 196 (Deneme Sınavı): Çok sınıflı bir görüntü sınıflandırma modelinin en son çıkış katmanında hangi aktivasyon fonksiyonu kullanılır?
A) Sigmoid
B) Softmax
C) ReLU
D) Tanh
E) Step

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Çok sınıflı problemlerde toplamı 1.0 olan olasılık dağılımı için Softmax kullanılır.</details>

---

### Soru 197 (Deneme Sınavı): Görüntüdeki Tuz-Biber gürültüsünü kenarları koruyarak en iyi temizleyen filtre hangisidir?
A) Ortalama Filtresi
B) Medyan Filtresi
C) Gauss Filtresi
D) Sobel Filtresi
E) Keskinleştirme Filtresi

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Medyan filtresi aykırı 0 ve 255 değerlerinden etkilenmez.</details>

---

### Soru 198 (Deneme Sınavı): $64 \times 64 \times 3$ girdiye 16 adet $3 \times 3$ filtre ($P=1, S=1$) uygulanan Conv2D katmanının çıktı boyutu nedir?
A) $62 \times 62 \times 16$
B) $64 \times 64 \times 16$
C) $64 \times 64 \times 3$
D) $32 \times 32 \times 16$
E) $16 \times 16 \times 64$

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — $\frac{64 - 3 + 2}{1} + 1 = 64 \implies 64 \times 64 \times 16$.</details>

---

### Soru 199 (Deneme Sınavı): Bir CNN mimarisinden Max Pooling katmanı kaldırılırsa ne tür bir olumsuzluk yaşanır?
A) Model daha az bellek kullanır.
B) Parametre sayısı ve hesaplama maliyeti devasa boyutta artar, aşırı öğrenme riski fırlar.
C) Model hiç eğitilemez.
D) Kanal sayısı sıfırlanır.
E) Görüntü siyah-beyaza döner.

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Boyut indirgeme yapılamadığı için Flatten sonrası parametre patlaması yaşanır.</details>

---

### Soru 200 (Deneme Sınavı): CNN modelleri ses sınıflandırmada nasıl kullanılır?
A) Ses dalgaları doğrudan metne çevrilip işlenir.
B) Ses sinyallerinin Fourier dönüşümüyle 2D Mel-spektrogramları (ısı haritası) çıkarılır ve bir resim gibi CNN'e verilir.
C) CNN ses verisinde kullanılamaz.
D) Sesler ikili sayılara bölünür.
E) Yalnızca karar ağaçları kullanılır.

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Ses dalgalarının Mel-spektrogramları görsel bir resim matrisi gibi CNN'de işlenir.</details>

---

## 🏁 Tebrikler!
Toplam 200 soruluk kapsamlı soru bankasını tamamladınız. Vize sınavındaki tüm teorik, mimari, sayısal hesaplama ve senaryo sorularına artık eksiksiz hazırsınız!
"""
