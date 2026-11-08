# Yapay Zekâya Giriş Vize Sınavına Hazırlık: Kapsamlı ve İnteraktif Soru Bankası

Bu doküman, **Dr. Seda Bayat Tosun** tarafından verilen **Yapay Zekâya Giriş** dersinin tüm transkriptleri, ders içi soru-cevap oturumları, haftalık sunum slaytları (`Hafta01`–`Hafta09`) ve Colab defterleri taranarak **sadece vize kapsamındaki ilk 8-9 haftanın** konularını kapsayacak şekilde hazırlanmış resmi sınav soru bankasıdır.

İçerisinde:
1. **BÖLÜM 1:** Hocanın derste bizzat tahtada/öğrencilere sorduğu ve *"Bunlar vizede çıkacak sorular"* dediği **16 orijinal sınav sorusu ve birebir onaylı çözümleri**,
2. **BÖLÜM 2:** Vizede çıkacağı hocaca garanti edilen **adım adım öğretici sayısal matris ve boyut hesaplama soruları**,
3. **BÖLÜM 3:** Hafta 1–9 sunum slaytlarındaki **"Kendinizi Sınayın" değerlendirme soruları ve çözümleri**,
4. **BÖLÜM 4:** Hocanın belirlediği formatta (orta-şekerli, kavramsal, 20 soru) hazırlanmış **Örnek Vize Deneme Sınavı** yer almaktadır.

> [!TIP]
> **Çalışma Yöntemi (Self-Testing):**
> Tüm soruların cevapları ve ayrıntılı çözüm adımları **açılır-kapanır (toggle / `<details>`)** kutular içerisine gizlenmiştir. Çalışırken önce soruyu ve şıkları okuyup kendi cevabınızı bir kağıda yazınız; ardından **"🔍 Çözümü ve Detaylı Anlatımı Gör"** butonuna tıklayarak cevabınızı ve gerekçenizi kontrol ediniz.

---

## 📑 İÇİNDEKİLER

