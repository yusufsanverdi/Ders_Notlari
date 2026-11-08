# Sections 4 to 6: Weeks 4 to 6 (Questions 55 to 114)

def get_section_4():
    return r"""## BÖLÜM 4: Hafta 04 – Sınıflandırma Yöntemleri

### Soru 55 (Kavramsal): Karar Sınırı (Decision Boundary)
Sınıflandırma problemlerinde **Karar Sınırı (Decision Boundary)** nedir? Doğrusal sınıflandırıcılar (Lojistik Regresyon) ile doğrusal olmayan sınıflandırıcıların (k-NN, Karar Ağaçları) karar sınırları geometrik olarak nasıl ayrışır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Tanım:** Modelin girdi uzayında bir sınıf ile diğer sınıfı birbirinden ayırdığı geometrik yüzeydir (olasılığın $\hat{p} = 0.5$ olduğu yer).
2. **Geometrik Fark:**
   * **Doğrusal Sınıflandırıcılar (Lojistik Regresyon, Doğrusal SVM):** Düz bir çizgi (2D) veya düz bir hiperdüzlem ($D$-boyutlu) çizer.
   * **Doğrusal Olmayan Sınıflandırıcılar (k-NN, Karar Ağaçları, MLP):** Kıvrımlı, basamaklı veya ada şeklinde karmaşık karar sınırları üretebilir.

</details>

---

### Soru 56 (Çoktan Seçmeli): Sigmoid Fonksiyonu Değerleri
Lojistik regresyonda kullanılan Sigmoid fonksiyonu $\sigma(z) = \frac{1}{1 + e^{-z}}$ için aşağıdakilerden hangisi **DOĞRUDUR**?
A) $z = 0$ iken $\sigma(z) = 0.0$ olur.
B) $z = 0$ iken $\sigma(z) = 0.5$ olur; $z \rightarrow +\infty$ iken $1.0$'a, $z \rightarrow -\infty$ iken $0.0$'a yaklaşır.
C) Sigmoid fonksiyonunun çıktıları $[-1, +1]$ aralığındadır.
D) Sigmoid fonksiyonu yalnızca negatif değerler için tanımlıdır.
E) Sigmoid fonksiyonunun türevi her noktada sabittir.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $\sigma(0) = \frac{1}{1 + e^0} = \frac{1}{1 + 1} = 0.5$. Tüm gerçel sayıları $(0, 1)$ olasılık aralığına sıkıştırır.

</details>

---

### Soru 57 (Kavramsal): İkili Çapraz Entropi (BCE) Mantığı
İkili sınıflandırmada neden MSE yerine İkili Çapraz Entropi (Binary Cross-Entropy / Log Loss) kayıp fonksiyonu tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Dışbükeylik (Convexity):** MSE formülü Sigmoid fonksiyonuyla birleştiğinde konveks olmayan, çok sayıda yerel minimum içeren dalgalı bir yüzey oluşturur ve gradyan inişi takılır. Çapraz entropi ise konvekstir, tek bir küresel minimum garantisi verir.
2. **Ağır Ceza Mekanizması:** Model kendinden emin bir şekilde yanlış tahminde bulunduğunda ($y=1$ iken $\hat{p} \rightarrow 0$), $-\ln(\hat{p}) \rightarrow +\infty$ olur; yani model aşırı şiddetle cezalandırılır.

</details>

---

### Soru 58 (Sayısal Kayıp - SLAYTLARDAN): $y=0$ İken BCE Hesabı
Gerçek sınıfı $y = 0$ olan bir örnek için model pozitif sınıf olasılığını $\hat{p} = 0.8$ tahmin etmiştir. İkili çapraz entropi kaybı yaklaşık kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$L = - \left[ y \ln(\hat{p}) + (1-y) \ln(1-\hat{p}) \right]$$
2. **$y = 0$ Yerine Koyalım:**
   $$L = - \left[ 0 + (1-0) \ln(1 - 0.8) \right] = -\ln(0.2)$$
3. **Hesap:**
   $$\ln(0.2) \approx -1.609 \implies L \approx \mathbf{1.61}$$
* Model yanlış sınıfa yüksek olasılık verdiği için kayıp büyüktür.

</details>

---

### Soru 59 (Sayısal Kayıp): $y=1$ İken BCE Hesabı
Gerçek sınıfı $y = 1$ olan bir örnek için model $\hat{p} = 0.90$ tahmininde bulunmuştur. İkili çapraz entropi kaybı kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül ($y = 1$):**
   $$L = -\ln(\hat{p}) = -\ln(0.90)$$
2. **Hesap:**
   $$L \approx \mathbf{0.105}$$
* Model doğru sınıfa yüksek olasılık verdiği için kayıp sıfıra çok yakındır.

</details>

---

### Soru 60 (Çoktan Seçmeli): k-NN Algoritması Çalışma Prensibi
k-En Yakın Komşu (k-NN) algoritması hakkında aşağıdakilerden hangisi **YANLIŞTIR**?
A) Eğitim aşamasında model parametresi öğrenmez; veriyi bellekte saklar (Lazy Learner).
B) Yeni gelen örneğin sınıfı, en yakın $k$ adet komşusunun çoğunluk oylamasıyla (*majority voting*) belirlenir.
C) Mesafe temelli olduğu için öznitelik ölçekleme gerektirmez.
D) Veri seti büyüdükçe test (tahmin) aşaması yavaşlar.
E) Genellikle Öklid veya Manhattan mesafesi kullanılır.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: C**
* **Açıklama:** k-NN mesafe hesabına dayandığı için öznitelik ölçekleme **ZORUNLUDUR**. Ölçekleme yapılmazsa büyük sayısal aralıklı sütunlar mesafeyi tamamen domine eder.

</details>

---

### Soru 61 (Kavramsal - BANKO): k-NN'de $k=1$ Tuzağı
k-NN algoritmasında $k = 1$ seçildiğinde modelin eğitim kümesindeki doğruluk oranı neden daima %100 çıkar ve bu durum neden tehlikelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Neden %100 Çıkar?**
   * Eğitimdeki bir nokta sorgulandığında, kendisine en yakın komşu (0 mesafe ile) yine kendisidir. Bu yüzden her noktayı %100 doğru tahmin eder.
2. **Neden Tehlikelidir?**
   * Verideki tüm aykırı değerleri, etiket hatalarını ve gürültüyü birebir ezberler. Karar sınırı her noktanın etrafından dolanan aşırı girintili çıkıntılı bir hal alır $\implies$ **Aşırı Öğrenme (Overfitting / Yüksek Varyans)**. Test kümesinde başarısız olur.

</details>

---

### Soru 62 (Çoktan Seçmeli): k-NN'de $k$ Değerinin Büyümesi
k-NN algoritmasında $k$ komşu sayısı 1'den 50'ye doğru büyütüldüğünde aşağıdakilerden hangisi gerçekleşir?
A) Model aşırı öğrenmeye düşer.
B) Karar sınırı daha düzgün ve yumuşak hale gelir, yerel detaylar kaybolur, model eksik öğrenmeye (underfitting) kayabilir.
C) Tahmin süresi kısalır.
D) Bellek ihtiyacı sıfırlanır.
E) Her sınıf eşit sayıda tahmin edilir.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $k$ büyüdükçe yerel gürültülerin etkisi azalır, karar sınırı yumuşar; ancak çok büyütülürse çoğunlukta olan baskın sınıf tüm oyları alır ve model genellemeyi kaybedip eksik öğrenmeye düşer.

</details>

---

### Soru 63 (Sayısal Mesafe): k-NN Öklid Mesafesi
İki boyutlu uzayda yeni bir test noktası $q = (5, 4)$ olarak verilmiştir. İki komşu nokta $A = (2, 0)$ ve $B = (5, 1)$ olduğuna göre $q$ noktası hangisine daha yakındır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **$A$ ile Mesafe:**
   $$d(q, A) = \sqrt{(5 - 2)^2 + (4 - 0)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = \mathbf{5.0}$$
2. **$B$ ile Mesafe:**
   $$d(q, B) = \sqrt{(5 - 5)^2 + (4 - 1)^2} = \sqrt{0 + 3^2} = \sqrt{9} = \mathbf{3.0}$$
* $d(q, B) < d(q, A)$ olduğundan $q$ noktası **$B$ noktasına daha yakındır**.

</details>

---

### Soru 64 (Kavramsal): Karar Ağaçlarında Entropi
Bilgi teorisinde Entropi $H(S) = - \sum_{i=1}^{C} p_i \log_2(p_i)$ olarak tanımlanır.
1. Bir düğümdeki örneklerin tamamı aynı sınıfa aitse (tam saflık) entropi değeri kaç olur?
2. Örnekler iki sınıfa %50 - %50 eşit dağılmışsa (maksimum belirsizlik) entropi kaç olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Tam Saflık ($p_1 = 1.0, p_2 = 0$):**
   $$H(S) = - (1 \cdot \log_2(1)) = \mathbf{0}$$
   (Belirsizlik tamamen yok olmuştur).
2. **Maksimum Belirsizlik ($p_1 = 0.5, p_2 = 0.5$):**
   $$H(S) = - [0.5 \log_2(0.5) + 0.5 \log_2(0.5)] = - [0.5(-1) + 0.5(-1)] = \mathbf{1.0}$$

</details>

---

### Soru 65 (Sayısal Hesaplama): Gini Kirliliği Hesabı
Bir karar ağacı düğümünde 6 adet "Elma", 2 adet "Armut" bulunmaktadır. Bu düğümün Gini Kirliliği ($Gini(S) = 1 - \sum p_i^2$) kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Olasılıklar:**
   $$p(Elma) = \frac{6}{8} = 0.75, \quad p(Armut) = \frac{2}{8} = 0.25$$
2. **Kareler Toplamı:**
   $$(0.75)^2 + (0.25)^2 = 0.5625 + 0.0625 = 0.625$$
3. **Gini Kirliliği:**
   $$Gini(S) = 1 - 0.625 = \mathbf{0.375}$$

</details>

---

### Soru 66 (Kavramsal): Bilgi Kazancı (Information Gain)
Karar ağaçlarında (ID3 / C4.5) kök düğümden başlayarak bölünme yapılacak en iyi öznitelik hangi kritere göre seçilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Bilgi Kazancı (Information Gain) En Yüksek Olan Öznitelik Seçilir.**
* Bilgi kazancı; bölünme öncesi ebeveyn düğümün entropisi ile bölünme sonrası çocuk düğümlerin ağırlıklı entropisi arasındaki farktır. Bilgi kazancını maksimize etmek, alt düğümlerde saflığı en çok artıran ve belirsizliği en çok düşüren özniteliği seçmek demektir.

</details>

---

### Soru 67 (Çoktan Seçmeli): Karar Ağaçlarında Aşırı Öğrenmeyi Engelleme
Karar ağaçlarının sınırsız derinleşerek eğitim verisini ezberlemesini (overfitting) engellemek için hangi yöntem kullanılır?
A) Ağaç Budama (Pruning) ve Maksimum Derinlik (`max_depth`) kısıtı koyma
B) Öğrenme oranını artırma
C) Veri setindeki satırları silme
D) Aktivasyon fonksiyonunu ReLU yapma
E) Sınıf sayısını iki katına çıkarma

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: A**
* **Açıklama:** Ağacın aşırı dallanmasını engellemek için `max_depth` (maksimum derinlik), `min_samples_split` (bölünme için gereken minimum örnek) parametreleri kısıtlanır ve eğitim sonrası gereksiz yapraklar budanır (*pruning*).

</details>

---

### Soru 68 (Kavramsal): Naive Bayes'in "Naif" Varsayımı
Naive Bayes algoritmasına neden "Naif" (Saf / Toy) adı verilmiştir? Bu varsayım gerçek hayatta neden çoğunlukla tutmaz?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Naif Varsayım:** Verideki tüm özniteliklerin verilen sınıf koşulu altında birbirinden **tamamen bağımsız olduğunu** varsayar ($P(x_1, x_2 | y) = P(x_1|y) P(x_2|y)$).
2. **Neden Gerçekçi Değildir?**
   * Gerçek hayatta öznitelikler birbiriyle ilişkilidir. Örneğin metin işlemede "Yapay" kelimesi geçtiğinde arkasından "Zekâ" kelimesinin gelme olasılığı çok yüksektir; bu iki kelime birbirinden bağımsız değildir. Buna rağmen algoritma spam filtrelemede şaşırtıcı derecede iyi çalışır.

</details>

---

### Soru 69 (Çoktan Seçmeli): Destek Vektör Makineleri (SVM)
Destek Vektör Makineleri (SVM) algoritmasının temel felsefesi nedir?
A) Sınıflar arasındaki veri yoğunluğunu ortalamak
B) İki sınıf arasındaki ayrım boşluğunu (Marj / Margin) maksimize eden en ideal karar sınırını (hiperdüzlemi) bulmak
C) Tüm noktaları tek bir kümede toplamak
D) Verileri rastgele doğrularla bölmek
E) Gini kirliliğini sıfırlamak

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** SVM, sınıflar arasına rastgele bir doğru çekmez; her iki sınıfın sınıra en yakın noktalarına (Destek Vektörleri) olan mesafeyi (Marjı) en büyük yapacak hiperdüzlemi optimize eder.

</details>

---

### Soru 70 (Kavramsal): SVM Çekirdek Hilesi (Kernel Trick)
Doğrusal olarak ayrılamayan (Örn: İç içe iki halka şeklindeki veri) bir problemde SVM nasıl başarı sağlar?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Çekirdek Hilesi (Kernel Trick):** Veriyi açıkça yüksek boyutlu uzaya taşımadan, çekirdek fonksiyonları (RBF / Radyal Tabanlı Fonksiyon, Polinom) yardımıyla yüksek boyuttaki iç çarpımları doğrudan düşük boyutta hesaplar.
* Orijinal 2 boyutlu uzayda doğrusal ayrılamayan halkalar, 3. boyuta (yükseklik eksenine) fırlatıldığında aralarına düz bir hiperdüzlem tabakası sokularak kolayca ayrılabilir.

</details>

---

### Soru 71 (Doğru / Yanlış - Gerekçeli): SVM ve Destek Vektörleri
**İfade:** *"SVM modelinde sınırdan çok uzakta yer alan güvenli eğitim noktaları silinirse karar hiperdüzleminin konumu tamamen değişir."*
Bu ifade Doğru mudur, Yanlış mıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** SVM karar sınırının konumunu YALNIZCA sınıra en yakın duran **Destek Vektörleri (Support Vectors)** belirler. Sınırın çok gerisinde kalan güvenli noktaların silinmesi veya ötelenmesi hiperdüzlemin matematiksel çözümünü hiç değiştirmez.

</details>

---

### Soru 72 (Çoktan Seçmeli): Sınıflandırıcı Karşılaştırması
Eğitim süresi $0$ olan, tüm hesaplama yükünü tahmin (test) anına erteleyen algoritma hangisidir?
A) Lojistik Regresyon
B) k-En Yakın Komşu (k-NN)
C) Karar Ağacı
D) Yapay Sinir Ağı
E) Destek Vektör Makinesi

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** k-NN "Tembel Öğrenici"dir (Lazy Learner). Eğitim aşamasında model fit etmez; sadece veriyi saklar. Tüm mesafeleri test anında hesaplar.

</details>

---

### Soru 73 (Kavramsal): Çok Sınıflı Lojistik Regresyonda OvR
3 sınıflı bir problemde (Kedi, Köpek, Kuş) ikili lojistik regresyon kullanarak sınıflandırma yapmak için **Bire Karşı Hepsi (One-vs-Rest / OvR)** yaklaşımı nasıl kurgulanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* 3 ayrı ikili sınıflandırıcı eğitilir:
  1. Model 1: Kedi (1) vs. Kedi Değil [Köpek+Kuş] (0)
  2. Model 2: Köpek (1) vs. Köpek Değil [Kedi+Kuş] (0)
  3. Model 3: Kuş (1) vs. Kuş Değil [Kedi+Köpek] (0)
* Test aşamasında her üç modele görüntü verilir; en yüksek olasılık skorunu üreten modelin sınıfı nihai tahmin olarak seçilir.

</details>

---

### Soru 74 (Vaka Analizi): Karar Ağaçlarının Yorumlanabilirliği
Medikal veya finansal kredi onaylama sistemlerinde derin öğrenme modelleri yerine neden sıklıkla Karar Ağaçları tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Açıklanabilirlik ve Beyaz Kutu (White-Box) Özelliği:**
  * Karar ağaçlarının aldığı her karar kökten yaprağa izlenebilir kurallardan oluşur: *"Eğer Kredi Skoru > 700 VE Gelir > 50.000 TL ise Kredi Ver"*.
  * Derin sinir ağları milyonlarca ağırlıkla bir "Kara Kutu" (Black-Box) gibi davranırken; karar ağaçları yasal denetimlerde ve doktorlara teşhis gerekçesi sunmada %100 şeffaftır.

</details>

---
"""

