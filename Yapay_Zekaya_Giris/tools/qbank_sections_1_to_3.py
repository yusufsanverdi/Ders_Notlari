# Sections 1 to 3: Weeks 1 to 3 (Questions 1 to 54)

def get_section_1():
    return r"""## BÖLÜM 1: Hafta 01 – Yapay Zekâya Giriş, Tarihçe, Turing Testi ve Paradigmalar

### Soru 1 (Çoktan Seçmeli): Turing Testi ve Taklit Oyunu
Alan Turing'in 1950 yılında önerdiği "Taklit Oyunu"na (Turing Testi) göre bir makine ne zaman testi başarıyla geçmiş ve "düşünebilme yetisine sahip" kabul edilir?
A) Satranç oyununda dünya şampiyonunu yendiğinde
B) İnsan sorgulayıcı, görmediği iki ayrı odadan gelen yazılı yanıtlara bakarak hangisinin insan hangisinin makine olduğunu güvenilir biçimde ayırt edemediğinde
C) Kendisine verilen 1000 soruluk bilgi yarışmasında tüm soruları hatasız yanıtladığında
D) Kendi kaynak kodunu harici müdahaleye gerek kalmadan yeniden derleyebildiğinde
E) İnsan beynindeki tüm biyolojik nöron bağlantılarını fiziksel olarak simüle ettiğinde

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Turing Testi, zekânın felsefi tanımıyla uğraşmak yerine operasyonel bir kriter getirir: Bir sorgulayıcı (insan hakem), göremediği iki tarafla (biri insan, diğeri makine) yalnızca metin üzerinden yazışır. Sorgulayıcı hangisinin insan hangisinin makine olduğunu ayırt edemezse (%50 rastgele tahmin düzeyine inerse), makine testi geçmiş sayılır.

</details>

---

### Soru 2 (Senaryo / Eşleştirme): Yapay Zekâ Türleri
Aşağıdaki 3 yapay zekâ uygulamasını kapsamlarına göre **Dar (Zayıf) YZ**, **Genel (Güçlü / AGI) YZ** veya **Süper YZ (ASI)** olarak sınıflandırınız:
1. Yalnızca MR görüntülerinden beyin tümörünü %98 doğrulukla tespit eden fakat satranç oynayamayan bir derin öğrenme modeli.
2. Bir tıp doktoru gibi ameliyat yapabilen, aynı zamanda hukuk davalarında savunma hazırlayıp şiir yazabilen ve yeni bilimsel teoriler üreten insan dengi bir sistem.
3. İnsan ırkının tüm bilişsel, sanatsal ve bilimsel kapasitesini trilyonlarca kat aşan varsayımsal zekâ düzeyi.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Dar (Zayıf) Yapay Zekâ (Narrow AI):** Tek bir özel görevde uzmanlaşmıştır. (Günümüzde kullanılan tüm YZ sistemleri bu gruptadır).
2. **Genel (Güçlü) Yapay Zekâ (General AI / AGI):** İnsan zekâsı gibi disiplinler arası öğrenme ve genelleme yeteneğine sahiptir. (Geliştirilme aşamasındadır).
3. **Süper Yapay Zekâ (Super AI / ASI):** İnsan zekâsının ötesine geçen varsayımsal düzeydir.

</details>

---

### Soru 3 (Çoktan Seçmeli): YZ Hiyerarşisi
Yapay zekâ disiplinleri arasındaki hiyerarşik ilişkiyi gösteren aşağıdaki ifadelerden hangisi **DOĞRUDUR**?
A) $Makine\ Öğrenmesi \supset Yapay\ Zekâ \supset Derin\ Öğrenme$
B) $Yapay\ Zekâ \supset Makine\ Öğrenmesi \supset Derin\ Öğrenme \supset Üretken\ YZ\ (LLM)$
C) $Derin\ Öğrenme \supset Makine\ Öğrenmesi \supset Yapay\ Zekâ$
D) $Yapay\ Zekâ \supset Derin\ Öğrenme \supset Makine\ Öğrenmesi$
E) Makine Öğrenmesi ile Derin Öğrenme birbirinden tamamen bağımsız ve kesişmeyen iki ayrı kümedir.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Yapay Zekâ en geniş kümedir (kural tabanlı uzman sistemleri de içerir). Makine Öğrenmesi onun bir alt kümesidir. Derin Öğrenme, çok katmanlı yapay sinir ağlarını kullanan bir ML alt dalıdır. Üretken YZ (LLM) ise en içteki güncel çekirdektir.

</details>

---

### Soru 4 (Kavramsal Karşılaştırma): Geleneksel Programlama vs. Makine Öğrenmesi
Geleneksel kural tabanlı yazılım geliştirme paradigması ile Makine Öğrenmesi paradigması arasındaki temel girdi-çıktı farkını formüle ediniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Geleneksel Programlama:**
   $$\text{Veri} + \text{Kurallar (Mühendisin Yazdığı Kod)} \implies \text{Cevaplar (Çıktı)}$$
2. **Makine Öğrenmesi (ML):**
   $$\text{Veri} + \text{Cevaplar (Etiketler)} \implies \text{Kurallar (Eğitilmiş Model)}$$
* Mühendis kuralları elle yazamaz; model veri ile cevap arasındaki istatistiksel ilişkiyi öğrenerek kuralı (model ağırlıklarını) kendi üretir.

</details>

---

### Soru 5 (Soru-Cevap / Mitchell Tanımı): Mitchell'in Makine Öğrenmesi Tanımı
Tom Mitchell'in (1997) matematiksel makine öğrenmesi tanımında yer alan **Görev ($T$)**, **Deneyim ($E$)** ve **Performans Ölçütü ($P$)** bileşenlerini bir **Otonom Araç Şerit Takip Sistemi** için tanımlayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Görev ($T$ - Task):** Kamera görüntüsünden yol şerit çizgilerini tespit etmek ve direksiyon açısını belirlemek.
* **Deneyim ($E$ - Experience):** Farklı hava ve ışık koşullarında kaydedilmiş milyonlarca kilometrelik sürüş videosu ve insan sürücü direksiyon verisi.
* **Performans Ölçütü ($P$ - Performance):** Şeritte kalma yüzdesi ve şerit ihlali başına düşen kilometre sayısı.

</details>

---

### Soru 6 (Tablo / Senaryo): PEAS Modeli
Bir **Akıllı Süpürge Robotu** için PEAS bileşenlerini eksiksiz doldurunuz:

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Performans ($P$):** Temizlenen alanın yüzdesi, tüketilen elektrik/pil miktarı, temizlik süresi, eşyalara çarpmama.
* **Ortam ($E$):** Oda zeminleri (halı, parke), mobilyalar, kablolar, merdiven boşlukları, evcil hayvanlar.
* **Eyleyiciler ($A$):** Tekerlek motorları, fırça motoru, vakum emiş motoru, sesli uyarı hoparlörü.
* **Algılayıcılar ($S$):** Lidar sensörü, çarpışma sensörleri, uçurum (düşme önleyici) kızılötesi sensörleri, toz haznesi doluluk sensörü.

</details>

---

### Soru 7 (Çoktan Seçmeli): Derin Öğrenmeyi Başlatan 3 Etken
Derin öğrenmenin 1980'lerde değil de 2010'lu yıllardan sonra devrimsel bir patlama yaşamasını sağlayan üç temel faktör hangisidir?
A) Kuantum bilgisayarlar, C dili, Lisp işlemcileri
B) Büyük Veri (ImageNet), GPU'ların Paralel İşlem Gücü, Algoritmik Gelişmeler (ReLU, Dropout, Adam)
C) Mikroişlemcilerin küçülmesi, nesne yönelimli programlama, ilişkisel veritabanları
D) İnternet hızının artması, uzman sistemlerin başarısı, mekanik robotlar
E) Prolog dili, mantıksal çıkarım motorları, sembolik yapay zekâ

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Yapay sinir ağlarının matematiksel temeli bilinmekteydi; ancak bunları eğitecek milyonlarca etiketli veri (Büyük Veri), matris çarpımlarını yapacak binlerce çekirdekli donanım (GPU) ve gradyan kaybolmasını çözen algoritmalar (ReLU) 2010'larda bir araya gelmiştir.

</details>

---

### Soru 8 (Çoktan Seçmeli): $A^*$ Arama Algoritması
$A^*$ arama algoritmasında bir $n$ düğümünün toplam maliyetini hesaplayan fonksiyon $f(n) = g(n) + h(n)$ olarak tanımlanır. Buradaki $g(n)$ ve $h(n)$ terimleri neyi ifade eder?
A) $g(n)$: Hedefe kalan tahmini maliyet; $h(n)$: Başlangıçtan $n$'ye kadar olan gerçek maliyet
B) $g(n)$: Başlangıçtan $n$'ye kadar harcanan gerçek maliyet; $h(n)$: $n$'den hedefe kalan sezgisel (heuristic) tahmini maliyet
C) $g(n)$: Düğümün derinliği; $h(n)$: Grafikteki toplam düğüm sayısı
D) $g(n)$: Algoritmanın çalışma süresi; $h(n)$: Bellek karmaşıklığı
E) $g(n)$: En kısa yol; $h(n)$: En uzun yol

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $g(n)$ başlangıçtan o ana kadar kat edilen kesin maliyettir. $h(n)$ ise o düğümden hedefe ulaşmak için gereken sezgisel (tahmini) maliyettir. $A^*$ algoritması $f(n) = g(n) + h(n)$ toplamını en küçük yapan düğümü öncelikli açar.

</details>

---

### Soru 9 (Vaka Analizi): Yapay Zekâda İnsan Faktörü ve Gizlilik
Büyük Dil Modellerinde (LLM) kullanıcıların girdiği verilerin denetlenmesi ve "Fiş hâlâ bizim elimizde" prensibi ne anlama gelmektedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Veri Gizliliği:** Kullanıcıların girdiği promptlar ve özel bilgiler, model geliştiricileri tarafından insan geri bildirimiyle takviyeli öğrenme (RLHF) aşamasında denetçilerin önüne düşebilir; bu nedenle mahrem ve kritik şifreler paylaşılmamalıdır.
2. **İnsan Faktörü:** YZ modelleri bağımsız iradeye sahip sihirli varlıklar değildir; veri setlerini hazırlayan, modellerin mimarisini çizen, güvenlik sınırlarını belirleyen ve gerektiğinde fişi çekecek olan insan mühendislerdir.

</details>

---

### Soru 10 (Çoktan Seçmeli): Russell ve Norvig'in 4 Yaklaşımı
Russell ve Norvig'e göre modern yapay zekâ araştırmalarının en çok benimsediği ve odaklandığı yaklaşım hangisidir?
A) İnsan gibi düşünen sistemler
B) İnsan gibi davranan sistemler
C) Rasyonel (akılcı) davranan sistemler (Rasyonel Ajan)
D) Felsefi düşünen sistemler
E) Yalnızca kural ezberleyen sistemler

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: C**
* **Açıklama:** Modern yapay zekâ, insan gibi hata yapabilen veya duygusal davranan sistemler yerine; verilen hedef doğrultusunda beklenen başarıyı matematiksel olarak maksimize eden "Rasyonel Ajan" (Rational Agent) yaklaşımını benimser.

</details>

---

### Soru 11 (Tarihçe / Kısa Cevap): Dartmouth Konferansı
"Yapay Zekâ" (Artificial Intelligence) terimi ilk kez hangi yıl ve hangi tarihi konferansta resmen literatüre kazandırılmıştır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Yıl ve Konferans:** **1956 yılı Dartmouth Konferansı**.
* John McCarthy, Marvin Minsky, Claude Shannon ve Nathaniel Rochester tarafından organize edilmiş ve yapay zekâ bağımsız bir akademik disiplin olarak kabul edilmiştir.

</details>

---

### Soru 12 (Kavramsal): Uzman Sistemlerin Çöküşü
1980'lerde popüler olan Kural Tabanlı Uzman Sistemler (*Expert Systems*) neden tıkanmış ve ikinci Yapay Zekâ Kışı'na yol açmıştır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Ölçeklenemezlik:** İnsan bilgisini on binlerce `if-else` kuralı halinde elle sisteme aktarmak imkânsız hale gelmiştir.
2. **Kırılganlık:** Kurallar en küçük bir belirsizlikte veya istisnai durumda çökmüş, yeni durumlara uyum sağlayamamıştır.
3. **Öğrenme Eksikliği:** Sistem veriden kendi kendine öğrenme yeteneğine sahip olmadığı için bakım maliyetleri karşılanamaz hale gelmiştir.

</details>

---

### Soru 13 (Eşleştirme): Medikal Teşhis Sistemi PEAS Analizi
Bir otomatik medikal teşhis yapay zekâsı için PEAS bileşenlerini eşleştiriniz:
1. Röntgen filmi tarayıcısı ve kan tahlili sayısal çıktısı
2. Doğru teşhis oranı ve yanlış alarmın minimize edilmesi
3. Ekrana yazdırılan tedavi önerisi ve reçete taslağı
4. Hasta, hastane veritabanı ve laboratuvar

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* 1 $\rightarrow$ **Sensörler (Algılayıcılar - S)**
* 2 $\rightarrow$ **Performans Ölçütü (P)**
* 3 $\rightarrow$ **Eyleyiciler (Actuators - A)**
* 4 $\rightarrow$ **Ortam (Environment - E)**

</details>

---

### Soru 14 (Doğru / Yanlış - Gerekçeli): Turing Testi ve ASI
**İfade:** *"Turing Testi'ni başarıyla geçen bir yapay zekâ sistemi mutlaka Süper Yapay Zekâ (ASI) düzeyine ulaşmış demektir."*
Bu ifade Doğru mudur, Yanlış mıdır? Gerekçesiyle açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** Turing Testi insan zekâsını taklit etme yeteneğini ölçer. Bir sistem insan gibi esprili yanıtlar verip metin üzerinden hakemi kandırabilir; ancak bu durum onun tüm bilimsel ve bilişsel alanlarda insanlığı katbekat aşan bir "Süper Yapay Zekâ" olduğu anlamına gelmez.

</details>

---

### Soru 15 (Sayısal Mantık): Mitchell Tanımını Satranca Uygulamak
Deep Blue satranç motoru için Mitchell'in $T, E, P$ üçlüsünü yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Görev ($T$):** Satranç tahtasında hamle yapmak ve şah-mat hedefine ulaşmak.
* **Deneyim ($E$):** Büyükustaların oynadığı binlerce tarihi maç kaydı veya kendi kendine oynadığı oyunlar.
* **Performans ($P$):** Usta oyunculara karşı kazanılan maçların yüzdesi veya ELO satranç puanı.

</details>

---

### Soru 16 (Çoktan Seçmeli): Üretken YZ (GenAI) vs. Ayırt Edici YZ (Discriminative AI)
Aşağıdaki ikililerden hangisinde ilk sistem "Ayırt Edici", ikinci sistem "Üretken" yapay zekâya örnektir?
A) ChatGPT — Spam Filtresi
B) ResNet Görüntü Sınıflandırıcı — Midjourney Görsel Üreteci
C) Stable Diffusion — Claude Metin Modeli
D) K-Means Kümeleme — PCA Boyut İndirgeme
E) Doğrusal Regresyon — Lojistik Regresyon

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** ResNet girdi olarak aldığı fotoğrafı "Kedi/Köpek" diye sınıflandırır (Ayırt Edici - $P(Y|X)$). Midjourney ise sıfırdan yeni pikseller ve sanat eseri üretir (Üretken - $P(X)$).

</details>

---

### Soru 17 (Doğru / Yanlış - Gerekçeli): ML ve Yapay Zekâ Kapsamı
**İfade:** *"Tüm yapay zekâ sistemleri makine öğrenmesi algoritmalarını kullanmak zorundadır."*
Bu ifade Doğru mudur, Yanlış mıdır? Gerekçesini belirtiniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** Kural tabanlı uzman sistemler, $A^*$ arama algoritmaları, Minimax oyun ağacı aramaları ve karar tabloları veriden öğrenmez; insan tarafından tanımlanmış mantıksal kurallarla çalışır. Bu sistemler Yapay Zekâdır fakat Makine Öğrenmesi değildir.

</details>

---

### Soru 18 (Vaka Analizi): Otonom Sistemlerde Etik ve Mühendislik
Bir otonom aracın önüne aniden çıkan yayaya çarpmamak için direksiyonu kırıp duvara çarpması ve yolcunun yaralanması senaryosunda (Trolley Problemi), yazılım mühendisinin etik ve yasal sorumluluğu nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. Mühendisler algoritmaların karar alma mekanizmalarını şeffaf, test edilebilir ve uluslararası emniyet standartlarına (ISO 26262 vb.) uygun tasarlamalıdır.
2. Modellerin ayrımcılık yapmasını (yaş, cinsiyet önyargısı) engelleyecek denetim mekanizmaları kurulmalıdır.
3. Kritik sistemlerde karar sorumluluğu algoritmaya değil; tasarımı yapan üretici ve denetleyici kurumlara aittir.

</details>

---
"""

