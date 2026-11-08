# Mobil Cihazlar İçin Yazılım Mühendisliği

---

# 30 Eylül 2026

---

- **Dersin Adı:** Mobil Cihazlar İçin Yazılım Mühendisliği
- **Tarih:** 30 Eylül 2026
- **Kullanılan Teknoloji / Dil:** C# / .NET MAUI (XAML & C#)
- **Geliştirme Ortamı:** Visual Studio (İş Yükü: .NET Multi-platform App UI)

---

## 1. Giriş ve Dönem Planı

- Ders kapsamında bu dönem mobil uygulama geliştirme için **.NET MAUI** teknolojisi kullanılacaktır.
- İlerleyen dönemlerde mobil oyun geliştirme gibi konulara da değinilecektir.
- **Platform hedefleri:** Birincil hedef **Android** ve **iOS** platformlarıdır. Test ve geliştirme kolaylığı açısından yerel **Windows (WinUI 3)** hedefi de aktif olarak kullanılacaktır.

---

## 2. Neden .NET MAUI? (Çapraz Platform Karşılaştırması)

- **Web Tabanlı Çapraz Platformlar (React Native, Ionic vb.):**
    - Bu ortamlar arka planda HTML, CSS ve JavaScript kullanarak aslında bir web sayfası üretir.
    - Mobil uygulamada bir `WebView` bileşeni açılarak hazırlanan web sitesi bu pencereye gömülür.
    - Saf (native) bir mobil uygulama deneyimi ve performansı sunmaktan uzaktır.
- **Flutter ve Kotlin:**
    - Flutter kendine ait Skia/Impeller motoruyla pikselleri ekrana doğrudan çizer (render eder). Android ve iOS'ta birebir aynı görünümü sağlar ancak platformun saf doğal bileşenlerini (native controls) kullanmaz.
- **.NET MAUI'nin Avantajı:**
    - Doğrudan hedef işletim sisteminin yerel arayüz bileşenlerini (native controls) eşler.
    - Yüksek performans sunar ve işletim sisteminin doğal görünümünü/davranışını yansıtır.

---

## 3. .NET MAUI'nin Tarihçesi ve Microsoft Ekosistemi