def get_section_5():
    return r"""## BÖLÜM 5: Hafta 05 – Model Değerlendirme, Karışıklık Matrisi, ROC/AUC ve Kümeleme

### Soru 75 (Kavramsal): Karışıklık Matrisi Bileşenleri
İkili bir sınıflandırma probleminde Karışıklık Matrisinin ($2 \times 2$) 4 hücresini (TP, TN, FP, FN) bir **Havalimanı Güvenlik X-Ray Bagaj Kontrol Sistemi** için açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **TP (Doğru Pozitif):** Çantada kesici alet vardır; sistem alarm vermiş ve yakalamıştır.
* **TN (Doğru Negatif):** Çanta temizdir; sistem alarm vermemiş, yolcu geçmiştir.
* **FP (Yanlış Pozitif / Tip I Hata):** Çanta temizdir; sistem yanlış alarm verip çantayı boş yere açtırmıştır.
* **FN (Yanlış Negatif / Tip II Hata):** Çantada kesici alet vardır; sistem tespit edememiş ve tehlikeli alet uçağa girmiştir (En ölümcül hata).

</details>

---

### Soru 76 (Kavramsal): Doğruluk Paradoksu (Accuracy Paradox)
Neden kredi kartı dolandırıcılığı tespiti gibi binde 1 oranında pozitif vaka içeren dengesiz problemlerde **Doğruluk (Accuracy)** metriği tek başına bir başarı ölçütü olarak kullanılamaz?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* 100.000 işlemden 99.900'ü normal, 100'ü dolandırıcılıktır.
* Hiçbir şey öğrenmeyen ve her işleme "Normal" diyen tembel bir model:
  $$\text{Doğruluk} = \frac{99.900}{100.000} = \mathbf{\%99.9}$$
* Model kâğıt üzerinde %99.9 gibi kusursuz bir doğruluk verir; ancak 100 dolandırıcılık vakasının tamamını kaçırdığı için bankayı batırır.

</details>

---

### Soru 77 (Çoktan Seçmeli): Kesinlik (Precision) Formülü
Modelin "Pozitif" olarak etiketlediği tahminlerin ne kadarının gerçekten doğru olduğunu ölçen metrik hangisidir?
A) $\frac{TP}{TP + FN}$ (Duyarlılık)
B) $\frac{TP}{TP + FP}$ (Kesinlik)
C) $\frac{TN}{TN + FP}$ (Özgüllük)
D) $\frac{TP + TN}{TP + TN + FP + FN}$ (Doğruluk)
E) $\frac{FP}{FP + TN}$ (Yanlış Pozitif Oranı)

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Kesinlik (*Precision*) $= \frac{TP}{TP + FP}$ formülüyle hesaplanır. Paydada modelin pozitif dediği tüm vakalar ($TP + FP$) yer alır.

</details>

---

### Soru 78 (Çoktan Seçmeli): Duyarlılık (Recall) Formülü
Evrendeki gerçek pozitif vakaların yüzde kaçının model tarafından yakalanabildiğini ölçen metrik hangisidir?
A) Kesinlik (Precision)
B) Duyarlılık (Recall / Sensitivity)
C) F1-Skoru
D) Hata Oranı
E) ROC Alanı

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Duyarlılık (*Recall*) $= \frac{TP}{TP + FN}$ formülüyle bulunur. Paydada gerçekte pozitif olan tüm vakalar ($TP + FN$) bulunur.

</details>

---

### Soru 79 (Sayısal Hesaplama - SLAYTLARDAN): Metrik Hesabı
Bir modelin test kümesindeki karışıklık matrisi şöyledir:
$TP = 30$, $FP = 10$, $FN = 20$, $TN = 140$.
Bu modelin Kesinlik (*Precision*), Duyarlılık (*Recall*) ve Doğruluk (*Accuracy*) değerlerini hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Kesinlik (Precision):**
   $$\text{Precision} = \frac{TP}{TP + FP} = \frac{30}{30 + 10} = \frac{30}{40} = \mathbf{0.75}$$
2. **Duyarlılık (Recall):**
   $$\text{Recall} = \frac{TP}{TP + FN} = \frac{30}{30 + 20} = \frac{30}{50} = \mathbf{0.60}$$
3. **Doğruluk (Accuracy):**
   $$\text{Accuracy} = \frac{TP + TN}{\text{Toplam}} = \frac{30 + 140}{30 + 10 + 20 + 140} = \frac{170}{200} = \mathbf{0.85}$$

</details>

---

### Soru 80 (Kavramsal): F1-Skorunda Neden Harmonik Ortalama?
F1-Skoru hesabında Kesinlik ve Duyarlılığın aritmetik ortalaması $(\frac{P + R}{2})$ yerine neden **Harmonik Ortalama** ($2 \times \frac{P \times R}{P + R}$) tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Aritmetik Ortalama Tuzağı:** Bir model $Precision = 1.0$ ve $Recall = 0.0$ verdiğinde aritmetik ortalama $\frac{1.0 + 0.0}{2} = 0.50$ gibi yanıltıcı bir vasat skor üretir.
* **Harmonik Ortalama:** Aşırı uçlara karşı son derece cezalandırıcıdır. İki metrikten biri sıfıra yaklaştığında harmonik ortalama da **sıfıra çöker**:
  $$F1 = 2 \times \frac{1.0 \times 0.0}{1.0 + 0.0} = \mathbf{0.0}$$
  Böylece dengesiz modellerin maskelenmesini engeller.

</details>

---

### Soru 81 (Sayısal Hesaplama): F1-Skoru Hesabı
$Precision = 0.75$ ve $Recall = 0.60$ olan bir sınıflandırıcının F1-Skorunu hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
2. **Hesap:**
   $$F1 = 2 \times \frac{0.75 \times 0.60}{0.75 + 0.60} = 2 \times \frac{0.45}{1.35} = \frac{0.90}{1.35} = \frac{2}{3} \approx \mathbf{0.667}$$

</details>

---

### Soru 82 (Vaka Analizi): Medikal Teşhiste Metrik Önceliği
Bir kanser teşhis yapay zekâsında yanlış pozitif (sağlıklı birine hasta demek) ve yanlış negatif (hasta birine sağlıklı demek) hatalarından hangisi insan hayatı açısından daha tehlikelidir? Hangi metrik maksimize edilmelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **En Tehlikeli Hata: Yanlış Negatif (FN):** Hasta bir insana "temizsin" denilip evine yollandığında tümör ilerler ve hasta hayatını kaybedebilir. Yanlış pozitifte ise hasta sadece fazladan bir biyopsi/test yaptırır.
* Bu nedenle medikal teşhiste $FN \rightarrow 0$ hedeflenir ve **Duyarlılık (Recall)** metriği maksimize edilir.

</details>

---

### Soru 83 (Vaka Analizi): Spam Filtresinde Metrik Önceliği
Bir e-posta spam filtresinde Yanlış Pozitif (normal bir iş teklifi mailini spam kutusuna atmak) hatası mı, yoksa Yanlış Negatif (reklam mailini gelen kutusuna düşürmek) hatası mı kullanıcı için daha yıkıcıdır? Hangi metrik yüksek tutulmalıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **En Yıkıcı Hata: Yanlış Pozitif (FP):** Üniversite sınav sonuç belgesi veya iş mülakatı daveti spam kutusuna atılıp kaçırılırsa kullanıcı telafisi imkânsız bir zarara uğrar. Birkaç spam mailin gelen kutusuna düşmesi ise önemsiz bir rahatsızlıktır.
* Bu nedenle spam filtrelerinde $FP \rightarrow 0$ tutulmalı ve **Kesinlik (Precision)** maksimize edilmelidir.

</details>

---

### Soru 84 (Çoktan Seçmeli): ROC Eğrisi Eksenleri
Bir ROC (*Receiver Operating Characteristic*) eğrisinin yatay (X) ve dikey (Y) eksenlerinde hangi metrikler yer alır?
A) X: Kesinlik, Y: Duyarlılık
B) X: Yanlış Pozitif Oranı (FPR), Y: Doğru Pozitif Oranı (TPR / Recall)
C) X: Eğitim Kaybı, Y: Test Kaybı
D) X: Doğruluk, Y: Hata Oranı
E) X: Epoch Sayısı, Y: Öğrenme Oranı

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** ROC eğrisi karar eşiği 0'dan 1'e taranırken X eksenine Yanlış Pozitif Oranını ($FPR = \frac{FP}{FP + TN}$), Y eksenine Doğru Pozitif Oranını ($TPR = \frac{TP}{TP + FN} = Recall$) yerleştirir.

</details>

---

### Soru 85 (Kavramsal - BANKO): $AUC = 0.5$ Anlamı
Bir modelin ROC eğrisinin altında kalan alan $AUC = 0.5$ olarak ölçülmüştür. Bu durum neyi ifade eder?
A) Model sınıfları mükemmel ayırmaktadır.
B) Model sınıfları rastgele tahminden (yazı-tura atmaktan) daha iyi ayıramamaktadır.
C) Modelin test kümesindeki doğruluğu %50'dir.
D) Modelde aşırı öğrenme engellenmiştir.
E) Model yalnızca pozitif sınıfları tahmin etmektedir.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $AUC = 0.5$ grafikte $(0,0)$ ile $(1,1)$ noktalarını birleştiren köşegen çizgiye denk gelir; model pozitif bir örneğe negatif bir örnekten daha yüksek olasılık verme konusunda tamamen şans düzeyindedir.

</details>

---

### Soru 86 (Çoktan Seçmeli): İdeal AUC Değerleri
Aşağıdaki AUC değerlerinden hangisi endüstriyel olarak kabul edilebilir ve başarılı bir sınıflandırma modelini gösterir?
A) $0.15$
B) $0.50$
C) $0.88$
D) $-0.50$
E) $0.00$

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: C**
* **Açıklama:** $AUC \ge 0.80$ genellikle iyi, $AUC \ge 0.90$ çok iyi, $AUC = 1.0$ ise kusursuz modeli temsil eder.

</details>

---

### Soru 87 (Kavramsal): Karar Eşiği Kaydırması
İkili bir sınıflandırma modelinde pozitif karar eşiği varsayılan $\tau = 0.5$'ten $\tau = 0.2$'ye indirilirse Kesinlik (*Precision*) ve Duyarlılık (*Recall*) metrikleri nasıl değişir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Eşik $0.2$'ye çekildiğinde model önüne gelene çok daha kolay "Pozitif" demeye başlar.
* **Duyarlılık (Recall) ARTAR:** Kaçırılan pozitif vaka sayısı azalır ($FN \downarrow$).
* **Kesinlik (Precision) DÜŞER:** Daha çok şüpheli örneğe pozitif dendiği için yanlış alarm sayısı artar ($FP \uparrow$).

</details>

---

### Soru 88 (Kavramsal): k-Katlı Çapraz Doğrulama
5-Katlı Çapraz Doğrulama (*5-Fold Cross Validation*) sürecini adım adım özetleyiniz. Tek bir train/test ayrımına göre üstünlüğü nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Adımlar:** Veri seti rastgele 5 eşit parçaya bölünür. 5 iterasyon boyunca sırayla her parça birer kez test, kalan 4 parça eğitim için kullanılır. 5 farklı skorun ortalaması ve standart sapması raporlanır.
2. **Üstünlüğü:** Tek bir rastgele train/test ayrımındaki şans faktörünü (örneğin test setine kolay örneklerin denk gelmesini) ortadan kaldırır; modelin genelleme kararlılığını güvenilir biçimde kanıtlar.

</details>

---

### Soru 89 (Çoktan Seçmeli): Yanlılık-Varyans Dengesi
Bir modelin eğitim kümesinde %99.5 doğruluk alırken, test kümesinde %62.0 doğruluk alması hangi hatanın yüksek olduğunu gösterir?
A) Yüksek Yanlılık (High Bias / Underfitting)
B) Yüksek Varyans (High Variance / Overfitting)
C) İndirgenemez Hata
D) Düşük Karmaşıklık Hatası
E) Dengesiz Veri Hatası

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Yüksek Varyans (Overfitting); modelin eğitim verisine aşırı duyarlı olup yeni verilere karşı kararsız kalmasıdır.

</details>

---

### Soru 90 (Çoktan Seçmeli): L1 Düzenlileştirme (Lasso)
Kayıp fonksiyonuna katsayıların mutlak değerler toplamının ($\lambda \sum |w_i|$) eklendiği L1 düzenlileştirmenin (Lasso) L2'ye kıyasla en ayırt edici özelliği nedir?
A) Ağırlıkları sadece küçültür ama asla sıfır yapmaz.
B) Önemsiz özniteliklerin ağırlıklarını TAM OLARAK SIFIR yaparak otomatik öznitelik seçimi (seyrek model) sağlar.
C) Hesaplama süresini uzatır.
D) Yalnızca sınıflandırmada çalışır.
E) Veriyi normalize eder.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** L1 geometrisi köşeli bir elmas şeklindedir; eksenleri kestiği noktalarda bazı ağırlık katsayılarını birebir $0$ yapar ve gereksiz sütunları eler.

</details>

---

### Soru 91 (Çoktan Seçmeli): L2 Düzenlileştirme (Ridge / Weight Decay)
Kayıp fonksiyonuna ağırlıkların kareler toplamının ($\lambda \sum w_i^2$) eklendiği L2 düzenlileştirmenin temel etkisi nedir?
A) Tüm ağırlıkları sıfır yapmak
B) Aşırı büyük ağırlıkları sert biçimde cezalandırarak tüm katsayıları sıfıra yakın küçük değerlerde tutmak ve aşırı öğrenmeyi engellemek
C) Modelin katman sayısını artırmak
D) Öğrenme oranını sıfırlamak
E) Verideki eksik değerleri silmek

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** L2 katsayıları sıfıra doğru çeker ama hiçbirini tam sıfır yapmaz; modelin belirli birkaç özniteliğe aşırı bağımlı olmasını önler.

</details>

---

### Soru 92 (Sıralama): K-Means Algoritmasının Adımları
K-Means kümeleme algoritmasının çalışma adımlarını doğru sıraya diziniz:
1. Her veri noktasını kendisine en yakın merkez noktasına (centroid) ata.
2. Uzayda rastgele $k$ adet merkez noktası belirle.
3. Merkezlerin konumları değişmeyene kadar döngüyü sürdür.
4. Her kümenin yeni merkezini o kümeye atanan noktaların ortalaması olarak güncelle.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Sıralama:** **2 $\rightarrow$ 1 $\rightarrow$ 4 $\rightarrow$ 3**
* Başlatma (2) $\rightarrow$ Ata (1) $\rightarrow$ Güncelle (4) $\rightarrow$ Yakınsama Kontrolü (3).

</details>

---

### Soru 93 (Kavramsal): K-Means Dirsek Yöntemi (Elbow Method)
K-Means algoritmasında en uygun küme sayısını ($k$) seçmek için kullanılan **Dirsek Yöntemi (Elbow Method)** nasıl çalışır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Farklı $k$ değerleri için (Örn: $k=1..10$) Küme İçi Kareler Toplamı (WCSS / Inertia) hesaplanır ve grafiğe çizilir.
* $k$ arttıkça hata azalır; ancak bir noktadan sonra hata düşüş hızı aniden yavaşlar ve eğri bir "kol dirseği" gibi bükülür. O bükülme noktası, aşırı karmaşıklığa girmeden en ideal küme sayısını verir.

</details>

---

### Soru 94 (Çoktan Seçmeli): Siluet Skoru (Silhouette Score)
Siluet Skoru ($-1$ ile $+1$ arasında) için aşağıdakilerden hangisi **DOĞRUDUR**?
A) $+1$'e yakın skorlar örneklerin kendi kümesine çok yakın, komşu kümelere çok uzak olduğunu (mükemmel kümelenme) gösterir.
B) $0$'a yakın skorlar aşırı öğrenmeyi gösterir.
C) $-1$ en iyi skordur.
D) Siluet skoru yalnızca denetimli öğrenmede hesaplanır.
E) Siluet skoru modelin doğruluk yüzdesidir.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: A**
* **Açıklama:** Siluet skoru bir noktanın kendi kümesine olan yakınlığı ile diğer kümelere olan uzaklığını kıyaslar. $+1.0$ noktaların ait oldukları kümeye kusursuz oturduğunu ve kümelerin net ayrıştığını gösterir.

</details>

---
"""