def get_section_2():
    return r"""## BÖLÜM 2: Hafta 02 – Makine Öğrenmesinin Temelleri, Yaşam Döngüsü ve Veri Ön İşleme

### Soru 19 (Senaryo / Eşleştirme): Öğrenme Türlerini Ayırt Etme
Aşağıdaki 4 farklı mühendislik problemini **Denetimli (Sınıflandırma/Regresyon)**, **Denetimsiz** veya **Pekiştirmeli** öğrenme olarak eşleştiriniz:
1. Banka müşterilerinin kredi kartı dolandırıcılığı (fraud) geçmiş etiketli verilerle tespit edilmesi.
2. Bir e-ticaret sitesinde müşterilerin geçmiş satın alma geçmişine göre segmente edilerek 5 gizli tüketici grubuna ayrılması.
3. Bir fabrikanın bacasından çıkan gaz sensörü verilerine bakılarak anlık karbondioksit miktarının ($PPM$ cinsinden) tahmin edilmesi.
4. Bir insansı robotun yürümeyi öğrenirken düşmemesi için denge hareketlerine ödül ve ceza verilmesi.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Denetimli Öğrenme - Sınıflandırma:** Çıktı kesiklidir (Dolandırıcılık Var / Yok).
2. **Denetimsiz Öğrenme - Kümeleme:** Etiket yoktur; veri kendi iç benzerliklerine göre kümelenir.
3. **Denetimli Öğrenme - Regresyon:** Çıktı sürekli sayısal bir skalerdir (Karbondioksit PPM değeri).
4. **Pekiştirmeli Öğrenme (RL):** Ajan deneme-yanılma ve ödül/ceza ile politika geliştirir.

</details>

---

### Soru 20 (Çoktan Seçmeli): Veri Bölümleme Standartları
Bir makine öğrenmesi projesinde veri setinin Eğitim (%70), Doğrulama (%15) ve Test (%15) olarak üçe bölünmesinde **Doğrulama (Validation)** kümesinin temel işlevi nedir?
A) Modelin nihai doğruluğunu müşteriye raporlamak
B) Hiperparametreleri optimize etmek (Örn: Öğrenme oranı, katman sayısı, k-NN'deki $k$) ve aşırı öğrenmeyi izlemek
C) Modelin ağırlık ($w$) ve bias ($b$) parametrelerini gradyan inişi ile doğrudan güncellemek
D) Eksik verileri tespit edip silmek
E) Veri setindeki aykırı değerleri yok etmek

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Eğitim kümesi model ağırlıklarını ($w, b$) öğrenir. Doğrulama kümesi mühendisin hiperparametreleri ayarlamasına ve aşırı öğrenmeyi tespit etmesine yarar. Test kümesi ise geliştirme bittikten sonra tarafsız son değerlendirme için kullanılır.

</details>

---

### Soru 21 (Vaka Analizi - BANKO): Veri Sızıntısı (Data Leakage)
Bir veri bilimci, 10.000 satırlık veri setine train/test ayrımı yapmadan önce `StandardScaler().fit_transform(X)` uygulamış ve ardından veriyi %80 Eğitim, %20 Test olarak bölmüştür. Eğitilen model test kümesinde %99.2 doğruluk verirken canlıya alındığında %61 doğruluğa düşmüştür.
Bu çöküşün sebebi nedir ve doğru kod akışı nasıl olmalıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Çöküşün Nedeni: Veri Sızıntısı (Data Leakage):**
   * Veri seti bölünmeden önce tüm veriden ortalama ($\mu$) ve varyans ($\sigma$) hesaplandığı için test kümesine ait istatistiksel bilgiler eğitim kümesine sızmıştır. Model test verisinin dağılımını gizlice öğrenerek sınavda sahte bir başarı göstermiş, canlıda ise çökmüştür.
2. **Doğru Kod Akışı:**
   ```python
   # Önce böl:
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
   # Scaler'ı YALNIZCA Train verisi ile eğit:
   scaler = StandardScaler()
   X_train_scaled = scaler.fit_transform(X_train)
   # Test verisini SADECE dönüştür:
   X_test_scaled = scaler.transform(X_test)
   ```

</details>

---

### Soru 22 (Sayısal Hesaplama): Min-Maks Normalizasyonu
Bir veri kümesindeki "Maaş" özniteliğinde en düşük değer $x_{min} = 20.000$ TL, en yüksek değer $x_{max} = 80.000$ TL olarak bulunmuştur.
Buna göre $x = 35.000$ TL maaş alan bir çalışanın $[0, 1]$ aralığına normalize edilmiş $x'$ değeri kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$$
2. **Hesap:**
   $$x' = \frac{35.000 - 20.000}{80.000 - 20.000} = \frac{15.000}{60.000} = \frac{1}{4} = \mathbf{0.25}$$

</details>

---

### Soru 23 (Sayısal Hesaplama): Z-Skoru Standardizasyonu
Bir sınıftaki öğrencilerin sınav notlarının ortalaması $\mu = 60$, standart sapması $\sigma = 15$'tir. Sınavdan $x = 75$ alan bir öğrencinin standartlaştırılmış Z-skoru kaçtır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$z = \frac{x - \mu}{\sigma}$$
2. **Hesap:**
   $$z = \frac{75 - 60}{15} = \frac{15}{15} = \mathbf{1.0}$$

</details>

---

### Soru 24 (Kavramsal): Eksik Verilerde Medyan vs. Ortalama
Neden gayrimenkul fiyatları veya şirket maaşları gibi çarpık (*skewed*) ve aykırı değer içeren sayısal sütunlarda eksik veriler ortalama (*mean*) yerine **medyan (ortanca)** ile doldurulur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Açıklama:** Ortalama, aşırı uç ve aykırı değerlerden (*outliers*) çok sert etkilenir. Örneğin 9 kişinin 20.000 TL kazandığı bir ofise 1 milyon TL kazanan bir CEO girdiğinde aritmetik ortalama 118.000 TL'ye fırlar ve gerçek çalışan profilini yansıtmaz.
* **Medyan** ise sıralamadaki ortadaki değeri aldığı için aykırı değerlere karşı son derece dirençlidir (*robust*) ve dağılımın merkezini doğru temsil eder.

</details>

---

### Soru 25 (Vaka Analizi): Label Encoding Sıralama Tuzağı
Bir modelde araba renkleri (Kırmızı, Mavi, Yeşil) için `LabelEncoder` kullanılmış ve `[Kırmızı=0, Mavi=1, Yeşil=2]` şeklinde kodlama yapılmıştır. Doğrusal regresyon veya sinir ağı bu veriyi işlerken ne tür bir matematiksel yanılgıya düşer?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Yanılgı:** Model, tamsayı değerleri arasında yapay bir büyüklük ve sıralama varsayar:
  $$\text{Yeşil (2)} > \text{Mavi (1)} > \text{Kırmızı (0)}$$
  Hatta $\text{Yeşil} = \text{Mavi} + \text{Mavi}$ gibi anlamsız bir cebirsel ilişki türetebilir.
* Renkler nominal (sırasız) değişken olduğu için bu kodlama modeli yanıltır. Doğrusu her renge ayrı ikili sütun açan **One-Hot Encoding** yöntemidir.

</details>

---

### Soru 26 (Sayısal Mantık): One-Hot Encoding Matris Boyutu
Eğitim kümesinde 4 farklı kategoriye sahip bir "Kan Grubu" özniteliği ($A, B, AB, 0$) 100 hasta için One-Hot Encoding ile kodlanırsa, ortaya çıkan yeni öznitelik matrisinin satır ve sütun boyutu ne olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Her kategori için 1 yeni ikili sütun açılır $\implies 4$ sütun.
* Hasta sayısı sabit kalır $\implies 100$ satır.
* **Yeni Matris Boyutu:** $\mathbf{100 \times 4}$

</details>

---

### Soru 27 (Çoktan Seçmeli): Aşırı Öğrenme Belirtisi
Bir makine öğrenmesi modelinin aşırı öğrendiğini (*overfitting*) gösteren en net metrik davranışı hangisidir?
A) Eğitim kaybı yüksek, test kaybı yüksek
B) Eğitim kaybı çok düşük (%99 doğruluk), test kaybı çok yüksek (%60 doğruluk)
C) Hem eğitim hem test kaybı sürekli azalıyor
D) Eğitim süresi çok kısa sürüyor
E) Ağırlıkların tümü sıfır oluyor

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Aşırı öğrenmede model eğitim verisindeki tüm gürültüyü ezberlediği için eğitim hatası sıfıra yaklaşır; ancak hiç görmediği test verisinde genelleme yapamayarak büyük hata üretir.

</details>

---

### Soru 28 (Kavramsal): Katmanlı Bölümleme (Stratified Split)
Sınıflandırma problemlerinde veriyi eğitim ve test olarak ayırırken neden rastgele ayırma yerine **Katmanlı Bölümleme (Stratified Split)** tercih edilir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Açıklama:** Özellikle dengesiz veri kümelerinde (Örn: %95 Sağlam, %5 Hasta), rastgele bölme yapıldığında test kümesine tesadüfen hiç hasta düşmeyebilir veya oran bozulabilir.
* Katmanlı bölme, hedef sınıfların orijinal veri setindeki yüzdelik dağılımını (örneğin %95'e %5 oranını) hem eğitim hem de test kümesinde birebir korur.

</details>

---

### Soru 29 (Sayısal Yorum): Pearson Korelasyon Katsayısı
İki değişken arasında hesaplanan Pearson korelasyon katsayısı $r = -0.92$ çıkmıştır. Bu ilişki nasıl yorumlanır?
A) Değişkenler arasında hiçbir ilişki yoktur.
B) Değişkenler arasında çok güçlü pozitif yönlü doğrusal ilişki vardır.
C) Değişkenler arasında çok güçlü ters (negatif) yönlü doğrusal ilişki vardır; biri artarken diğeri düzenli olarak azalır.
D) Modelde aşırı öğrenme vardır.
E) Veride eksik değerler bulunmaktadır.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: C**
* **Açıklama:** Pearson korelasyonu $[-1, +1]$ arasındadır. $-1.0$'a yakın değerler çok güçlü ters yönlü doğrusal bağıntıyı gösterir (Örn: Aracın yaşı arttıkça piyasa değeri düşer).

</details>

---

### Soru 30 (Çoktan Seçmeli): Temel Bileşen Analizi (PCA)
Temel Bileşen Analizi (PCA) algoritması hakkında aşağıdakilerden hangisi **DOĞRUDUR**?
A) Denetimli bir sınıflandırma algoritmasıdır.
B) Verideki varyansı (bilgiyi) maksimum düzeyde koruyarak boyut sayısını azaltan denetimsiz bir yöntemdir.
C) Kategorik değişkenleri sayısallaştırmak için kullanılır.
D) Eksik verileri medyan ile doldurur.
E) Çıktı olarak sınıf olasılıkları üretir.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** PCA, verideki kovaryans matrisinin özvektörlerini ve özdeğerlerini bularak en yüksek varyansa sahip dikey eksenleri seçer; yüksek boyutlu veriyi (örneğin 100 boyuttan 2 boyuta) bilgi kaybını en aza indirerek sıkıştırır.

</details>

---

### Soru 31 (Doğru / Yanlış - Gerekçeli): Test Kümesinin Kullanımı
**İfade:** *"Modelin hiperparametrelerini (örneğin öğrenme oranı ve katman sayısı) optimize etmek için test kümesindeki doğruluk oranına bakılarak seçim yapılmalıdır."*
Bu ifade Doğru mudur, Yanlış mıdır? Gerekçesini yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** Hiperparametre seçimi için **Doğrulama Kümesi (Validation Set)** kullanılır. Eğer test kümesine bakılarak hiperparametre seçilirse, model dolaylı olarak test kümesine göre ayarlanmış olur (Test Leakage) ve bağımsızlığını kaybeder.

</details>

---

### Soru 32 (Sayısal Senaryo): Doğruluk Paradoksu (Accuracy Paradox)
Bir hastalık teşhis veri setinde 990 sağlıklı, 10 kanserli hasta bulunmaktadır. Bir model gelen tüm hastalara hiçbir özniteliğe bakmaksızın "Sağlıklı" teşhisi koymaktadır.
Bu modelin Doğruluk (*Accuracy*) oranı kaçtır ve neden bu model işe yaramazdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Doğruluk Hesabı:**
   $$\text{Doğruluk} = \frac{\text{Doğru Tahminler}}{\text{Toplam Hasta}} = \frac{990}{1000} = \mathbf{\%99.0}$$
2. **Neden İşe Yaramaz?**
   * Model %99 doğruluk vermesine rağmen 10 kanserli hastanın tamamını kaçırmıştır (Duyarlılık / Recall = 0). Dengesiz verilerde tek başına "Doğruluk" metriği aldatıcıdır.

</details>

---

### Soru 33 (Sayısal Hesaplama): Min-Maks Dönüşümü
$[10, 50]$ aralığında değişen bir öznitelikte $x = 30$ değerinin Min-Maks normalizasyonu sonrası değeri nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
$$x' = \frac{30 - 10}{50 - 10} = \frac{20}{40} = \mathbf{0.50}$$

</details>

---

### Soru 34 (Kavramsal): Yüksek Kardinalite Sorunu
Bir müşteri veri setinde "Posta Kodu" sütununda 5.000 farklı benzersiz değer bulunmaktadır. Bu sütuna doğrudan One-Hot Encoding uygulandığında ne tür bir teknik kriz yaşanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Boyut Laneti (*Curse of Dimensionality*):** Veri setine 5.000 adet yeni sütun eklenir. Matris aşırı derecede seyrekleşir (*sparse matrix* - %99.9'u sıfır olur).
2. **Bellek Taşması ve Aşırı Öğrenme:** Model parametreleri katlanarak artar, RAM tükenir ve model ezberlemeye düşer. Çözüm: Hedef Kodlama (*Target Encoding*) veya frekans bazlı gruplamadır.

</details>

---

### Soru 35 (Doğru / Yanlış - Gerekçeli): StandardScaler Aralığı
**İfade:** *"StandardScaler işlemi verideki tüm sayısal değerleri kesinlikle $[0, 1]$ aralığına sıkıştırır."*
Bu ifade Doğru mudur, Yanlış mıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** Veriyi $[0, 1]$ aralığına sıkıştıran yöntem **MinMaxScaler**'dır. StandardScaler ise verinin ortalamasını 0, varyansını 1 yapar ($z = \frac{x-\mu}{\sigma}$); değerler teorik olarak $(-\infty, +\infty)$ aralığında olabilir (çoğunlukla $[-3, +3]$ aralığındadır).

</details>

---

### Soru 36 (Sıralama): Veri Ön İşleme Yaşam Döngüsü
Aşağıdaki adımları standart bir makine öğrenmesi boru hattındaki doğru uygulama sırasına diziniz:
1. Modeli eğitme (`model.fit`)
2. Veriyi Train ve Test olarak bölme (`train_test_split`)
3. Test kümesinde performansı değerlendirme (`model.evaluate`)
4. Eksik verileri train medyanı ile doldurma ve ölçekleme (`scaler.fit_transform`)

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Sıralama:** **2 $\rightarrow$ 4 $\rightarrow$ 1 $\rightarrow$ 3**
* Önce veri bölünür (2), ardından train verisinden istatistikler öğrenilerek ön işleme yapılır (4), model eğitilir (1) ve en son test kümesinde değerlendirilir (3).

</details>

---
"""

