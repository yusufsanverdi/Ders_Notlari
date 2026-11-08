# Bölüm 04: Sınıflandırma Yöntemleri ve Karar Sınırları

---

## 🚨 HOCANIN VİZE SINAVI UYARILARI VE KRİTİK İPUÇLARI

> [!IMPORTANT]
> **Vize Sınavı Odak Noktaları:**
> * **Lojistik Regresyon ve Sigmoid Fonksiyonu:** $\sigma(z) = \frac{1}{1 + e^{-z}}$ formülü. $z \rightarrow +\infty$ iken $\sigma(z) \rightarrow 1$; $z \rightarrow -\infty$ iken $\sigma(z) \rightarrow 0$; $z = 0$ iken $\sigma(z) = 0.5$.
> * **İkili Çapraz Entropi (Log-Loss) Sayısal Sorusu:**
>   $$L = - \left[ y \ln(\hat{p}) + (1-y) \ln(1-\hat{p}) \right]$$
>   Örnek Sınav Sorusu: Gerçek sınıf $y = 0$ iken model $\hat{p} = 0.8$ tahmin ederse kayıp:
>   $$L = -\ln(1 - 0.8) = -\ln(0.2) \approx 1.61$$
> * **k-NN Algoritması:** $k$ parametresinin rolü. Sınav uyarısı: **"$k=1$ seçmek aşırı öğrenmeyi önler mi?"** $\implies$ **HAYIR!** $k=1$ her eğitim noktasını ezberler, gürültüyü birebir modeller ve **aşırı öğrenmeye (overfitting)** neden olur. $k$ büyüdükçe karar sınırı yumuşar.
> * **k-NN'de Ölçekleme Zorunluluğu:** Mesafe hesabına (Öklid) dayandığı için öznitelik ölçekleme yapılmazsa büyük ölçekli değişken tüm kararı domine eder.
> * **Karar Ağaçları:** Entropi ($H(S) = - \sum p_i \log_2 p_i$), Gini Kirliliği ($1 - \sum p_i^2$) ve Bilgi Kazancı (Information Gain).
> * **Naive Bayes:** Özniteliklerin birbirinden koşullu bağımsız olduğu "naif" varsayımı ile çalışır.

---

## 1. Sınıflandırma Problemi ve Karar Sınırı

Sınıflandırma; girdileri önceden tanımlanmış kesikli sınıflardan birine atama işlemidir. 
* İkili Sınıflandırma (*Binary*): 2 sınıf vardır ($y \in \{0, 1\}$).
* Çok Sınıflı Sınıflandırma (*Multiclass*): 3 veya daha fazla ayrık sınıf vardır (Kedi, Köpek, Kuş, At).

**Karar Sınırı (Decision Boundary):** Modelin girdi uzayında bir sınıf ile diğer sınıfı birbirinden ayırdığı geometrik yüzeydir. Doğrusal modeller (Lojistik Regresyon, Doğrusal SVM) düz bir doğru/düzlem çizerken; parametrik olmayan modeller (k-NN, Karar Ağaçları, MLP) kıvrımlı ve karmaşık sınırlar üretebilir.

---

## 2. Lojistik Regresyon ve Sigmoid Fonksiyonu

Lojistik Regresyon, adına rağmen bir regresyon değil; bir **ikili sınıflandırma** algoritmasıdır.

Doğrusal modelin ürettiği skoru ($z = w^T x + b \in (-\infty, +\infty)$) alıp **Sigmoid (Lojistik) Fonksiyonu** içerisinden geçirerek $[0, 1]$ aralığında bir olasılık değerine ($\hat{p}$) dönüştürür:

$$\hat{p} = \sigma(z) = \frac{1}{1 + e^{-z}}$$

```
  Sigmoid Değer Tablosu:
  z = -inf  ==>  sigma(z) = 0.0
  z = -2.0  ==>  sigma(z) ≈ 0.12
  z =  0.0  ==>  sigma(z) = 0.50  (Varsayılan Karar Eşiği)
  z = +2.0  ==>  sigma(z) ≈ 0.88
  z = +inf  ==>  sigma(z) = 1.0
```

* **Sınıf Kararı:** Genellikle standart eşik $\tau = 0.5$ alınır:
  $$\hat{y} = \begin{cases} 1, & \hat{p} \ge 0.5 \\ 0, & \hat{p} < 0.5 \end{cases}$$

---

## 3. İkili Çapraz Entropi Kaybı (Binary Cross-Entropy / Log Loss)

Doğrusal regresyondaki MSE lojistik fonksiyona uygulandığında konveks olmayan (çok sayıda yerel minimumlu) bir yüzey üretir. Bu yüzden sınıflandırmada **İkili Çapraz Entropi** kullanılır:

$$L(y, \hat{p}) = - \left[ y \ln(\hat{p}) + (1-y) \ln(1-\hat{p}) \right]$$

### Kayıp Fonksiyonunun Mekanizması:
1. **Gerçek Değer $y = 1$ ise:**
   $$L = -\ln(\hat{p})$$
   * Model $\hat{p} = 0.99$ tahmin ederse: $L = -\ln(0.99) \approx 0.01$ (Kayıp sıfıra yakın).
   * Model $\hat{p} = 0.01$ tahmin ederse: $L = -\ln(0.01) \approx 4.60$ (Ağır ceza).
2. **Gerçek Değer $y = 0$ ise:**
   $$L = -\ln(1 - \hat{p})$$
   * Model $\hat{p} = 0.80$ tahmin ederse: $L = -\ln(0.20) \approx 1.61$ (Hatalı yüksek tahmin için ceza).

