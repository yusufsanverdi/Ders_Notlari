import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_maui_architecture_and_hierarchy(output_path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7.5), dpi=300)
    
    # ------------------ PANEL 1: CROSS-PLATFORM ARCHITECTURES ------------------
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('.NET MAUI vs. Diğer Mobil Mimariler', fontsize=14, fontweight='bold', color='#1E3A8A', pad=15)

    # 1. Web-based / WebView (React Native, Ionic vb.)
    p1 = patches.FancyBboxPatch((0.5, 6.8), 9, 2.6, boxstyle="round,pad=0.2", fc='#FEF2F2', ec='#EF4444', lw=2)
    ax1.add_patch(p1)
    ax1.text(0.8, 8.9, '1. Web Tabanlı Çapraz Platformlar (React Native, Ionic, Cordova)', fontsize=10.5, fontweight='bold', color='#991B1B')
    ax1.text(0.8, 8.3, '• Mantık: HTML/CSS/JS kodları mobil içine gömülü bir WebView (tarayıcı) içinde çalışır.', fontsize=8.5, color='#374151')
    ax1.text(0.8, 7.8, '• Eksileri: Gerçek yerel (native) performans ve arayüz deneyiminden uzaktır.', fontsize=8.5, color='#B91C1C')
    ax1.text(0.8, 7.3, '• Yapı: [ Web Kodu ] ──> [ WebView Tarayıcı Motoru ] ──> [ Cihaz Ekranı ]', fontsize=8.2, color='#1F2937', family='monospace')

    # 2. Flutter (Kendi Çizim Motoru - Skia/Impeller)
    p2 = patches.FancyBboxPatch((0.5, 3.6), 9, 2.6, boxstyle="round,pad=0.2", fc='#EFF6FF', ec='#3B82F6', lw=2)
    ax1.add_patch(p2)
    ax1.text(0.8, 5.7, '2. Flutter & Skia/Impeller Çizim Motoru Yaklaşımı', fontsize=10.5, fontweight='bold', color='#1E40AF')
    ax1.text(0.8, 5.1, '• Mantık: Kendi çizim motoruyla (Skia/Impeller) pikselleri ekrana doğrudan tuval (canvas) gibi çizer.', fontsize=8.5, color='#374151')
    ax1.text(0.8, 4.6, '• Özellik: Android ve iOS\'ta birebir aynı piksel görünümü; fakat sistemin doğal kontrollerini kullanmaz.', fontsize=8.5, color='#1D4ED8')
    ax1.text(0.8, 4.1, '• Yapı: [ Dart Kodu ] ──> [ Skia / Impeller Motoru ] ──> [ Doğrudan Piksel Çizimi ]', fontsize=8.2, color='#1F2937', family='monospace')

    # 3. .NET MAUI (Doğrudan Yerel Bileşen Eşleme - Native Controls Mapping)
    p3 = patches.FancyBboxPatch((0.5, 0.4), 9, 2.7, boxstyle="round,pad=0.2", fc='#ECFDF5', ec='#10B981', lw=2.5)
    ax1.add_patch(p3)
    ax1.text(0.8, 2.6, '3. .NET MAUI (Doğrudan Yerel Kontrol Eşleme - En Yüksek Performans)', fontsize=10.5, fontweight='bold', color='#065F46')
    ax1.text(0.8, 2.0, '• Mantık: Tek XAML tanımı, derleme anında doğrudan hedef sistemin yerel (native) kontrollerine eşlenir.', fontsize=8.5, color='#374151')
    ax1.text(0.8, 1.5, '  - Android\'de: Native Android Button / Entry / DatePickerDialog', fontsize=8.2, color='#047857')
    ax1.text(0.8, 1.1, '  - iOS\'ta: Native UIButton / UITextField / UIDatePicker', fontsize=8.2, color='#047857')
    ax1.text(0.8, 0.7, '• Avantaj: Yüksek hız, donanım ivmelendirmesi, platformun doğal görünüm ve hissi (Look & Feel).', fontsize=8.5, color='#064E3B', fontweight='semibold')

    # ------------------ PANEL 2: MAUI CONTROL HIERARCHY ------------------
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('.NET MAUI Arayüz Kontrol Hiyerarşisi', fontsize=14, fontweight='bold', color='#4338CA', pad=15)

    # Level 1: Sayfa (Page)
    b_page = patches.FancyBboxPatch((1.0, 7.8), 8.0, 1.7, boxstyle="round,pad=0.2", fc='#EEF2FF', ec='#6366F1', lw=2)
    ax2.add_patch(b_page)
    ax2.text(5.0, 8.8, '1. SAYFA (Page) - Ekranın Tamamını Kapsar', ha='center', va='center', fontsize=11, fontweight='bold', color='#3730A3')
    ax2.text(5.0, 8.2, 'ContentPage, FlyoutPage, NavigationPage, TabbedPage', ha='center', va='center', fontsize=9, color='#4F46E5')

    # Arrow Down 1
    ax2.annotate('', xy=(5, 7.1), xytext=(5, 7.7), arrowprops=dict(facecolor='#4F46E5', shrink=0.05, width=2, headwidth=7))

    # Level 2: Yerleşim (Layout)
    b_layout = patches.FancyBboxPatch((1.0, 5.0), 8.0, 2.0, boxstyle="round,pad=0.2", fc='#FDF4FF', ec='#C084FC', lw=2)
    ax2.add_patch(b_layout)
    ax2.text(5.0, 6.4, '2. YERLEŞİM (Layout) - Görünümleri Ekrana Dizer', ha='center', va='center', fontsize=11, fontweight='bold', color='#6B21A8')
    ax2.text(5.0, 5.8, 'VerticalStackLayout (Dikey)  |  HorizontalStackLayout (Yatay)', ha='center', va='center', fontsize=8.8, color='#7E22CE')
    ax2.text(5.0, 5.3, 'Grid (Satır/Sütun Izgarası)   |  FlexLayout  |  AbsoluteLayout', ha='center', va='center', fontsize=8.8, color='#7E22CE')

    # Arrow Down 2
    ax2.annotate('', xy=(5, 4.3), xytext=(5, 4.9), arrowprops=dict(facecolor='#7E22CE', shrink=0.05, width=2, headwidth=7))

    # Level 3: Görünümler / Kontroller (Views)
    b_views = patches.FancyBboxPatch((0.5, 0.4), 9.0, 3.8, boxstyle="round,pad=0.2", fc='#F0FDF4', ec='#22C55E', lw=2)
    ax2.add_patch(b_views)
    ax2.text(5.0, 3.7, '3. GÖRÜNÜM / KONTROL (View) - Kullanıcı Etkileşim Elemanları', ha='center', va='center', fontsize=11, fontweight='bold', color='#14532D')
    
    # Sub categories
    ax2.text(1.0, 3.0, '• Metin / Girdi: Label, Entry, Editor, SearchBar', fontsize=9, color='#15803D', fontweight='semibold')
    ax2.text(1.0, 2.4, '• Aksiyon & Seçim: Button, CheckBox, Switch, RadioButton', fontsize=9, color='#15803D', fontweight='semibold')
    ax2.text(1.0, 1.8, '• Sayısal / Tarih: Slider, Stepper, DatePicker, TimePicker, Picker', fontsize=9, color='#15803D', fontweight='semibold')
    ax2.text(1.0, 1.2, '• Görsel / Biçim: Image, Border, BoxView, ActivityIndicator, ProgressBar', fontsize=9, color='#15803D', fontweight='semibold')
    ax2.text(1.0, 0.7, '• Kapsayıcı Yardımcılar: ScrollView (Kaydırma), RefreshView', fontsize=8.5, color='#166534', style='italic')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'MAUI Architecture and Hierarchy saved to: {output_path}')

if __name__ == '__main__':
    draw_maui_architecture_and_hierarchy('/home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/assets/maui_architecture_hierarchy.png')