def get_section_3():
    return r"""## BÖLÜM 3: Hafta 03 – Doğrusal Regresyon, Kayıp Fonksiyonları ve Gradyan İnişi

### Soru 37 (Kavramsal): Doğrusal Regresyon ve Artık Tanımı
Basit doğrusal regresyon denklemi $\hat{y} = wx + b$ olduğuna göre:
1. $w$ ve $b$ parametrelerinin geometrik anlamı nedir?
2. Bir $i$. veri noktası için **artık (residual - $e_i$)** nasıl tanımlanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. $w$ doğrunun **eğimi (ağırlık / slope)**, $b$ ise doğrunun y-eksenini kestiği noktadır (**kesen / bias / intercept**).
2. **Artık ($e_i$):** Gerçek gözlem değeri ($y_i$) ile modelin tahmin ettiği değer ($\hat{y}_i$) arasındaki dikey farktır:
   $$e_i = y_i - \hat{y}_i$$

</details>

---

### Soru 38 (Çoktan Seçmeli): MSE vs. MAE
Kayıp fonksiyonu olarak Ortalama Kare Hata (MSE) kullanımının Ortalama Mutlak Hataya (MAE) kıyasla en belirgin matematiksel ve pratik farkı nedir?
A) MSE aykırı değerlerden hiç etkilenmez.
B) MSE hataların karesini aldığı için büyük hataları küçük hatalara göre katbekat daha şiddetli cezalandırır.
C) MSE her zaman negatif değerler üretir.
D) MSE'nin türevi alınamaz.
E) MAE yalnızca sınıflandırmada kullanılır.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** MSE'de $(y_i - \hat{y}_i)^2$ alındığı için 1 birimlik hata 1 ceza getirirken, 10 birimlik hata 100 ceza getirir; bu nedenle model aykırı hataları küçültmeye aşırı odaklanır. MAE ise hatalarla doğrusal orantılı ceza verir ($|y_i - \hat{y}_i|$).

</details>

---

### Soru 39 (Çoktan Seçmeli): RMSE Birim Uyumu
Regresyon analizinde MSE yerine Kök Ortalama Kare Hatanın (RMSE) raporlanmasının temel pratik gerekçesi nedir?
A) RMSE'nin sıfırdan küçük olabilmesi
B) Karekök alma işlemi sayesinde metrik biriminin hedef değişkenin orijinal birimiyle (TL, cm, kg) birebir aynı hale gelmesi
C) Gradyan inişinin daha hızlı yakınsaması
D) Parametre sayısını azaltması
E) Aşırı öğrenmeyi otomatik olarak durdurması

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Örneğin ev fiyatı tahmininde hedef birimi TL ise, MSE'nin birimi "$\text{TL}^2$" olur ve yorumlanması zordur. RMSE karekök alarak hatayı tekrar "TL" cinsine döndürür.

</details>

---

### Soru 40 (Kavramsal - BANKO): $R^2 = 0$ Anlamı
Bir doğrusal regresyon modelinin test kümesindeki Belirlilik Katsayısı $R^2 = 0$ olarak hesaplanmıştır. Bu sonuç model hakkında ne söyler?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Anlamı:** $R^2 = 1 - \frac{SSE}{SST} = 0 \implies SSE = SST$.
* Model, girdi özniteliklerini ($x$) kullanarak hedef değişkendeki varyansın **hiçbir kısmını açıklayamamıştır**. Her örneğe girdi değerine bakılmaksızın doğrudan hedefin genel ortalamasını ($\bar{y}$) atayan "aptal bir temel modelden" (baseline) daha iyi tahmin yapamamaktadır.

</details>

---

### Soru 41 (Sayısal Hesaplama): $R^2$ Skoru Hesabı
Bir regresyon modelinde yapılan tahmin hatalarının kareler toplamı $SSE = 20$, hedef değişkenin toplam varyansı $SST = 100$ bulunmuştur. Modelin $R^2$ skorunu hesaplayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Formül:**
   $$R^2 = 1 - \frac{SSE}{SST}$$
2. **Hesap:**
   $$R^2 = 1 - \frac{20}{100} = 1 - 0.20 = \mathbf{0.80}$$
* Model verideki değişimin %80'ini açıklamaktadır.

</details>

---

### Soru 42 (Kavramsal): Gradyan İnişi Güncelleme Kuralı
Gradyan inişinde ağırlık güncelleme kuralı $w_{yeni} = w_{eski} - \eta \frac{\partial L}{\partial w}$ şeklindedir. Neden formülde artı ($+$) yerine eksi ($-$) işareti vardır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Gerekçe:** Gradyan ($\frac{\partial L}{\partial w}$), kayıp fonksiyonunun en dik **arttığı** yönü gösterir.
* Biz kayıp fonksiyonunu minimize etmek (çukurun tabanına inmek) istediğimiz için gradyanın **tersi yönünde** adım atmak zorundayız. Eksi işareti iniş yönünü sağlar.

</details>

---

### Soru 43 (Sayısal Gradyan - SLAYTLARDAN): $L(w) = w^2$ Adımı
Kayıp fonksiyonu $L(w) = w^2$ olan bir modelde başlangıç ağırlığı $w_0 = 4$ ve öğrenme oranı $\eta = 0.25$ ise bir gradyan iniş adımından sonra $w_1$ ağırlığı kaç olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Türev (Gradyan):**
   $$\frac{dL}{dw} = 2w \implies 2 \times 4 = 8$$
2. **Güncelleme:**
   $$w_1 = w_0 - \eta \frac{dL}{dw} = 4 - (0.25 \times 8) = 4 - 2 = \mathbf{2}$$

</details>

---

### Soru 44 (Sayısal Gradyan - SLAYTLARDAN): $L(w) = (w-3)^2$ Adımı
Kayıp fonksiyonu $L(w) = (w - 3)^2$ olan bir modelde başlangıç ağırlığı $w_0 = 0$ ve öğrenme oranı $\eta = 0.1$ ise bir gradyan iniş adımı sonrasında $w_1$ değeri kaç olur?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Türev (Gradyan):**
   $$\frac{dL}{dw} = 2(w - 3) \implies 2(0 - 3) = -6$$
2. **Güncelleme:**
   $$w_1 = w_0 - \eta \frac{dL}{dw} = 0 - (0.1 \times -6) = 0 - (-0.6) = \mathbf{0.6}$$

</details>

---

### Soru 45 (Çoktan Seçmeli): Öğrenme Oranı ($\eta$) Davranışları
Aşağıdakilerden hangisi bir modelin öğrenme oranının ($\eta$) **aşırı büyük** seçildiğinin göstergesidir?
A) Eğitim kaybının çok yavaş ama kararlı bir şekilde azalması
B) Modelin kayıp değerinin salınım yaparak adımdan adıma büyümesi ve sonsuza doğru patlaması (Iraksama)
C) Modelin hemen aşırı öğrenmeye düşmesi
D) Ağırlıkların sıfırda sabit kalması
E) Doğrulama kaybının eğitim kaybından daha hızlı düşmesi

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Aşırı büyük $\eta$ çukurun genişliğinden büyük adımlar atar, minimum noktasının üzerinden atlar (overshooting) ve kayıp sonsuza ıraksar.

</details>

---

### Soru 46 (Çoktan Seçmeli): Batch vs. SGD vs. Mini-Batch
Büyük veri kümelerinde modern derin öğrenme kütüphanelerinin varsayılan olarak **Mini-Batch Gradient Descent** kullanmasının temel sebebi nedir?
A) Her adımda tüm veri setini belleğe yükleyebilmesi
B) GPU'nun paralel matris işlem gücünden tam yararlanırken, hem kararlı hem de SGD'ye göre daha az gürültülü gradyan adımları sağlaması
C) Öğrenme oranı gereksinimini ortadan kaldırması
D) Hiçbir hiperparametreye ihtiyaç duymaması
E) Kaybı doğrudan analitik kapalı formülle çözmesi

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** Batch GD büyük veride RAM'e sığmaz; saf SGD ise tek tek işlediği için GPU paralelliğini kullanamaz ve çok dalgalıdır. Mini-Batch (16, 32, 64) her iki dünyanın en iyi yönlerini birleştirir.

</details>

---

### Soru 47 (Kavramsal): Normal Denklem vs. Gradyan İnişi
Doğrusal regresyonun analitik kapalı form çözümü olan Normal Denklem ($w = (X^T X)^{-1} X^T y$), öznitelik sayısı $D > 100.000$ olduğunda neden tercih edilmez?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Gerekçe: Matris Tersinin Hesaplama Karmaşıklığı:**
  * $(X^T X)^{-1}$ matris tersi alma işlemi $O(D^3)$ zaman karmaşıklığına sahiptir.
  * $D = 100.000$ olduğunda $(100.000)^3 = 10^{15}$ işlem gerekir; donanım kilitlenir. Gradyan inişi ise matris tersi almadan iteratif olarak $O(k \cdot N \cdot D)$ sürede rahatça çözüme ulaşır.

</details>

---

### Soru 48 (Kavramsal): Öznitelik Ölçeklemenin Gradyan İnişine Etkisi
Çoklu regresyonda öznitelikler ölçeklenmediğinde (Örn: $x_1 \in [0, 1]$ iken $x_2 \in [0, 1.000.000]$), gradyan inişinin kayıp yüzeyindeki ilerleyişi nasıl etkilenir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Kayıp yüzeyinin eş-seviye eğrileri (kontur çizgileri) aşırı basık, dar ve uzun bir elips (vadi) şeklini alır.
* Gradyan inişi dik yönde şiddetli salınımlar ve zikzaklar yapar, tabana doğru ilerlemesi son derece yavaşlar.
* Ölçekleme yapıldığında konturlar simetrik dairelere dönüşür ve gradyan doğrudan merkeze (minimuma) yönelir.

</details>

---

### Soru 49 (Doğru / Yanlış - Gerekçeli): Küresel Minimum
**İfade:** *"Basit doğrusal regresyonda MSE kayıp fonksiyonunun birden fazla yerel minimumu (local minima) bulunur; bu yüzden model yanlış bir çukura saplanıp kalabilir."*
Bu ifade Doğru mudur, Yanlış mıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **YANLIŞTIR.**
* **Gerekçe:** Doğrusal regresyonun MSE kayıp fonksiyonu matematiksel olarak kesinlikle **dışbükeydir (konveks - çanak şeklinde)**. Tek bir küresel minimumu ($w^*$) vardır; yerel minimum tuzağı barındırmaz.

</details>

---

### Soru 50 (Sayısal Hesaplama): MSE ve MAE Karşılaştırması
Bir veri kümesinde gerçek değerler $y = [10, 20]$, modelin tahminleri $\hat{y} = [12, 18]$'dir. Modelin MSE ve MAE değerlerini bulunuz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Artıklar:**
   $$e_1 = 10 - 12 = -2, \quad e_2 = 20 - 18 = 2$$
2. **MSE Hesabı:**
   $$MSE = \frac{(-2)^2 + (2)^2}{2} = \frac{4 + 4}{2} = \mathbf{4.0}$$
3. **MAE Hesabı:**
   $$MAE = \frac{|-2| + |2|}{2} = \frac{2 + 2}{2} = \mathbf{2.0}$$

</details>

---

### Soru 51 (Çoktan Seçmeli): Negatif $R^2$ Değeri
Bir regresyon modelinde test kümesinde $R^2 = -0.35$ elde edilmiştir. Bu durum nasıl açıklanır?
A) Model mükemmel uyum sağlamıştır.
B) Model o kadar kötüdür ki, hedef değişkenin basit ortalamasını ($\bar{y}$) sabit tahmin eden çizgiden bile daha büyük hata üretmektedir.
C) Hataların karesi negatif çıkmıştır.
D) Veride hiç gürültü yoktur.
E) Modelde aşırı öğrenme engellenmiştir.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Doğru Cevap: B**
* **Açıklama:** $R^2 = 1 - \frac{SSE}{SST}$ formülünde, eğer modelin yaptığı hatalar ($SSE$) verinin kendi doğal varyansından ($SST$) daha büyükse $R^2$ negatif çıkar. Model berbat durumdadır.

</details>

---

### Soru 52 (Kavramsal): Öğrenme Oranı Zamanlaması (Learning Rate Decay)
Eğitimin başlangıcında büyük, epoch'lar ilerledikçe giderek küçülen bir öğrenme oranı politikası (*Learning Rate Decay / Annealing*) izlemenin avantajı nedir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Başlangıçta büyük adımlar atmak modelin dik yamaçları hızla inmesini ve düzlükleri çabuk geçmesini sağlar.
* Minimum çukuruna yaklaşıldığında adımları küçültmek, modelin minimumun üzerinden atlamasını engeller ve tam dip noktaya hassas biçimde yerleşmesini sağlar.

</details>

---

### Soru 53 (Doğru / Yanlış - Gerekçeli): Artıkların Toplamı
**İfade:** *"En küçük kareler yöntemiyle kapalı formda çözülen basit doğrusal regresyonda, artıkların cebirsel toplamı ($\sum e_i$) her zaman sıfıra eşittir."*
Bu ifade Doğru mudur, Yanlış mıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **DOĞRUDUR.**
* **Gerekçe:** Modelde kesen (bias - $b$) terimi bulunduğu sürece, en küçük kareler türevi sıfıra eşitlendiğinde artıkların toplamının sıfır olması matematiksel bir zorunluluktur ($\sum (y_i - \hat{y}_i) = 0$). Pozitif hatalar ile negatif hatalar birbirini dengeler.

</details>

---

### Soru 54 (Vaka Analizi): Polinom Regresyonda Aşırı Öğrenme
2. dereceden bir parabolik ilişki içeren veriye 15. dereceden bir polinom modeli ($y = w_1 x + w_2 x^2 + \dots + w_{15} x^{15} + b$) uydurulduğunda ne yaşanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Model eğitim noktalarının tamamından geçebilmek için çılgınca dalgalanan, yüksek salınımlı kıvrımlar çizer.
* Eğitim hatası sıfıra yaklaşır ancak noktalar arasındaki bölgelerde saçma sapan tahminler üretir $\implies$ **Aşırı Öğrenme (Overfitting / Yüksek Varyans)**. Çözüm: Polinom derecesini düşürmek veya L2 (Ridge) düzenlileştirme eklemektir.

</details>

---
"""
