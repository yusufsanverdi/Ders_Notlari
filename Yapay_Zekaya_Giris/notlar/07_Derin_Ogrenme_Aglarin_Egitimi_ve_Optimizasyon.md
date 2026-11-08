# Bölüm 07: Derin Ağların Eğitimi, Geri Yayılım ve Optimizasyon

---

## 🚨 HOCANIN VİZE SINAVI UYARILARI VE KRİTİK İPUÇLARI

> [!IMPORTANT]
> **Vize Sınavı Odak Noktaları:**
> * **BANKO SORU - Softmax ve Çıkış Katmanı:**
>   - Çok sınıflı problemlerde çıkış katmanında neden Softmax kullanılır?
>   - *Cevap:* Çıkış değerlerini toplamı **tam olarak 1.0 olan** bir olasılık dağılımına dönüştürür.
>   - *Slaytlardaki Sayısal Soru:* Doğru sınıfa 0.5 olasılık veren bir modelin kategorik çapraz entropi kaybı kaçtır?
>     $$L = -\ln(\hat{p}_{doğru}) = -\ln(0.5) \approx \mathbf{0.693}$$
> * **HOCANIN DERSTE SORDUĞU SORU: Epoch Nedir?**
>   - *Cevap:* Eğitim veri setindeki tüm verilerin yapay sinir ağından **bir tam geçiş (ileri ve geri yayılım)** yapmasıdır.
> * **HOCANIN DERSTE SORDUĞU SORU: Batch Size (Yığın Boyutu) Nedir?**
>   - *Cevap:* Modelin ağırlıklarını güncellemeden önce tek seferde belleğe (GPU'ya) alınan ve işlenen örnek sayısıdır. 
>   - *Hesaplama:* 10.000 veri, Batch Size = 100 ise $\implies$ 1 Epoch'ta **100 adım (iterasyon)** yapılır.
> * **SAYISAL SORU - Geri Yayılımda ReLU Türevi (Slaytlardan):**
>   - İleri yayılımda ön aktivasyonu $z = -1.3$ olan bir ReLU nöronuna geriden $0.8$ gradyanı gelmektedir. Nöronun girdisine iletilen gradyan nedir?
>   - *Cevap:* $z < 0$ iken ReLU'nun türevi $\mathbf{0}$'dır; dolayısıyla iletilen gradyan $0.8 \times 0 = \mathbf{0}$ olur!
> * **Aşırı Öğrenmeye Karşı Savunma Yöntemleri:** Dropout (Seyreltme), Erken Durdurma (Early Stopping), Veri Artırma (Data Augmentation) ve L2 Ağırlık Azaltımı.
> * **Optimizasyon Algoritmaları:** SGD, Momentum, RMSProp ve endüstri standardı olan **Adam (Adaptive Moment Estimation)**.

---

## 1. Çok Sınıflı Çıktı: Softmax ve Kategorik Çapraz Entropi

Çok sınıflı sınıflandırma problemlerinde ağın son katmanı her bir sınıf için ham bir sayısal puan (logit - $z_k$) üretir. Bu puanlar **Softmax Fonksiyonu** ile olasılığa çevrilir:

$$P(y = k | \mathbf{z}) = \hat{p}_k = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}$$

### Softmax'ın Temel Özellikleri:
1. Üstel ($e^z$) fonksiyon kullanıldığı için en yüksek puana sahip sınıfın olasılığı belirgin biçimde öne fırlar.
2. Tüm sınıfların olasılıkları toplamı **kesinlikle 1.0'a eşittir**:
   $$\sum_{k=1}^{K} \hat{p}_k = 1.0$$

### Kategorik Çapraz Entropi (Categorical Cross-Entropy - CCE):
Doğru sınıfın birim vektörle (one-hot) gösterildiği durumda kayıp formülü:
$$L = - \sum_{k=1}^{K} y_k \ln(\hat{p}_k) = - \ln(\hat{p}_{doğru})$$
Model doğru sınıfa ne kadar yüksek olasılık verirse ($\hat{p} \rightarrow 1$), kayıp o kadar sıfıra yaklaşır ($-\ln 1 = 0$).

---

## 2. Eğitim Döngüsü (Training Loop): Dört Adımın Sonsuz Tekrarı