def get_section_6():
    return r"""## BÖLÜM 6: Hafta 06 – Yapay Sinir Ağları (YSA), Perceptron, XOR ve MLP Mimarisi

### Soru 95 (Eşleştirme): Biyolojik vs. Yapay Nöron Eşleşmesi
Aşağıdaki biyolojik nöron bileşenlerini yapay nöron matematiksel karşılıklarıyla eşleştiriniz:
1. Dendritler
2. Sinapslar
3. Hücre Gövdesi (Soma)
4. Akson

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* 1. **Dendritler** $\rightarrow$ **Girdi Değerleri ($x_1, x_2, \dots, x_n$)**
* 2. **Sinapslar** $\rightarrow$ **Bağlantı Ağırlıkları ($w_1, w_2, \dots, w_n$)**
* 3. **Hücre Gövdesi (Soma)** $\rightarrow$ **Ağırlıklı Toplam ($z = \sum w_i x_i + b$)**
* 4. **Akson** $\rightarrow$ **Aktivasyon Fonksiyonu ve Çıktı ($a = f(z)$)**

</details>

---

### Soru 96 (Kavramsal): Bias (Kesen) Teriminin Rolü
Bir yapay nöronda bias ($b$) terimi kullanılmazsa ($z = w^T x$) nöronun karar verme yeteneği nasıl kısıtlanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Bias terimi olmadığında karar doğrusu/düzlemi **orijinden ($(0, 0)$ noktasından) geçmek zorundadır**.
* Bias ($b$), karar sınırını uzayda serbestçe sağa, sola, yukarı veya aşağı kaydırma esnekliği sağlar; böylece orijinden geçmeyen sınıflar da ayrılabilir.

</details>

---

### Soru 97 (Sayısal Nöron Hesabı - SLAYTLARDAN): Tek Nöron Çıktısı
Girdileri $x = [2, -1, 3]$, ağırlıkları $w = [0.5, 1, -0.5]$ ve bias değeri $b = 1$ olan bir yapay nöronun aktivasyon fonksiyonu ReLU ise çıktısı kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Ağırlıklı Toplam ($z$):**
   $$z = (2 \times 0.5) + (-1 \times 1) + (3 \times -0.5) + 1$$
   $$z = 1.0 - 1.0 - 1.5 + 1.0 = -0.5$$
2. **ReLU Aktivasyonu:**
   $$\text{Çıktı} = \max(0, z) = \max(0, -0.5) = \mathbf{0}$$

</details>

---

### Soru 98 (Çoktan Seçmeli): Frank Rosenblatt Perceptron Modeli
1958 yılında geliştirilen orijinal Perceptron modeli hangi aktivasyon fonksiyonunu kullanıyordu?
A) ReLU
B) Sigmoid
C) Basamak Fonksiyonu (Heaviside Step Function)
D) Softmax
E) Tanh

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: C**
* **Açıklama:** Orijinal Perceptron $z \ge 0$ ise 1, $z < 0$ ise 0 üreten ikili basamak fonksiyonunu kullanıyordu.

</details>

---

### Soru 99 (Kavramsal): Doğrusal Ayrılabilirlik (AND ve OR)
Tek bir yapay nöron (Perceptron) neden Mantıksal AND ve OR kapılarını öğrenebilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* AND ve OR kapılarının doğruluk tabloları 2 boyutlu koordinat düzlemine çizildiğinde; 1 çıktıları ile 0 çıktıları arasına **tek bir düz doğru çekilerek** birbirinden tamamen ayrılabilir (Doğrusal Ayrılabilirlik / Linear Separability).

</details>

---

### Soru 100 (Kavramsal - BANKO): XOR Çıkmazı ve 1. Yapay Zekâ Kışı
Minsky ve Papert'in 1969 tarihli *"Perceptrons"* kitabı neden yapay sinir ağları araştırmalarının 10 yıl boyunca durmasına (1. YZ Kışı) yol açmıştır? Çözümü nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Sorun:** Tek katmanlı bir Perceptron'un mantıksal XOR (Özel VEYA) problemini matematiksel olarak asla ayıramayacağını ispatlamışlardır. Çünkü XOR düzlemde çapraz yerleşir ve tek bir düz doğruyla ayrılamaz (Doğrusal Ayrılamaz).
2. **Çözüm:** Araya en az bir **Gizli Katman (Hidden Layer)** ve doğrusal olmayan aktivasyonlar ekleyerek uzayı bükmektir (**Çok Katmanlı Algılayıcı - MLP**).

</details>

---

### Soru 101 (Çoktan Seçmeli): Gizli Katmanların Fonksiyonu
Çok Katmanlı Algılayıcıda (MLP) girdi ile çıktı arasına eklenen gizli katmanların (*Hidden Layers*) matematiksel rolü nedir?
A) Yalnızca modelin çalışma süresini artırmak
B) Orijinal girdi uzayını doğrusal olmayan biçimde bükerek sınıfları son katmanda doğrusal olarak ayrılabilir hale getirmek
C) Veri setindeki eksik sütunları silmek
D) Tüm ağırlıkları sıfırlamak
E) Sınıf sayısını azaltmak

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Gizli katmanlar öznitelikleri yeni bir uzaya taşır. Düşük boyutta doğrusal ayrılamayan karmaşık problemler (XOR gibi), gizli katmanların temsili sayesinde doğrusal ayrılabilir hale gelir.

</details>

---

### Soru 102 (İspat / Kavramsal - BANKO): Doğrusal Olmayan Aktivasyon Zorunluluğu
Yapay sinir ağlarında eğer tüm gizli katmanlarda doğrusal aktivasyon ($f(z) = z$) kullanılsaydı ne olurdu? İki katmanlı bir ağ için matematiksel olarak ispatlayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **İspat:**
  1. Katman 1 Çıktısı: $\mathbf{h}_1 = \mathbf{W}_1 \mathbf{x} + \mathbf{b}_1$
  2. Katman 2 Çıktısı: $\hat{\mathbf{y}} = \mathbf{W}_2 \mathbf{h}_1 + \mathbf{b}_2$
  3. $\mathbf{h}_1$'i yerine koyalım:
     $$\hat{\mathbf{y}} = \mathbf{W}_2 (\mathbf{W}_1 \mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2 = (\mathbf{W}_2 \mathbf{W}_1) \mathbf{x} + (\mathbf{W}_2 \mathbf{b}_1 + \mathbf{b}_2)$$
  4. İki matrisin çarpımı ($\mathbf{W}_2 \mathbf{W}_1$) yeni bir matristir ($\mathbf{W}'$), parantez içi de yeni bir vektördür ($\mathbf{b}'$):
     $$\hat{\mathbf{y}} = \mathbf{W}' \mathbf{x} + \mathbf{b}'$$
* **Sonuç:** Ağ 100 katmandan da oluşsa matematiksel olarak tek bir basit doğrusal regresyona çöker! Ağa temsil gücü kazandıran unsur **doğrusal olmayan (non-linear) aktivasyonlardır**.

</details>

---

### Soru 103 (Çoktan Seçmeli): Sigmoid Aktivasyonunun Kısıtı
Derin yapay sinir ağlarının gizli katmanlarında Sigmoid aktivasyon fonksiyonunun terk edilmesinin temel sebebi nedir?
A) Çıktısının çok büyük sayılar üretmesi
B) Pozitif ve negatif uç bölgelerde doymaya (*saturation*) uğraması ve türevinin sıfıra yaklaşarak **Kaybolan Gradyan (Vanishing Gradient)** sorununa yol açması
C) İkili sınıflandırmada kullanılamaması
D) Kodlanmasının imkânsız olması
E) Çok yavaş türev alınması

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Sigmoid'in türevi en fazla 0.25'tir. Derin ağlarda geriye doğru gidildikçe 0.25'ler çarpılarak ilk katmanlarda gradyan sıfırlanır ve ağ öğrenmeyi durdurur.

</details>

---

### Soru 104 (Çoktan Seçmeli): Tanh vs. Sigmoid
Hiperbolik Tanjant ($\tanh(z)$) fonksiyonunun Sigmoid'e göre en büyük avantajı nedir?
A) Pozitif bölgede türevinin 1 olması
B) Çıktısının $[-1, +1]$ aralığında ve **sıfır merkezli (zero-centered)** olması; böylece ağırlık güncellemelerinin zikzak yapmasını azaltması
C) Hiçbir zaman doymaya uğramaması
D) Parametre sayısını yarıya indirmesi
E) Negatif değer almaması

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Sigmoid daima pozitif $(0, 1)$ üretir; bu da gradyanların aynı yönde akmasına neden olur. Tanh ise $(-1, 1)$ üreterek sıfır merkezli bir dağılım sunar.

</details>

---

### Soru 105 (Çoktan Seçmeli): ReLU'nun Üstünlüğü
Düzeltilmiş Doğrusal Birim (ReLU - $\max(0, z)$) aktivasyon fonksiyonunun derin öğrenmede devrim yaratmasının temel matematiksel sebebi nedir?
A) Her noktada ikinci türevinin alınabilmesi
B) Pozitif bölgede ($z > 0$) türevinin daima sabit **$1.0$** olması sayesinde gradyanın gücünü kaybetmeden ilk katmanlara kadar akabilmesi
C) Negatif sayıları ikiye katlaması
D) Parametre sayısını azaltması
E) Çıktıların toplamını 1 yapması

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $z > 0$ iken $\text{ReLU}'(z) = 1$'dir. 1 ile çarpılan gradyan zayıflamaz; bu sayede kaybolan gradyan problemi çözülmüş ve yüzlerce katmanlı derin ağlar eğitilebilir hale gelmiştir.

</details>

---

### Soru 106 (Kavramsal): Ölen ReLU (Dying ReLU) Problemi
"Ölen ReLU" (*Dying ReLU*) problemi nedir ve **Leaky ReLU** bu sorunu nasıl çözer?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Sorun:** Bir nöron büyük bir negatif gradyan adımı alıp tüm eğitim verisi için $z < 0$ bölgesine düşerse, ReLU çıktısı 0 ve türevi 0 olur. O nöron bir daha asla güncellenemez ve "ölür".
2. **Leaky ReLU Çözümü:** Negatif bölgede çıktıyı tam sıfır yapmak yerine küçük bir eğim verir:
   $$f(z) = \max(\alpha z, z) \quad (\alpha \approx 0.01)$$
   Böylece negatif bölgede de küçük bir gradyan akar ($0.01$) ve nöronun canlanma şansı korunur.

</details>

---

### Soru 107 (Sayısal Parametre - SLAYTLARDAN): Dense Parametre Sayısı
100 nöronlu bir katmandan 50 nöronlu tam bağlantılı (Dense) bir katmana geçişte kaç adet öğrenilebilir parametre (ağırlık + bias) vardır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Ağırlıklar:** $100 \times 50 = 5.000$
2. **Bias Terimleri:** Her çıkış nöronu için 1 bias $\implies 50$
3. **Toplam Parametre:** $5.000 + 50 = \mathbf{5.050}$

</details>

---

### Soru 108 (Sayısal Parametre): MNIST MLP Parametre Sayısı
$28 \times 28$ piksellik MNIST görüntüleri için tasarlanan $784 - 128 - 10$ mimarisine sahip tam bağlantılı bir ağda toplam kaç öğrenilebilir parametre vardır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Katman 1 (Girdi $\rightarrow$ Gizli):**
   $$(784 \times 128) + 128 = 100.352 + 128 = 100.480$$
2. **Katman 2 (Gizli $\rightarrow$ Çıkış):**
   $$(128 \times 10) + 10 = 1.280 + 10 = 1.290$$
3. **Ağın Toplam Parametresi:**
   $$100.480 + 1.290 = \mathbf{101.770}$$

</details>

---

### Soru 109 (Kavramsal): Sıfır Başlatma Hatası
Bir yapay sinir ağındaki tüm ağırlıklar eğitime başlarken tam olarak sıfır ($W = 0$) olarak başlatılırsa ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Simetri Sorunu (*Symmetry Breaking Failure*):** Aynı katmandaki tüm nöronlar aynı girdileri alır, aynı ağırlıklı toplamı ($0$) üretir ve geri yayılımda aynı gradyanı hesaplar.
* Tüm nöronlar aynı değeri öğrenir; katmandaki 100 nöron tek bir nöron gibi davranır. Bu yüzden ağırlıklar küçük rastgele sayılarla (He veya Xavier başlatma) başlatılmalıdır.

</details>

---

### Soru 110 (Çoktan Seçmeli): He ve Xavier Başlatma
ReLU aktivasyonu kullanan derin ağlarda ağırlıkların standart sapmasını katmanın girdi boyutuna göre ayarlayan en uygun başlatma yöntemi hangisidir?
A) Sıfır Başlatma
B) Sabit 1 Başlatma
C) He (Kaiming) Başlatma ($\text{Var}(W) = \frac{2}{N_{in}}$)
D) Negatif Başlatma
E) Rasgele Büyük Sayılarla Başlatma

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: C**
* **Açıklama:** ReLU pozitif bölgede varyansı yarıya düşürdüğü için Kaiming He (2015) varyansı $2/N_{in}$ olarak ölçeklemiş ve derin ağların sinyal kaybı yaşamadan başlamasını sağlamıştır.

</details>

---

### Soru 111 (Tablo): Problem Türü ve Çıkış Eşleşmesi
Aşağıdaki problem türleri için çıkış katmanı nöron sayısını, aktivasyon fonksiyonunu ve kayıp fonksiyonunu yazınız:
1. Bir evin piyasa satış fiyatının tahmini
2. Bir hastanın diyabet olup olmadığının (0 veya 1) tahmini
3. 10 farklı hayvan türü arasından tek bir hayvanın sınıflandırılması

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Regresyon:** 1 nöron | Doğrusal (None) | Ortalama Kare Hata (MSE)
2. **İkili Sınıflandırma:** 1 nöron | **Sigmoid** | İkili Çapraz Entropi (BCE)
3. **Çok Sınıflı Sınıflandırma:** 10 nöron | **Softmax** | Kategorik Çapraz Entropi (CCE)

</details>

---

### Soru 112 (Kavramsal): Evrensel Yaklaşım Teoremi
Evrensel Yaklaşım Teoremi (*Universal Approximation Theorem*) tek bir gizli katmana sahip yapay sinir ağları hakkında ne söyler ve pratikte neden derin ağlar tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Teorem:** Doğrusal olmayan aktivasyona ve yeterli sayıda nörona sahip tek bir gizli katmanlı MLP, herhangi bir sürekli matematiksel fonksiyona istenen hassasiyette yaklaşabilir.
2. **Pratikte Neden Derin Ağlar?** Tek katmanla bu yaklaşımı yapmak astronomik sayıda (trilyonlarca) nöron gerektirir. Katmanları derinleştirmek (derin ağlar), öznitelikleri hiyerarşik olarak soyutladığı için katbekat daha az parametreyle çok daha karmaşık problemleri çözer.

</details>

---

### Soru 113 (Doğru / Yanlış - Gerekçeli): Nöron Sayısı ve Overfitting
**İfade:** *"Bir MLP ağındaki gizli katman sayısını ve nöron sayısını artırmak modelin ezberleme (overfitting) riskini artırır."*
Bu ifade Doğru mudur, Yanlış mıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **DOĞRUDUR.**
* **Gerekçe:** Parametre sayısı arttıkça modelin serbestlik derecesi ve kapasitesi büyür; verideki gürültüleri ve aykırı noktaları ezberleme yeteneği artar.

</details>

---

### Soru 114 (Vaka Analizi): Giriş Katmanı Boyutu
$64 \times 64$ boyutundaki 3 kanallı (RGB) renkli fotoğrafları klasik bir MLP ağına girdi olarak vermek için giriş katmanında kaç adet nöron bulunmalıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Klasik MLP tek boyutlu vektör girdi kabul eder.
* Görüntüdeki toplam piksel değeri:
  $$\text{Girdi Nöron Sayısı} = 64 \times 64 \times 3 = \mathbf{12.288\text{ Nöron}}$$

</details>

---
"""