- [BÖLÜM 1: Hocanın Derste Bizzat Sorduğu 16 Vize Sorusu ve Çözümleri](#bölüm-1-hocanın-derste-bizzat-sorduğu-16-vize-sorusu-ve-çözümleri)
- [BÖLÜM 2: Vizede Garanti Çıkacak Matris ve Boyut Hesaplama Soruları](#bölüm-2-vizede-garanti-çıkacak-matris-ve-boyut-hesaplama-soruları)
- [BÖLÜM 3: Hafta 1–9 Slaytlarındaki "Kendinizi Sınayın" Soruları](#bölüm-3-hafta-19-slaytlarındaki-kendinizi-sınayın-soruları)
- [BÖLÜM 4: 20 Soruluk Örnek Vize Deneme Sınavı (Gerçek Format)](#bölüm-4-20-soruluk-örnek-vize-deneme-sınavı-gerçek-format)

---

## BÖLÜM 1: Hocanın Derste Bizzat Sorduğu 16 Vize Sorusu ve Çözümleri

### Soru 1 (Dersteki Soru 1): Dijital Görüntü ve Renk Kanalları
**Soru:**
Bilgisayarlar dijital bir görüntüyü nasıl algılarlar? Gri tonlamalı (*grayscale*) ve RGB (renkli) görüntü arasındaki temel fark kanal sayısı ve matris yapısı açısından nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Bilgisayarın Görüntüyü Algılama Biçimi:**
   * Bilgisayarlar görüntüyü insan gibi bir bütün olarak değil; **sayısal piksel matrisleri** olarak algılarlar.
   * Her bir piksel 8-bitlik tamsayılarla ($[0, 255]$) temsil edilir. $0$ değeri tam siyahı, $255$ değeri tam beyazı, aradaki değerler ise ton yoğunluğunu gösterir.
2. **Gri Tonlama vs. RGB Farkı:**
   * **Gri Tonlamalı Görüntü (*Grayscale*):** Yalnızca parlaklık bilgisini taşıyan **tek kanallı (2 boyutlu)** bir matristir ($H \times W \times 1$).
   * **RGB Görüntü:** Kırmızı (*Red*), Yeşil (*Green*) ve Mavi (*Blue*) olmak üzere üst üste binmiş **üç ayrı renk kanallı (3 boyutlu)** bir tensördür ($H \times W \times 3$).

</details>

---

### Soru 2 (Dersteki Soru 2): Konvolüsyon Katmanı ve Filtrelerin (Kernel) Görevi
**Soru:**
CNN mimarisinde yer alan Konvolüsyon (Evrişim) katmanının ve bu katmanda kullanılan filtrelerin (*kernel*) temel görevi nedir? Ağın ilk katmanları ile derin katmanları arasında ne tür öznitelik farkı vardır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Temel Görev: Öznitelik Çıkarımı (*Feature Extraction*):**
   * Evrişim katmanının görevi görüntüden öznitelikleri (*feature map*) çıkarmaktır. Filtreler görüntü üzerinde kayarak kenarları, köşeleri ve desenleri tespit eder.
2. **Hiyerarşik Öznitelik Farkı:**
   * **İlk Katmanlar:** Basit, düşük seviyeli geometrik öznitelikleri (dikey/yatay kenarlar, renk geçişleri, keskin hatlar) öğrenir.
   * **Orta Katmanlar:** Dokuları ve temel şekilleri (daireler, eğriler, kareler) birleştirir.
   * **Derin Katmanlar:** Nesneye özgü karmaşık parçaları ve semantik yapıları (göz, burun, pati, araba tekerleği) tespit eder.

</details>

---

### Soru 3 (Dersteki Soru 3): Havuzlama (Pooling / Max Pooling)
**Soru:**
CNN mimarisinde Havuzlama (*Pooling / Max Pooling*) katmanı neden kullanılır ve temel mühendislik faydaları nelerdir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Boyut İndirgeme ve Maliyet Azaltma:** Öznitelik haritasının genişlik ve yükseklik boyutunu küçülterek hesaplama yükünü ve sonraki katmanlara aktarılan parametre sayısını azaltır.
2. **En Baskın Özellikleri Koruma:** Max Pooling, belirlenen pencere (örneğin $2\times2$) içindeki en büyük değeri alarak nesnenin en belirgin kenar ve hatlarını muhafaza eder; önemsiz detayları eler.
3. **Öteleme Dayanıklılığı (*Translation Invariance*):** Görüntüdeki nesnelerin küçük kaymalarına, açı değişimlerine ve bozulmalara karşı modelin daha dirençli olmasını sağlar.
4. **Aşırı Öğrenmeyi (Overfitting) Engelleme:** Parametre sayısını azalttığı için modelin eğitim verisini ezberlemesini zorlaştırır.

</details>

---

### Soru 4 (Dersteki Soru 4): Aktivasyon Fonksiyonları ve ReLU'nun Önemi
**Soru:**
Yapay sinir ağlarında ve CNN'lerde neden doğrusal olmayan (*non-linear*) aktivasyon fonksiyonları kullanmak zorundayız? Neden evrişim katmanlarından sonra genellikle **ReLU** fonksiyonu tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Doğrusal Olmayan Aktivasyonun Zorunluluğu:**
   * Eğer aktivasyon fonksiyonu kullanılmazsa (doğrusal kalırsa), katmanların arkasındaki matris çarpımları zincirleme olarak tek bir matrise indirgenir:
     $$W_2(W_1 x + b_1) + b_2 = (W_2 W_1)x + (W_2 b_1 + b_2) = W' x + b'$$
   * 100 katmanlı devasa bir ağ kursanız dahi model tek bir basit doğrusal regresyondan farksız hale gelir ve karmaşık problemleri (XOR, görüntü sınıflandırma) çözemez.
2. **Neden ReLU ($\max(0, z)$)?**
   * **Gradyan Kaybolmasını Önler:** Pozitif bölgede türevi daima 1'dir ($\text{ReLU}'(z) = 1$). Sigmoid gibi derin katmanlarda gradyanı eritmez.
   * **Hesaplama Hızı:** Üstel hesaplama ($e^z$) yapmaz; negatifleri sıfırlayarak ($z < 0 \implies 0$) çok hızlı çalışır.
   * **Seyreklik (Sparsity):** Gereksiz ve negatif yanıt veren nöronları susturarak biyolojik beyne benzer biçimde seyrek ve verimli bir temsil sağlar.

</details>

---

### Soru 5 (Dersteki Soru 5): Aşırı Öğrenme (Overfitting) ve Çözüm Yolları
**Soru:**
Bir CNN modeli eğitim kümesindeki fotoğrafları %99 doğru tahmin ederken, ilk kez gördüğü yeni test fotoğraflarında %60 gibi çok düşük bir başarı gösteriyorsa bu durum nasıl adlandırılır? Görüntü işlemede bunu engellemek için hangi yöntemler kullanılır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Durumun Adı: Aşırı Öğrenme (Overfitting / Ezberleme):**
   * Model eğitim verisindeki nesnelerin gerçek ayırt edici özniteliklerini öğrenmek yerine, arka plan gürültülerini ve pikselleri ezberlemiştir.
2. **Çözüm Yolları:**
   * **Veri Artırma (*Data Augmentation*):** Mevcut görüntüleri rastgele döndürerek, yatay/dikey aynalayarak, parlaklığını değiştirerek ve kırparak modele aynı nesnenin binlerce farklı varyasyonunu göstermek.
   * **Dropout (Seyreltme):** Eğitim sırasında her adımda nöronların rastgele %20 ila %50'sini geçici olarak kapatarak nöronların birbirine körü körüne bağımlı olmasını (*co-adaptation*) engellemek.
   * **Erken Durdurma (*Early Stopping*):** Doğrulama kaybı ($Loss_{val}$) artmaya başladığı anda eğitimi kesmek.
   * **Transfer Öğrenme (*Transfer Learning*):** ImageNet gibi devasa veri setleriyle önceden eğitilmiş hazır modellerin (ResNet, VGG) ilk katmanlarındaki dondurulmuş ağırlıkları kullanmak.
   * **L1/L2 Regülarizasyon:** Ağırlıkların aşırı büyümesini cezalandırmak.

</details>

---

### Soru 6 (Dersteki Soru 6): Dolgulama (Padding)
**Soru:**
Dolgulama (*Padding / Zero-Padding*) işlemi nedir? Görüntünün etrafına sıfırlardan çerçeve eklemek kenar piksellerini nasıl kurtarır ve boyut erimesini nasıl önler?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Tanım:** Evrişim işlemine başlamadan önce girdi görüntüsünün veya öznitelik haritasının dört bir tarafına genellikle sıfır değerine sahip yapay pikseller eklenmesidir.
2. **Kenar Piksellerini Kurtarma:** Çekirdek (filtre) matris üzerinde kayarken merkeze yakın pikseller defalarca taranırken, kenar ve köşe pikselleri filtrenin altında yalnızca bir veya birkaç kez kalır. Dolgulama kenarları içeriye çekerek köşe detaylarının kaçırılmasını engeller.
3. **Boyut Erimesini Önleme (*Same Padding*):** Dolgusuz evrişimde ($P=0$) her katmanda matris küçülür. 30 katmanlı derin bir ağda dolgu yapılmazsa görüntü birkaç katman sonra $1\times1$ piksele erir ve yok olur. Doğru dolgu ($P = \frac{K-1}{2}$) çıktı boyutunun girdi boyutuyla eşit kalmasını sağlar.

</details>

---

### Soru 7 (Dersteki Soru 7): Çıkış Katmanı ve Softmax Fonksiyonu
**Soru:**
Kedi, köpek, kuş ve araba sınıflarının bulunduğu çok sınıflı bir görüntü sınıflandırma probleminde CNN modelinin en son çıkış katmanında hangi aktivasyon fonksiyonu kullanılır? İkili (binary) bir problem olsaydı ne kullanılırdı?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Çok Sınıflı Problemde:** **Softmax Fonksiyonu** kullanılır.
   * Softmax, modelin ürettiği tüm ham sayısal skorları (logitleri) alır ve toplamı **tam olarak 1.0 olan** bir olasılık dağılımına dönüştürür ($P(kedi)=0.70, P(köpek)=0.20, P(kuş)=0.05, P(araba)=0.05$).
2. **İkili (Binary) Sınıflandırma Probleminde:** **Sigmoid Fonksiyonu** kullanılır.
   * Tek bir çıkış nöronu üzerinden $[0, 1]$ aralığında pozitif sınıf olasılığı üretir.

</details>

---

### Soru 8 (Dersteki Soru 8): CNN'in Farklı Veri Tiplerinde Kullanımı
**Soru:**
CNN mimarisi yalnızca 2D fotoğraflarda mı kullanılır? Ses ve biyomedikal sinyal işlemede CNN'lerden nasıl faydalanılır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Kullanım Kapsamı:** **HAYIR, sadece resimlerde kullanılmaz.**
2. **Ses Tanıma:** Ses dalgalarının zaman içindeki frekans değişimleri Fourier dönüşümü ile görsel bir ısı haritasına, yani **Mel-spektrogramlarına (Mel-Spectrogram)** dönüştürülür. Bu spektrogramlar tıpkı birer resim matrisi gibi 2D-CNN modellerine verilerek ses sınıflandırılır.
3. **1D Sinyaller:** Kalp atışı (EKG) ve beyin dalgaları (EEG) gibi tek boyutlu zaman serisi verileri 1D-CNN filtreleriyle taranarak ritim bozuklukları teşhis edilir.
4. **Video:** Zaman boyutunu da içeren ardışık kareler 3D-CNN mimarileriyle işlenir.

</details>

---

### Soru 9 (Dersteki Soru 9): Flatten (Düzleştirme) Katmanı
**Soru:**
CNN mimarisindeki Flatten (Düzleştirme) katmanının görevi nedir? Matematiksel olarak tensör üzerinde ne yapar?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Görevi:** Evrişim ve havuzlama katmanlarından çıkan çok boyutlu (3D tensör: $H \times W \times C$) öznitelik haritalarını **tek boyutlu bir sütun vektörüne** dönüştürür.
2. **Matematiksel Dönüşüm:** Örneğin $4 \times 4$ boyutunda 16 adet öznitelik haritası ($4 \times 4 \times 16$) varsa; Flatten katmanı bu veriyi $4 \times 4 \times 16 = \mathbf{256}$ elemanlı tek bir 1D vektöre açar.
3. **Amacı:** Çıkarılan öznitelikleri, sadece tek boyutlu vektörlerle çalışan tam bağlantılı (*Dense / Fully Connected*) sınıflandırma katmanına uygun girdi formatına sokmaktır.

</details>

---

### Soru 10 (Dersteki Soru 10): Tam Bağlantılı Katman (Dense / Fully Connected)
**Soru:**
CNN mimarisinde Flatten katmanından sonra gelen Tam Bağlantılı (*Dense / Fully Connected*) katmanların görevi nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Görevi: Öznitelikleri Birleştirme ve Sınıflandırma:**
  * Evrişim katmanları görüntünün yerel parçalarındaki (kenar, doku, göz, tekerlek) öznitelikleri çıkarır.
  * Tam bağlantılı katman ise çıkarılan tüm bu dağınık özellikleri birbirleriyle çapraz bağlar, yüksek seviyeli ilişkileri sentezler ve görüntünün hangi sınıfa ait olduğuna dair nihai kararı üretir.

</details>

---

### Soru 11 (Dersteki Soru 11): Epoch Kavramı
**Soru:**
Bir yapay zekâ modelinin eğitiminde **Epoch (Epok)** değeri neyi ifade eder?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Tanım:** Eğitim veri setinde bulunan tüm örneklerin model tarafından **tam olarak bir kez işlenmesi (ileri ve geri yayılımın tamamlanması)** sürecidir.
* Örneğin 100 epoch belirlediğimizde; veri setindeki tüm fotoğraflar ağdan 100 defa baştan sona geçmiş ve model ağırlıklarını bu tekrarlar boyunca optimize etmiş demektir.

</details>

---

### Soru 12 (Dersteki Soru 12): Batch Size (Yığın Boyutu)
**Soru:**
Eğitimde **Batch Size (Yığın Boyutu)** nedir? Neden donanım elveriyor diye 1024 gibi çok yüksek değerler seçilmemelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Tanım:** Model ağırlıklarını bir kez güncellemek (bir gradyan adımı atmak) için GPU'ya tek seferde verilen ve paralel işlenen örnek (fotoğraf) sayısıdır.
2. **Neden Aşırı Büyük Seçilmemelidir?**
   * Batch size 1024 gibi çok yüksek seçilirse model çok büyük adımlar atar, küçük veri varyasyonlarını kaçırır ve genelleme yeteneğini kaybederek **Overfitting'e** düşebilir.
   * 8, 16, 32 gibi makul yığın boyutları gradyana hafif stokastik gürültü ekleyerek modelin dar yerel çukurlardan kurtulmasını ve daha kararlı genelleme yapmasını sağlar.

</details>

---

### Soru 13 (Dersteki Soru 13): Average Pooling ile Max Pooling Farkı
**Soru:**
Average Pooling ile Max Pooling arasındaki farkı tek bir cümleyle açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Temel Fark:** Max Pooling belirlenen pencere içindeki **en büyük piksel değerini** alarak baskın kenar ve öznitelikleri korurken; Average Pooling o penceredeki tüm piksellerin **aritmetik ortalamasını** alarak arka planı pürüzsüzleştirir.

</details>

---

### Soru 14 (Dersteki Soru 14): Pooling Katmanının Kaldırılmasının Etkileri
**Soru:**
Bir CNN mimarisinden Pooling (Havuzlama) katmanını tamamen kaldırırsak ne tür olumsuzluklar yaşanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Parametre ve Hesaplama Patlaması:** Havuzlama uzamsal boyutu yarıya indiremediği için öznitelik haritası büyük kalır. Flatten katmanına ulaşıldığında vektör boyutu ve tam bağlantılı katmanın ağırlık sayısı on katına çıkar.
2. **Bellek Taşması:** GPU RAM'i ve bellek kullanımı fırlar, eğitim aşırı derecede yavaşlar.
3. **Aşırı Öğrenme (Overfitting):** Devasa parametre sayısı nedeniyle model eğitim verisindeki küçük gürültüleri ezberler, test başarımında çöker.
4. **Öteleme Kırılganlığı:** Nesnedeki küçük kaymalara ve dönüşümlere karşı modelin dayanıklılığı zayıflar.

</details>

---

### Soru 15 (Dersteki Soru 15): Neden Sadece Fully Connected Kullanmıyoruz?
**Soru:**
Tam bağlantılı (*Fully Connected*) katmanlar her nöronla bağlantı kurup çok iyi öğrendiği halde, CNN'de neden sadece Fully Connected katmanlar kullanmıyoruz?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Parametre Sayısı İmkânsız Derecede Artar:** $224\times224\times3$ bir resmi sadece 1000 nörona bağlamak 150 milyon ağırlık gerektirir.
2. **Uzamsal Düzen Kaybolur:** Tam bağlantılı katman pikselleri yan yana sıralar; pikseller arasındaki 2 boyutlu mesafe ve komşuluk bilgisini yok sayar.
3. **Ağırlık Paylaşımı Yoktur:** CNN küçük $3\times3$ filtreleri resmin her yerinde gezdirerek aynı parametreleri paylaşırken; tam bağlantılı katman her piksel için bağımsız yeni ağırlıklar tutmak zorundadır.

</details>

---

### Soru 16 (Dersteki Soru 16): CNN'in Öteleme ve Açı Değişkenliğinde Başarımı
**Soru:**
CNN modelleri bir kediyi arkasından, sağından, solundan veya farklı ışık koşullarında çekilmiş fotoğraflarda nasıl %95+ doğrulukla tanıyabilmektedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Hiyerarşik Öznitelik Temsili:** CNN kedinin fotoğrafını bir bütün piksel bloğu olarak ezberlemez; kulak açısı, bıyık yapısı, göz formu, tüy dokusu gibi hiyerarşik parçaları soyutlayarak öğrenir.
* Kedi hangi açıdan durursa dursun model bu temel öznitelik parçalarını tespit ettiği anda bu parçaları birleştirerek nesnenin bir kedi olduğunu yüksek olasılıkla çıkarır.
* Veri artırma (*data augmentation*) ve evrişimin öteleme değişmezliği (*translation invariance*) bu başarıyı pekiştirir.

</details>

---

## BÖLÜM 2: Vizede Garanti Çıkacak Matris ve Boyut Hesaplama Soruları

### Soru 17 (Sayısal Matris Sorusu): 2D Evrişim Matris Çarpımı Hesabı
**Soru:**
Aşağıda $5 \times 5$ boyutunda bir girdi matrisi ve $3 \times 3$ boyutunda bir kernel (filtre) verilmiştir:

$$\text{Girdi Matrisi} = \begin{bmatrix} 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 \end{bmatrix}, \qquad \text{Kernel} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$$

Dolgu uygulanmadığına ($P=0$) ve adım $S=1$ olduğuna göre, üretilen öznitelik haritasının **sol üst köşesindeki ilk elemanını ($C_{1,1}$)** adım adım hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. Girdi matrisinin sol üst $3 \times 3$ bölgesini izole edelim:
   $$\text{Bölge} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$$
2. Kernel ile eleman eleman çarpıp toplayalım:
   $$\text{Satır 1:} \quad (1 \times 1) + (1 \times 0) + (1 \times 1) = 1 + 0 + 1 = 2$$
   $$\text{Satır 2:} \quad (0 \times 0) + (1 \times 1) + (1 \times 0) = 0 + 1 + 0 = 1$$
   $$\text{Satır 3:} \quad (0 \times 1) + (0 \times 0) + (1 \times 1) = 0 + 0 + 1 = 1$$
3. Toplam:
   $$C_{1,1} = 2 + 1 + 1 = \mathbf{4}$$

</details>

---

### Soru 18 (Sayısal Boyut Hesabı - Slaytlardan): Evrişim Katmanı Çıktı Boyutu
**Soru:**
$64 \times 64 \times 3$ boyutundaki renkli bir görüntüye; $3 \times 3$ boyutunda 16 adet filtre, dolgu $P = 1$ ve adım $S = 1$ parametreleriyle uygulanmaktadır.
Üretilen çıktının uzamsal boyutunu ve kanal sayısını formülle hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Çıktı Boyutu Formülü:**
   $$W_{çıkış} = \left\lfloor \frac{W_{girdi} - K + 2P}{S} \right\rfloor + 1$$
2. **Değerleri Yerine Koyalım:**
   $$W_{girdi} = 64, \quad K = 3, \quad P = 1, \quad S = 1$$
   $$W_{çıkış} = \left\lfloor \frac{64 - 3 + 2(1)}{1} \right\rfloor + 1 = \frac{63}{1} + 1 = \mathbf{64}$$
3. **Kanal Sayısı:** Uygulanan filtre sayısına eşittir $\implies \mathbf{16}$.
* **Nihai Çıktı Tensörü:** $\mathbf{64 \times 64 \times 16}$

</details>

---

### Soru 19 (Sayısal Boyut Hesabı - Slaytlardan): Havuzlama Katmanı Çıktı Boyutu
**Soru:**
$55 \times 55 \times 96$ boyutundaki bir öznitelik haritasına $3 \times 3$ pencere boyutu ($K=3$), adım $S = 2$ ve dolgu $P = 0$ ile maksimum havuzlama uygulanırsa çıktı boyutu ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Havuzlama Boyut Formülü:**
   $$W_{çıkış} = \left\lfloor \frac{W_{girdi} - K + 2P}{S} \right\rfloor + 1$$
   $$W_{çıkış} = \left\lfloor \frac{55 - 3 + 0}{2} \right\rfloor + 1 = \left\lfloor \frac{52}{2} \right\rfloor + 1 = 26 + 1 = \mathbf{27}$$
2. **Kanal Kuralı:** Havuzlama katmanı kanal sayısını asla değiştirmez $\implies \mathbf{96}$.
* **Nihai Çıktı Tensörü:** $\mathbf{27 \times 27 \times 96}$

</details>

---

### Soru 20 (Sayısal Parametre Hesabı): Conv2D Katmanı Parametre Sayısı
**Soru:**
$32 \times 32 \times 3$ boyutundaki bir RGB girdiye 32 adet $5 \times 5$ boyutunda filtre uygulanan bir Conv2D katmanında kaç adet öğrenilebilir parametre (ağırlık + bias) vardır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$\text{Parametre Sayısı} = (K_w \times K_h \times C_{in} + 1) \times C_{out}$$
2. **Değerler:** $K_w = 5, K_h = 5, C_{in} = 3, C_{out} = 32$
   $$\text{Tek Bir Filtrenin Ağırlıkları} = 5 \times 5 \times 3 = 75$$
   $$\text{Bias Dahil Tek Filtre} = 75 + 1 = 76$$
   $$\text{Toplam Parametre} = 76 \times 32 = \mathbf{2.432}$$

</details>

---

### Soru 21 (Sayısal Parametre Hesabı - Slaytlardan): Dense Katmanı Parametre Sayısı
**Soru:**
100 nöronlu bir katmandan 50 nöronlu tam bağlantılı (Dense) bir katmana geçişte kaç adet öğrenilebilir parametre vardır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$\text{Parametre Sayısı} = (N_{girdi} \times N_{çıkış}) + N_{çıkış}$$
2. **Hesap:**
   $$\text{Parametre} = (100 \times 50) + 50 = 5000 + 50 = \mathbf{5.050}$$

</details>

---

### Soru 22 (Dersteki Gerçek Quiz Sorusu): Flatten Çıktı Eleman Sayısı
**Soru:**
$64 \times 64$ boyutunda RGB (3 kanallı) bir görüntü sırasıyla şu katmanlardan geçirilmektedir:
1. `Conv2D(in_channels=3, out_channels=16, kernel_size=3, padding=1, stride=1)`
2. `MaxPool2D(kernel_size=2, stride=2)`
3. `Flatten()`

Flatten katmanından sonra elde edilen tek boyutlu özellik sayısı kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Conv2D Sonrası Boyut:**
   $$W_1 = \frac{64 - 3 + 2(1)}{1} + 1 = 64 \implies 64 \times 64 \times 16$$
2. **MaxPool2D Sonrası Boyut:**
   $$W_2 = \frac{64 - 2}{2} + 1 = 31 + 1 = 32 \implies 32 \times 32 \times 16$$
3. **Flatten Sonrası Eleman Sayısı:**
   $$\text{Eleman Sayısı} = 32 \times 32 \times 16 = \mathbf{16.384}$$
   *(Not: Derste hocanın belirttiği 8192 değeri, kanal sayısının 8 veya havuzlamanın stride 4 olduğu varyasyondur: $16 \times 16 \times 32 = 8192$ veya $32 \times 32 \times 8 = 8192$).*

</details>

---

### Soru 23 (Sayısal Bellek Hesabı - Slaytlardan): Görüntü Bellek Boyutu
**Soru:**
$640 \times 480$ çözünürlüklü, kanal başına 8 bitlik sıkıştırılmamış bir RGB görüntü bellekte kaç bayt yer kaplar?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$\text{Bayt} = Genişlik \times Yükseklik \times Kanal \times 1\text{ Bayt}$$
2. **Hesap:**
   $$\text{Bayt} = 640 \times 480 \times 3 \times 1 = \mathbf{921.600\text{ Bayt}} \approx 900\text{ KB}$$

</details>

---

### Soru 24 (Sayısal Normalizasyon - Slaytlardan): Min-Maks Normalizasyonu
**Soru:**
Bir veri setinde bir özniteliğin en küçük değeri $x_{min} = 20$, en büyük değeri $x_{max} = 80$ olarak ölçülmüştür. Bu öznitelikteki $x = 35$ değerinin Min-Maks normalizasyonu sonrası karşılığı nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$$
2. **Hesap:**
   $$x' = \frac{35 - 20}{80 - 20} = \frac{15}{60} = \mathbf{0.25}$$

</details>

---

### Soru 25 (Sayısal Nöron Çıktısı - Slaytlardan): Tek Nöron Çıktısı
**Soru:**
Girdileri $x = [2, -1, 3]$, ağırlıkları $w = [0.5, 1, -0.5]$ ve bias değeri $b = 1$ olan ReLU aktivasyonlu bir nöronun çıktısı nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Ağırlıklı Toplam ($z$):**
   $$z = (2 \times 0.5) + (-1 \times 1) + (3 \times -0.5) + 1 = 1 - 1 - 1.5 + 1 = -0.5$$
2. **ReLU Aktivasyonu:**
   $$\text{Çıktı} = \max(0, z) = \max(0, -0.5) = \mathbf{0}$$

</details>

---

### Soru 26 (Sayısal Gradyan İniş - Slaytlardan): Ağırlık Güncellemesi
**Soru:**
Kayıp fonksiyonu $L(w) = w^2$ olan bir modelde, başlangıç ağırlığı $w_0 = 4$ ve öğrenme oranı $\eta = 0.25$ ise bir gradyan iniş adımından sonra $w_1$ kaç olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Türev (Gradyan):**
   $$\frac{dL}{dw} = 2w \implies 2 \times 4 = 8$$
2. **Güncelleme Kuralı:**
   $$w_1 = w_0 - \eta \frac{dL}{dw} = 4 - (0.25 \times 8) = 4 - 2 = \mathbf{2}$$

</details>

---

### Soru 27 (Sayısal Metrik Hesabı - Slaytlardan): Kesinlik ve Duyarlılık
**Soru:**
Bir modelin karışıklık matrisinde $TP = 30, FP = 10, FN = 20, TN = 140$'tır. Kesinlik (*Precision*) ve Duyarlılık (*Recall*) değerlerini bulunuz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Kesinlik (Precision):**
   $$\text{Precision} = \frac{TP}{TP + FP} = \frac{30}{30 + 10} = \frac{30}{40} = \mathbf{0.75}$$
2. **Duyarlılık (Recall):**
   $$\text{Recall} = \frac{TP}{TP + FN} = \frac{30}{30 + 20} = \frac{30}{50} = \mathbf{0.60}$$

</details>

---

### Soru 28 (Sayısal Kayıp Hesabı - Slaytlardan): İkili Çapraz Entropi
**Soru:**
Gerçek sınıfı $y = 0$ olan bir örnek için model pozitif sınıf olasılığını $\hat{p} = 0.8$ tahmin etmiştir. İkili çapraz entropi kaybı yaklaşık kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül ($y = 0$ iken):**
   $$L = -\ln(1 - \hat{p})$$
2. **Hesap:**
   $$L = -\ln(1 - 0.8) = -\ln(0.2) \approx \mathbf{1.61}$$

</details>

---

### Soru 29 (Sayısal Kayıp Hesabı - Slaytlardan): Çok Sınıflı Çapraz Entropi
**Soru:**
Doğru sınıfa $0.5$ olasılık veren bir modelin kategorik çapraz entropi kaybı yaklaşık kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$L = -\ln(\hat{p}_{doğru})$$
2. **Hesap:**
   $$L = -\ln(0.5) \approx \mathbf{0.693}$$

</details>

---

### Soru 30 (Sayısal Gradyan Akışı - Slaytlardan): ReLU Geri Yayılımı
**Soru:**
İleri yayılımda ön aktivasyonu $z = -1.3$ olan bir ReLU nöronuna geri yayılımda $0.8$ hata gradyanı gelmektedir. Bu nöronun girdisine iletilen gradyan nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* $z < 0$ olduğundan ReLU'nun türevi $\mathbf{0}$'dır ($\frac{da}{dz} = 0$).
* Gelen gradyan türevle çarpılır:
  $$\text{İletilen Gradyan} = 0.8 \times 0 = \mathbf{0}$$

</details>

---

## BÖLÜM 3: Hafta 1–9 Slaytlarındaki "Kendinizi Sınayın" Soruları

### Soru 31: Mitchell'in ML Tanımı
**Soru:**
Mitchell'in makine öğrenmesi tanımına göre, bir spam filtresi için *"doğru sınıflandırılan e-postaların yüzdesi"* hangi bileşene karşılık gelir?
A) Görev ($T$)  
B) Deneyim ($E$)  
C) Performans ölçütü ($P$)  
D) Ortam  
E) Eyleyici  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **C) Performans ölçütü ($P$)**
* **Açıklama:** Başarımı ölçen nicelik performans ölçütüdür ($P$). Etiketli geçmiş e-postalar deneyim ($E$), yeni bir e-postayı sınıflandırma eylemi ise görevdir ($T$).