Bir yapay sinir ağının eğitimi, binlerce kez tekrarlanan 4 temel adımdan ibarettir:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        EĞİTİM DÖNGÜSÜ (1 ADIM)                         │
│                                                                        │
│   1. İLERİ YAYILIM     2. KAYIP HESABI    3. GERİ YAYILIM    4. GÜNCELLEME │
│    (Forward Pass)     (Loss Compute)     (Backpropagation)    (Optimizer)  │
│                                                                        │
│   X -> [ Ağ ] -> ŷ ───> L(y, ŷ) hesapla ───> dL/dW hesapla ───> W = W - η·dW│
└────────────────────────────────────────────────────────────────────────┘
```

1. **İleri Yayılım (*Forward Pass*):** Girdi yığını ($X$) ağdan geçirilir, tahminler ($\hat{y}$) üretilir.
2. **Kayıp Hesabı (*Loss Computation*):** Tahminler ile gerçek etiketler ($y$) arasındaki kayıp skoru ($L$) ölçülür.
3. **Geri Yayılım (*Backward Pass / Backpropagation*):** Zincir kuralı (*Chain Rule*) uygulanarak kaybın tüm ağırlıklara ve bias'lara göre türevi ($\frac{\partial L}{\partial \mathbf{W}}$) geriye doğru hesaplanır.
4. **Parametre Güncelleme (*Optimizer Step*):** Optimizer (Adam, SGD vb.) bu gradyanları kullanarak ağırlıkları günceller.

---

## 3. Epoch, Batch Size ve İterasyon İlişkisi

* **Epoch (Epok):** Eğitim kümesindeki her bir örneğin ağ tarafından **tam olarak 1 kez** görülmesi sürecidir. 100 epoch, verinin 100 kez baştan sona işlenmesidir.
* **Batch Size (Yığın Boyutu):** Ağırlıkları güncellemeden önce GPU'ya tek seferde verilen örnek sayısıdır (Örn: 16, 32, 64).
* **İterasyon (Adım Sayısı):** 1 epoch'un tamamlanması için gereken ağırlık güncelleme sayısıdır:
  $$\text{İterasyon Sayısı} = \frac{\text{Toplam Eğitim Örneği Sayısı}}{\text{Batch Size}}$$

> [!TIP]
> **Dr. Seda Bayat Tosun'un Dersteki Vurgusu:**
> "Batch size'ı donanım elveriyor diye 1024 gibi çok yüksek seçmek her zaman iyi değildir. Model çok büyük adımlar atar, küçük detayları kaçırır ve genelleme yeteneğini kaybederek **Overfitting'e** düşebilir. Küçük yığınlar (16, 32) gradyana hafif bir stokastik gürültü ekleyerek modelin dar yerel çukurlardan kurtulup daha iyi genelleme yapmasını sağlar."

---

## 4. Geri Yayılım (Backpropagation) ve Zincir Kuralı

Geri yayılım, kalkülüsteki **Zincir Kuralı'nın (Chain Rule)** bir hesaplama grafiği (computational graph) üzerinde verimli uygulanmasıdır:

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w}$$

Hata sinyali ağın sonundan (kayıp fonksiyonundan) başlar ve katman katman girdi katmanına doğru akar.

### Kaybolan Gradyan (Vanishing Gradient) Problemi:
Eski ağlarda gizli katmanlarda Sigmoid veya Tanh kullanılıyordu. Sigmoid'in türevi en fazla $0.25$'tir:
$$\sigma'(z) \le 0.25$$
10 katmanlı bir ağda geriye doğru gidildikçe gradyanlar birbiriyle çarpılır:
$$0.25 \times 0.25 \times \dots \times 0.25 \approx 10^{-6}$$
İlk katmanlara ulaşıldığında gradyan sıfıra o kadar yaklaşır ki, **ilk katmanlardaki ağırlıklar hiçbir şey öğrenemez (ağ donar)**.
* **ReLU Devrimi:** Pozitif bölgede $z > 0$ iken $\text{ReLU}'(z) = 1.0$'dır. Sayı 1 ile çarpıldığı için gradyan derinlik ne olursa olsun gücünü kaybetmeden ilk katmanlara kadar akar!

---

## 5. Optimizasyon Algoritmaları

1. **SGD (Stochastic Gradient Descent):** Sabit öğrenme oranıyla gradyan yönünde adım atar. Düz vadilerde salınım yapar ve çok yavaş ilerler.
2. **Momentum:** Fizikteki yuvarlanan top analojisidir. Geçmiş adımların hızını (momentum) ekler; doğru yönde hızlanır, zikzakları sönümler.
3. **RMSProp:** Her parametrenin geçmiş gradyan karelerinin hareketli ortalamasını tutar. Çok dik yönlerde adımları küçültür, sığ yönlerde adımları büyütür.
4. **Adam (Adaptive Moment Estimation):** **Modern derin öğrenmenin altın standardıdır.** Momentum ile RMSProp'un üstün yönlerini birleştirir. Hem birinci momenti (hız) hem ikinci momenti (varyans) takip ederek her parametre için öğrenme oranını otomatik ve adaptif olarak ayarlar.

---

## 6. Aşırı Öğrenmeye (Overfitting) Karşı Savunma Hattı

Derin ağlar milyonlarca parametreye sahip olduğu için eğitim verisini ezberleme eğilimindedir. Bunu engellemek için şu 4 mekanizma kullanılır:

```
[ Aşırı Öğrenme Karşıtı Savunma ]
  ├── 1. Dropout (Seyreltme)       -> Eğitimde rastgele nöronları kapatma (%20-50)
  ├── 2. Erken Durdurma (Early St.) -> Doğrulama kaybı artınca eğitimi kesme
  ├── 3. Veri Artırma (Data Aug.)   -> Görselleri döndürme, kırpma, renk değiştirme
  └── 4. L2 Ağırlık Azaltımı (Decay) -> Ağırlıkların aşırı büyümesini cezalandırma