- **Mono / MonoDevelop:** Linux, macOS ve Windows'ta .NET çalıştırma girişimi olarak başladı.
- **Xamarin Dönemi:**
    - MonoDevelop evrilerek **Xamarin** adını aldı.
    - `Xamarin.iOS` ve `Xamarin.Android` ile tek dilde (C#) yazılan kodlar platforma özel derlenmeye başlandı.
- **Xamarin.Forms:**
    - Microsoft'un Xamarin'i satın almasıyla tek bir XAML arayüzü üzerinden Android, iOS ve Windows Phone hedeflendi.
- **.NET MAUI (Multi-platform App UI):**
    - Xamarin.Forms'un modernize edilmiş, .NET çatısıyla (Modern .NET) tam entegre edilmiş halidir.
    - **Desteklenen Platformlar:** Android, iOS, macOS (Mac Catalyst), Windows, Tizen. (Topluluk desteğiyle Linux).

---

## 4. Geliştirme ve Test Ortamının Hazırlanması

### A. Gerekli Kurulumlar

1. **Visual Studio:**
    - Visual Studio Installer açılarak **".NET Multi-platform App UI geliştirme"** iş yükü (workload) seçilmeli ve yüklenmelidir.
2. **Framework / Hedef Sürüm:**
    - Projelerde **.NET 10 (LTS)** kullanılacaktır. (.NET 11 STS/kısa süreli destek sürümü olduğu için uzun vadeli kararlı projelerde LTS sürümler tercih edilir).
3. **Android SDK & Öykünücü (Emulator):**
    - *Araçlar > Android > Android SDK Manager* ve *Android Device Manager* üzerinden yönetilir.

---

### B. Fiziksel Cihaz ile Test (Önerilen Yöntem)

#### Android Cihazlar:

1. Telefon ile bilgisayar arasına sadece şarj eden değil, **veri aktarımı (data)** yapabilen bir kablo bağlanmalıdır.
2. Telefonda **Geliştirici Seçenekleri** açılmalıdır:
    - *Ayarlar > Telefon Hakkında / Yazılım Bilgileri > Yapım Numarası (Build Number)* üzerine arka arkaya **7 kez** tıklanır.
3. Açılan *Geliştirici Seçenekleri* menüsünden **USB Hata Ayıklama (USB Debugging)** aktif edilir.
4. Telefon bağlandığında gelen "Bu bilgisayara her zaman izin ver (RSA Anahtarı)" uyarısı onaylanır.
5. Visual Studio üst menüsündeki hedef cihaz listesinde telefonun modeli doğrudan görünür.
*(Not: Bankacılık uygulamaları geliştirici modu açıkken güvenlik uyarısı verebilir).*

#### iOS Cihazlar ve Mac Bağımlılığı (Apple Kısıtlamaları):

- Apple'ın kapalı ekosistem politikaları ve API kısıtlamaları nedeniyle doğrudan Windows üzerinden iPhone'a uygulama yüklenemez (Microsoft da Visual Studio for Mac desteğini sonlandırmıştır).
- **Gerekli Yapı:** Windows üzerinde yazılan kodun derlenebilmesi için aynı yerel ağda bir **Mac cihazı (MacBook, Mac mini, iMac)** bulunmalı ve üzerinde **Xcode** kurulu olmalıdır.
- Visual Studio'dan *"Pair to Mac"* (Mac ile Eşleştir) özelliği kullanılarak derleme işlemi ağdaki Mac üzerinden yürütülür.
- Alternatif olarak sanal makineye macOS (Hackintosh) kurulabilir veya buluttan Mac sunucu kiralanabilir; ancak sanal makineler yüksek donanım kaynağı tüketir ve yavaş çalışır.

---

### C. Sanal Cihaz (Android Emulator) Yapılandırması

- Visual Studio içinden *Araçlar > Android > Android Device Manager* açılarak sanal cihaz tanımlanır.
- Hedef Android sürümü (API seviyesi), ekran çözünürlüğü ve RAM miktarı belirlenir.
- **Kritik Uyarı:** Bilgisayarın RAM kapasitesine dikkat edilmelidir (Örn: 16 GB RAM'li bir bilgisayarda sanal cihaza 8 GB RAM verilirse, işletim sistemi sanal belleğe/diske başvurur ve sistem ciddi şekilde yavaşlar).
- Ağır çalışan sistemlerde alternatif hafif emülatörler (NoxPlayer, BlueStacks vb.) de tercih edilebilir.

---

## 5. NuGet ve .NET MAUI Community Toolkit

- **NuGet ([nuget.org](http://nuget.org/)):** .NET dünyasının merkezi paket yöneticisidir (Python'daki `pip` gibi).
- **.NET MAUI Community Toolkit:**
    - Microsoft'tan bağımsız olarak topluluk tarafından geliştirilen, Microsoft'un da resmi olarak desteklediği açık kaynaklı kütüphanedir.
    - `CameraView`, `AvatarView`, `MediaElement` gibi standart MAUI kütüphanesinde bulunmayan veya eksik olan gelişmiş arayüz ve donanım bileşenlerini sağlar.

---

## 6. Proje Anatomisi ve Katmanlı Mimari

Visual Studio'da açılan yeni bir .NET MAUI projesi (`Ders01`) katmanlı mimariye uygun şu dosya yapısıyla gelir:

1. **`MauiProgram.cs`:**
    - Uygulamanın başlatıcısıdır. `CreateMauiApp()` fonksiyonu ile uygulama örneği (`MauiApp`) oluşturulur; fontlar, servisler ve bağımlılıklar burada kaydedilir.
2. **`App.xaml` & `App.xaml.cs`:**
    - Uygulama düzeyindeki global kaynakları (renkler, fırçalar, genel stiller) barındırır.
    - `MainPage` olarak `AppShell`'i yükler.
3. **`AppShell.xaml`:**
    - Uygulamanın navigasyon hiyerarşisini, sekmelerini (Tab) ve çekmece menülerini (Flyout) yönetir.
4. **`MainPage.xaml` & `MainPage.xaml.cs`:**
    - İlk açılış sayfasıdır.
    - **Sunum Katmanı (Presentation Layer):** `MainPage.xaml` dosyasında XAML ile yazılır.
    - **İş Mantığı Katmanı (Business Layer / Code-Behind):** `MainPage.xaml.cs` dosyasında C# ile yazılır.
5. **`Resources` Klasörü:**
    - `Fonts`: Yazı tipleri.
    - `Images`: Uygulama içi görseller.
    - `Styles`: CSS benzeri tema, renk ve bileşen stilleri (`Colors.xaml`, `Styles.xaml`).

---

## 7. .NET MAUI Kontrol Hiyerarşisi

.NET MAUI arayüz tasarımı üç temel yapı taşı üzerine kuruludur:

```
[ SAYFA (Page) ]
       └── [ YERLEŞİM (Layout) ]
                 └── [ GÖRÜNÜM / KONTROL (View) ]
```

1. **Sayfalar (Pages):** Ekranın tamamını kaplar.
    - `ContentPage`: Tek bir görünüm içeren temel sayfa türüdür (en sık kullanılan).
    - `FlyoutPage`, `NavigationPage`, `TabbedPage`.
2. **Yerleşimler (Layouts):** Görünümlerin ekranda nasıl dizileceğini belirler.
    - `VerticalStackLayout`: Elemanları dikeyde alt alta sıralar.
    - `HorizontalStackLayout`: Elemanları yatayda yan yana sıralar.
    - `Grid`: Satır ve sütun mantığıyla tablo düzeni kurar.
    - `FlexLayout`, `AbsoluteLayout`.
3. **Görünümler (Views):** Kullanıcının gördüğü ve etkileşime girdiği kontrollerdir.
    - `Label`, `Button`, `Entry`, `Editor`, `Image`, `CheckBox` vb.
4. **Kapsayıcılar:**
    - `ScrollView`: İçeriğin ekrana sığmadığı durumlarda dikey veya yatay kaydırma çubuğu sağlar.

---

## 8. Hot Reload ve Temel XAML Etiket Mantığı

- **XAML (eXtensible Application Markup Language):** XML tabanlı bir işaretleme dilidir.
- **Etiket Kuralları:**
    - Açma etiketi (`<Label>`) ve kapama etiketi (`</Label>`) bulunur.
    - Eğer bir etiketin içine alt eleman konulmayacaksa tek satırda self-closing (`<Label Text="Merhaba" />`) olarak kapatılır.
- **XAML Hot Reload:** XAML dosyasında yapılan arayüz değişiklikleri, projeyi yeniden derleyip başlatmaya gerek kalmadan canlı olarak emülatör veya cihaza yansır.

---

## 9. `Label` (Etiket) Kontrolü ve Özellikleri

Derste incelenen temel `Label` özellikleri:

| Özellik | Veri Tipi | Açıklama |
| --- | --- | --- |
| `Text` | `string` | Ekranda gösterilecek metin içeriği. |
| `CharacterSpacing` | `double` | Harfler arasındaki boşluk mesafesi. Pozitif değerler harfleri açar, negatif değerler sıkıştırır (Örn: `2.75`, `-1`). |
| `FontAttributes` | `enum` | Yazının kalınlık ve eğiklik durumu: `Bold`, `Italic`, `None`. |
| `FontAutoScalingEnabled` | `bool` | İşletim sisteminin erişilebilirlik yazı boyutu ayarlarına göre otomatik ölçeklenip ölçeklenmeyeceği (`True` / `False`). |
| `FontFamily` | `string` | Kullanılacak font ailesi. Özel fontların önce `MauiProgram.cs` ve `Resources/Fonts` altına tanıtılması gerekir. |

---

## 10. Tasarım Parantezi: Tipografi, Grafoloji ve Kurumsal Kimlik

- Yazılım mühendisi sadece kod yazmaz; **UI (Kullanıcı Arayüzü)** ve **UX (Kullanıcı Deneyimi)** kurallarına da hakim olmalıdır.
- **Büyük Harf Kullanımı:** Agresiflik, bağırma ve kuralcılık hissi uyandırır.
- **Küçük Harf ve Yuvarlak Hatlar:** Samimiyet, erişilebilirlik ve halka yakınlık hissi verir (Örn: Arçelik ve Beko'nun büyük/sert harflerden modern küçük/yuvarlak fontlara geçişi).
- **Sağa Yatık (İtalik) Yazı:** Dinamizm, hız, gelecek hedefleri ve yükseliş algısı yaratır.
- **Renklerin Dili:**
    - *Mavi:* Güven, kurumsallık, sakinlik.
    - *Turuncu:* Sıcaklık, samimiyet, dinamizm.
    - *Yeşil:* Doğa, huzur, sürdürülebilirlik.
    - *Siyah:* Güç, prestij, lüks.

---

## 11. Haftanın Ödevi / Araştırma Sorusu

- XAML içerisinde bir `Label` bileşeni **aynı anda hem `Bold` hem `Italic`** nasıl yapılır? (XAML sözdiziminde `FontAttributes="Bold, Italic"` veya alternatif C# kodlama yöntemlerinin araştırılması).

---

# 14 Ekim 2026

---

- **Konu:** Slider, Stepper, Button Kontrolleri, Grid Mimarisi ve Renk Sistemleri
- **Hedef:** XAML ve C# ile dinamik mobil arayüz geliştirme
- **Tarih:** 14 Ekim 2026

---

## 1. Slider (Kaydırıcı) Kontrolü

Slider, kullanıcıdan kaydırma yoluyla sayısal değer almak için kullanılan bir arayüz elemanıdır.

- **Varsayılan Değer Aralığı:** Varsayılan olarak `0.0` ile `1.0` arasında ondalıklı (`double`) değer üretir. İhtiyaca göre bu aralık genişletilebilir.
- **Temel Özellikleri:**
    - `Minimum`: Slider'ın en solundaki başlangıç/alt sınır değeridir (Örn: Not girişi için `0`).
    - `Maximum`: Slider'ın en sağındaki bitiş/üst sınır değeridir (Örn: Not girişi için `100`).
    - `Value`: Slider'ın o anki seçili değerini belirtir (koddan okunabilir veya atanabilir; örn: `Value="50"` verildiğinde çubuk tam ortaya konumlanır).
- **Değer Atama Kuralları:**
    - `Minimum` değeri her zaman `Maximum` değerinden küçük olmalıdır.
    - Eğer `Value` özelliği `Maximum`'dan büyük verilirse, değer otomatik olarak `Maximum` sınırına çekilir; `Minimum`'dan küçük verilirse `Minimum` değerine çekilir.
    - Negatif sayılarla çalışırken mutlak değer büyüklüklerine dikkat edilmelidir (Örn: `20`, `10`'dan daha küçüktür).
- **Olay (Event):**
    - `ValueChanged`: Kaydırıcının değeri her değiştiğinde tetiklenir (Örn: `sldNot_ValueChanged`).

---

## 2. Sayısal Dönüşüm ve Hassasiyet Filtreleme (Math.Round)

Slider, kaydırma esnasında çok basamaklı ondalıklı değerler üretir. Bu değerlerin filtrelenmesi ve istenen formata dönüştürülmesi gerekir:

- **Tamsayıya Çevirme (Tip Dönüşümü):**
    - Not girişi gibi durumlarda tamsayı gerekiyorsa C# tarafında `(int)` tür dönüşümü (cast) yapılarak `Label`'a aktarılır.
- **Ondalıklı Basamak Sabitleme (Çarpma ve Yuvarlama Taktiği):**
    - Örneğin GANO/Not ortalaması gibi iki basamaklı hassasiyet gerektiren değerlerde (ör. `3.528` yerine `3.53` elde etmek için):
        
        $$
        \text{Sonuç} = \frac{\text{Math.Round}(\text{Değer} \times 100)}{100}
        $$
        
    - Bu yöntemle değer önce 100 ile çarpılarak tamsayıya yuvarlanır, ardından tekrar 100'e bölünerek virgülden sonra tam iki basamak kalması sağlanır.

---

## 3. Dijital Renk Sistemleri ve Renk Uzayları (Color Spaces)

.NET MAUI'de renk tanımlamaları önceden tanımlı renk adları (Named Colors), Hexadecimal kodlar (`#RGB`, `#ARGB`, `#RRGGBB`, `#AARRGGBB`) veya renk uzayı fonksiyonları ile yapılabilir.

- **RGB (Red, Green, Blue):**
    - Ekranlar ve elektronik cihazların kullandığı ana modeldir. Piksel arkasındaki kırmızı, yeşil ve mavi ışık kanallarının birleşimiyle yaklaşık 16.7 milyon renk tonu elde edilir.
    - Üç rengin tamamen kapalı olması ($0$) **Siyah**, hepsinin tam güçte yanması ($255$ veya $1.0$) **Beyaz** oluşturur.
    - Üç kanalın değerleri birbirine eşit olduğunda grinin tonları elde edilir.
    - Kırmızı + Yeşil = Sarı, Kırmızı + Mavi = Macenta/Fuşya, Yeşil + Mavi = Turkuaz (Cam Göbeği).
- **Alpha (Kanalı):** Şeffaflık/opaklık değeridir. $1$ veya $255$ tam opak, $0$ ise tamamen saydamdır.
- **HSL / HSV (Hue, Saturation, Lightness/Value):**
    - Özellikle boyacılık ve resim sanatında kullanılan, insan algısına daha uygun renk modelidir.
    - **Hue ($H$):** Gökkuşağı renk çemberidir (0–360 derece).
    - **Saturation ($S$):** Rengin merkezden dışa doğru saflaşması/doygunluğu.
    - **Value / Lightness ($V/L$):** Rengin parlaklık/açıklık düzeyi.

---

## 4. Slider'ın Görsel Özellikleri ve İkon Eklenmesi

- `MinimumTrackColor`: Çubuğun sol tarafında (geçilen kısım) kalan çizgi rengi.
- `MaximumTrackColor`: Çubuğun sağ tarafında (kalan kısım) kalan çizgi rengi.
- `ThumbColor`: Kaydırma düğmesinin (başparmak tırnağı / tutamaç) rengi.
- `ThumbImageSource`: Tutamaç yerine özel bir resim/ikon yerleştirilmesini sağlar.
    - **Dosya Kuralları:** Eklenen ikon dosyaları `Resources/Images` klasörüne kopyalanmalıdır. Android ve iOS (Linux tabanlı yapıları gereği) dosya adlarında büyük harf, Türkçe karakter ve boşluk kabul etmez; dosya adları tamamen **küçük harf** olmalı ve boşluk yerine **alt çizgi (`_`)** kullanılmalıdır.
    - Yeni resim eklendiğinde projenin yeniden başlatılması gerekir.

---

## 5. Stepper (Adımlayıcı) Kontrolü

Butonlara basarak değeri adım adım artırıp azaltmak için kullanılır.

- **Temel Özellikleri:**
    - `Minimum` / `Maximum`: Değer sınırları.
    - `Increment`: Butona her basıldığında değerin ne kadar artıp azalacağını belirler (Örn: GANO için `0.01`).
    - `Value`: Başlangıç veya geçerli değer.
- **Slider ve Stepper'ın Birlikte Kullanımı:**
    - Slider dar alanlarda hassas ayarlama yapmayı zorlaştırabilir (ör. 25'ten 28'e atlayabilir, 26'yı tutturmak zor olabilir).
    - Bu nedenle kaba ayar **Slider** ile yapılırken, hassas ince ayar yanına eklenen **Stepper** ile yapılır. İki kontrolün `ValueChanged` olayları birbirine bağlanarak değerleri senkronize edilir.
- `Rotation`: Kontrolü döndürür (Örn: `Rotation="-90"` verilerek Stepper yataydan dikey konuma getirilebilir).

---

## 6. Grid (Izgara) Mimarisi ile Arayüz Düzenleme

`StackLayout`'un `FillAndExpand` gibi eski esneme özellikleri yeni standartlarda kısıtlandığı için, esnek ve ölçeklenebilir arayüzlerde **Grid** kullanılır:

- `RowDefinitions`: Satır tanımları (Yükseklikler:  oransal, `Auto` içerik kadar, ya da sabit piksel).
- `ColumnDefinitions`: Sütun tanımları (Genişlikler: `4*`, `1*` veya sabit piksel).
- `Grid.Row` ve `Grid.Column`: Kontrolün yerleşeceği satır ve sütun indeksi (0'dan başlar).
- `Grid.ColumnSpan`: Bir kontrolün birden fazla sütunu kaplamasını sağlar (Örn: `ColumnSpan="2"`).
- `RowSpacing` ve `ColumnSpacing`: Satırlar ve sütunlar arasındaki boşluk mesafesi.
- `Padding`: Grid'in kenarlarından içeriye doğru bırakılacak boşluk (Tek değer: dört taraf; Çift değer: yatay-dikey; Dört değer: Sol, Üst, Sağ, Alt - saat yönü).

---

## 7. Button (Düğme) Kontrolü ve Gelişmiş Özellikleri

Düğmeler kullanıcı etkileşimini tetikleyen en temel bileşenlerdir.

- **Çerçeve ve Şekil:**
    - `BorderColor`: Çerçeve rengi.
    - `BorderWidth`: Çerçeve kalınlığı (Piksel cinsinden).
    - `CornerRadius`: Köşe yuvarlama yarıçapı. Buton yüksekliğinin tam yarısı verildiğinde köşeler tam ovalleşir; yarısından büyük değer verilirse elips formuna kayar.
- **Tipografi ve Metin:**
    - `Text`, `TextColor`, `FontAttributes="Bold"`, `FontSize`.
    - `CharacterSpacing`: Düğme metnindeki harf aralığı mesafesi.
    - `TextTransform`: Metni otomatik büyük (`Uppercase`) veya küçük (`Lowercase`) harfe çevirir. *(Not: Türkçe karakterlerde 'ı/i' dönüşüm sorunlarına dikkat edilmelidir).*
    - `LineBreakMode`: Metin sığmadığında nasıl davranılacağını belirler (`NoWrap`, `WordWrap`, `CharacterWrap`, `HeadTruncation`, `TailTruncation`). Windows masaüstünde kırpmalar çoğunlukla `TailTruncation` (sona üç nokta) olarak işlenir.
- **Görsel İçerik:**
    - `ImageSource`: Düğmeye ikon ekler.
    - `ContentLayout`: İkon ile metnin birbirine göre konumunu ve aralarındaki boşluğu belirler (`Top`, `Bottom`, `Left`, `Right` ve boşluk pikseli; örn: `ContentLayout="Left,10"`).
- **Olay ve Bildirim:**
    - `Clicked`: Tıklama olayı.
    - `DisplayAlert("Başlık", "Mesaj", "Kapat Butonu Metni")`: Tıklama sonrasında kullanıcıya pop-up mesaj penceresi gösterir.

---

## 8. Verilen Uygulama / Ödev Görevi

Öğrencilerden yaratıcılıklarını kullanarak sadece şu kontrolleri barındıran işlevsel ve çalışan bir uygulama tasarlamaları istenmiştir:

- `Label`
- `Entry`
- `Slider`
- `Stepper`
- `Button`

---

# 21 Ekim 2026

---

- **Konu:** `Image` (Resim) Kontrolü, Vektörel/Raster Formatlar, `Aspect` Oranları, Animasyonlu GIF'ler, Dinamik Kaynak Yönetimi ve İkon Fontları

---

## 1. Giriş ve Proje Görevi (Kart Eşleştirme Oyunu)

- Derse hazırlık olarak Türkiye Futbol Federasyonu (TFF), Süper Lig ve Türk futbol takımlarına ait yaklaşık 120 adet logo (özellikle **SVG** formatında) temin edilmiştir.
- **Haftalık Proje / Ödev:** Öğrencilerden bu logoları kullanarak bir **"Kart Eşleştirme Oyunu"** geliştirmeleri istenmiştir.
    - **Oyun Mantığı:** Ekranda kapalı kartlar yer alır. Kullanıcı iki kart açar; görseller eşleşirse kartlar açık kalır (veya silinir/puan eklenir), eşleşmezse tekrar kapanır. Amaç en az hamle ile tüm kartları eşleştirmektir.
- Bu proje altyapısını kurabilmek için dersin ana odağı .NET MAUI'de **`Image`** bileşeni ve görsel yönetimidir.

---

## 2. Görsel Formatları: Vektörel (SVG) ve Raster (PNG, JPG, GIF)

| Format Türü | Formatlar | Özellikler ve Kullanım Alanları |
| --- | --- | --- |
| **Vektörel (Vector)** | **SVG** | Çizgiler ve matematiksel eğrilerle tanımlanır. Çözünürlükten bağımsızdır; ne kadar büyütülürse büyütülsün pikselleşme ve kalite kaybı **yaşanmaz**. .NET MAUI logolarda, uygulama simgelerinde ve açılış (splash) ekranlarında SVG'yi öncelikli olarak tercih eder. |
| **Piksel Tabanlı (Raster)** | **PNG** | Taşınabilir ağ grafiğidir (Portable Network Graphics). Saydam (transparan/alpha) arka planı destekler. Kalitelidir ancak boyutu büyütüldüğünde pikselleşme oluşur. |
| **Piksel Tabanlı (Raster)** | **JPEG / JPG** | Fotoğraflar için ideal, yüksek sıkıştırma sağlayan kayıplı bir formattır. **Saydam arka planı desteklemez.** |
| **Piksel Tabanlı (Raster)** | **GIF** | Hareketli/animasyonlu görselleri ve saydamlığı destekler. Maksimum 256 renk paletiyle sınırlıdır. |
| **Modern Formatlar** | **WebP** | Google tarafından geliştirilen, hem yüksek sıkıştırma hem saydamlık sunan modern web formatıdır. |
- **Ekran Çözünürlüğü Gerçeği:** Günümüz akıllı telefonlarının ekran çözünürlükleri (FHD+, 2K, QHD), çoğu standart bilgisayar monitöründen daha yüksektir. Bu sebeple raster (piksel) tabanlı görsel kullanılırken çözünürlüğün yüksek seçilmesi; imkân varsa doğrudan SVG tercih edilmesi gerekir.

---

## 3. Görsellerin Projeye Eklenmesi ve Dosya İsimlendirme Kuralları

1. **Klasör Yapısı:**
    - Görseller proje içerisindeki **`Resources/Images`** klasörüne eklenir.
    - `Resources/Images` altındaki görsellere XAML içinde doğrudan dosya adıyla erişilebilir:
        
        ```xml
        <Image Source="galatasaray1.png" />
        ```
        
    - İstenirse alt klasör açılabilir (Örn: `Resources/Images/takimlar/`). Bu durumda yol `Source="takimlar/galatasaray1.png"` şeklinde belirtilir.
2. **Kritik İsimlendirme Kuralları (Android ve iOS Derleme Hatalarını Önleme):**
    - Android ve iOS işletim sistemleri Linux/Unix çekirdeği tabanlı dosya sistemlerine sahiptir.
    - Dosya isimlerinde **kesinlikle Türkçe karakter** (`ç, ğ, ı, ö, ş, ü`) ve **boşluk** kullanılmamalıdır.
    - Dosya adları **tamamen küçük harf** olmalı, özel işaret veya tire () yerine alt çizgi (`_`) tercih edilmelidir (Örn: `fenerbahce_logo.png`).
3. **Derleme Gereksinimi:** Projenin `Resources` klasörüne yeni bir resim veya font eklendiğinde Hot Reload tek başına yetmez; kaynakların derlenip cihaza aktarılması için uygulamanın **yeniden başlatılması (Rebuild/Restart)** gerekir.

---

## 4. `Image` Kontrolünün En Önemli Özelliği: `Aspect` (En-Boy Oranı Yönetimi)

*(Hoca bu konunun sınavda kesinlikle sorulacağını özellikle vurgulamıştır).*

Bir resmin ayrılan kutucuğa (`WidthRequest` ve `HeightRequest`) nasıl yerleşeceğini `Aspect` özelliği belirler. 4 seçeneği vardır:

```
+---------------------------------------------------------------------------------+
|                                 ASPECT TÜRLERİ                                  |
+---------------------------------------------------------------------------------+
| AspectFit   : En-boy oranını korur. Resmin tamamını kutuya sığdırır.            |
|               Kutu ile resim oranı uyuşmazsa kenarlarda boşluk (bant) kalır.   |
| AspectFill  : En-boy oranını korur. Kutuyu tamamen doldurur. Boşluk kalmaz,     |
|               ancak sığmayan kısımlar kırpılır (crop edilir).                   |
| Fill        : En-boy oranını BOZAR. Resmi kutunun enine ve boyuna esnetir.     |
|               Görsel basık/yayvanlaşır. Fotoğraflar için tavsiye edilmez.       |
| Center      : Resmi boyutlandırmaz (1:1 orijinal piksel boyutu). Kutu içine    |
|               ortalayarak yerleştirir; taşan kısımlar görünmez.                 |
+---------------------------------------------------------------------------------+
```

- **Responsive Tasarım Örneği:** Web sitelerinde manşet haber görsellerinde genellikle `AspectFill` veya `Center` kullanılır; böylece ekran daraldığında görselin sadece ortası odak noktası olarak kalır, yanlar kesilir. Ürün detaylarında ise ürünün hiçbir parçasının kaybolmaması için `AspectFit` tercih edilir.

---

## 5. Animasyonlu GIF Kullanımı ve `IsAnimationPlaying`

.NET MAUI, animasyonlu GIF dosyalarını üçüncü parti bir kütüphaneye ihtiyaç duymadan doğrudan oynatabilir:

- **XAML Tanımı:**
    
    ```xml
    <Image x:Name="imgAnime"
           Source="anime.gif"
           IsAnimationPlaying="True"
           HeightRequest="250"
           WidthRequest="250"
           Aspect="AspectFit" />
    ```
    
- **C# ile Oynatma / Duraklatma (Toggle) Kontrolü:**
Bir buton aracılığıyla animasyon tek satırda tersine çevrilebilir ve buton metni güncellenebilir:
    
    ```csharp
    private void btnPlay_Clicked(object sender, EventArgs e)
    {
        // Animasyonun durumunu tersine çevir (true ise false, false ise true)
        imgAnime.IsAnimationPlaying = !imgAnime.IsAnimationPlaying;
    
        // Buton üzerindeki metni güncelle
        btnPlay.Text = (btnPlay.Text == "Oynat") ? "Durdur" : "Oynat";
    }
    ```
    

---

## 6. İnternetten Yüklenen Görseller ve `IsLoading` Özelliği

- Uzak sunucudan (`https://...`) resim çekilirken görselin anlık indirme durumunu denetlemek için **`IsLoading`** (`bool`) özelliği kullanılır.
- `IsLoading` salt-okunur (read-only) bir özelliktir.
- **Kullanım Senaryosu:** `ActivityIndicator` (yükleniyor çarkı/spinner) bileşeninin `IsRunning` ve `IsVisible` özellikleri `Image.IsLoading` değerine bağlanır (Data Binding). Resim internetten inerken ekranda yükleme halkası döner; indirme tamamlanıp `IsLoading = false` olduğunda indikatör gizlenir ve asıl görsel ekrana gelir.

---

## 7. Dinamik Olarak Kod Tarafından (C#) Resim Değiştirme

Çalışma zamanında (runtime) bir butona basıldığında resmi listeden sırayla değiştirmek için `ImageSource.FromFile(...)` yöntemi kullanılır:

```csharp
public partial class MainPage : ContentPage
{
    // Resim adları dizisi (Resources/Images altında tanımlı olanlar)
    string[] resimler = { "dut.png", "soyut.png", "osimhen.png", "dotnet_bot.png" };
    int sayac = 0;

    public MainPage()
    {
        InitializeComponent();
    }

    private void btnDegistir_Clicked(object sender, EventArgs e)
    {
        // Sayaç değerini dizi boyutu içinde döngüye sokmak için mod (%) alma işlemi
        sayac = (sayac + 1) % resimler.Length;

        // Görselin kaynağını dinamik olarak güncelle
        imgDegisen.Source = ImageSource.FromFile(resimler[sayac]);
    }
}
```

---

## 8. `IsOpaque` Özelliği ve Çizim Optimizasyonu

- **`IsOpaque` (`bool`):** Görselin arka planının tamamen opak (geçirgen olmayan) olup olmadığını render motoruna bildiren performans bayrağıdır.
- Varsayılan değeri `false`'tur (yani saydamlık kanalı dikkate alınır).
- Eğer görselin saydamlık (alpha) içermediği kesinse `IsOpaque="True"` yapılarak çizim motorunun pikselleri üst üste harmanlama (alpha blending) yükü hafifletilebilir.

---

## 9. Özel Yazı Tipleri (Custom Fonts) ve İkon Fontları (Font Icons)

.NET MAUI'de görsel dosyaları yerine vektörel ikon kütüphaneleri (FontAwesome, Ionicons vb.) yazı tipi olarak yüklenebilir.

### Adım Adım Font ve İkon Fontu Yükleme:

1. **İndirme ve Konumlandırma:** Font dosyası (`.ttf` veya `.otf`) indirilip **`Resources/Fonts`** klasörüne atılır (Örn: `ionicons.ttf`).
2. **Kayıt (`MauiProgram.cs`):** Fontun uygulama başlangıcında sisteme tanıtılması gerekir:
    
    ```csharp
    builder
        .UseMauiApp<App>()
        .ConfigureFonts(fonts =>
        {
            fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
            fonts.AddFont("Anton-Regular.ttf", "Anton");
            fonts.AddFont("ionicons.ttf", "IonIcons"); // Font dosyası ve alias adı
        });
    ```
    
3. **XAML'da Metin Fontu Olarak Kullanım:**
    
    ```xml
    <Label Text="Özel Fontlu Metin" FontFamily="Anton" FontSize="24" />
    ```
    
4. **XAML'da İkon (FontImageSource) Olarak Kullanım:**
İkon fontları metin değil glif (glyph) karakter kodları barındırır. Bu glif kodu `&#x....;` formatında verilir:
    
    ```xml
    <Image>
        <Image.Source>
            <FontImageSource FontFamily="IonIcons"
                             Glyph="&#xf10a;"
                             Color="Black"
                             Size="44" />
        </Image.Source>
    </Image>
    ```
    

---

## 10. Özet ve Haftaya Hazırlık

- Bu derste görsel formatlarının farkları, `Aspect` oranlarının ekran davranışları, animasyonlu GIF oynatma/durdurma mekaniği, çalışma zamanında kaynak yönetimi ve ikon fontlarının kullanımı uygulamalı olarak tamamlanmıştır.
- **Gelecek Hafta:** Verilen futbol takımı logoları kullanılarak tasarlanacak olan **Kart Eşleştirme Oyunu** kontrol edilecek ve çoklu kontrol etkileşimlerine devam edilecektir.

---

# 28 Ekim 2026

## Part 1

- **Tarih:** 28 Ekim 2026 (Part 1)
- **Kullanılan Teknoloji / Dil:** C# / .NET MAUI (XAML & C#)
- **Konu:** Ergonomi ve Donanım Bilgilendirmesi, Geçen Haftanın Proje İncelemesi (Kart Eşleştirme Oyunu), .NET MAUI Derleme Hatalarının Çözümü, `ActivityIndicator` (Etkinlik Göstergesi), `Border` (Çerçeve) Mimarisi ve Gelişmiş `Stroke` Özellikleri

---

## 1. Giriş ve Donanım / Ergonomi Notları

- **Karpal Tünel Sendromu ve Fare Seçimi:**
    - Masaüstü ve dizüstü bilgisayarlarda uzun süreli standart/küçük fare kullanımı el bileğine aşırı yük bindirerek karpal tünel sendromuna yol açabilmektedir.
    - Ergonomik (özellikle dikey / vertical) fareler elin doğal duruşunu korur ve hareketi bilek yerine dirsekten yaptırdığı için tendon sıkışmalarını önler. Mobil yazılımcıların çalışma sağlığı açısından donanım ergonomisine dikkat etmesi önerilir.

---

## 2. Geçen Haftanın Ödevi: Kart Eşleştirme Oyunu İncelemesi ve Geri Bildirimler

- Önceki haftalarda verilen Türk takımlarının logolarıyla **Kart Eşleştirme Oyunu** projeleri incelenmiştir:
    - **Uygulama Mimarisi Tavsiyesi:** Oyunda doğrudan sabit sayıda (örn. 20 kart) başlamak yerine kademeli zorluk (level) yapısı kurulmalıdır (örneğin 2 çift ile başlayıp 3, 4, 5 çift şeklinde ilerleyen seviyeler).
    - **Ticarileştirme:** Oyun seviyeli yapıya dönüştürülüp Google Play Store veya App Store'a yüklendiğinde kullanıcı deneyimi (UX) açısından çok daha başarılı bir portföy projesi haline gelecektir.

---

## 3. Mac Cihazı Olmayanlar İçin iOS / iPhone Test Alternatifi

- .NET 10 MAUI sürümünde Apple kısıtlamaları nedeniyle doğrudan Windows'a takılan iPhone'a derleme yapmak için ağda bir Mac cihazı (Pair to Mac) zorunludur.
- **Geçici Geliştirici Çözümü:**
    - Bilgisayarına **Visual Studio 2022** ve **.NET 9** kuran geliştiriciler, Microsoft ile Apple arasındaki köprülerin henüz tam kopmadığı bu eski sürümde iPhone cihazlarını doğrudan USB kablosuyla bağlayıp Hot Restart üzerinden yerel test yapabilirler.
    - Ancak .NET 9 ile .NET 10 MAUI arasında bazı API ve XAML bileşen farklılıkları olduğu göz önünde bulundurulmalıdır.

---

## 4. .NET MAUI Derleme / Cache Hataları ve Çözüm Adımları

Visual Studio'da yeni bir MAUI projesi açıldığında paketler yüklenmeden önce kod yazmaya başlanırsa `ScrollView`, `ContentPage`, `VerticalStackLayout` gibi temel sınıflar tanınmayabilir veya derleme kilitlenebilir.

- **Çözüm Yolu:**
    1. Visual Studio'yu kapatın.
    2. Proje dizininde yer alan **`bin`** ve **`obj`** klasörlerini (özellikle `bin/Debug` veya `bin/Release` altındaki tüm önbellek dosyalarını) tamamen silin.
    3. Visual Studio'yu tekrar açıp projeyi yeniden derleyin (**Rebuild**).

---

## 5. `ActivityIndicator` (Etkinlik / Yükleniyor Göstergesi) Kontrolü

Uzun süren arka plan işlemlerinde (veritabanı sorguları, internetten dosya/resim indirme, koleksiyon taramaları) kullanıcının cihazın donduğunu zannetmemesi için döner halka (spinner) animasyonu gösteren kontroldür.

### A. Temel Özellikler

- **`IsRunning` (`bool`):** Animasyonun aktif olarak dönüp dönmediğini belirler. `false` yapıldığında kontrol ekranda tamamen gizlenir / durur.
- **`Color`:** Göstergenin rengidir. Renk isimleri (`Red`), 3 veya 6 haneli Hex kodları (`#F00`, `#FF0000`), opaklık içeren Alpha Hex kodları (`#8F00`, `#80FF0000`) formatında tanımlanabilir.

### B. XAML ve C# Örneği (Manuel Buton ile Aç/Kapa)

#### XAML:

```xml
<VerticalStackLayout Spacing="15" Padding="20">
    <ActivityIndicator x:Name="indicatorYukleniyor"
                       Color="Red"
                       IsRunning="False" />

    <Button x:Name="btnKontrol"
            Text="Oynat"
            Clicked="btnKontrol_Clicked" />
</VerticalStackLayout>
```

#### C# (Code-Behind):

```csharp
private void btnKontrol_Clicked(object sender, EventArgs e)
{
    if (indicatorYukleniyor.IsRunning)
    {
        indicatorYukleniyor.IsRunning = false;
        btnKontrol.Text = "Oynat";
    }
    else
    {
        indicatorYukleniyor.IsRunning = true;
        btnKontrol.Text = "Durdur";
    }
}
```

*(Gerçek hayat senaryolarında bir butondan ziyade asenkron bir `async/await` işlemi başlamadan önce `IsRunning = true`, işlem bittiğinde `false` yapılır).*

---

## 6. `BlazorWebView` Kontrolü Hakkında Bilgi

- Önceden hazırlanmış bir Blazor web uygulamasını doğrudan .NET MAUI içine gömüp hibrit (Hybrid) mobil uygulama olarak çalıştırmak için kullanılır.
- Mobil uygulamanın içinde tam ekran, yerel bir tarayıcı motoru (Edge WebView2 / WKWebView / Chrome tabanlı) barındırarak Blazor bileşenlerini çalıştırır.

---

## 7. `Border` (Çerçeve) Kontrolü ve Mimarisi

İçerisindeki herhangi bir görseli (`Image`), metni (`Label`) veya düzeni (`Layout`) çevreleyen, kenarlık çizgilerini ve köşe yarıçaplarını gelişmiş düzeyde biçimlendiren bir kapsayıcıdır.

```xml
<Border Stroke="Black"
        StrokeThickness="2"
        Padding="10">
    <Image Source="bayrak.png"
           WidthRequest="227"
           HeightRequest="164" />
</Border>
```

---

## 8. Gelişmiş Kenarlık (`Stroke`) ve Şekil (`StrokeShape`) Özellikleri

| Özellik | Tanım ve Kullanım Şekli |
| --- | --- |
| **`Stroke`** | Çerçeve çizgisinin fırça/renk tanımıdır (`Stroke="Red"`, `Stroke="Black"`). |
| **`StrokeThickness`** | Çizgi kalınlığıdır (piksel cinsinden, örn: `StrokeThickness="4"`). |
| **`StrokeShape`** | Çerçevenin formunu belirler. `Rectangle` (düz dikdörtgen) veya `RoundRectangle` (köşeleri yuvarlatılmış dikdörtgen) alır. |
| **`CornerRadius` (RoundRectangle)** | 4 köşe için ayrı ayrı yarıçap tanımlanabilir: Sol-Üst, Sağ-Üst, Sağ-Alt, Sol-Alt (örn: `StrokeShape="RoundRectangle 40,0,40,0"`). |
| **`StrokeDashArray`** | Çerçevenin kesikli/noktalı çizgi desenidir. Çizgi uzunluğu ve boşluk uzunluğu çiftler halinde verilir (örn: `1,1` eşit noktalı; `4,1,1,1` teknik eksen çizgisi deseni). |
| **`StrokeDashOffset`** | Kesikli çizgi deseninin başladığı piksel kaydırmasını (ofset) belirler (ondalıklı değerler alabilir). |
| **`StrokeLineCap`** | Kesikli çizgilerin uç noktalarının bitiş biçimidir: `Flat` (düz kesim), `Round` (yuvarlatılmış uç), `Square` (kare uç). |
| **`StrokeLineJoin`** | Köşelerin birleşim geometrisidir: `Miter` (sivri/keskin köşe), `Bevel` (pah kırılmış/düz kesilmiş köşe), `Round` (yuvarlatılmış köşe). |
| **`StrokeMiterLimit`** | Miter birleşiminin sivrilik sınır oranıdır (genellikle çizgi kalınlığının yarısı baz alınır). |

> **Platform Farklılıkları Notu:** .NET MAUI doğrudan yerel (native) bileşenleri kullandığı için `StrokeLineCap` ve `StrokeLineJoin` gibi bazı gelişmiş çizim parametreleri Android ve iOS'ta eksiksiz çizilirken, Windows masaüstü platformunda varsayılan render motoru nedeniyle farklı görünebilir.
> 

---

## 9. `Padding` ve `Thickness` Mantığı (Saat Yönü Kuralı)

`Padding` ve `Margin` gibi boşluk değerleri `Thickness` sınıfından türetilir ve parametre sayısına göre şu şekilde işlenir:

1. **Tek Değer (`10`):** Dört kenardan da eşit 10 piksel boşluk bırakır.
2. **İki Değer (`20, 5`):** `[Yatay (Sol-Sağ)], [Dikey (Üst-Alt)]` anlamına gelir.
3. **Dört Değer (`10, 5, 20, 15`):** Sol kenardan başlar ve **saat yönünde** ilerler:
    - **1. Değer:** Sol (Left)
    - **2. Değer:** Üst (Top)
    - **3. Değer:** Sağ (Right)
    - **4. Değer:** Alt (Bottom)

---

## 10. Özet ve Bir Sonraki Bölüm (Part 2) Beklentisi

- Bu derste görsel arayüzlerde kullanıcıyı bilgilendiren `ActivityIndicator` ve içeriklerin etrafına profesyonel kenarlıklar tasarlamayı sağlayan `Border` kontrolü tüm parametreleriyle incelenmiştir.
- Verilen 20 dakikalık aranın ardından dersin ikinci kısmında (Part 2) diğer gelişmiş MAUI görünümleriyle devam edilecektir.

## Part 2

- **Tarih:** 28 Ekim 2026 (Part 2)
- **Kullanılan Teknoloji / Dil:** C# / .NET MAUI (XAML & C#)
- **Konu:** `BoxView`, `CheckBox`, `Switch` Kontrolleri, Grid ile Hassas Hizalama, Dinamik Renk Yönetimi ve Seviyeli Kart Eşleştirme Projesi

---

## 1. `BoxView` (Kutu / Dikdörtgen Görünümü) Kontrolü

`BoxView`, ekrana basit bir renkli kutu, ayırıcı çizgi veya geometrik şekil yerleştirmek için kullanılan temel bir çizim kontrolüdür.

### A. Temel Özellikleri ve Davranışı

- **Boyut Zorunluluğu:** `BoxView` bileşenine `HeightRequest` ve `WidthRequest` değerleri verilmezse ekranda görünmez; bu nedenle en ve boy boyutlarının açıkça tanımlanması gerekir.
- `Color`: Kutunun dolgu rengini belirler (Örn: `Color="BlueViolet"`, `Color="Black"`).
- `CornerRadius`: Köşeleri yuvarlatma yarıçapıdır.

### B. `CornerRadius` ile Geometrik Şekil Üretimi

- **Daire (Circle) Oluşturma:**
Eğer kutu bir kare ise (örn. `WidthRequest="100"` ve `HeightRequest="100"`), `CornerRadius` değeri kenar uzunluğunun tam yarısı (`50`) yapıldığında kutu kusursuz bir **daireye** dönüşür.
- **Kapsül / Stadyum / Terminal Şekli:**
Genişlik yükseklikten büyükse (örn. $200 \times 100$) ve `CornerRadius` yüksekliğin yarısı (`50`) verilirse uçları yuvarlak, yatay bir hap/kapsül şekli elde edilir.
- **Kritik Kural:** `CornerRadius` değerini kenarın yarısından daha büyük yapmak şekli daha fazla değiştirmez; yarıçap sınırından sonrası işlevsizdir.

### C. Kullanım Alanları

- Arayüzde elemanlar arasına dikey/yatay renkli ayırıcı çizgiler çekmek.
- İlerleyen aşamalarda `Gradient` (geçişli renkler) verilerek modern arka plan kartları ve dolgu blokları oluşturmak.

---

## 2. Gelecek Konular: Koleksiyon Görünümleri

Koleksiyon yapılarını ve veri listelerini ekranda göstermek için kullanılan şu gelişmiş kontrollerin ilerleyen derslerde toplu olarak işleneceği belirtilmiştir:

- `CarouselView`
- `CollectionView`
- `ListView`
- `TableView`

---

## 3. `CheckBox` (Onay Kutusu) Kontrolü

Kullanıcıdan "Evet / Hayır" veya mantıksal (`true` / `false`) veri almak için kullanılan iki durumlu seçim bileşenidir.

### A. Yapısal Özellikler ve Kısıtlar

- **Etiket (Label) Kısıtı:** .NET MAUI'de `CheckBox` kontrolünün kendi üzerinde doğrudan bir metin (`Text` / `Caption`) özelliği **bulunmaz**.
- Açıklama metni eklemek için yanına bir `Label` konulmalı ve her ikisi bir düzen (`HorizontalStackLayout` veya `Grid`) içine alınmalıdır.
- `IsChecked` (`bool`): Kutunun işaretli olup olmadığını belirler (`true` / `false`). Varsayılanı `false`'tur.
- `Color`: Onay kutusunun ve içindeki "tik" işaretinin rengini belirler (Varsayılan .NET MAUI rengi mor tonlarındadır).
- `CheckedChanged`: Kullanıcı kutuyu işaretlediğinde veya işareti kaldırdığında tetiklenen olaydır (event).

---

## 4. `CheckBox` ile Dinamik Renk Değişimi (C# Code-Behind)

Kullanıcı kutuyu işaretlediğinde yeşil, işareti kaldırdığında kırmızı renk alması için `CheckedChanged` olayı kullanılır:

### XAML:

```xml
<CheckBox x:Name="chkOnay"
          IsChecked="False"
          CheckedChanged="chkOnay_CheckedChanged" />
```

### C# (Code-Behind):

```csharp
private void chkOnay_CheckedChanged(object sender, CheckedChangedEventArgs e)
{
    // Olayı tetikleyen nesneyi CheckBox tipine dönüştürme
    var onayKutusu = sender as CheckBox;

    if (onayKutusu != null)
    {
        // İşaretli ise yeşil (RGB: 0, 192, 0), işaretsiz ise kırmızı (RGB: 255, 0, 0)
        onayKutusu.Color = onayKutusu.IsChecked
            ? Color.FromRgb(0, 192, 0)
            : Color.FromRgb(255, 0, 0);
    }
}
```

---

## 5. `Switch` (Açma / Kapama Anahtarı) Kontrolü

`CheckBox` ile aynı mantıkta (`true`/`false`) çalışan fakat mobil işletim sistemlerine özgü kaydırmalı anahtar görünümüne sahip bileşendir.

### A. Temel Özellikleri

- Genellikle arayüzde sağ tarafa konumlandırılır.
- `IsToggled` (`bool`): Anahtarın açık mı kapalı mı olduğunu belirtir.
- `OnColor`: Anahtar açık (`true`) konumdayken arka plan rengi (Örn: `ForestGreen`).
- `OffColor`: Anahtar kapalı (`false`) konumdayken arka plan rengi (Örn: `Red` veya `Silver`). *(CheckBox'ın aksine bu renkler doğrudan XAML üzerinden kod yazmadan ayarlanabilir)*.
- `ThumbColor`: Kaydırılan yuvarlak düğmenin (tutamaç) rengidir (Örn: `Brown`, `White`).

---

## 6. Grid ile Hassas Hizalama (`StackLayout` vs. `Grid`)

Arayüzde solda açıklama metni (`Label`), sağda ise `Switch` veya `CheckBox` bulunması istenildiğinde `HorizontalStackLayout` yetersiz kalabilmektedir:

- **Sorun:** Eski Xamarin standartlarındaki `FillAndExpand` özelliği modern .NET MAUI'de kaldırıldığı için, `HorizontalStackLayout` satırın tamamına yayılmaz ve `HorizontalOptions="End"` bileşeni ekranın en sağına itemez.
- **Çözüm (Grid Kullanımı):** Sayfa satır ve sütunlara bölünür. Metin sol sütuna, `Switch` ise sağ sütuna yerleştirilerek ekran genişliğine göre esnek ve responsive bir yapı elde edilir:

```xml
<Grid ColumnDefinitions="4*, 1*"
      RowDefinitions="Auto, Auto, Auto"
      Padding="10">

    <!-- 1. Şart Satırı -->
    <Label Grid.Row="0" Grid.Column="0"
           Text="Derse devam ettim"
           VerticalOptions="Center" />
    <Switch Grid.Row="0" Grid.Column="1"
            IsToggled="False"
            OnColor="ForestGreen"
            OffColor="Red"
            ThumbColor="Brown"
            VerticalOptions="Center" />

    <!-- 2. Şart Satırı -->
    <Label Grid.Row="1" Grid.Column="0"
           Text="Finalden en az 50 aldım"
           VerticalOptions="Center" />
    <Switch Grid.Row="1" Grid.Column="1"
            IsToggled="False"
            OnColor="ForestGreen"
            OffColor="Red"
            VerticalOptions="Center" />

    <!-- 3. Şart Satırı -->
    <Label Grid.Row="2" Grid.Column="0"
           Text="Ortalamam en az 60"
           VerticalOptions="Center" />
    <Switch Grid.Row="2" Grid.Column="1"
            IsToggled="False"
            OnColor="ForestGreen"
            OffColor="Red"
            VerticalOptions="Center" />
</Grid>
```

*(Not: `0` indeksli satır ve sütunlar varsayılan kabul edildiğinden `Grid.Row="0"` yazılması zorunlu değildir).*

---

## 7. Derleme ve Mono Çalışma Zamanı (Runtime) Hatası

- Android emülatör veya cihaz testlerinde `"Unexpected install output"` gibi dağıtım/yükleme hataları alındığında, .NET MAUI'nin temelinde yer alan **Mono** çalışma zamanı motorunda kilitlenme oluşmuş olabilir.
- **Çözüm:** Visual Studio üst menüsünden *Build > Rebuild Solution (Çözümü Yeniden Derle)* adımı uygulanmalıdır.

---

## 8. Sınıf İçi Laboratuvar Pratiği

Ders esnasında öğrencilerden şu kontrolleri bir arada kullanan bir deneme projesi hazırlamaları istenmiştir:

1. Bir buton ile `IsRunning` durumu açılıp kapatılabilen **`ActivityIndicator`** *(Not: `IsRunning = false` olduğunda gösterge otomatik olarak gizlenir; ekstra `IsVisible` yazmaya gerek yoktur)*.
2. Özel `Stroke`, `Padding` ve `StrokeShape` tanımlanmış **`Border`**.
3. Grid kullanılarak oluşturulmuş **$4 \times 4$'lük `BoxView` matrisi**.
4. Durumuna göre renk değiştiren **`CheckBox`** ve **`Switch`** kontrolleri.

---

## 9. Mesleki Standartlar, Lisanslama ve Yazılım Mühendisliği Üzerine

- **Sektörel Dönüşüm:** Elektrikçilik, optisyenlik, kuaförlük ve gastronomi gibi alanlarda diplomasız/sertifikasız dükkan açma devrinin kapandığı, devlet ve sektör denetimlerinin standartlaştığı vurgulanmıştır.
- **Yazılıma Yansıması:** Benzer standartlaşma ve yasal sorumluluk süreçleri zamanla yazılım ve teknoloji sektöründe de sertleşecektir. Sadece kod yazmak değil; standartlara, güvenliğe ve kullanıcı deneyimi kurallarına tam uyum sağlayan mühendislik disiplini kazanılmalıdır.

---

## 10. Haftalık Büyük Proje Görevi: Seviyeli Kart Eşleştirme Oyunu

Önceki hafta başlanan futbol takımı logolu **Kart Eşleştirme Oyunu**, seviye (level) atlama mekanizmasıyla yeniden geliştirilecektir:

- **Oyun Kuralları:**
    - **Seviye 1:** Ekranda **2 çift (toplam 4 kart)** bulunur. Eşleşmeler tamamlandığında Seviye 2'ye geçilir.
    - **Seviye 2:** Ekranda **3 çift (toplam 6 kart)** yer alır.
    - **Kademeli İlerleme:** Her seviye tamamlandığında kart sayısı 1 çift artarak devam eder.
    - **Üst Sınır:** Oyun **maksimum 10 çift (toplam 20 kart)** seviyesine kadar ulaşacaktır.
- Proje önümüzdeki hafta öğrencilerin kendi cihazlarında veya emülatörlerinde canlı çalışır şekilde teslim alınacaktır.

---

## 11. Kapanış

- 29 Ekim Cumhuriyet Bayramı tebrik edilmiş ve ders tamamlanmıştır.

---

# 4 Kasım 2026

- **Tarih:** 4 Kasım 2026
- **İşlenen Kontroller:** `DatePicker`, `TimePicker`, `Picker`, `Editor` (ve `Entry` ile karşılaştırması)
- **İdari / Kariyer Konuları:** Vize Sınav Formatı, Ulusal Staj Programı (Kariyer Kapısı), İŞKUR Gençlik Programı, Mesleki İngilizce Gelişimi

---

## 1. Giriş ve .NET MAUI Kontrol Ekosistemine Genel Bakış

Dersin başında .NET MAUI arayüz kontrolleri ve ilerleyen haftalarda işlenecek kütüphaneler genel bir harita halinde özetlenmiştir:

- **Geçmiş Haftalardan Hatırlatma:** `Label`, `Button`, `Entry`, `Slider`, `Stepper`, `Image`, `ActivityIndicator`, `Border`, `BoxView`, `CheckBox`, `Switch` kontrolleri tamamlanmıştır.
- **Toplu İşlenecek Koleksiyon Bileşenleri:** `CollectionView`, `ListView`, `TableView`, `CarouselView` gibi veri dizilerini ve modelleri ekranda listeleyen bileşenler ilerleyen haftalarda tek bir mimari başlık altında incelenecektir.
- **Özel Kontroller (`ContentView`):** İleride kendi kullanıcı kontrollerimizi (User Controls) veya koleksiyonlar için karmaşık şablonları geliştirmek amacıyla kullanılacaktır.
- **Diğer MAUI Kontrolleri:**
    - **`ProgressBar`:** Yürütülen bir işlemin yüzde kaçının tamamlandığını gösteren ilerleme çubuğudur.
    - **`RadioButton`:** Birden fazla seçenek arasından yalnızca tek bir seçimin yapılmasına izin veren radyo düğmeleridir.
    - **`RefreshView` & `ScrollView`:** Ekrana doğrudan piksel çizmeyen, kaydırma ve "çek-yenile" (pull-to-refresh) gibi kapsayıcı davranışları yöneten yardımcı elemanlardır.
    - **`SearchBar`:** Arama işlemleri için özel klavye ve olaylara sahip metin kutusudur.
    - **`Shapes` (Şekiller):** `Ellipse`, `Line`, `Polygon`, `Rectangle` ve serbest vektör eğrileri çizmek için kullanılan `Path` bileşenleridir.
    - **`SwipeView`:** Genellikle `ListView`/`CollectionView` satırlarında sağa veya sola kaydırıldığında silme/düzenleme butonlarını açığa çıkaran kapsayıcıdır.
    - **`TwoPaneView`:** Ekranı çift panele (özellikle katlanabilir telefonlarda veya yan yana bölünmüş arayüzlerde) bölmeye yarar.
    - **`WebView`:** Bir web sayfasını doğrudan uygulama içerisine gömmek için kullanılır.
    - **`Entry` vs. `Editor`:** `Entry` tek satırlı veri girişi (ad, soyad, e-posta vb.) sağlarken; `Editor` adres, yorum veya serbest düşünce girişi gibi çok satırlı (multi-line) uzun metinler için kullanılır.

---

## 2. Kariyer, Staj Fırsatları ve Mesleki İngilizce Tavsiyeleri

Teknik geliştirmeye geçilmeden önce yazılım mühendisliği öğrencilerine sektörel tavsiyeler ve fırsatlar aktarılmıştır:

1. **Vize Sınavı Formatı:**
    - Öğrencilerden gelen soru üzerine: Dönem içi vize sınavı laboratuvarda uygulamalı kodlama değil, amfide/sınıfta **yazılı sınav** şeklinde yapılacaktır.
2. **Ulusal Staj Programı (Cumhurbaşkanlığı İnsan Kaynakları Ofisi - CBİKO):**
    - Staj başvurularının başladığı, staj arayan öğrencilerin **Kariyer Kapısı** üzerinden başvuru yapması gerektiği belirtilmiştir.
    - Devlet kurumlarının stajyerlere yasal olarak asgari ücretin en az %30'u (kurum ve çalışan sayısına göre tamamı) tutarında ücret ödemekle yükümlü olduğu hatırlatılmıştır.
3. **Kariyer Planlama Platformu (`kariyerplanlama.gov.tr`):**
    - Üniversitelerin 1. sınıfında verilen Kariyer Planlama dersinin bu platforma entegre edildiği, platform üzerinde Robotik Sistemler, Yapay Zekâ Mühendisliği, Oyun Programcılığı, Siber Güvenlik, Veri Bilimi, Yenilenebilir Enerji ve E-Ticaret için Gıda Fotoğrafçılığı gibi pek çok ücretsiz eğitim ve sertifika programı bulunduğu vurgulanmıştır.
4. **İŞKUR Kampüs / Gençlik Programları:**
    - İŞKUR programlarının il bazında ve takvim sırasına göre etap etap açıldığı, üniversite kontenjanlarının yaklaşık %5'lik bir kitleye (örneğin 15.000 öğrencili bir üniversitede yaklaşık 750 kişiye) imkân sağladığı belirtilmiştir. İlanların İŞKUR ve üniversite duyurularından takip edilmesi gerekmektedir.
5. **Mesleki İngilizce ve BBC 6 Minute English:**
    - Bilgisayar mühendisliği ve yazılım alanındaki güncel teknik kaynakların tamamı İngilizce olduğundan, yabancı dil engelinin aşılması zorunludur.
    - **BTK Akademi** üzerinde A1'den C2'ye kadar ücretsiz seviye kurslarının ve sertifikasyonların bulunduğu belirtilmiştir.
    - **BBC Learning English (6 Minute English):** İşe/okula gidiş gelişlerde (minibüste, serviste) kulaklık takılarak dinlenebilecek en pratik araçtır. Günde sadece 6 dakikada 10 kelime/deyim öğretir; podcast dinleme, metin takibi ve PDF ders materyalleri sunar.

---

## 3. Geliştirme Ortamı Notları ve Framework Sürümü

- Proje `Ders06A` adıyla oluşturulmuştur.
- **.NET Versiyonları:** Uzun süreli destek (LTS) olan **.NET 10** sürümü kullanılmaktadır. Kısa süreli destek (STS) olan .NET 11'in kasım ayının ortalarında çıkacağı, ancak kurumsal ve istikrarlı mobil projelerde her zaman LTS sürümlerin öncelikli olduğu yinelenmiştir.

---

## 4. `DatePicker` (Tarih Seçici) Kontrolü

Mobil platformlarda yerel (native) takvim tekerleğini veya açılır takvim penceresini tetikleyen kontroldür.

```xml
<DatePicker x:Name="dtpTarih"
            MinimumDate="2026/12/15"
            MaximumDate="2026/12/29"
            Date="2026/12/16"
            Format="dd.MM.yyyy"
            FontSize="20"
            FontAttributes="Bold"
            TextColor="Red"
            CharacterSpacing="3"
            Opened="dtpTarih_Opened"
            Closed="dtpTarih_Closed"
            DateSelected="dtpTarih_DateSelected" />
```

### A. Temel Özellikler

- **`MinimumDate`:** Seçilebilecek en küçük (alt sınır) tarihtir.
- **`MaximumDate`:** Seçilebilecek en büyük (üst sınır) tarihtir.
    - *Varsayılan Sınırlar:* Eğer bir kısıtlama verilmezse varsayılan aralık **1 Ocak 1900** ile **31 Aralık 2100** tarihleri arasındadır.
    - *Senaryo:* Örneğin +18 yaş kısıtı olan bir uygulamada doğum tarihi alınırken `MaximumDate`, bugünün tarihinden 18 yıl öncesine sabitlenmelidir.
- **`Date`:** Kontrolün ilk açıldığında veya o anda seçili duran varsayılan tarihidir. Belirtilmezse o günün tarihi veya `MinimumDate` yüklenir.
- **Tarih Yazım Standartları:**
    - Yazılımcılar için karmaşayı önlemek adına büyükten küçüğe (`Yıl/Ay/Gün` - `2026/12/15`) yazım biçimi önerilir.

### B. `Format` Belirleme Kuralları

Ekranda tarihin hangi desende görüneceğini belirler:

- **`yyyy`:** Yılı 4 haneli olarak gösterir (`2026`). (İki haneli `yy` tavsiye edilmez).
- **`MM` (Büyük Harf):** Ayı temsil eder. **Mutlaka büyük harf yazılmalıdır;** çünkü küçük `mm` saatin dakikasını (minute) temsil eder.
    - Tek `M`: 1–9 arasındaki ayları tek hane (`1`, `2`) yazar.
    - Çift `MM`: Tek haneli ayların başına sıfır ekler (`01`, `02`).
- **`dd`:** Günü temsil eder. Çift `dd` tek haneli günleri `01`, `02` formatında sıfır dolgulu yazar.
- **Ayırıcı Karakterler:** Uluslararası standartlarda eğik çizgi (`/`) veya tire () kullanılsa da Türk Dil Kurumu ve yerel standartlara göre **nokta (`.`)** kullanımı (`dd.MM.yyyy`) tercih edilmelidir.

### C. Diğer Özellikler ve Olaylar (Events)

- **`IsOpen` (`bool`):** Takvim açılır penceresinin açık mı kapalı mı olduğunu belirtir. Kod tarafından programatik olarak kontrol edilebilir.
- **`Opened`:** Takvim kutusu açıldığı anda tetiklenir.
- **`Closed`:** Kullanıcı takvimi kapattığında tetiklenir (tarih seçse de seçmeden kapatsa da çalışır).
- **`DateSelected`:** Kullanıcı takvimden yeni bir tarih seçip onayladığında tetiklenir.

---

## 5. `TimePicker` (Saat Seçici) Kontrolü

Kullanıcının zaman (saat ve dakika) seçmesini sağlayan tekerlek veya saat kadranı kontrolüdür.

```xml
<TimePicker x:Name="tmpSaat"
            Format="HH.mm"
            FontSize="20"
            FontAttributes="Bold"
            TextColor="Red"
            CharacterSpacing="3"
            Opened="tmpSaat_Opened"
            Closed="tmpSaat_Closed" />
```

### A. Temel Özellikler

- **`Time` (`TimeSpan`):** Seçilen saati `TimeSpan` (gün içi süre) türünden döndürür veya ayarlar (Örn: `Time="09:15:00"`).
- **`Format` Kuralları:**
    - **`HH` (Büyük Harf):** 24 saatlik formatı temsil eder (`00` - `23`).
    - **`hh` (Küçük Harf):** 12 saatlik AM/PM formatını temsil eder (`01` - `12`).
    - **`mm` (Küçük Harf):** Dakikayı temsil eder (`00` - `59`).
    - *TDK Standardı:* Dijital saat yazımlarında saat ile dakika arasında Türkçe yazım kurallarına göre iki nokta (`:`) değil, **tek nokta (`.`)** kullanılmalıdır (`HH.mm`).
- **`IsOpen` (`bool`):** Saat seçim penceresinin görünürlük/açıklık durumu.
- **Olaylar:** `Opened`, `Closed` ve değer değişimi için `PropertyChanged` olayları mevcuttur.

---

## 6. `Picker` (Açılır Liste / Dropdown / ComboBox) Kontrolü

Masaüstü uygulamalarındaki `ComboBox` bileşenine karşılık gelir. Kullanıcıya belirli seçenekler arasından tek bir seçim yapma imkânı sunar.

### A. XAML İçerisinde Statik Dizi Tanımlama (`x:Array`)

Veri kaynağı henüz C# kodundaki dinamik bir koleksiyona bağlanmamışken XAML içinde doğrudan statik eleman tanımlamak için `x:Array` kullanılır:

```xml
<Picker x:Name="pkrYer"
        Title="Bir yer seçiniz"
        TitleColor="Red"
        FontSize="20"
        FontAttributes="Bold"
        TextColor="Red"
        HorizontalTextAlignment="Center">
    <Picker.ItemsSource>
        <x:Array Type="{x:Type x:String}">
            <x:String>Bilgisayar Laboratuvarı</x:String>
            <x:String>Amfi</x:String>
            <x:String>Konferans Salonu</x:String>
        </x:Array>
    </Picker.ItemsSource>
</Picker>
```

### B. Temel Özellikler

- **`Title`:** Liste açılmadan önce ekranda silik olarak görünen yer tutucu başlıktır (Placeholder).
- **`TitleColor`:** `Title` metninin rengidir.
- **`SelectedItem`:** O an seçilmiş olan nesneyi (örneğin `"Konferans Salonu"` metnini) `object` tipinde döndürür.
- **`SelectedIndex`:** Seçili elemanın $0$'dan başlayan indeks numarasıdır.
    - **Kritik Hata Uyarısı:** Eğer kullanıcı henüz bir seçim yapmamışsa `SelectedIndex` değeri **`1`** olur ve `SelectedItem` **`null`** döner. Kod tarafında doğrudan okunmaya çalışılırsa uygulama `NullReferenceException` veya `ArgumentOutOfRangeException` vererek çöker. Mutlaka denetlenmelidir:
        
        ```csharp
        if (pkrYer.SelectedIndex != -1)
        {
            string secilenYer = pkrYer.SelectedItem.ToString();
            int siraNo = pkrYer.SelectedIndex;
        }
        ```
        
- **`HorizontalTextAlignment`:** Metnin yatayda hizalanması (`Start`, `Center`, `End`).
    - *Not:* `Justify` seçeneği mobilde (özellikle Android) desteklenmez; verildiğinde varsayılan olarak `Start` gibi davranır.
- **`VerticalTextAlignment`:** Metnin dikeydeki hizasıdır. Yalnızca kontrole `HeightRequest` ile sabit bir yükseklik verildiğinde etkisi belirginleşir.
- **`TextTransform` Notu:** .NET MAUI 10'un bazı ara derlemelerinde (özellikle 10.0.403 güncellemesi sonrası) `Picker` bileşeninde `TextTransform="Uppercase"` kullanımı arayüz motoru tarafından sınırlandırıldığı için metinlerin büyük/küçük harf dönüşümlerinin veri kaynağında veya C# tarafında yapılması daha güvenlidir.

---

## 7. `Editor` (Çok Satırlı Metin Girişi) Kontrolü

Kullanıcının adres, dilekçe, açıklama veya geri bildirim gibi uzun metinler girebileceği zengin metin kutusudur.

```xml
<Editor x:Name="edtDusunceler"
        Placeholder="Lütfen düşüncelerinizi yazınız..."
        PlaceholderColor="Navy"
        FontSize="20"
        TextColor="Indigo"
        AutoSize="TextChanges"
        MaxLength="2000"
        IsSpellCheckEnabled="True"
        IsTextPredictionEnabled="True"
        Keyboard="Chat" />
```

### A. `Editor` Özellikleri ve Davranışları

- **`AutoSize`:** Metin kutusunun dikeyde nasıl genişleyeceğini belirler.
    - `Disabled` (Varsayılan): Sabit yükseklikte kalır, sığmayan metin içeri doğru kayar (scroll).
    - `TextChanges`: **Kullanıcı yeni satıra geçtikçe (`Enter` bastıkça) veya yazdıkça kutunun boyutu otomatik olarak aşağıya doğru kendiliğinden uzar.** (Bu özellik açıkken çakışma olmaması için sabit `HeightRequest` verilmemelidir).
- **`Placeholder` & `PlaceholderColor`:** Kutu boşken arka planda duran açıklayıcı ipucu metni ve rengi.
- **`MaxLength`:** Kullanıcının girebileceği maksimum karakter sayısıdır (Örn: `MaxLength="200"` verildiğinde kullanıcı 200 karakterden sonrasını yazamaz).
- **`IsReadOnly` (`bool`):** `true` yapılırsa kutu salt-okunur olur; kullanıcı metin yazamaz veya silemez, sadece okuyup kopyalayabilir.
- **`IsSpellCheckEnabled` (`bool`):** Cihazın sözlüğüne göre hatalı yazılan kelimelerin altını kırmızı tırtıklı çizgiyle çizer.
- **`IsTextPredictionEnabled` (`bool`):** Klavyenin üzerinde kelime tamamlama/tahmin çubuğunun açılıp açılmayacağını belirler.
- **`Keyboard`:** Hangi sanal klavye türünün açılacağını belirler (`Chat`, `Numeric`, `Email`, `Telephone`, `Text`).
- **`CursorPosition` & `SelectionLength`:** İmlecin metin içindeki konumunu okumak veya istenilen bir metin aralığını programatik olarak seçili hale getirmek için kullanılır.

---

## 8. Sınıf İçi Uygulama: "Proje Sunumu Oylama ve Geri Bildirim Formu"

Derste anlatılan tüm kontrolleri bir araya getiren örnek form mimarisi aşağıda sunulmuştur:

### A. XAML Arayüz Tasarımı (`MainPage.xaml`)

```xml
<ScrollView>
    <VerticalStackLayout Spacing="15" Padding="20">

        <!-- Başlık ve Açıklama -->
        <Label Text="Mobil Cihazlar İçin Yazılım Mühendisliği Dersi Sunumu"
               FontSize="20"
               FontAttributes="Bold"
               TextColor="DarkRed"
               HorizontalTextAlignment="Center" />

        <Label Text="Mobil Cihazlar İçin Yazılım Mühendisliği kapsamında öğrencilerimizin hazırlamış olduğu projelerin sunumu için tarih, saat ve yer seçimine katkıda bulunursanız memnun oluruz."
               FontSize="14"
               TextColor="Gray" />

        <!-- 1. Tarih Seçici -->
        <Label Text="Tarih Seçiniz:" FontAttributes="Bold" />
        <DatePicker x:Name="dtpTarih"
                    MinimumDate="2026/12/15"
                    MaximumDate="2026/12/29"
                    Date="2026/12/16"
                    Format="dd.MM.yyyy"
                    FontSize="18"
                    TextColor="Red"
                    Opened="dtpTarih_Opened"
                    Closed="dtpTarih_Closed"
                    DateSelected="dtpTarih_DateSelected" />
        <Label x:Name="lblTarihDurum" FontSize="12" TextColor="DarkSlateGray" />

        <!-- 2. Saat Seçici -->
        <Label Text="Saat Seçiniz:" FontAttributes="Bold" />
        <TimePicker x:Name="tmpSaat"
                    Time="09:15:00"
                    Format="HH.mm"
                    FontSize="18"
                    TextColor="Red" />

        <!-- 3. Yer Seçici (Picker) -->
        <Label Text="Yer Seçiniz:" FontAttributes="Bold" />
        <Picker x:Name="pkrYer"
                Title="Bir yer seçiniz"
                TitleColor="Red"
                FontSize="18"
                TextColor="Red">
            <Picker.ItemsSource>
                <x:Array Type="{x:Type x:String}">
                    <x:String>Bilgisayar Laboratuvarı</x:String>
                    <x:String>Amfi</x:String>
                    <x:String>Konferans Salonu</x:String>
                </x:Array>
            </Picker.ItemsSource>
        </Picker>

        <!-- 4. Çok Satırlı Düşünceler (Editor) -->
        <Label Text="Eklemek İstediğiniz Düşünceleriniz:" FontAttributes="Bold" />
        <Editor x:Name="edtDusunceler"
                Placeholder="Lütfen düşüncelerinizi yazınız..."
                PlaceholderColor="Navy"
                FontSize="16"
                AutoSize="TextChanges"
                MaxLength="500" />

        <!-- Gönder Butonu -->
        <Button x:Name="btnGonder"
                Text="Oyumu Gönder"
                Clicked="btnGonder_Clicked"
                Margin="0,20,0,0" />

    </VerticalStackLayout>
</ScrollView>
```

### B. C# İş Mantığı (`MainPage.xaml.cs`)

```csharp
namespace Ders06A;

public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
    }

    private void dtpTarih_Opened(object sender, EventArgs e)
    {
        lblTarihDurum.Text = "DatePicker açıldı, lütfen bir tarih seçiniz.";
    }

    private void dtpTarih_Closed(object sender, EventArgs e)
    {
        lblTarihDurum.Text = "DatePicker kapandı, umarım bir tarih seçtiniz.";
    }

    private void dtpTarih_DateSelected(object sender, DateChangedEventArgs e)
    {
        lblTarihDurum.Text = "Tarih seçtiğiniz için teşekkür ederiz.";
    }

    private async void btnGonder_Clicked(object sender, EventArgs e)
    {
        // Tarih Bilgisi
        string secilenTarih = dtpTarih.Date.ToString("dd.MM.yyyy");

        // Saat Bilgisi
        string secilenSaat = tmpSaat.Time.ToString(@"hh\:mm");

        // Yer Bilgisi (Seçim kontrolü ile)
        string secilenYer = "Seçilmedi";
        int yerIndeksi = pkrYer.SelectedIndex;

        if (yerIndeksi != -1)
        {
            secilenYer = $"{pkrYer.SelectedItem} (İndeks: {yerIndeksi})";
        }
        else
        {
            await DisplayAlert("Uyarı", "Lütfen bir sunum yeri seçiniz!", "Tamam");
            return;
        }

        // Düşünceler (Editor)
        string dusunceler = string.IsNullOrWhiteSpace(edtDusunceler.Text)
            ? "Belirtilmedi"
            : edtDusunceler.Text;

        // Çapraz platform uyumlu satır sonu (\n) ile mesaj derleme
        string bildirimMesaji = $"Oyunuz kaydedildi.\n\n" +
                                $"Tarih: {secilenTarih}\n" +
                                $"Saat: {secilenSaat}\n" +
                                $"Yer: {secilenYer}\n" +
                                $"Not: {dusunceler}";

        await DisplayAlert("Oylama Sonucu", bildirimMesaji, "Tamam");
    }
}
```

---

## 9. Özet ve Kapanış

- Ders kapsamında form girişlerinin temel yapı taşları olan **`DatePicker`**, **`TimePicker`**, **`Picker`** ve **`Editor`** kontrollerinin tüm XAML nitelikleri, formatlama kuralları ve C# çalışma zamanı (runtime) etkileşimleri incelenmiştir.
- Öğrencilere bu dört kontrolü ve hata denetimlerini içeren formu kendi cihazlarında/emülatörlerinde derleyip test etmeleri söylenerek ders tamamlanmıştır.

---