</details>

---

### Soru 32: PEAS Tanımı
**Soru:**
Otonom bir araç için yapılan PEAS tanımında *"kamera, LiDAR ve GPS"* hangi bileşene aittir?
A) Performans ölçütü  
B) Ortam  
C) Eyleyiciler  
D) Algılayıcılar (Sensors)  
E) Ajan programı  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **D) Algılayıcılar (Sensors)**
* **Açıklama:** Kamera, LiDAR ve GPS çevreden girdi toplayan algılayıcılardır. Direksiyon ve fren eyleyici (actuator); yollar ve trafik ise ortamdır (environment).

</details>

---

### Soru 33: Veri Sızıntısı (Data Leakage)
**Soru:**
Aşağıdakilerden hangisi tipik bir veri sızıntısı (*data leakage*) örneğidir?
A) Veriyi eğitim ve test kümelerine katmanlı (stratified) olarak bölmek  
B) Standardizasyon için ortalama ve standart sapmayı, veriyi bölmeden önce tüm veri setinden hesaplamak  
C) Hiperparametreleri doğrulama kümesine göre seçmek  
D) Eksik değerleri eğitim kümesinin medyanıyla doldurmak  
E) Test kümesini yalnızca en sonda bir kez kullanmak  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **B) Standardizasyon için ortalama ve standart sapmayı, veriyi bölmeden önce tüm veri setinden hesaplamak**
* **Açıklama:** Veri bölünmeden önce hesaplanan istatistikler test verisinin bilgisini eğitim aşamasına sızdırır; model sahte başarı gösterir.

