# Yapay Zekâya Giriş Vize Sınavına Hazırlık: 200 Soruluk Kapsamlı ve İnteraktif Soru Bankası

Bu doküman, **Dr. Seda Bayat Tosun** tarafından yürütülen **Yapay Zekâya Giriş** dersinin tüm transkriptleri, ders içi soru-cevap oturumları, haftalık sunum slaytları (`Hafta01`–`Hafta09`) ve Colab defterleri taranarak **sadece vize kapsamındaki ilk 8-9 haftanın** konularını kapsayacak şekilde hazırlanmış resmi soru bankasıdır.

İçerisinde:
- **Çoktan Seçmeli (Test) Soruları:** Kavramsal, mimari, model karşılaştırmalı,
- **Sayısal ve Matris Hesaplama Soruları:** 2D evrişim matris çarpımları, çıktı boyut formülleri, parametre hesapları, bellek hesabı, gradyan güncellemesi, normalizasyon ve metrik türetimleri,
- **Doğru / Yanlış (Gerekçeli) Soruları:** Sınavda şaşırtmaca yaratabilecek ince teknik detaylar,
- **Senaryo ve Vaka Analizi Soruları:** Gerçek hayat mühendislik problemleri, aşırı öğrenme teşhisi, gürültü temizleme ve metrik seçimi,
- **Hocanın Derste Bizzat Sorduğu 16 Vize Sorusu ve Gerçek Sınav Uyarıları**,
- **20 Soruluk Gerçek Formatlı Vize Deneme Sınavı** yer almaktadır.

> [!TIP]
> **Çalışma Yöntemi (Self-Testing):**
> Tüm soruların cevapları ve ayrıntılı çözüm adımları **açılır-kapanır (toggle / `<details>`)** kutular içerisine gizlenmiştir. Çalışırken önce soruyu okuyup kendi cevabınızı bir kağıda yazınız; ardından **"🔍 Çözümü ve Detaylı Anlatımı Gör"** butonuna tıklayarak cevabınızı ve gerekçenizi kontrol ediniz.

---

## 📑 İÇİNDEKİLER VE MÜFREDAT SIRASI

1. [BÖLÜM 1: Hafta 01 – Yapay Zekâya Giriş, Tarihçe, Turing Testi ve Paradigmalar (Soru 1 – 18)](#bölüm-1-hafta-01--yapay-zekâya-giriş-tarihçe-turing-testi-ve-paradigmalar)
2. [BÖLÜM 2: Hafta 02 – Makine Öğrenmesinin Temelleri, Yaşam Döngüsü ve Veri Ön İşleme (Soru 19 – 36)](#bölüm-2-hafta-02--makine-öğrenmesinin-temelleri-yaşam-döngüsü-ve-veri-ön-i̇şleme)
3. [BÖLÜM 3: Hafta 03 – Doğrusal Regresyon, Kayıp Fonksiyonları ve Gradyan İnişi (Soru 37 – 54)](#bölüm-3-hafta-03--doğrusal-regresyon-kayıp-fonksiyonları-ve-gradyan-i̇nişi)
4. [BÖLÜM 4: Hafta 04 – Sınıflandırma Yöntemleri (Lojistik Regresyon, k-NN, Ağaçlar, Naive Bayes, SVM) (Soru 55 – 74)](#bölüm-4-hafta-04--sınıflandırma-yöntemleri)
5. [BÖLÜM 5: Hafta 05 – Model Değerlendirme, Karışıklık Matrisi, ROC/AUC ve Kümeleme (Soru 75 – 94)](#bölüm-5-hafta-05--model-değerlendirme-karışıklık-matrisi-rocauc-ve-kümeleme)
6. [BÖLÜM 6: Hafta 06 – Yapay Sinir Ağları (YSA), Perceptron, XOR ve MLP Mimarisi (Soru 95 – 114)](#bölüm-6-hafta-06--yapay-sinir-ağları-ysa-perceptron-xor-ve-mlp-mimarisi)
7. [BÖLÜM 7: Hafta 07 – Derin Ağların Eğitimi, Geri Yayılım ve Optimizasyon (Soru 115 – 134)](#bölüm-7-hafta-07--derin-ağların-eğitimi-geri-yayılım-ve-optimizasyon)
8. [BÖLÜM 8: Hafta 08 – Görüntü İşlemenin Temelleri, Filtreler ve 2D Evrişim (Soru 135 – 154)](#bölüm-8-hafta-08--görüntü-i̇şlemenin-temelleri-filtreler-ve-2d-evrişim)
9. [BÖLÜM 9: Hafta 09 – Evrişimli Sinir Ağları (CNN), Katmanlar ve Boyut Hesaplamaları (Soru 155 – 180)](#bölüm-9-hafta-09--evrişimli-sinir-ağları-cnn-katmanlar-ve-boyut-hesaplamaları)
10. [BÖLÜM 10: Hocanın Formatında 20 Soruluk Tam Kapsamlı Vize Deneme Sınavı (Soru 181 – 200)](#bölüm-10-hocanın-formatında-20-soruluk-tam-kapsamlı-vize-deneme-sınavı)

---


## BÖLÜM 1: Hafta 01 – Yapay Zekâya Giriş, Tarihçe, Turing Testi ve Paradigmalar

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


## BÖLÜM 2: Hafta 02 – Makine Öğrenmesinin Temelleri, Yaşam Döngüsü ve Veri Ön İşleme

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


## BÖLÜM 3: Hafta 03 – Doğrusal Regresyon, Kayıp Fonksiyonları ve Gradyan İnişi

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


## BÖLÜM 4: Hafta 04 – Sınıflandırma Yöntemleri

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


## BÖLÜM 5: Hafta 05 – Model Değerlendirme, Karışıklık Matrisi, ROC/AUC ve Kümeleme

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


## BÖLÜM 6: Hafta 06 – Yapay Sinir Ağları (YSA), Perceptron, XOR ve MLP Mimarisi

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


## BÖLÜM 7: Hafta 07 – Derin Ağların Eğitimi, Geri Yayılım ve Optimizasyon

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


## BÖLÜM 8: Hafta 08 – Görüntü İşlemenin Temelleri, Filtreler ve 2D Evrişim

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


## BÖLÜM 9: Hafta 09 – Evrişimli Sinir Ağları (CNN), Katmanlar ve Boyut Hesaplamaları

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