---

## 4. k-En Yakın Komşu Algoritması (k-Nearest Neighbors - k-NN)

k-NN, herhangi bir parametre öğrenmeyen (*non-parametric*), eğitim aşamasında yalnızca veri noktalarını bellekte saklayan **Tembel Bir Öğrenicidir (Lazy Learner)**.

### Nasıl Çalışır?
1. Yeni gelen test noktası ($q$) ile eğitim kümesindeki tüm noktalar arasındaki mesafe (genellikle Öklid mesafesi) hesaplanır:
   $$d(x, q) = \sqrt{\sum_{i=1}^{D} (x_i - q_i)^2}$$
2. En yakın $k$ adet komşu seçilir.
3. Sınıflandırmada bu $k$ komşu arasında çoğunluk oylaması (*majority voting*) yapılır.

### $k$ Hiperparametresinin Seçimi:
* **Küçük $k$ ($k=1$):**
  * Model karar sınırını her noktanın etrafından dolanacak şekilde aşırı detaylandırır.
  * Verideki gürültü ve aykırı değerleri doğrudan ezberler $\implies$ **Aşırı Öğrenme (Overfitting / Yüksek Varyans)**.
* **Büyük $k$ ($k=50$):**
  * Karar sınırı aşırı düzleşir, yerel detaylar kaybolur.
  * Baskın olan sınıf her zaman çoğunluğu kazanır $\implies$ **Eksik Öğrenme (Underfitting / Yüksek Yanlılık)**.
* **Ölçekleme Kuralı:** Eğer öznitelikler normalize edilmezse, 10.000 TL maaş farkı 5 yaşlık farkı tamamen ezer ve komşuluk mesafesi sadece maaşa göre belirlenir. Bu yüzden **k-NN'de ölçekleme ZORUNLUDUR**.

---

## 5. Karar Ağaçları (Decision Trees)

Karar ağaçları; veriyi öznitelikler üzerinden art arda sorulan mantıksal sorularla ($x_j \le eşik$) dallara ayıran hiyerarşik modellerdir.

### En İyi Bölünmenin Seçilmesi (Düğüm Saflığı Ölçütleri):

1. **Entropi (Belirsizlik / Düzensizlik Ölçüsü):**
   $$H(S) = - \sum_{i=1}^{C} p_i \log_2(p_i)$$
   * Bir düğümdeki tüm örnekler aynı sınıftan ise (tam saf) $H(S) = 0$.
   * Örnekler sınıflara eşit dağılmışsa (tam belirsiz) $H(S) = 1.0$.

2. **Gini Kirliliği (Gini Impurity - CART Algoritması):**
   $$Gini(S) = 1 - \sum_{i=1}^{C} p_i^2$$
   * Logaritma hesabı gerektirmediği için hesaplama hızı yüksektir.

3. **Bilgi Kazancı (Information Gain):**
   $$IG(S, A) = H(S) - \sum_{v \in Değerler} \frac{|S_v|}{|S|} H(S_v)$$
   * Bölünme öncesi entropi ile bölünme sonrası alt düğümlerin ağırlıklı entropisi arasındaki farktır. **En yüksek bilgi kazancını sağlayan öznitelik kök veya karar düğümü olarak seçilir.**

---

## 6. Naive Bayes ve Destek Vektör Makineleri (SVM)

### A. Naive Bayes Sınıflandırıcısı
Bayes Teoremi'ne dayanır:
$$P(y|X) = \frac{P(X|y) P(y)}{P(X)}$$
* **Neden "Naif" (Naive)?** Verideki tüm özniteliklerin verilen sınıf koşulu altında birbirinden **tamamen bağımsız olduğunu varsayar** ($P(x_1, x_2|y) = P(x_1|y) P(x_2|y)$).
* Gerçek hayatta bu bağımsızlık varsayımı çoğunlukla tutmaz; buna rağmen metin sınıflandırma ve spam filtrelemede şaşırtıcı derecede hızlı ve etkilidir.

### B. Destek Vektör Makineleri (Support Vector Machines - SVM)
* Sınıflar arasına sadece rastgele bir ayırıcı doğru çekmekle kalmaz; iki sınıf arasındaki **Marjı (Margin - Boşluğu) maksimize eden** en ideal hiperdüzlemi bulur.
* Sınıra en yakın olan ve hiperdüzlemin konumunu belirleyen kritik sınır noktalarına **Destek Vektörleri (Support Vectors)** denir.
* Doğrusal ayrılamayan problemlerde veriyi daha yüksek bir boyuta eşleyen **Çekirdek Hilesi (Kernel Trick - RBF, Polinom)** kullanılır.

---

## 7. Özet ve Modül Kontrol Listesi

- [x] Lojistik regresyonun Sigmoid fonksiyonunu ($\sigma(z) = \frac{1}{1 + e^{-z}}$) ve $[0, 1]$ olasılık dönüşümünü kavradım.
- [x] İkili Çapraz Entropi kaybını $y=0$ ve $y=1$ senaryolarında sayısal olarak hesaplayabiliyorum.
- [x] k-NN algoritmasında $k=1$ seçiminin aşırı öğrenmeye (overfitting) yol açtığını ve ölçeklemenin hayati olduğunu öğrendim.
- [x] Karar ağaçlarında Entropi, Gini Kirliliği ve Bilgi Kazancı kavramlarının rolünü biliyorum.
- [x] Naive Bayes'in bağımsızlık varsayımını ve SVM'in marj maksimizasyonu mantığını açıklayabiliyorum.