</details>

---

### Soru 34: $R^2$ Skoru Yorumu
**Soru:**
Bir doğrusal regresyon modeli için $R^2 = 0$ bulunmuştur. Bu durum neyi ifade eder?
A) Model tüm örnekleri hatasız tahmin etmektedir.  
B) Model, her örnek için hedefin genel ortalamasını tahmin etmekten daha iyi değildir.  
C) Modelin MSE değeri sıfırdır.  
D) Model aşırı öğrenmiştir.  
E) Öznitelikler ile hedef arasında mükemmel ilişki vardır.  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **B) Model, her örnek için hedefin genel ortalamasını tahmin etmekten daha iyi değildir.**
* **Açıklama:** $R^2 = 1 - \frac{SSE}{SST} = 0 \implies SSE = SST$. Model verideki hiçbir varyansı açıklayamamıştır.

</details>

---

### Soru 35: k-NN Algoritması
**Soru:**
k-NN algoritması için aşağıdaki ifadelerden hangisi **YANLIŞTIR**?
A) Uzaklık hesabına dayandığı için özniteliklerin ölçeklenmesi önemlidir.  
B) Eğitim aşamasında parametre öğrenmez, veriyi saklar.  
C) $k$ değeri büyüdükçe karar sınırı daha düzgün (yumuşak) hâle gelir.  
D) Tahmin aşaması, eğitim kümesi büyüdükçe yavaşlar.  
E) $k = 1$ seçmek aşırı öğrenmeyi her zaman önler.  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **E) $k = 1$ seçmek aşırı öğrenmeyi her zaman önler.**
* **Açıklama:** Tam tersine, $k=1$ seçimi eğitimdeki tüm gürültüyü birebir ezberler ve **aşırı öğrenmeye (overfitting)** neden olur!

