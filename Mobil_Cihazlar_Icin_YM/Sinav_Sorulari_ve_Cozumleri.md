# Mobil Cihazlar İçin Yazılım Mühendisliği Vize Sınavına Hazırlık: Kapsamlı ve İnteraktif Soru Bankası

Bu doküman, **Mobil Cihazlar İçin Yazılım Mühendisliği** dersinin tüm transkriptleri, hocanın derste bizzat tahtada çözdüğü örnekler, 7 Ekim el yazısı notları ve vize sınavı uyarıları taranarak hazırlanmış; müfredatın **birebir öğrenme sırasına göre (Modül 1'den Modül 6'ya)** yapılandırılmış kapsamlı klasik sınav soru bankasıdır.

İçerisinde:
* **Hocanın "sınavda kesin sorarım" dediği garantili sorular** (Örn: `AspectFit/AspectFill/Fill/Center` analizi, `Thickness` saat yönü kuralı, `BoxView` daire geometrisi),
* **Klasik kağıt üzerinde XAML form tasarımı ve C# code-behind kodlama soruları**,
* **`NullReferenceException` ve çalışma zamanı çökme (crash) senaryolarını önleme kodları**,
* **Sayısal hassasiyet (`Math.Round`), renk sistemleri ve Grid matris hesaplamaları**,
* **Çapraz platform mimari karşılaştırmaları (.NET MAUI vs. Flutter vs. WebView)** yer almaktadır.

> [!TIP]
> **Çalışma Yöntemi (Self-Testing):**
> Sınav kağıt üzerinde klasik formatta olacağından, her sorunun cevabı ve adım adım ayrıntılı çözümü **açılır-kapanır (toggle / `<details>`)** kutular içerisine gizlenmiştir. Çalışırken önce soruyu okuyup kendi cevabınızı boş bir kağıda yazınız; ardından **"🔍 Çözümü ve Detaylı Anlatımı Gör"** butonuna tıklayarak cevabınızı, sözdiziminizi ve mühendislik gerekçelerinizi kontrol ediniz.

---

## 📑 İÇİNDEKİLER VE MÜFREDAT SIRASI

