# Mobil Cihazlar İçin Yazılım Mühendisliği – Kapsamlı ve Modüler Ders Notları

Bu dizin, **Mobil Cihazlar İçin Yazılım Mühendisliği** dersinin tüm transkriptleri, teorik anlatımları, hocanın bizzat vurguladığı vize sınavı uyarıları, dersteki tahta kodları, 7 Ekim 2026 tarihli el yazısı notları ve pratik uygulama mimarileri taranarak pedagojik bir öğrenme sırasına göre yapılandırılmış modüler ders notlarını içermektedir.

Tüm kod blokları XAML ve C# standartlarında hazırlanmış, `assets/` klasöründeki yüksek çözünürlüklü şemalar ve grafiklerle desteklenmiş; yardımcı Python çizim scriptleri ise `tools/` klasöründe toplanmıştır.

---

## 📚 Müfredat ve Modül İndeksi

| Modül No | Konu Başlığı | Dosya Bağlantısı | Ana İçerikler ve Vize Sınavı Odakları |
| :---: | :--- | :--- | :--- |
| **01** | **Giriş, Çapraz Platform Mimarileri ve .NET MAUI Temelleri** | [01_Giris_ve_NET_MAUI_Mimarisi.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/notlar/01_Giris_ve_NET_MAUI_Mimarisi.md) | .NET MAUI vs. Flutter vs. Web Tabanlı (WebView) karşılaştırması, Mono/Xamarin'den MAUI'ye evrim, .NET 10 LTS tercihi, Android USB Hata Ayıklama (7 tık kuralı), Apple/Mac bağımlılığı ve Pair to Mac, Proje anatomisi (`MauiProgram`, `AppShell`), Kontrol hiyerarşisi (`Page` $\rightarrow$ `Layout` $\rightarrow$ `View`), `Label` kontrolü ve tipografi psikolojisi. |
| **02** | **Temel Metin, Girdi ve Etkileşim Bileşenleri (7 Ekim Notları Dahil)** | [02_Temel_Metin_Girdi_ve_Etkilesim_Bilesenleri.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/notlar/02_Temel_Metin_Girdi_ve_Etkilesim_Bilesenleri.md) | **[7 EKİM EL YAZISI NOTLARI ENTEGRE]** `Entry` kontrolünün derinlemesine tüm nitelikleri: `IsPassword` (`*`), `Keyboard` türleri (`Numeric`, `Email`, `Chat` vb.), `ClearButtonVisibility`, `MaxLength`, `HorizontalTextAlignment` (Justify tek satır davranışı), `TextTransform` ve Türkçe `i/ı` harf tuzağı, `x:Name` adlandırma kuralı, `Completed` olayı ve C# metot imzası, `DisplayAlert` diyalog penceresi, Temel `Grid` ve `Button` etkileşimi. |
| **03** | **Sayısal Seçiciler, Renk Sistemleri ve Grid Mimarisi** | [03_Sayisal_Seciciler_Renk_Sistemleri_ve_Grid.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/notlar/03_Sayisal_Seciciler_Renk_Sistemleri_ve_Grid.md) | `Slider` kontrolü ve özellikleri, Sayısal hassasiyet ve GANO yuvarlama formülü ($\frac{\text{Math.Round}(\text{Değer} \times 100)}{100}$), Dijital renk sistemleri (RGB, RGBA, Hex, HSL/HSV), `Stepper` (Rotation="-90" dikey Stepper), **Slider ve Stepper senkronizasyonu (Kaba ayar + İnce ayar)**, `Grid` mimarisi (`Row/ColumnDefinitions`, `*`, `Auto`, piksel, Span), `Button` köşe yarıçapı ($\frac{\text{Height}}{2}$) ile tam oval kuralı. |
| **04** | **Görsel Yönetimi, Aspect Oranları ve İkon Fontları** | [04_Gorsel_Yonetimi_Aspect_Oranlari_ve_Ikon_Fontlari.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/notlar/04_Gorsel_Yonetimi_Aspect_Oranlari_ve_Ikon_Fontlari.md) | **[HOCANIN KESİN SINAV UYARISI] `Image.Aspect` türleri (`AspectFit`, `AspectFill`, `Fill`, `Center`)** çizim ve şematik davranışları, Vektörel (SVG) vs. Raster (PNG, JPG, GIF, WebP), `Resources/Images` Android/iOS Unix dosya adlandırma kısıtları (küçük harf, alt çizgi, boşluksuz), Animasyonlu GIF (`IsAnimationPlaying` toggle), İnternet resimleri (`IsLoading`), C# dinamik resim değiştirme (mod `%` döngüsü), `IsOpaque` GPU optimizasyonu, Özel fontlar ve İkon fontları (`FontImageSource`, glifler). |
| **05** | **Gelişmiş Arayüz Elemanları (Border, Stroke, BoxView, Seçim Kontrolleri)** | [05_Gelismis_Arayuz_Elemanlari_Border_ve_Secim_Kontrolleri.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/notlar/05_Gelismis_Arayuz_Elemanlari_Border_ve_Secim_Kontrolleri.md) | `ActivityIndicator` (otomatik gizlenme kuralı), `Border` kontrolü ve gelişmiş `Stroke` özellikleri (`StrokeShape="RoundRectangle"`, `StrokeDashArray`), **`Thickness` Saat Yönü Kuralı (`Padding="Sol, Üst, Sağ, Alt"`)**, `BoxView` ile tam daire üretme geometrisi ($CornerRadius = \frac{\text{Kenar}}{2}$), `CheckBox` (kendi üzerinde metin olmaması kısıtı) ve `CheckedChanged` ile dinamik renk, `Switch` kontrolü (`OnColor`, `OffColor`, `ThumbColor`), Grid ile responsive yerleşim, `bin` ve `obj` temizleme reçetesi. |
| **06** | **Tarih/Saat Seçiciler, Açılır Listeler ve Çok Satırlı Editör** | [06_Tarih_Saat_Seciciler_Listeler_ve_Editor.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/notlar/06_Tarih_Saat_Seciciler_Listeler_ve_Editor.md) | **Kağıt üzerinde klasik yazılı sınav formatı duyurusu**, `DatePicker` (`MinimumDate`, `MaximumDate`, +18 yaş kısıtı senaryosu), Format kuralları (`yyyy`, `MM` büyük harf ay, `dd`), `TimePicker` (`HH` 24h büyük harf, `mm` dakika, TDK nokta kuralı), `Picker` (statik `x:Array`, **`SelectedIndex == -1` çökme / NullReferenceException koruması**), `Editor` (**`AutoSize="TextChanges"`** dikey uzama davranışı), `Entry` vs. `Editor` karşılaştırması, Sınıf içi kapsamlı Proje Oylama Formu mimarisi. |