</details>

---

### Soru 36: ROC Eğrisi ve AUC
**Soru:**
Bir modelin ROC eğrisinin altında kalan alan $AUC = 0.5$ olarak ölçülmüştür. Bu ne anlama gelir?
A) Model mükemmel ayrım yapmaktadır.  
B) Model, sınıfları rastgele tahminden (yazı-tura atmaktan) daha iyi ayıramamaktadır.  
C) Modelin doğruluğu %50'dir.  
D) Modelin kesinliği ve duyarlılığı eşittir.  
E) Model her zaman pozitif tahmin etmektedir.  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **B) Model, sınıfları rastgele tahminden (yazı-tura atmaktan) daha iyi ayıramamaktadır.**
* **Açıklama:** $AUC = 0.5$ köşegen çizgiye denk gelir; model sınıfları ayırt etme yeteneğine sahip değildir.

</details>

---

### Soru 37: Gürültü ve Filtre Eşleşmesi
**Soru:**
Görüntüdeki **Tuz-Biber gürültüsünü** kenarları en iyi koruyarak gideren filtre hangisidir?
A) Ortalama filtresi (Mean filter)  
B) Medyan filtresi (Median filter)  
C) Keskinleştirme filtresi  
D) Sobel filtresi  
E) Histogram eşitleme  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **B) Medyan filtresi (Median filter)**
* **Açıklama:** Medyan filtresi doğrusal değildir; penceredeki değerleri sıralayıp ortancayı seçtiği için 0 ve 255 uç değerlerinden hiç etkilenmez ve kenarları bozmadan gürültüyü temizler.

