import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_grid_architecture(output_path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), dpi=300)
    fig.suptitle('.NET MAUI Grid (Izgara) Mimarisi ve Hizalama İlkeleri', fontsize=15, fontweight='bold', color='#1E3A8A', y=0.98)

    # ------------------ PANEL 1: GRID DEFINITIONS & SPAN ------------------
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Grid Satır / Sütun Mimarisi & Span Özellikleri', fontsize=12.5, fontweight='bold', color='#1E40AF', pad=12)

    # Column headers
    ax1.text(2.2, 9.3, 'Sütun 0 (Column 0)\nWidth="Auto"', ha='center', va='center', fontsize=9, fontweight='bold', color='#1D4ED8')
    ax1.text(5.5, 9.3, 'Sütun 1 (Column 1)\nWidth="2*"', ha='center', va='center', fontsize=9, fontweight='bold', color='#1D4ED8')
    ax1.text(8.5, 9.3, 'Sütun 2 (Column 2)\nWidth="1*"', ha='center', va='center', fontsize=9, fontweight='bold', color='#1D4ED8')

    # Row headers
    ax1.text(0.3, 7.5, 'Satır 0\nHeight="Auto"', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#4B5563', rotation=90)
    ax1.text(0.3, 4.8, 'Satır 1\nHeight="1*"', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#4B5563', rotation=90)
    ax1.text(0.3, 1.8, 'Satır 2\nHeight="80"', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#4B5563', rotation=90)

    # Cell 0,0: Label
    c00 = patches.FancyBboxPatch((1.0, 6.7), 2.4, 1.8, boxstyle="round,pad=0.1", fc='#EFF6FF', ec='#3B82F6', lw=1.5)
    ax1.add_patch(c00)
    ax1.text(2.2, 7.6, '[0, 0]\nLabel\nText="Ad Soyad:"', ha='center', va='center', fontsize=8.5, color='#1E40AF', fontweight='semibold')

    # Cell 0, 1-2: Entry with ColumnSpan=2
    c01 = patches.FancyBboxPatch((3.7, 6.7), 5.8, 1.8, boxstyle="round,pad=0.1", fc='#FEF3C7', ec='#F59E0B', lw=2)
    ax1.add_patch(c01)
    ax1.text(6.6, 7.6, 'Entry (Grid.Row="0" Grid.Column="1" Grid.ColumnSpan="2")\nPlaceholder="Adınızı ve soyadınızı giriniz..."', 
             ha='center', va='center', fontsize=8.5, color='#92400E', fontweight='bold')

    # Cell 1, 0-1: Editor with ColumnSpan=2
    c10 = patches.FancyBboxPatch((1.0, 3.7), 5.7, 2.4, boxstyle="round,pad=0.1", fc='#ECFDF5', ec='#10B981', lw=1.5)
    ax1.add_patch(c10)
    ax1.text(3.85, 4.9, 'Editor (Grid.Row="1" Grid.Column="0" Grid.ColumnSpan="2")\nAutoSize="TextChanges"\n(Çok Satırlı Not ve Açıklama Alanı)', 
             ha='center', va='center', fontsize=8.5, color='#065F46', fontweight='semibold')

    # Cell 1, 2: Switch
    c12 = patches.FancyBboxPatch((7.0, 3.7), 2.5, 2.4, boxstyle="round,pad=0.1", fc='#F3E8FF', ec='#9333EA', lw=1.5)
    ax1.add_patch(c12)
    ax1.text(8.25, 4.9, '[1, 2]\nSwitch\nOnColor="Green"\nIsToggled="True"', ha='center', va='center', fontsize=8.5, color='#6B21A8', fontweight='semibold')

    # Cell 2, 0-2: Button full span
    c20 = patches.FancyBboxPatch((1.0, 0.8), 8.5, 2.0, boxstyle="round,pad=0.1", fc='#FEE2E2', ec='#EF4444', lw=2)
    ax1.add_patch(c20)
    ax1.text(5.25, 1.8, 'Button (Grid.Row="2" Grid.Column="0" Grid.ColumnSpan="3")\nText="Formu Gönder ve Kaydet"  Clicked="btnGonder_Clicked"', 
             ha='center', va='center', fontsize=9, color='#991B1B', fontweight='bold')

    # ------------------ PANEL 2: UNITS AND SPACING ------------------
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Birim Türleri, Spacing ve Hizalama Seçenekleri', fontsize=12.5, fontweight='bold', color='#4338CA', pad=12)

    # Unit Types Card
    p_units = patches.FancyBboxPatch((0.5, 5.2), 9.0, 4.2, boxstyle="round,pad=0.2", fc='#F8FAFC', ec='#64748B', lw=1.8)
    ax2.add_patch(p_units)
    ax2.text(0.8, 9.0, '1. Satır ve Sütun Boyutlandırma Birimleri:', fontsize=10.5, fontweight='bold', color='#1E293B')
    ax2.text(0.8, 8.3, '• Yıldız / Oransal (*, 2*, 3*): Ekranın boşta kalan alanını paylaştırır.\n  Örn: ColumnDefinitions="4*, 1*" (Ekranı %80 ve %20 oranında ikiye böler).', fontsize=8.5, color='#334155')
    ax2.text(0.8, 7.3, '• Otomatik (Auto): İçindeki elemanın kapladığı alan kadar genişler.\n  Örn: Etiket içeriği ne kadar uzunsa satır o kadar yer kaplar.', fontsize=8.5, color='#334155')
    ax2.text(0.8, 6.3, '• Sabit Piksel (Örn: 80, 120): Ekrana ve çözünürlüğe bakılmaksızın mutlak boyuttur.\n  Örn: RowDefinitions="Auto, *, 60" (En alttaki buton satırı sabit 60px kalır).', fontsize=8.5, color='#334155')
    ax2.text(0.8, 5.5, '• Varsayılan Değer: Grid.Row="0" ve Grid.Column="0" varsayılandır, yazılmasa da çalışır.', fontsize=8, color='#0369A1', style='italic')

    # Spacing and Alignment Card
    p_align = patches.FancyBboxPatch((0.5, 0.4), 9.0, 4.4, boxstyle="round,pad=0.2", fc='#EEF2FF', ec='#4F46E5', lw=1.8)
    ax2.add_patch(p_align)
    ax2.text(0.8, 4.4, '2. Spacing ve Hizalama Mantığı (Options):', fontsize=10.5, fontweight='bold', color='#312E81')
    ax2.text(0.8, 3.7, '• RowSpacing="10" & ColumnSpacing="15": Hücreler arasındaki ızgara boşlukları.', fontsize=8.5, color='#1E1B4B')
    ax2.text(0.8, 3.0, '• HorizontalOptions / VerticalOptions:\n  - Start: Sol / Üst kenara yasla\n  - Center: Merkeze ortala\n  - End: Sağ / Alt kenara yasla\n  - Fill: Hücrenin tamamına yay / genişlet', fontsize=8.5, color='#1E1B4B')
    ax2.text(0.8, 1.2, '• [HOCANIN UYARISI]: StackLayout\'un "FillAndExpand" özelliği modern MAUI\'de kaldırılmıştır;\n  esnek arayüzlerde StackLayout yerine daima Grid tercih edilmelidir!', fontsize=8.2, color='#B91C1C', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Grid architecture saved to: {output_path}')

if __name__ == '__main__':
    draw_grid_architecture('/home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/assets/grid_layout_architecture.png')