---

## 🛠️ Klasör ve Dosya Organizasyonu

```text
Mobil_Cihazlar_Icin_YM/
├── notlar/                                           # Kronolojik ve pedagojik modüler notlar
│   ├── 01_Giris_ve_NET_MAUI_Mimarisi.md
│   ├── 02_Temel_Metin_Girdi_ve_Etkilesim_Bilesenleri.md
│   ├── 03_Sayisal_Seciciler_Renk_Sistemleri_ve_Grid.md
│   ├── 04_Gorsel_Yonetimi_Aspect_Oranlari_ve_Ikon_Fontlari.md
│   ├── 05_Gelismiş_Arayuz_Elemanlari_Border_ve_Secim_Kontrolleri.md
│   ├── 06_Tarih_Saat_Seciciler_Listeler_ve_Editor.md
│   └── README.md                                     # Ana dizin rehberi (Bu dosya)
├── assets/                                           # Yüksek çözünürlüklü teknik şemalar
│   ├── maui_architecture_hierarchy.png
│   ├── aspect_modes_comparison.png
│   ├── grid_layout_architecture.png
│   ├── border_stroke_thickness.png
│   └── input_picker_formats.png
├── tools/                                            # Şemaları üreten Python çizim araçları
│   ├── plot_maui_architecture_and_hierarchy.py
│   ├── plot_aspect_modes_comparison.py
│   ├── plot_grid_and_alignment.py
│   ├── plot_border_stroke_and_thickness.py
│   └── plot_input_and_picker_controls.py
└── Sinav_Sorulari_ve_Cozumleri.md                    # Açılır-kapanır (toggle) interaktif soru bankası
```

---

## 💡 Kağıt Üzerinde Klasik Vize Sınavına Hazırlık Stratejisi

1. **Önce Modülleri Sırayla Okuyun:** Her modülün başındaki **🚨 HOCANIN VİZE SINAVI UYARILARI** kutucuklarını mutlaka ezberleyin.
2. **Görselleri İnceleyin:** `assets/` klasöründeki şemaları gözünüzde canlandırın (Özellikle 4 Aspect modu ve Thickness saat yönü kuralı).
3. **İnteraktif Soru Bankasını Çözün:** [Sinav_Sorulari_ve_Cozumleri.md](file:///home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/Sinav_Sorulari_ve_Cozumleri.md) dosyasındaki soruları önce cevabı açmadan bir kağıda elle çözün, ardından `<details>` toggle'ına tıklayarak cevabınızı karşılaştırın.