</details>

---

### Soru 38: Histogram Yorumu
**Soru:**
Bir görüntünün histogramı 100–140 aralığına sıkışmıştır. Bu görüntü için en doğru yorum ve uygulanması gereken işlem hangisidir?
A) Görüntü çok karanlıktır; negatif alınmalıdır.  
B) Görüntünün kontrastı düşüktür; histogram eşitleme uygulanmalıdır.  
C) Görüntü gürültülüdür; medyan filtresi uygulanmalıdır.  
D) Görüntü ikilidir; eşikleme gerekmez.  
E) Görüntü renklidir; gri tona çevrilmelidir.  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **B) Görüntünün kontrastı düşüktür; histogram eşitleme uygulanmalıdır.**
* **Açıklama:** Piksel değerlerinin dar bir aralığa toplanması düşük kontrastı (mat/soluk görüntü) gösterir. Histogram eşitleme pikselleri $[0, 255]$ aralığına yayarak kontrastı artırır.

</details>

---

### Soru 39: Havuzlama Katmanı
**Soru:**
Maksimum havuzlama (*Max Pooling*) katmanı için aşağıdakilerden hangisi **YANLIŞTIR**?
A) Öğrenilebilir parametresi yoktur.  
B) Her kanala ayrı ayrı uygulanır.  
C) Uzamsal boyutu küçültür.  
D) Kanal sayısını iki katına çıkarır.  
E) Küçük kaymalara karşı dayanıklılık sağlar.  

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