1. [MODÜL 1: Giriş, Çapraz Platform Mimarileri ve .NET MAUI Temelleri (Soru 1 – 7)](#modül-1-giriş-çapraz-platform-mimarileri-ve-net-maui-temelleri)
2. [MODÜL 2: Temel Metin, Girdi ve Etkileşim Bileşenleri (7 Ekim Notları) (Soru 8 – 14)](#modül-2-temel-metin-girdi-ve-etkileşim-bileşenleri)
3. [MODÜL 3: Sayısal Seçiciler, Renk Sistemleri ve Grid Mimarisi (Soru 15 – 21)](#modül-3-sayısal-seçiciler-renk-sistemleri-ve-grid-mimarisi)
4. [MODÜL 4: Görsel Yönetimi, Aspect Oranları ve İkon Fontları (Soru 22 – 28 - HOCANIN KESİN SINAV UYARILARI)](#modül-4-görsel-yönetimi-aspect-oranları-ve-i̇kon-fontları)
5. [MODÜL 5: Gelişmiş Arayüz Elemanları (Border, Stroke, BoxView, Seçim Kontrolleri) (Soru 29 – 35)](#modül-5-gelişmiş-arayüz-elemanları)
6. [MODÜL 6: Tarih/Saat Seçiciler, Açılır Listeler ve Çok Satırlı Editör (Soru 36 – 42)](#modül-6-tarihsaat-seçiciler-açılır-listeler-ve-çok-satırlı-editör)
7. [BÖLÜM 7: Bütüncül Klasik Vize Sınav Provası (Senaryo ve Kodlama) (Soru 43 – 46)](#bölüm-7-bütüncül-klasik-vize-sınav-provası)

---

## MODÜL 1: Giriş, Çapraz Platform Mimarileri ve .NET MAUI Temelleri

### Soru 1 (Mimari Karşılaştırma): Çapraz Platform Mimarilerinin Temel Felsefeleri
**Soru:**
Mobil uygulama geliştirmede kullanılan **(a) Web Tabanlı Hibrit Platformlar (React Native / Cordova / Ionic)**, **(b) Kendi Çizim Motoru Olan Platformlar (Flutter)** ve **(c) Doğrudan Yerel Bileşen Eşleyen Platformlar (.NET MAUI)** arasındaki çalışma mantığı, arayüz çizim yöntemi ve performans farklarını karşılaştırarak açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Web Tabanlı Hibrit Platformlar (Cordova, Ionic, eski React Native yapıları):**
   * **Çalışma Mantığı:** HTML, CSS ve JavaScript kullanarak bir web sayfası üretir. Uygulama kabuğunun içine yerel bir `WebView` (gömülü web tarayıcısı motoru) yerleştirir ve arayüzü bu pencere içinde gösterir.
   * **Performans / Hissiyat:** Donanım ivmelendirmesinden ve işletim sisteminin saf bileşenlerinden yoksundur; web tarayıcısı köprüsü nedeniyle animasyonlarda ve yoğun işlemlerde takılmalar yaşanır.
2. **Kendi Çizim Motoru Olan Platformlar (Flutter):**
   * **Çalışma Mantığı:** İşletim sisteminin yerel buton veya liste bileşenlerini kullanmaz. Ekranı boş bir tuval (canvas) olarak kabul eder ve Google'ın geliştirdiği **Skia** veya **Impeller** grafik motoruyla pikselleri ekrana doğrudan kendi çizer.
   * **Performans / Hissiyat:** Android ve iOS üzerinde piksellerin tamamen aynı görünmesini sağlar; ancak platformun doğal Material/Cupertino yerel kontrol davranışlarını (native look and feel) birebir taşımaz.
3. **Doğrudan Yerel Bileşen Eşleyen Platformlar (.NET MAUI):**
   * **Çalışma Mantığı:** Tek bir XAML tanımı yazılır (Örn: `<Button Text="Giriş" />`). Derleme ve çalışma anında MAUI Handler katmanı bu kontrolü doğrudan hedef işletim sisteminin saf yerel bileşenine eşler (**Android'de `MaterialButton`**, **iOS'ta `UIButton`**, **Windows'ta WinUI 3 `Button`**).
   * **Performans / Hissiyat:** Arada ek bir tarayıcı veya sanal tuval katmanı bulunmadığı için en yüksek yerel performansı, doğrudan donanım ivmelendirmesini ve işletim sisteminin %100 doğal görünüm/davranışını sunar.

</details>

---

### Soru 2 (Sözel / Apple Politikaları): iOS Derleme Süreci ve Mac Bağımlılığı
**Soru:**
Windows işletim sistemine sahip bir bilgisayarda .NET 10 MAUI ile mobil uygulama geliştiren bir yazılım mühendisi, Android telefonuna doğrudan USB ile uygulama yükleyebilirken neden iPhone cihazına Windows üzerinden doğrudan derleme yapıp yükleyemez? Bu sorunu çözmek için kurulan "Pair to Mac" mimarisini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Apple Kısıtları ve Lisans Politikaları:**
   * Apple, iOS uygulamalarının derlenmesi, imzalanması (code signing) ve cihaza yüklenmesi için yalnızca kendi tescilli geliştirme aracı olan **Xcode** ve macOS işletim sistemine izin vermektedir.
   * Windows işletim sisteminde Xcode çalışamadığından, Apple'ın resmi SDK ve derleyicilerine doğrudan erişim mümkün değildir.
2. **"Pair to Mac" (Mac ile Eşleştir) Çözüm Mimarisi:**
   * Yazılımcı Windows üzerinde Visual Studio ile kodunu yazar.
   * Aynı yerel ağda (Wi-Fi veya Ethernet) bulunan bir **Mac cihazı (MacBook, Mac mini vb.)** ağ üzerinden Visual Studio'ya bağlanır ("Pair to Mac").
   * Windows'taki Visual Studio, yazılan C# ve XAML kodlarını ağ üzerinden Mac'e iletir; Mac üzerindeki Xcode ve derleme araçları kodu yerel iOS ikili dosyasına (binary) dönüştürür ve bağlı iPhone'a yükler.

</details>

---

### Soru 3 (Sözel / Versiyonlama): .NET Versiyon Politikası (LTS vs. STS)
**Soru:**
Ders kapsamında geliştirme yapılırken neden .NET 11 yerine **.NET 10 (LTS)** sürümü tercih edilmiştir? LTS ve STS (Standart / Kısa Süreli) kavramlarını yazılım mühendisliği projeleri açısından açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **LTS (Long Term Support - Uzun Süreli Destek):**
   * Microsoft tarafından **3 yıl boyunca** hata düzeltmeleri, performans yamaları ve güvenlik güncellemeleriyle desteklenen sürümlerdir (Örn: .NET 8, .NET 10).
   * Kurumsal, büyük ölçekli ve uzun vadeli üretim ortamları (production) için her zaman LTS sürümler tercih edilir; çünkü API değişiklikleri ve uyumsuzluk riski minimumdur.
2. **STS (Standard Term Support - Standart Destek):**
   * Yalnızca **18 ay** boyunca desteklenen ara sürümlerdir (Örn: .NET 9, .NET 11).
   * Genellikle yeni deneysel özellikleri erken test etmek isteyen geliştiricilere yöneliktir.
3. **Ders Açısından Gerekçe:** Kurumsal mobil mühendislik prensiplerine uygun olarak, kütüphane ve SDK istikrarı sağlandığı için derste .NET 10 LTS tercih edilmiştir.

</details>

---

### Soru 4 (Şematik / Mimari): .NET MAUI Kontrol Hiyerarşisi
**Soru:**
.NET MAUI'de bir kullanıcı arayüzü tasarlanırken uygulanan 3 seviyeli kontrol hiyerarşisini yukarıdan aşağıya doğru bir şema ile gösteriniz ve her katmana ikişer adet örnek MAUI sınıfı yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
Hiyerarşik yapı şu şekildedir:

```
[ SAYFA (Page) ]
       └── [ YERLEŞİM (Layout) ]
                 └── [ GÖRÜNÜM / KONTROL (View) ]
```

1. **Sayfalar (Pages):** Ekranın tamamını kaplayan ana kapsayıcıdır.
   * *Örnekler:* `ContentPage`, `FlyoutPage`, `NavigationPage`.
2. **Yerleşimler (Layouts):** Görünümleri ekran üzerinde belirli dizilim kurallarına göre konumlandıran şablonlardır.
   * *Örnekler:* `Grid`, `VerticalStackLayout`, `HorizontalStackLayout`, `FlexLayout`.
3. **Görünümler (Views):** Kullanıcının doğrudan ekranda gördüğü ve etkileşime girdiği temel kontrollerdir.
   * *Örnekler:* `Label`, `Button`, `Entry`, `Image`, `Slider`, `CheckBox`.

</details>

---

### Soru 5 (Sözel / Donanım): Android Cihazda Geliştirici Modunu Açma
**Soru:**
Fiziksel bir Android cihazı Visual Studio'da doğrudan hata ayıklama (debugging) hedefi haline getirmek için telefonda sırasıyla hangi adımların uygulanması gerekir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. Telefon ile bilgisayar arasına yalnızca şarj değil, veri aktarımı yapabilen bir USB kablo bağlanır.
2. Telefonda *Ayarlar > Telefon Hakkında / Yazılım Bilgileri* menüsüne gidilir.
3. **"Yapım Numarası" (Build Number)** seçeneği üzerine arka arkaya **7 kez** hızlıca tıklanır (Ekranda *"Artık bir geliştiricisiniz!"* bildirimi çıkar).
4. Ayarlar ana menüsüne eklenen **"Geliştirici Seçenekleri"** menüsüne girilir ve **"USB Hata Ayıklama" (USB Debugging)** seçeneği aktif hale getirilir.
5. Bilgisayara bağlandığında ekrana gelen "Bu bilgisayara her zaman izin ver (RSA Anahtarı)" uyarısı onaylanır.

</details>

---

### Soru 6 (Mimari / Dosya Yapısı): `MauiProgram.cs` ve `AppShell.xaml` Görevleri
**Soru:**
Yeni bir .NET MAUI projesi oluşturulduğunda kök dizinde yer alan `MauiProgram.cs` ve `AppShell.xaml` dosyalarının projedeki temel mühendislik görevlerini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **`MauiProgram.cs`:**
   * Uygulamanın başlatıcısıdır (`Main` giriş noktası).
   * `CreateMauiApp()` fonksiyonu ile `MauiApp` örneği inşa edilir (`MauiAppBuilder`).
   * Projede kullanılacak özel fontlar (`ConfigureFonts`), bağımlılık enjeksiyonları (Dependency Injection - DI servisleri) ve platform eklentileri (Community Toolkit vb.) burada sisteme tanıtılır ve kaydedilir.
2. **`AppShell.xaml`:**
   * Uygulamanın navigasyon ve yönlendirme omurgasını oluşturur.
   * Sekmeli sayfa geçişlerini (`TabBar` / `Tab`), yan çekmece menülerini (`FlyoutItem`) ve sayfa rotalarını (URI Navigation) tek bir merkezi XAML dosyasından yönetmeyi sağlar.

</details>

---

### Soru 7 (Tasarım & UI/UX): Tipografi ve Renk Psikolojisi
**Soru:**
Mobil uygulama tasarımında tipografi ve renk kullanımı kullanıcı psikolojisini doğrudan etkiler. Aşağıdaki tasarım tercihlerinin kullanıcıda uyandırdığı psikolojik algıyı birer cümleyle açıklayınız:
1. Başlık metinlerinin tamamen BÜYÜK HARF (UPPERCASE) yazılması,
2. Yuvarlak hatlı ve küçük harfli fontların tercih edilmesi,
3. Sağa yatık (İtalik) font kullanımı,
4. Bankacılık ve kurumsal uygulamalarda Mavi rengin baskın olması.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Büyük Harf (Uppercase):** Kullanıcıda bağırma, agresiflik, resmiyet ve katı kural hissi uyandırır. Form alanlarında aşırı kullanımı kullanıcıyı rahatsız eder.
2. **Yuvarlak Hatlı ve Küçük Harfler:** Samimiyet, erişilebilirlik, modernlik ve halka yakınlık duygusu oluşturur (Arçelik ve Beko'nun modernleşen logoları gibi).
3. **İtalik (Sağa Yatık):** Hız, dinamizm, sportiflik, gelecek hedefleri ve yükseliş algısı yaratır.
4. **Mavi Renk:** Güvenilirlik, istikrar, profesyonellik ve sakinlik telkin ettiği için finans ve bankacılık sektöründe standarttır.

</details>

---

## MODÜL 2: Temel Metin, Girdi ve Etkileşim Bileşenleri

### Soru 8 (Klasik Kod Yazma - 7 Ekim Notları): Kullanıcı Giriş Arayüzü XAML Tasarımı
**Soru:**
Aşağıdaki gereksinimleri karşılayan bir mobil oturum açma sayfasının XAML kodunu `Grid` düzeni kullanarak kağıt üzerine yazınız:
* Ekranın en üstünde ortalanmış, kalın (Bold), 22 punto ve harf aralığı (`CharacterSpacing="2"`) açılmış bir başlık (`Label`).
* Kullanıcı Adı girişi için: silme çarpısı aktif (`ClearButtonVisibility="WhileEditing"`), yer tutucu metni olan bir `Entry`.
* Şifre girişi için: girilen karakterleri gizleyen (`IsPassword="True"`), maksimum 8 karakter izin veren bir `Entry`.
* En altta "Oturum Aç" yazan bir `Button`.
* Tüm bileşenlerin code-behind'dan erişilebilecek `x:Name` adlandırmalarını eksiksiz yapınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (XAML):
```xml
<Grid RowDefinitions="Auto, Auto, Auto, Auto"
      ColumnDefinitions="*"
      RowSpacing="15"
      Padding="25">

    <!-- Başlık -->
    <Label Grid.Row="0"
           Text="KULLANICI GİRİŞİ"
           FontSize="22"
           FontAttributes="Bold"
           CharacterSpacing="2"
           HorizontalTextAlignment="Center"
           TextColor="#1E3A8A" />

    <!-- Kullanıcı Adı Girişi -->
    <Entry Grid.Row="1"
           x:Name="entKullaniciAdi"
           Placeholder="Kullanıcı adınızı giriniz..."
           ClearButtonVisibility="WhileEditing"
           Keyboard="Text" />

    <!-- Şifre Girişi -->
    <Entry Grid.Row="2"
           x:Name="entSifre"
           Placeholder="Şifrenizi giriniz..."
           IsPassword="True"
           MaxLength="8"
           Keyboard="Password" />

    <!-- Giriş Butonu -->
    <Button Grid.Row="3"
            x:Name="btnGiris"
            Text="Oturum Aç"
            HeightRequest="50"
            CornerRadius="25"
            BackgroundColor="#2563EB"
            TextColor="White" />
</Grid>
```

</details>

---

### Soru 9 (C# Code-Behind Kodlama): `Completed` Olayı ve `DisplayAlert` Entegrasyonu
**Soru:**
Soru 8'de tasarladığınız arayüz için C# code-behind dosyasında (`MainPage.xaml.cs`):
1. Kullanıcı şifresini yazıp klavyedeki "Tamam / Enter" tuşuna bastığında tetiklenecek `entSifre_Completed` metot imzasını ve gövdesini yazınız.
2. Metot içinde şifre alanı boşsa veya 6 karakterden azsa kullanıcıya `DisplayAlert` ile *"Şifreniz en az 6 karakter olmalıdır"* uyarısı veriniz; şart sağlanıyorsa *"Giriş başarılı"* mesajı gösteriniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (C#):
```csharp
private async void entSifre_Completed(object sender, EventArgs e)
{
    // 1. Şifre alanı boşluk veya uzunluk kontrolü
    if (string.IsNullOrWhiteSpace(entSifre.Text) || entSifre.Text.Length < 6)
    {
        await DisplayAlert("Güvenlik Hatası", "Şifreniz en az 6 karakter olmalıdır!", "Tekrar Dene");
        entSifre.Focus(); // İmleci tekrar şifre kutusuna odakla
        return;
    }

    // 2. Kullanıcı adı kontrolü
    string kullanici = string.IsNullOrWhiteSpace(entKullaniciAdi.Text) ? "Misafir" : entKullaniciAdi.Text;

    // 3. Başarılı bildirim
    await DisplayAlert("Başarılı", $"Hoş geldiniz, {kullanici}. Giriş onaylandı.", "Tamam");
}
```

</details>

---

### Soru 10 (Sözel / UX): `Keyboard` Nitelikleri ve Doğru Klavye Seçimi
**Soru:**
.NET MAUI'de `Entry` kontrolünün `Keyboard` özelliği kullanılarak aşağıdaki 4 farklı veri türü için hangi klavye tiplerinin atanması gerektiğini yazınız ve gerekçesini açıklayınız:
1. Öğrencinin harç ödemesi için girdiği T.C. Kimlik Numarası,
2. Öğrenci işleri kayıt sisteminde e-posta adresi,
3. Web sitesi portföy bağlantısı (URL),
4. Danışman öğretim üyesine gönderilecek kısa sohbet mesajı.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **T.C. Kimlik Numarası:** `Keyboard="Numeric"` $\implies$ Sadece rakamlar tuş takımını açarak harf girilmesini engeller ve kullanıcıyı hızlandırır.
2. **E-posta Adresi:** `Keyboard="Email"` $\implies$ Klavyenin ana ekranına `@` işareti ve `.com` kısayolunu getirir.
3. **Web Sitesi (URL):** `Keyboard="Url"` $\implies$ `/`, `.com`, `www` tuşlarını klavyenin altına yerleştirir.
4. **Kısa Sohbet Mesajı:** `Keyboard="Chat"` $\implies$ Emoji butonunu ve otomatik kelime tamamlama/tahmin çubuğunu ön plana çıkarır.

</details>

---

### Soru 11 (Kavramsal / Tuzak Soru): `Placeholder` vs. `Text` ve `HorizontalTextAlignment="Justify"`
**Soru:**
1. Bir `Entry` kontrolünde hem `Placeholder="Adınızı Giriniz"` hem de `Text="Ali"` tanımlanmışsa ekranda ne görünür? Neden?
2. Bir `Entry` bileşenine `HorizontalTextAlignment="Justify"` verildiğinde Android veya iOS'ta nasıl bir görsel davranış sergiler?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **`Placeholder` vs. `Text`:** Ekranda yalnızca **"Ali"** görünür. Kural gereği `Text` özelliği boş olmadığı sürece `Placeholder` (yer tutucu) metni otomatik olarak gizlenir. Sadece `Text` temizlendiğinde `Placeholder` tekrar görünür hale gelir.
2. **`Justify` Davranışı:** `Justify` (iki yana yaslama) özelliği, satır sonundaki boşlukları kelime aralarına paylaştırarak çalışan bir metin düzenidir. `Entry` tek satırlı bir kontrol olduğundan iki yana yayma yapamaz; bu nedenle mobil platformlarda varsayılan olarak sola yaslama (**`Start`**) gibi davranır.

</details>

---

### Soru 12 (Sözel / Dil ve Lokalizasyon): `TextTransform` ve Türkçe Karakter Tuzağı
**Soru:**
`Entry` kontrolünde `TextTransform="Uppercase"` tanımlandığında Türkçe karakterlerle çalışan bir mobil uygulamada ne gibi yazılımsal ve mantıksal hatalar meydana gelebilir? Nasıl önlenir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Sorun:** İşletim sisteminin varsayılan yerel ayarı (Locale) İngilizce olduğunda, `Uppercase` dönüşümü küçük `i` harfini Türkçe `İ` harfi yerine noktasız **`I`** harfine dönüştürür (`"diyarbakir"` $\implies$ `"DİYARBAKIR"` yerine `"DIYARBAKIR"` olur). Benzer şekilde `ı` harfinde de uyumsuzluklar oluşur.
* **Sonuç:** Kullanıcı veritabanında arama yaparken veya e-posta eşleştirirken harf farklılığından dolayı sorgular başarısız olur.
* **Önlem:** Büyük/küçük harf dönüşümleri arayüz seviyesinde rastgele bırakılmamalı; C# arka plan kodunda `CultureInfo.GetCultureInfo("tr-TR")` parametresi verilerek `ToUpper(culture)` şeklinde kontrollü dönüştürülmelidir.

</details>

---

### Soru 13 (XAML / Kural): `x:Name` ile `Name` Arasındaki Fark
**Soru:**
Neden XAML içerisinde bir kontrole ad verirken `Name="entAd"` yerine `x:Name="entAd"` yazmak zorundayız?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* `x:` ön eki, XAML dilinin temel isim alanını (XAML Namespace - `xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"`) temsil eder.
* `x:Name`, derleyiciye (XAML Compiler - XAMLC) bu bileşen için arka planda (`.g.cs` otomatik üretilen dosyada) o isimle bir C# alan değişkeni (field) tanımlaması gerektiğini bildirir.
* Doğrudan `Name` yazılırsa, sadece `Name` özelliğini kendi sınıfında tanımlamış olan az sayıdaki bileşen bunu tanır; ancak C# code-behind'dan nesneye değişken olarak doğrudan erişim sağlanamaz.

</details>

---

### Soru 14 (Kod Okuma / Çıktı): Form Temizleme ve Değer Aktarımı
**Soru:**
Aşağıdaki C# olay metodunun yaptığı işi adım adım açıklayınız:
```csharp
private void entAd_Completed(object sender, EventArgs e)
{
    lblSonuc.Text = entAd.Text;
    entAd.Text = string.Empty;
    entAd.Focus();
}
```

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. `lblSonuc.Text = entAd.Text;` $\implies$ Kullanıcının `entAd` kutusuna yazdığı metni okuyup ekrandaki `lblSonuc` etiketine aktarır.
2. `entAd.Text = string.Empty;` $\implies$ Metin kutusunun içini tamamen temizler (Böylece `Placeholder` yeniden görünür hale gelir).
3. `entAd.Focus();` $\implies$ İmleci yeniden bu metin kutusuna odaklar; böylece kullanıcı elini ekrana dokunmadan hemen yeni bir kayıt girmeye devam edebilir (Seri veri girişi döngüsü).

</details>

---

## MODÜL 3: Sayısal Seçiciler, Renk Sistemleri ve Grid Mimarisi

### Soru 15 (Sayısal Hesaplama & Kodlama): GANO Hassasiyet Filtreleme (`Math.Round`)
**Soru:**
Bir öğrenci işleri mobil uygulamasında öğrencinin Genel Ağırlıklı Not Ortalaması (GANO) `0.00` ile `4.00` arasında bir `Slider` ile seçilmektedir.
1. Slider hareket ettirildiğinde virgülden sonra tam iki basamak hassasiyet (`3.42`) elde etmek için kullanılan matematiksel yuvarlama formülünü yazınız.
2. Bu formülü C# dilinde `sldGano_ValueChanged` olay metodu içerisinde kodlayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Matematiksel Formül:**
   $$\text{HassasGANO} = \frac{\text{Math.Round}(\text{e.NewValue} \times 100)}{100}$$
   *Mantık:* Örneğin ham değer $3.42817$ ise, $100$ ile çarpıldığında $342.817$ olur. `Math.Round` bunu en yakın tamsayı olan $343$'e yuvarlar. Ardından tekrar $100$'e bölünerek virgülden sonra iki basamaklı $3.43$ elde edilir.
2. **C# Metot Kodu:**
```csharp
private void sldGano_ValueChanged(object sender, ValueChangedEventArgs e)
{
    double hassasDeger = Math.Round(e.NewValue * 100) / 100;
    lblGanoGosterge.Text = $"GANO: {hassasDeger:0.00}";
}
```

</details>

---

### Soru 16 (Tasarım & Mimari): Slider ve Stepper Neden Birlikte Kullanılır?
**Soru:**
Mobil cihazlarda sayısal bir değer seçimi yapılırken (örneğin ses düzeyi veya ürün adedi) arayüzde neden tek başına Slider yerine **yanına bir de Stepper** yerleştirilir? Mühendislik ve kullanıcı deneyimi (UX) açısından açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Slider'ın Sınırı (Kaba Ayar):** Slider dokunmatik ekranda parmakla geniş bir sayı aralığında (örn: 0–100) hızlıca gezinmeyi sağlar. Ancak insan parmağının dokunmatik ekran hassasiyeti sınırlıdır; örneğin 25'ten 28'e atlayabilir, tam 26 değerini tutturmak titreme ve ekran boyutu nedeniyle çok zordur.
* **Stepper'ın Avantajı (İnce Ayar):** Stepper üzerindeki `+` ve `-` butonları ile değeri her tıklamada tam belirlenen adım boyutu (`Increment="1"` veya `0.01`) kadar hassasça artırıp azaltır.
* **Birlikte Kullanım Sinerjisi:** Kullanıcı Slider ile hedef değere hızla yaklaşır (**Kaba Ayar**), ardından Stepper'a 1-2 kez basarak tam hedef sayıyı yakalar (**İnce Ayar**). İki kontrolün değerleri C# code-behind'da senkronize tutulur.

</details>

---

### Soru 17 (Hesaplama / Geometri): Buton Köşe Yarıçapı ve Oval Form Kuralı
**Soru:**
Yüksekliği 60 piksel (`HeightRequest="60"`) ve genişliği 200 piksel olan bir `Button` bileşeninin köşelerinin tam bir oval (hap / kapsül) şeklinde görünmesi için `CornerRadius` özelliğine kaç verilmelidir? Eğer `CornerRadius="50"` verilirse butonun geometrik şeklinde ne değişir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Tam Oval Kuralı:** Köşe kavsinin kenarın ortasında kusursuz birleşmesi için köşe yarıçapı yüksekliğin tam yarısı olmalıdır:
   $$\text{CornerRadius} = \frac{\text{HeightRequest}}{2} = \frac{60}{2} = 30$$
   Yani `CornerRadius="30"` verilmelidir.
2. **50 Verilirse Ne Olur?:**
   Yarıçap değeri yüksekliğin yarısından ($30$) daha büyük verilirse ($50$), köşe yayları kesişir ve butonun dairesel formu elips veya deforme bir şekle doğru kayar. Kenarın yarısından büyük değerler verilmesi tavsiye edilmez.

</details>

---

### Soru 18 (XAML & Grid): Satır ve Sütun Tanımlama Birimleri
**Soru:**
Aşağıdaki `Grid` tanımını inceleyerek 400 piksel genişliğindeki bir ekranda her bir sütunun alacağı net genişliği piksel olarak hesaplayınız:
```xml
<Grid ColumnDefinitions="100, 2*, 1*">
```

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Toplam Ekran Genişliği = $400\text{ px}$.
1. **Sütun 0 (Sabit Piksel):** $100\text{ px}$ doğrudan ayrılır.
2. **Kalan Genişlik:** $400 - 100 = 300\text{ px}$.
3. **Yıldız (*) Dağılımı:**
   * Kalan alan $2* + 1* = 3$ eşit parçaya bölünür.
   * $1* = \frac{300}{3} = 100\text{ px}$.
4. **Sonuçlar:**
   * **Sütun 0:** $100\text{ px}$
   * **Sütun 1 ($2*$):** $2 \times 100 = 200\text{ px}$
   * **Sütun 2 ($1*$):** $1 \times 100 = 100\text{ px}$

</details>

---

### Soru 19 (Renk Sistemleri): Alpha Kanalı ve Hex Kod Çözümleme
**Soru:**
.NET MAUI'de renk tanımlamalarında kullanılan `#80FF0000` hexadecimal renk kodunun rengini, opaklık (saydamlık) düzeyini ve RGB bileşenlerini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
Sekiz haneli Hex renk formatı `#AARRGGBB` şeklindedir:
* **AA (Alpha / Saydamlık) = `80`:** Hexadecimal `80`, onluk sistemde $128$'dir. Maksimum değer $255$ olduğuna göre $\frac{128}{255} \approx \%50$ düzeyinde yarı saydamdır (arkasını gösterir).
* **RR (Kırmızı - Red) = `FF`:** $255$ (Maksimum kırmızı ışık).
* **GG (Yeşil - Green) = `00`:** $0$ (Yeşil kapalı).
* **BB (Mavi - Blue) = `00`:** $0$ (Mavi kapalı).
* **Sonuç:** Bu renk **%50 Yarı Saydam Kırmızı** rengi temsil eder.

</details>

---

### Soru 20 (C# / Olay Senkronizasyonu): Slider ve Stepper Birbirine Nasıl Bağlanır?
**Soru:**
Bir ekranda `sldAyar` adında bir Slider ve `stpAyar` adında bir Stepper bulunmaktadır. Kullanıcı Slider'ı kaydırdığında Stepper'ın, Stepper'a bastığında ise Slider'ın güncellenmesini sağlayan C# kodunu yazınız. Sonsuz döngü (event loop) tehlikesi nasıl önlenir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (C#):
```csharp
private void sldAyar_ValueChanged(object sender, ValueChangedEventArgs e)
{
    // Değerler zaten eşitse tekrar atama yapma (sonsuz döngüyü engelle)
    if (Math.Abs(stpAyar.Value - e.NewValue) > 0.001)
    {
        stpAyar.Value = e.NewValue;
    }
}

private void stpAyar_ValueChanged(object sender, ValueChangedEventArgs e)
{
    if (Math.Abs(sldAyar.Value - e.NewValue) > 0.001)
    {
        sldAyar.Value = e.NewValue;
    }
}
```

</details>

---

### Soru 21 (XAML Kodlama): Grid Span Özellikleri
**Soru:**
3 satır ve 3 sütundan oluşan bir `Grid` içerisinde, 1. satırın 0. sütunundan başlayıp yatayda 3 sütunun tamamını kaplayan bir `Button` bileşeninin XAML etiketini yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
```xml
<Button Grid.Row="1"
        Grid.Column="0"
        Grid.ColumnSpan="3"
        Text="Tüm Satırı Kaplayan Buton" />
```

</details>

---

## MODÜL 4: Görsel Yönetimi, Aspect Oranları ve İkon Fontları

### Soru 22 (HOCANIN KESİN SINAV UYARISI - Çizim & Analiz): 4 `Aspect` Türünün Davranışları
**Soru:**
Hoca sınavda kesin çıkacağını belirttiği `Image.Aspect` özelliği için:
1. `AspectFit`,
2. `AspectFill`,
3. `Fill`,
4. `Center`
seçeneklerinin en-boy oranını (aspect ratio) koruma durumlarını, kutuyu doldurma biçimlerini ve kırpma (crop)/boşluk (letterbox) durumlarını açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
| Aspect Modu | En-Boy Oranını Korur mu? | Kutu Doldurma Davranışı | Kırpma (Crop) veya Boşluk Durumu |
| :--- | :---: | :--- | :--- |
| **`AspectFit`** | **EVET** (Korur) | Görselin **tamamını** ayrılan kutuya sığdırır. | Resim kutudan farklı orandaysa kenarlarda **boşluk (bant/letterbox)** kalır. |
| **`AspectFill`** | **EVET** (Korur) | Kutuyu hiçbir boşluk bırakmadan **tamamen doldurur**. | Kutuya sığmayan kısımlar dışarı taşar ve **kırpılır (crop edilir)**. |
| **`Fill`** | **HAYIR (BOZAR!)** | Resmi kutunun hem enine hem boyuna zorla esnetir. | Boşluk kalmaz, kırpma olmaz; ancak resim **basık veya sündürülmüş** olarak deforme olur. |
| **`Center`** | **EVET** (1:1 Boyut) | Resmi 1:1 orijinal piksel boyutunda kutunun tam ortasına yerleştirir. | Yeniden boyutlandırma yapmaz; kutudan büyükse taşan kısımlar gizlenir. |

</details>

---

### Soru 23 (Senaryo / UX Kararı): Hangi Ekranda Hangi `Aspect` Kullanılmalıdır?
**Soru:**
Aşağıdaki iki gerçek mobil senaryoda hangi `Aspect` modunun tercih edilmesi gerektiğini yazılım mühendisliği gerekçeleriyle belirtiniz:
* **Senaryo A:** Bir e-ticaret uygulamasında ayakkabı ürününün detay sayfası fotoğrafı.
* **Senaryo B:** Bir haber uygulamasının ana sayfasındaki manşet haber kartının arka plan görseli.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Senaryo A (E-Ticaret Ürün Fotoğrafı):** Kesinlikle **`AspectFit`** kullanılmalıdır. Çünkü müşteri ayakkabının burnunu, topuğunu ve tüm dikişlerini eksiksiz görmek zorundadır. `AspectFill` kullanılırsa ayakkabının uçları kırpılabilir, `Fill` kullanılırsa ayakkabı şekilsiz basık görünür.
* **Senaryo B (Haber Manşet Kartı):** Kesinlikle **`AspectFill`** kullanılmalıdır. Çünkü modern mobil tasarımda kartın sağında solunda siyah/gri boşluklar (bantlar) kalması amatör bir görüntü yaratır. Resmin odak noktası merkezde olduğu sürece kenarlarından bir miktar kırpılması tasarımı bozmaz; ekranın şık ve dolu görünmesini sağlar.

</details>

---

### Soru 24 (Sözel / Dosya Sistemi): Görsel Adlandırma Kuralları ve Derleme Hataları
**Soru:**
Visual Studio'da `Resources/Images` klasörüne eklenen bir görsel dosyasının adı `Turk Bayragi 2026.PNG` olarak kaydedilmiştir. Proje Android veya iOS emülatöründe derlenmeye çalışıldığında derleyici neden hata verir? Doğru dosya adlandırma kuralını yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Neden Hata Verir?:** Android ve iOS işletim sistemlerinin çekirdeği Linux/Unix tabanlı dosya sistemlerine (ext4, APFS) dayanır. Android derleme araçları (AAPT - Android Asset Packaging Tool):
  1. Büyük harf kullanımına (`PNG`),
  2. Dosya adında boşluk bulunmasına (` `),
  3. Türkçe/özel karakterlere (`ı`, `ğ`) kesinlikle izin vermez ve derleme kilitlenir.
* **Doğru Adlandırma:** Tamamen küçük harf, boşluk yerine alt çizgi (`_`) ve standart İngilizce karakterler kullanılmalıdır:
  `turk_bayragi_2026.png`

</details>

---

### Soru 25 (C# Code-Behind): Animasyonlu GIF Oynatma / Duraklatma Toggle Kodu
**Soru:**
Bir `Image` kontrolünde oynatılan animasyonlu GIF'i tek bir butona tıklayarak oynatıp duraklatan (toggle) ve buton üzerindeki yazıyı ("Oynat" / "Durdur") güncelleyen C# olay metodunu yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (C#):
```csharp
private void btnAnimasyonKontrol_Clicked(object sender, EventArgs e)
{
    // 1. Animasyonun durumunu tersine çevir (true ise false, false ise true)
    imgAnimasyon.IsAnimationPlaying = !imgAnimasyon.IsAnimationPlaying;

    // 2. Buton üzerindeki metni yeni duruma göre güncelle
    btnAnimasyonKontrol.Text = imgAnimasyon.IsAnimationPlaying ? "Durdur" : "Oynat";
}
```

</details>

---

### Soru 26 (C# Kodlama): Dizi Üzerinde Modülo (`%`) ile Dinamik Resim Değiştirme
**Soru:**
`Resources/Images` altında tanımlı 4 adet futbol takımı logosunu (`takim1.png`, `takim2.png`, `takim3.png`, `takim4.png`) bir butona her basıldığında sırayla ekrandaki `Image` bileşeninde gösteren ve son logoya gelindiğinde başa dönen C# kodunu yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (C#):
```csharp
public partial class MainPage : ContentPage
{
    private readonly string[] _logolar = { "takim1.png", "takim2.png", "takim3.png", "takim4.png" };
    private int _sayac = 0;

    public MainPage()
    {
        InitializeComponent();
    }

    private void btnIleri_Clicked(object sender, EventArgs e)
    {
        // Sayaç değerini dizi boyutu içinde döngüye sokmak için mod (%) alma
        _sayac = (_sayac + 1) % _logolar.Length;

        // Görseli çalışma zamanında dinamik güncelle
        imgTakim.Source = ImageSource.FromFile(_logolar[_sayac]);
    }
}
```

</details>

---

### Soru 27 (Performans / Grafik Motoru): `IsOpaque` Özelliğinin Önemi
**Soru:**
Bir `Image` kontrolüne `IsOpaque="True"` niteliği atandığında mobil cihazın grafik işlemcisi (GPU) üzerinde nasıl bir performans optimizasyonu sağlanır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* Varsayılan olarak `IsOpaque="False"` değerindedir ve GPU, resmin saydamlık (alpha) içerebileceğini varsayar. Bu durumda resmin arkasındaki pikseller ile önündeki pikselleri matematiksel formüllerle harmanlar (**Alpha Blending**).
* `IsOpaque="True"` yapıldığında render motoruna bu görselin hiçbir pikselinde saydamlık olmadığı bildirilir. GPU arka planı hesaplamayı bırakır ve pikselleri doğrudan ekrana yazar. Özellikle uzun listelerde kaydırma (scrolling) esnasında kare hızı (FPS) kayıplarını ve işlemci yükünü ciddi oranda düşürür.

</details>

---

### Soru 28 (XAML & Mimari): İkon Fontları (`FontImageSource`) Neden Resimlere Tercih Edilir?
**Soru:**
Mobil uygulamalarda düğmeler ve menüler için onlarca PNG dosyası kullanmak yerine neden IonIcons veya FontAwesome gibi **İkon Fontları (Font Icons)** tercih edilir? XAML'da nasıl kullanılır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **Tercih Nedenleri:**
   * **Paket Boyutu:** Yüzlerce PNG dosyasının getireceği megabaytlarca yük yerine tek bir küçük `.ttf` font dosyası (birkaç yüz KB) yeterlidir.
   * **Vektörel Çözünürlük:** Font tabanlı olduğu için ekran çözünürlüğüne bağlı kalmaksızın pikselsiz ve net görünür.
   * **Dinamik Renk Değişimi:** Tek bir kodla rengi (`Color="Red"`) değiştirilebilir; PNG'deki gibi her renk için ayrı resim üretmeye gerek kalmaz.
2. **XAML Kullanımı:**
```xml
<Image>
    <Image.Source>
        <FontImageSource FontFamily="IonIcons"
                         Glyph="&#xf10a;"
                         Color="Black"
                         Size="30" />
    </Image.Source>
</Image>
```

</details>

---

## MODÜL 5: Gelişmiş Arayüz Elemanları

### Soru 29 (HOCANIN VİZE UYARISI - Klasik Soru): `Thickness` Saat Yönü Kuralı
**Soru:**
Bir kontrol için `Padding="10, 5, 20, 15"` değeri tanımlanmıştır. Bu dört sayının hangi kenarlara kaçar piksel boşluk bıraktığını sırasıyla yazınız ve genel kuralı belirtiniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
Genel Kural: Dört parametreli `Thickness` tanımları sol kenardan başlar ve **saat yönünde** ilerler:

* **1. Değer (10):** **Sol (Left)** kenardan 10 piksel
* **2. Değer (5):** **Üst (Top)** kenardan 5 piksel
* **3. Değer (20):** **Sağ (Right)** kenardan 20 piksel
* **4. Değer (15):** **Alt (Bottom)** kenardan 15 piksel

*(Not: İki değer verilseydi `[Yatay (Sol-Sağ)], [Dikey (Üst-Alt)]` olurdu; tek değer verilseydi dört taraftan eşit olurdu).*

</details>

---

### Soru 30 (Geometri & Hesaplama): `BoxView` ile Kusursuz Daire Üretimi
**Soru:**
Genişliği ve yüksekliği 120 piksel (`WidthRequest="120" HeightRequest="120"`) olan bir `BoxView` kontrolünü kusursuz bir **daireye (circle)** dönüştürmek için `CornerRadius` özelliğine kaç verilmelidir? Formülüyle açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Formül:** Kare bir kutudan kusursuz bir daire elde etmek için köşe yarıçapı ($R$), kenar uzunluğunun tam yarısına eşit olmalıdır:
  $$R = \frac{\text{Kenar Uzunluğu}}{2} = \frac{120}{2} = 60$$
* **XAML Kodu:**
```xml
<BoxView WidthRequest="120"
         HeightRequest="120"
         CornerRadius="60"
         Color="MediumPurple" />
```
*(Not: `CornerRadius` değerini 60'tan daha büyük yapmak şekli daha fazla yuvarlaklaştırmaz; yarıçaptan sonrası işlevsizdir).*

</details>

---

### Soru 31 (Mimari & Tuzak Soru): `CheckBox` Kontrolünde Metin Kısıtı
**Soru:**
Bir geliştirici XAML koduna `<CheckBox Text="Kullanım şartlarını kabul ediyorum" />` yazmıştır. Bu kod neden derleme hatası verir? .NET MAUI'de bir onay kutusunun yanına metin eklemek için nasıl bir mimari kurulmalıdır?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Neden Hata Verir?:** .NET MAUI'de `CheckBox` sınıfının kendi üzerinde doğrudan bir `Text` / `Caption` özelliği **bulunmamaktadır**.
* **Doğru Mimari Çözüm:** Onay kutusunun yanına metin eklemek için bir `CheckBox` ve bir `Label` bileşeni yan yana getirilerek `Grid` veya `HorizontalStackLayout` içerisine yerleştirilmelidir:
```xml
<Grid ColumnDefinitions="Auto, *" ColumnSpacing="10">
    <CheckBox Grid.Column="0" x:Name="chkSart" />
    <Label Grid.Column="1"
           Text="Kullanım şartlarını kabul ediyorum."
           VerticalOptions="Center" />
</Grid>
```

</details>

---

### Soru 32 (XAML / Tasarım): Asimetrik Köşeli `Border` Mimarisi
**Soru:**
Yalnızca **sol-üst** ve **sağ-alt** köşeleri 35 piksel yuvarlatılmış, diğer iki köşesi sivri olan kırmızı çerçeveli bir `Border` tanımını XAML ile yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (XAML):
`StrokeShape` özelliğinin `RoundRectangle` parametresinde köşe sırası: `Sol-Üst, Sağ-Üst, Sağ-Alt, Sol-Alt` şeklindedir:
```xml
<Border Stroke="Red"
        StrokeThickness="2"
        StrokeShape="RoundRectangle 35, 0, 35, 0"
        Padding="10">
    <Label Text="Asimetrik Kart Tasarımı" />
</Border>
```

</details>

---

### Soru 33 (Sözel / Davranış): `ActivityIndicator` Otomatik Gizlenme Mantığı
**Soru:**
Bir `ActivityIndicator` bileşeni için arka plandaki veri yükleme işlemi bittiğinde `indicator.IsRunning = false;` kodu çalıştırılmıştır. Geliştiricinin ayrıca `indicator.IsVisible = false;` yazmasına gerek var mıdır? Neden?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Hayır, gerek yoktur.**
* Çünkü .NET MAUI mimarisinde `ActivityIndicator` bileşeni `IsRunning` değeri `false` yapıldığı anda ekranda yer kaplamayacak şekilde otomatik olarak gizlenir. Sadece `IsRunning = true` yapıldığında ekranda belirip dönmeye başlar.

</details>

---

### Soru 34 (XAML & C#): `Switch` ile Canlı Ayarlar Menüsü
**Soru:**
Kullanıcı karanlık mod anahtarını açtığında (`IsToggled="True"`) yeşil, kapattığında kırmızı olan ve varsayılan olarak açık duran bir `Switch` bileşeninin XAML tanımını yapınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (XAML):
`Switch` bileşeninin renkleri C# koduna gerek kalmadan doğrudan XAML üzerinden verilebilir:
```xml
<Switch x:Name="swtKaranlikMod"
        IsToggled="True"
        OnColor="ForestGreen"
        OffColor="Crimson"
        ThumbColor="White" />
```

</details>

---

### Soru 35 (Sorun Giderme / Reçete): .NET MAUI Derleme ve Cache Kilitlenmesi
**Soru:**
Visual Studio'da açılan bir MAUI projesinde `ScrollView` ve `VerticalStackLayout` gibi standart sınıfların altı kırmızı çizilmekte ve derleme esnasında Mono kilitlenmesi yaşanmaktadır. Bu sorunu çözmek için uygulanması gereken 3 adımlı kesin çözümü yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. Visual Studio tamamen kapatılır.
2. Projenin bulunduğu klasöre gidilerek **`bin`** ve **`obj`** klasörleri (özellikle `Debug`/`Release` önbellekleri) tamamen silinir.
3. Visual Studio tekrar açılır ve üst menüden **Build > Rebuild Solution (Çözümü Yeniden Derle)** seçeneği çalıştırılır.

</details>

---

## MODÜL 6: Tarih/Saat Seçiciler, Açılır Listeler ve Çok Satırlı Editör

### Soru 36 (HOCANIN VİZE UYARISI - Format Dizgeleri): `DatePicker` ve `TimePicker` Format Belirteçleri
**Soru:**
1. `DatePicker` kontrolünde Ay için neden küçük `mm` yerine **büyük `MM`** kullanılmalıdır?
2. `TimePicker` kontrolünde 24 saat formatı için hangi belirteç kullanılır?
3. Türk Dil Kurumu (TDK) kurallarına göre tarih ve saat formatı tanımlarını XAML sözdizimiyle yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **`MM` vs `mm`:** Biçimlendirme standartlarında büyük `MM` **Ayı (Month)** temsil eder; küçük `mm` ise saatin **dakikasını (Minute)** temsil eder. Eğer DatePicker'da `mm` yazılırsa ay yerine saatin dakikası görüntülenmeye çalışılır ve mantık hatası oluşur.
2. **24 Saat Belirteci:** 24 saatlik format için **büyük `HH`** kullanılır (`00` – `23`). Küçük `hh` ise 12 saatlik AM/PM formatını verir.
3. **TDK Uyumlu XAML Tanımları:** TDK'ya göre dijital tarih ve saatte ayırıcı olarak tek nokta (`.`) kullanılmalıdır:
   * Tarih: `Format="dd.MM.yyyy"`
   * Saat: `Format="HH.mm"`

</details>

---

### Soru 37 (HOCANIN VİZE UYARISI - Crash / NullReference): `Picker` Seçim Güvenliği
**Soru:**
Aşağıdaki C# kodunu inceleyiniz:
```csharp
private void btnOnayla_Clicked(object sender, EventArgs e)
{
    string secim = pkrSehir.SelectedItem.ToString();
    lblBilgi.Text = $"Seçilen İl: {secim}";
}
```
Kullanıcı henüz açılır listeden bir şehir seçmeden butona basarsa uygulama nasıl bir hata verir? Bu çökme hatasını önleyen güvenli C# kodunu yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Hata Analizi:** Kullanıcı henüz listeden bir seçim yapmadığında `pkrSehir.SelectedIndex` değeri **`-1`** olur ve `pkrSehir.SelectedItem` değeri **`null`** döner. Null olan bir nesne üzerinden `.ToString()` metodu çağrıldığında uygulama **`NullReferenceException`** fırlatarak çöker (crash).
* **Güvenli C# Kodu:**
```csharp
private async void btnOnayla_Clicked(object sender, EventArgs e)
{
    // SelectedIndex -1 kontrolü
    if (pkrSehir.SelectedIndex != -1)
    {
        string secim = pkrSehir.SelectedItem.ToString();
        lblBilgi.Text = $"Seçilen İl: {secim} (Sıra: {pkrSehir.SelectedIndex})";
    }
    else
    {
        await DisplayAlert("Uyarı", "Lütfen bir şehir seçiniz!", "Tamam");
    }
}
```

</details>

---

### Soru 38 (XAML Sözdizimi): `Picker` İçinde Statik `x:Array` Tanımlama
**Soru:**
Bir `Picker` bileşeni içine XAML ortamında "Lisans", "Yüksek Lisans" ve "Doktora" seçeneklerini statik bir dizi olarak ekleyen XAML kodunu yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (XAML):
```xml
<Picker x:Name="pkrEgitim"
        Title="Eğitim Düzeyinizi Seçiniz"
        HorizontalTextAlignment="Center">
    <Picker.ItemsSource>
        <x:Array Type="{x:Type x:String}">
            <x:String>Lisans</x:String>
            <x:String>Yüksek Lisans</x:String>
            <x:String>Doktora</x:String>
        </x:Array>
    </Picker.ItemsSource>
</Picker>
```

</details>

---

### Soru 39 (Sözel / Davranış): `Editor.AutoSize="TextChanges"` Mantığı
**Soru:**
`Editor` kontrolünde `AutoSize="TextChanges"` niteliğinin çalışma prensibini açıklayınız. Bu özellik aktifken neden bileşene sabit bir `HeightRequest="150"` verilmemelidir?

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Çalışma Prensibi:** Kullanıcı metin yazdıkça veya `Enter` tuşuna basıp yeni bir satıra geçtikçe, editör kutusunun dikey yüksekliği otomatik olarak aşağıya doğru kendiliğinden uzar.
* **Sabit `HeightRequest` Çakışması:** Eğer sabit bir yükseklik verilirse, `AutoSize` motoru kutunun dikey uzamasını sınırlandırır ve metin kutusu sabit kalıp içeri doğru kaymaya (scroll) başlar. İki özellik birbiriyle çelişeceği için `AutoSize="TextChanges"` kullanılırken sabit yükseklik verilmemelidir.

</details>

---

### Soru 40 (Karşılaştırma): `Entry` ve `Editor` Kontrolleri Arasındaki Farklar
**Soru:**
`Entry` ve `Editor` arayüz kontrollerini kullanım amaçları, satır kapasiteleri, tetiklenen olayları ve esneme kabiliyetleri açısından bir tablo halinde karşılaştırınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
| Karşılaştırma Kriteri | `Entry` Kontrolü | `Editor` Kontrolü |
| :--- | :--- | :--- |
| **Satır Kapasitesi** | Yalnızca **Tek Satır** (Single-line) | **Çok Satırlı** (Multi-line) |
| **Temel Kullanım Alanı** | Ad, soyad, e-posta, şifre, telefon, TC kimlik | Adres, serbest yorum, dilekçe, düşünce girişi |
| **Klavye 'Enter' Davranışı**| **`Completed`** olayını tetikler (Form onaylanır) | Bir alt satıra geçer (Yeni satır ekler) |
| **Şifre Desteği (`IsPassword`)**| Destekler (`*` maskelemesi yapılabilir) | Desteklemez (Şifre için kullanılmaz) |
| **Dikey Esneme (`AutoSize`)** | Bulunmaz | `AutoSize="TextChanges"` ile otomatik uzar |

</details>

---

### Soru 41 (İş Mantığı / Senaryo): +18 Yaş Sınırı Doğum Tarihi Kısıtı
**Soru:**
Yalnızca 18 yaşından büyüklerin kayıt olabileceği bir mobil uygulamada `DatePicker` kontrolünün `MaximumDate` özelliğine C# code-behind'da nasıl bir kısıtlama getirilmelidir? Kod satırını yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (C#):
Kullanıcının bugünden en az 18 yıl önceki bir tarihi seçebilmesi için üst sınır bugünden 18 yıl geriye çekilir:
```csharp
dtpDogumTarihi.MaximumDate = DateTime.Today.AddYears(-18);
```

</details>

---

### Soru 42 (Olay Yönetimi): `DatePicker` Olayları
**Soru:**
`DatePicker` kontrolünde bulunan `Opened`, `Closed` ve `DateSelected` olaylarının hangi durumlarda tetiklendiğini açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **`Opened`:** Kullanıcı tarih seçiciye dokunup yerel takvim penceresi ekranda açıldığı anda tetiklenir.
2. **`Closed`:** Kullanıcı takvim penceresini kapattığı anda tetiklenir (Tarih seçse de seçmeden vazgeçip kapatsa da çalışır).
3. **`DateSelected`:** Kullanıcı takvimden farklı bir tarih seçip onay butonuna bastığında tetiklenir (`DateChangedEventArgs` ile eski ve yeni tarihi döndürür).

</details>

---

## BÖLÜM 7: Bütüncül Klasik Vize Sınav Provası

### Soru 43 (Büyük Sınav Sorusu - XAML): "Proje Sunumu Oylama Formu" Tasarımı
**Soru:**
Dersin 4 Kasım tarihli oturumunda geliştirilen ve hocanın sınav prototipi olarak gösterdiği **"Proje Sunumu Oylama Formu"** arayüzünü aşağıdaki bileşenleri içerecek şekilde XAML ile tasarlayınız:
1. Sayfanın taşmasını önleyen bir `ScrollView` ve içinde `VerticalStackLayout`,
2. Koyu kırmızı renkte ortalanmış kalın bir başlık etiketi,
3. Varsayılan tarihi 16 Aralık 2026 olan, `dd.MM.yyyy` formatında bir `DatePicker`,
4. Varsayılan saati `09:15` olan, `HH.mm` formatında bir `TimePicker`,
5. Seçenekleri "Bilgisayar Laboratuvarı", "Amfi", "Konferans Salonu" olan bir `Picker`,
6. Kullanıcının görüşlerini girebileceği, `AutoSize="TextChanges"` özellikli bir `Editor`,
7. En altta formu gönderen bir `Button`.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (XAML):
```xml
<ScrollView>
    <VerticalStackLayout Spacing="15" Padding="20">

        <!-- Başlık -->
        <Label Text="Mobil Cihazlar Dersi Proje Sunumu Oylama Formu"
               FontSize="20"
               FontAttributes="Bold"
               TextColor="DarkRed"
               HorizontalTextAlignment="Center" />

        <!-- 1. Tarih Seçici -->
        <Label Text="Tarih Seçiniz:" FontAttributes="Bold" />
        <DatePicker x:Name="dtpTarih"
                    Date="2026/12/16"
                    MinimumDate="2026/12/15"
                    MaximumDate="2026/12/29"
                    Format="dd.MM.yyyy"
                    FontSize="18"
                    TextColor="Red" />

        <!-- 2. Saat Seçici -->
        <Label Text="Saat Seçiniz:" FontAttributes="Bold" />
        <TimePicker x:Name="tmpSaat"
                    Time="09:15:00"
                    Format="HH.mm"
                    FontSize="18"
                    TextColor="Red" />

        <!-- 3. Yer Seçici (Picker) -->
        <Label Text="Sunum Yeri Seçiniz:" FontAttributes="Bold" />
        <Picker x:Name="pkrYer"
                Title="Lütfen bir yer seçiniz..."
                FontSize="18">
            <Picker.ItemsSource>
                <x:Array Type="{x:Type x:String}">
                    <x:String>Bilgisayar Laboratuvarı</x:String>
                    <x:String>Amfi</x:String>
                    <x:String>Konferans Salonu</x:String>
                </x:Array>
            </Picker.ItemsSource>
        </Picker>

        <!-- 4. Çok Satırlı Düşünceler (Editor) -->
        <Label Text="Düşünceleriniz / Notlarınız:" FontAttributes="Bold" />
        <Editor x:Name="edtDusunceler"
                Placeholder="Lütfen düşüncelerinizi yazınız..."
                FontSize="16"
                AutoSize="TextChanges"
                MaxLength="500" />

        <!-- 5. Gönder Butonu -->
        <Button x:Name="btnGonder"
                Text="Oyumu Gönder"
                Clicked="btnGonder_Clicked"
                HeightRequest="50"
                CornerRadius="25"
                BackgroundColor="DarkRed"
                TextColor="White"
                Margin="0, 20, 0, 0" />

    </VerticalStackLayout>
</ScrollView>
```

</details>

---

### Soru 44 (Büyük Sınav Sorusu - C# Code-Behind): Form Doğrulama ve `DisplayAlert` Çıktısı
**Soru:**
Soru 43'te tasarladığınız arayüzün C# arka plan kodunda (`btnGonder_Clicked`):
* `DatePicker`'dan seçilen tarihi `dd.MM.yyyy` formatında bir string değişkene alınız.
* `TimePicker`'dan seçilen saati `hh\:mm` formatında bir string değişkene alınız.
* `Picker` bileşenini denetleyiniz; eğer kullanıcı yer seçmemişse (`SelectedIndex == -1`) kullanıcıyı `DisplayAlert` ile uyararak işlemi durdurunuz.
* `Editor` alanı boşsa "Belirtilmedi", doluysa kullanıcının yazdığı metni alınız.
* Tüm bilgileri derleyip tek bir `DisplayAlert` pop-up penceresinde kullanıcıya gösteriniz.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm (C#):
```csharp
private async void btnGonder_Clicked(object sender, EventArgs e)
{
    // 1. Tarih ve Saat Bilgilerini Formatlayarak Okuma
    string secilenTarih = dtpTarih.Date.ToString("dd.MM.yyyy");
    string secilenSaat = tmpSaat.Time.ToString(@"hh\:mm");

    // 2. Picker Seçim Kontrolü (NullReference / Crash Önleme)
    if (pkrYer.SelectedIndex == -1)
    {
        await DisplayAlert("Eksik Bilgi", "Lütfen bir sunum yeri seçiniz!", "Tamam");
        pkrYer.Focus();
        return;
    }
    string secilenYer = $"{pkrYer.SelectedItem} (İndeks: {pkrYer.SelectedIndex})";

    // 3. Çok Satırlı Editor Metin Kontrolü
    string dusunceler = string.IsNullOrWhiteSpace(edtDusunceler.Text)
        ? "Belirtilmedi"
        : edtDusunceler.Text;

    // 4. Çapraz Platform Uyumlu Bildirim Mesajı Oluşturma
    string bildirim = $"Oyunuz sisteme kaydedildi.\n\n" +
                      $"Tarih: {secilenTarih}\n" +
                      $"Saat: {secilenSaat}\n" +
                      $"Yer: {secilenYer}\n" +
                      $"Görüşler: {dusunceler}";

    // 5. Ekranda Gösterme
    await DisplayAlert("Oylama Sonucu", bildirim, "Kapat");
}
```

</details>

---

### Soru 45 (Bütüncül Analiz): Sınavda Kağıda Kod Yazarken Dikkat Edilecek 5 Altın Kural
**Soru:**
Kağıt üzerinde yapılan klasik yazılı sınavlarda öğrencilerin en çok puan kaybettiği 5 sözdizimi ve mimari hatayı yazınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
1. **`x:Name` Yerine `Name` Yazmak:** XAML'da `x:` isim alanını unutarak C# tarafından kontrole erişememek.
2. **`Picker`'da Seçim Kontrolü Yapmamak:** `pkr.SelectedItem.ToString()` yazıp `SelectedIndex == -1` durumunu kontrol etmeyerek uygulamanın çökmesine yol açmak.
3. **Tarih/Saat Formatlarında Büyük-Küçük Harf Karışıklığı:** Ay için `MM` yerine dakika belirteci olan `mm` yazmak; 24 saat için `HH` yerine `hh` yazmak.
4. **`CheckBox`'a `Text` Özelliği Vermek:** MAUI'de `CheckBox` üzerinde `Text` özelliği olmadığını unutup derleme hatası almak.
5. **`Editor.AutoSize` Varken Sabit Yükseklik Vermek:** `AutoSize="TextChanges"` tanımlıyken `HeightRequest="100"` vererek kutunun dikey uzamasını engellemek.

</details>

---

### Soru 46 (Algoritma & Proje Tasarımı): Seviyeli Kart Eşleştirme Oyunu Mimarisi
**Soru:**
Derste verilen Türk takımları logolu **Kart Eşleştirme Oyunu** projesinin seviyeli (level) oyun mimarisi kurallarını ve seviye atlama algoritmasını açıklayınız.

<details>
<summary><b>🔍 Çözümü ve Detaylı Anlatımı Gör</b></summary>

#### Çözüm:
* **Oyun Kuralları:**
  * **Seviye 1:** Ekranda **2 çift (toplam 4 kart)** bulunur. Çiftler eşleştiğinde Seviye 2'ye geçilir.
  * **Seviye 2:** Ekranda **3 çift (toplam 6 kart)** bulunur.
  * **Kademeli Artış:** Her başarılı seviyede kart sayısı 1 çift (2 kart) artar.
  * **Maksimum Seviye:** Oyun **10 çift (toplam 20 kart)** seviyesine kadar devam eder.
* **Eşleştirme Algoritması:**
  1. Kullanıcı 1. karta tıklar $\implies$ Kart görseli açılır (`ImageSource` görünür olur).
  2. Kullanıcı 2. karta tıklar $\implies$ İki kartın takım logoları karşılaştırılır.
  3. **Eşleşirse:** Her iki kart açık bırakılır (veya ekrandan gizlenir), puan eklenir ve eşleşen çift sayacı artırılır.
  4. **Eşleşmezse:** Kısa bir gecikme (`Task.Delay(500)`) sonrası her iki kart tekrar kapalı duruma çevrilir.
  5. Seviyedeki tüm çiftler bulunduğunda seviye sayacı `_aktifSeviye++` yapılır ve yeni kart dizilimi oluşturulur.

</details>