```

### A. Dropout (Seyreltme)
* **Nasıl Çalışır?** Eğitim sırasında her ileri yayılım adımında gizli katmandaki nöronların rastgele bir yüzdesi (örneğin $p = 0.5$, yani %50'si) sıfırlanarak devre dışı bırakılır.
* **Mühendislik Mantığı:** Nöronların belirli bir diğer nörona körü körüne bağımlı olmasını (*co-adaptation*) engeller. Her nöron tek başına yararlı öznitelikler öğrenmek zorunda kalır; devasa bir model topluluğu (*ensemble*) gibi davranır.
* **Test Aşamasında:** Test sırasında hiçbir nöron kapatılmaz; tüm nöronlar aktif çalışır.

### B. Erken Durdurma (Early Stopping)
Eğitim boyunca her epoch sonunda doğrulama kümesindeki kayıp ($Loss_{val}$) izlenir. Eğitim kaybı düşmeye devam ederken doğrulama kaybı $k$ epoch boyunca üst üste artmaya başlarsa eğitim derhal durdurulur ve en düşük doğrulama kaybının alındığı ağırlıklar kaydedilir.

### C. Toplu Normalizasyon (Batch Normalization - BatchNorm)
* Her mini-yığındaki nöron çıktılarının ortalamasını 0, standart sapmasını 1 yapacak şekilde normalize eder.
* İçsel ortak değişken kaymasını (*Internal Covariate Shift*) azaltır, çok daha yüksek öğrenme oranları kullanılmasına izin verir ve eğitimi dramatik biçimde hızlandırır.

---

## 7. Özet ve Modül Kontrol Listesi

- [x] Softmax fonksiyonunun formülünü ve olasılıkların toplamının 1 olduğunu biliyorum.
- [x] Kategorik çapraz entropi kaybını $\hat{p}=0.5$ için elle hesaplayabiliyorum ($-\ln 0.5 \approx 0.693$).
- [x] Epoch, Batch Size ve İterasyon arasındaki ilişkiyi ve hesaplamasını öğrendim.
- [x] Geri yayılımda ReLU nöronunun $z < 0$ iken gradyanı sıfırladığını kavradım.
- [x] Kaybolan gradyan probleminin nedenini ve ReLU'nun bunu nasıl çözdüğünü biliyorum.
- [x] Adam optimizasyon algoritmasının Momentum ve RMSProp birleşimi olduğunu öğrendim.
- [x] Dropout, Erken Durdurma ve Batch Normalization tekniklerinin işleyişini kavradım.