* **Doğru Cevap:** **D) Kanal sayısını iki katına çıkarır.**
* **Açıklama:** Havuzlama katmanı kanal sayısını asla değiştirmez! Kanal sayısını belirleyen unsur uygulanan filtre sayısıdır.

</details>

---

## BÖLÜM 4: 20 Soruluk Örnek Vize Deneme Sınavı (Gerçek Format)

*(Süre: 30 Dakika | Test Sınavı Standartı)*

#### 1. Alan Turing'in 1950 yılında önerdiği "Taklit Oyunu"na (Turing Testi) göre bir makine ne zaman testi geçmiş sayılır?
A) Satrançta dünya şampiyonunu yendiğinde  
B) İnsan sorgulayıcı, aldığı yazılı yanıtlara bakarak karşısındakinin insan mı makine mi olduğunu güvenilir biçimde ayırt edemediğinde  
C) Belleğindeki tüm bilgileri hatasız geri çağırdığında  
D) Kendi kodunu kendi başına yeniden yazabildiğinde  
E) İnsan beynindeki tüm biyolojik nöronları birebir kopyaladığında  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Turing testi, sorgulayıcının insan ile makineyi metin tabanlı iletişimde ayırt edememesi prensibine dayanır.</details>

---

#### 2. Kural tabanlı geleneksel programlama ile makine öğrenmesi arasındaki temel felsefe farkı aşağıdakilerden hangisinde doğru özetlenmiştir?
A) Geleneksel: $Veri + Cevaplar \rightarrow Kurallar$ ; ML: $Veri + Kurallar \rightarrow Cevaplar$  
B) Geleneksel: $Veri + Kurallar \rightarrow Cevaplar$ ; ML: $Veri + Cevaplar \rightarrow Kurallar$  
C) Geleneksel programlama istatistik kullanır, ML mantıksal kurallar kullanır.  
D) Geleneksel programlama yalnızca GPU'da, ML ise yalnızca CPU'da çalışır.  
E) Geleneksel programlama her zaman daha yüksek doğruluk üretir.  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Geleneksel yazılımda mühendis kuralları kodlar ve çıktı alır; ML'de ise algoritma veri ve etiketlerden kuralları kendisi öğrenir.</details>

---

#### 3. Derin öğrenme devrimini 2010'lu yıllardan itibaren mümkün kılan üç temel itici güç hangisidir?
A) Kuantum bilgisayarlar – Prolog dili – İnternet  
B) Büyük Veri – GPU'lar (Paralel İşlem) – Algoritmik Gelişmeler (ReLU, Dropout, Adam)  
C) Mikroişlemciler – Robotik kollar – C dili  
D) Uzman sistemler – Karar ağaçları – Veritabanları  
E) Lisp dili – Turing makineleri – CPU çekirdekleri  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Büyük veri, GPU matris işlem gücü ve algoritmik gelişmeler derin öğrenmenin önünü açmıştır.</details>

---

#### 4. Bir otonom sürüş ajanı için yapılan PEAS analizinde direksiyon simidi, gaz ve fren pedalları hangi bileşendir?
A) Algılayıcılar (Sensors)  
B) Eyleyiciler (Actuators)  
C) Ortam (Environment)  
D) Performans Ölçütü (Performance)  
E) Ajan Fonksiyonu  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Çevre üzerinde fiziksel etki yaratan mekanizmalar eyleyicidir (Actuators).</details>

---

#### 5. Veri setini Eğitim, Doğrulama ve Test olarak ayırırken; tüm veri setine bölünmeden önce `StandardScaler` uygulanması durumunda ortaya çıkan problem nedir?
A) Underfitting  
B) Veri Sızıntısı (Data Leakage)  
C) Boyut Laneti  
D) Kaybolan Gradyan  
E) Aykırı Değer Patlaması  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Test verisinin ortalaması eğitime karıştığı için veri sızıntısı oluşur.</details>

---

#### 6. Şehir isimleri (Ankara, İstanbul, İzmir) için 0, 1, 2 şeklinde `Label Encoding` yapıldığında doğrusal modellerde ortaya çıkabilecek en büyük risk nedir?
A) Bellek kullanımının taşması  
B) Modelin İzmir > Ankara şeklinde yapay bir sayısal büyüklük/sıralama ilişkisi varsayması  
C) Verinin boyutunun aşırı büyümesi  
D) Gradyanın sıfırlanması  
E) Eksik verilerin silinememesi  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Nominal kategorik verilerde etiket kodlama yapay bir sıralama önyargısı üretir; doğrusu One-Hot Encoding'dir.</details>

---

#### 7. Bir regresyon probleminde Ortalama Kare Hatanın (MSE) Ortalama Mutlak Hataya (MAE) göre en belirgin özelliği nedir?
A) Asla sıfır olamaz.  
B) Hataların karesini aldığı için büyük/aykırı hataları çok daha şiddetli cezalandırır.  
C) Aykırı değerlere karşı MAE'den daha dayanıklıdır.  
D) Birimi hedef değişkenle aynıdır.  
E) Türevi hesaplanamaz.  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — MSE kare alma işleminden ötürü büyük sapmaları çok sert cezalandırır.</details>

---

