import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_input_picker_formats(output_path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7.5), dpi=300)
    fig.suptitle('.NET MAUI Girdi, Seçici ve Metin Kontrolleri Mimarisi', 
                 fontsize=14, fontweight='bold', color='#1E3A8A', y=0.98)

    # ------------------ PANEL 1: ENTRY VS EDITOR ------------------
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Entry (Tek Satır) vs. Editor (Çok Satır) Karşılaştırması', fontsize=12.5, fontweight='bold', color='#1E40AF', pad=12)

    # Entry Box
    b_entry = patches.FancyBboxPatch((0.5, 5.2), 9.0, 4.2, boxstyle="round,pad=0.2", fc='#EFF6FF', ec='#3B82F6', lw=2)
    ax1.add_patch(b_entry)
    ax1.text(0.8, 8.9, '1. Entry Kontrolü (Tek Satırlı Metin ve Veri Girişi)', fontsize=10.5, fontweight='bold', color='#1D4ED8')
    ax1.text(0.8, 8.2, '• Kullanım Alanı: Ad, soyad, e-posta, şifre, TC kimlik no gibi kısa tek satırlık girdiler.', fontsize=8.5, color='#1F2937')
    ax1.text(0.8, 7.6, '• Klavye Tipleri: Keyboard="Email", "Numeric", "Telephone", "Chat", "Text", "Url".', fontsize=8.5, color='#1F2937')
    ax1.text(0.8, 7.0, '• Güvenlik: IsPassword="True" (girilen karakterler "*" olarak maskelenir).', fontsize=8.5, color='#1F2937')
    ax1.text(0.8, 6.4, '• Silme Butonu: ClearButtonVisibility="WhileEditing" (yazarken sağda "X" ikonu çıkar).', fontsize=8.5, color='#1F2937')
    ax1.text(0.8, 5.7, '• Tetikleyici Olay: Completed="ent_Completed" (Kullanıcı klavyede Tamam/Enter\'a bastığında).', fontsize=8.5, color='#047857', fontweight='bold')

    # Editor Box
    b_editor = patches.FancyBboxPatch((0.5, 0.4), 9.0, 4.4, boxstyle="round,pad=0.2", fc='#FEF3C7', ec='#F59E0B', lw=2)
    ax1.add_patch(b_editor)
    ax1.text(0.8, 4.3, '2. Editor Kontrolü (Çok Satırlı Metin ve Geri Bildirim)', fontsize=10.5, fontweight='bold', color='#92400E')
    ax1.text(0.8, 3.6, '• Kullanım Alanı: Adres, dilekçe, serbest düşünce, yorum, geri bildirim girişleri.', fontsize=8.5, color='#1F2937')
    ax1.text(0.8, 2.9, '• [EN ÖNEMLİ ÖZELLİK]: AutoSize="TextChanges"\n  Kullanıcı Enter\'a basıp alt satıra geçtikçe kutunun yüksekliği aşağıya doğru kendiliğinden uzar!', 
             fontsize=8.5, color='#B45309', fontweight='bold')
    ax1.text(0.8, 1.8, '• Çakışma Uyarısı: AutoSize açıkken sabit HeightRequest verilmemelidir!', fontsize=8.2, color='#991B1B', style='italic')
    ax1.text(0.8, 1.2, '• Ek Denetimler: MaxLength="500", IsSpellCheckEnabled="True", IsTextPredictionEnabled="True".', fontsize=8.5, color='#1F2937')

    # ------------------ PANEL 2: DATE/TIME FORMAT & PICKER ------------------
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Tarih/Saat Format Belirteçleri ve Picker Yaşam Döngüsü', fontsize=12.5, fontweight='bold', color='#4338CA', pad=12)

    # Date / Time Format Card
    b_format = patches.FancyBboxPatch((0.5, 4.8), 9.0, 4.6, boxstyle="round,pad=0.2", fc='#FDF4FF', ec='#A855F7', lw=2)
    ax2.add_patch(b_format)
    ax2.text(0.8, 8.9, '1. DatePicker & TimePicker Format Deseni Kuralları', fontsize=10.5, fontweight='bold', color='#6B21A8')
    ax2.text(0.8, 8.2, '• DatePicker (Format="dd.MM.yyyy"):', fontsize=9, fontweight='bold', color='#4A044E')
    ax2.text(1.2, 7.6, '- yyyy: 4 haneli yıl (Örn: 2026)\n- MM (BÜYÜK HARF!): Ay (Örn: 10, 12). Küçük mm dakikadır, karıştırılmamalı!\n- dd: 2 haneli sıfır dolgulu gün (Örn: 05, 16)\n- TDK Kuralı: Dijital tarihte ayırıcı nokta (".") olmalıdır.', fontsize=8.2, color='#1F2937')
    ax2.text(0.8, 5.8, '• TimePicker (Format="HH.mm"):', fontsize=9, fontweight='bold', color='#4A044E')
    ax2.text(1.2, 5.2, '- HH (BÜYÜK HARF): 24 saat formatı (00 - 23)\n- hh (Küçük Harf): 12 saat formatı (01 - 12 AM/PM)\n- mm (Küçük Harf): Dakika (00 - 59)\n- TDK Kuralı: Dijital saat ile dakika arasında tek nokta kullanılmalıdır.', fontsize=8.2, color='#1F2937')

    # Picker Lifecycle & Crash Prevention Card
    b_picker = patches.FancyBboxPatch((0.5, 0.4), 9.0, 4.0, boxstyle="round,pad=0.2", fc='#FEE2E2', ec='#EF4444', lw=2.2)
    ax2.add_patch(b_picker)
    ax2.text(0.8, 3.9, '2. Picker (Açılır Liste) Çökme (Crash) Riski ve Önlemi', fontsize=10.5, fontweight='bold', color='#991B1B')
    ax2.text(0.8, 3.3, '• Varsayılan Durum: Henüz seçim yapılmadığında SelectedIndex = -1 ve SelectedItem = null olur.', fontsize=8.5, color='#1F2937')
    ax2.text(0.8, 2.7, '• HATA: if kontrolü yapılmadan doğrudan pkr.SelectedItem.ToString() okunursa\n  uygulama NullReferenceException vererek çöker!', fontsize=8.5, color='#991B1B', fontweight='bold')
    ax2.text(0.8, 1.3, '• KORUYUCU KOD (Code-Behind Güvenliği):\n  if (pkrYer.SelectedIndex != -1) {\n      string yer = pkrYer.SelectedItem.ToString();\n  }', fontsize=8.5, color='#065F46', family='monospace', fontweight='semibold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Input and Picker formats saved to: {output_path}')

if __name__ == '__main__':
    draw_input_picker_formats('/home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/assets/input_picker_formats.png')