#### 8. Gradyan inişi optimizasyonunda Öğrenme Oranının ($\eta$) aşırı büyük seçilmesi neye yol açar?
A) Modelin çok yavaş yakınsamasına  
B) Minimumun üzerinden atlayarak kaybın sonsuza doğru patlamasına (Iraksama)  
C) Modelin hemen aşırı öğrenmesine  
D) Ağırlıkların sıfıra kilitlenmesine  
E) GPU'nun soğumasına  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Adım boyu çukurdan büyük olduğu için kayıp salınım yaparak ıraksar.</details>

---

#### 9. Lojistik regresyonda doğrusal çıktıyı $[0, 1]$ aralığında olasılığa dönüştüren aktivasyon fonksiyonu hangisidir?
A) Basamak Fonksiyonu  
B) Sigmoid  
C) ReLU  
D) Softmax  
E) Leaky ReLU  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — İkili sınıflandırmada tek çıkış için Sigmoid kullanılır.</details>

---

#### 10. Kanser tarama testinde en tehlikeli hata Yanlış Negatif (FN) olduğuna göre, bu modelde öncelikli olarak maksimize edilmesi gereken metrik hangisidir?
A) Kesinlik (Precision)  
B) Duyarlılık (Recall)  
C) Doğruluk (Accuracy)  
D) Özgüllük (Specificity)  
E) Gini Katsayısı  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Gerçek kanserli vakaları kaçırmamak ($FN \rightarrow 0$) için Recall maksimize edilmelidir.</details>

---

#### 11. Bir sınıflandırma modelinde $AUC = 0.5$ ölçülmesi ne anlama gelir?
A) Model mükemmel çalışmaktadır.  
B) Model rastgele tahmin seviyesindedir (yazı-turadan farksızdır).  
C) Model eğitim verisini ezberlemiştir.  
D) Modelin kesinliği %100'dür.  
E) Model negatif sınıfları kaçırmaktadır.  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — AUC = 0.5 köşegendir, ayırt etme yeteneği sıfırdır.</details>

---

#### 12. Tek katmanlı Perceptron'un XOR problemini çözememesi tarihte neye yol açmıştır?
A) İnternetin icadına  
B) 1. Yapay Zekâ Kışı'na (AI Winter)  
C) GPU'ların icat edilmesine  
D) ResNet mimarisinin geliştirilmesine  
E) Python dilinin yazılmasına  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Minsky ve Papert'in 1969 tarihli kitabı fonların kesilmesine ve yapay zekâ kışına neden olmuştur.</details>

---

#### 13. Yapay sinir ağlarında gizli katmanlarda doğrusal olmayan aktivasyon fonksiyonu (ReLU) kullanılmazsa ne olur?
A) Ağ çok hızlı öğrenir.  
B) 100 katman da eklense ağ tek bir doğrusal regresyon katmanına çöker.  
C) Model aşırı öğrenmeye düşer.  
D) Ağırlıklar tersine döner.  
E) Hiçbir matris çarpımı yapılamaz.  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Matris çarpımlarının bileşimi yine doğrusal bir matristir.</details>

---

#### 14. 50 nöronlu bir katmandan 10 nöronlu bir Dense katmanına geçişte kaç adet öğrenilebilir parametre vardır?
A) 60  
B) 500  
C) 510  
D) 550  
E) 600  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: C</b> — $(50 \times 10) + 10 = 500 + 10 = 510$.</details>

---

#### 15. Geri yayılımda ön aktivasyonu $z = -2.5$ olan bir ReLU nöronunun girdisine aktarılan gradyan kaçtır?
A) -2.5  
B) 1.0  
C) 0  
D) 0.5  
E) Sonsuz  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: C</b> — $z < 0$ iken ReLU türevi 0'dır, gradyan sıfırlanır.</details>

---

#### 16. Tuz-biber gürültüsünü kenarları koruyarak en iyi temizleyen görüntü işleme filtresi hangisidir?
A) Ortalama Filtresi  
B) Medyan Filtresi  
C) Gauss Filtresi  
D) Sobel Filtresi  
E) Canny Filtresi  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Medyan filtresi aykırı 0 ve 255 değerlerinden etkilenmez.</details>

---

#### 17. Bir CNN modelinde $32 \times 32 \times 3$ girdiye 16 adet $3 \times 3$ filtre ($P=1, S=1$) uygulanırsa çıktı boyutu ne olur?
A) $30 \times 30 \times 16$  
B) $32 \times 32 \times 16$  
C) $32 \times 32 \times 3$  
D) $16 \times 16 \times 16$  
E) $64 \times 64 \times 16$  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — $\frac{32 - 3 + 2}{1} + 1 = 32 \implies 32 \times 32 \times 16$.</details>

---

#### 18. CNN mimarisinden Max Pooling katmanı kaldırılırsa aşağıdakilerden hangisi gerçekleşir?
A) Model daha az bellek kullanır.  
B) Parametre sayısı ve hesaplama maliyeti devasa oranda artar, overfitting riski fırlar.  
C) Model hiç eğitilemez.  
D) Kanal sayısı sıfırlanır.  
E) Görüntü siyah-beyaza döner.  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Havuzlama yapılmadığında tensör büyük kalır, Flatten sonrası parametre patlaması yaşanır.</details>

---

#### 19. Çok sınıflı bir görüntü sınıflandırma modelinin çıkış katmanında hangi aktivasyon fonksiyonu kullanılır?
A) Sigmoid  
B) Softmax  
C) ReLU  
D) Tanh  
E) Step  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Çok sınıflı problemlerde toplamı 1.0 olan olasılık dağılımı için Softmax kullanılır.</details>

---

#### 20. Eğitim sırasında rastgele nöronların belirli bir oranını devre dışı bırakarak ezberlemeyi engelleyen yöntem hangisidir?
A) Batch Normalization  
B) Dropout (Seyreltme)  
C) Erken Durdurma  
D) Max Pooling  
E) One-Hot Encoding  

<details><summary><b>Çözümü Gör</b></summary><b>Doğru Cevap: B</b> — Dropout eğitim sırasında nöronları geçici kapatarak aşırı öğrenmeyi engeller.</details>

---

## 🏁 Tebrikler!
Tüm modülleri ve soruları tamamladınız. Vize sınavı için bu dokümandaki formülleri, hocanın derste sorduğu 16 soruyu ve deneme testindeki mantıkları pekiştirerek sınava tam hazır hale gelebilirsiniz!
