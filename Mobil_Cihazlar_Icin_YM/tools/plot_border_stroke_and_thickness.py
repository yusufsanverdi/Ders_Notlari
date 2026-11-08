import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_border_stroke_and_thickness(output_path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7.5), dpi=300)
    fig.suptitle('.NET MAUI Border, Stroke Nitelikleri, Thickness ve Geometri İlkeleri', 
                 fontsize=14, fontweight='bold', color='#1E3A8A', y=0.98)

    # ------------------ PANEL 1: THICKNESS & CLOCKWISE RULE ------------------
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Thickness (Padding & Margin) Saat Yönü Kuralı', fontsize=12.5, fontweight='bold', color='#1E40AF', pad=12)

    # Big Central Box for 4 values
    box_main = patches.FancyBboxPatch((2.2, 3.2), 5.6, 4.2, boxstyle="round,pad=0.2", fc='#FEF3C7', ec='#D97706', lw=2.5)
    ax1.add_patch(box_main)
    ax1.text(5.0, 5.3, 'Thickness Sınıfı\n(Padding / Margin)\n"Sol, Üst, Sağ, Alt"\n(Saat Yönü Kuralı)', 
             ha='center', va='center', fontsize=11, fontweight='bold', color='#92400E')

    # Top Arrow & Label (Üst - Top)
    ax1.annotate('2. DEĞER: ÜST (Top)\nÖrn: 5px', xy=(5.0, 7.5), xytext=(5.0, 8.8),
                 arrowprops=dict(facecolor='#D97706', shrink=0.08, width=2, headwidth=7),
                 ha='center', va='center', fontsize=9.5, fontweight='bold', color='#B45309')

    # Right Arrow & Label (Sağ - Right)
    ax1.annotate('3. DEĞER:\nSAĞ (Right)\nÖrn: 20px', xy=(7.9, 5.3), xytext=(9.2, 5.3),
                 arrowprops=dict(facecolor='#D97706', shrink=0.08, width=2, headwidth=7),
                 ha='center', va='center', fontsize=9, fontweight='bold', color='#B45309')

    # Bottom Arrow & Label (Alt - Bottom)
    ax1.annotate('4. DEĞER: ALT (Bottom)\nÖrn: 15px', xy=(5.0, 3.1), xytext=(5.0, 1.8),
                 arrowprops=dict(facecolor='#D97706', shrink=0.08, width=2, headwidth=7),
                 ha='center', va='center', fontsize=9.5, fontweight='bold', color='#B45309')

    # Left Arrow & Label (Sol - Left)
    ax1.annotate('1. DEĞER (Başlangıç):\nSOL (Left)\nÖrn: 10px', xy=(2.1, 5.3), xytext=(0.8, 5.3),
                 arrowprops=dict(facecolor='#D97706', shrink=0.08, width=2, headwidth=7),
                 ha='center', va='center', fontsize=9, fontweight='bold', color='#B45309')

    # Summary box at bottom
    ax1.text(5.0, 0.6, '• Tek Değer (10): Dört taraftan eşit 10px\n• Çift Değer (20, 5): [Yatay (Sol-Sağ)], [Dikey (Üst-Alt)]\n• Dört Değer (10, 5, 20, 15): Sol=10, Üst=5, Sağ=20, Alt=15', 
             ha='center', va='center', fontsize=8.5, color='#1F2937', 
             bbox=dict(boxstyle="round,pad=0.4", fc='#F3F4F6', ec='#D1D5DB'))

    # ------------------ PANEL 2: BORDER STROKE & BOXVIEW GEOMETRY ------------------
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Border Stroke Özellikleri ve BoxView Geometrisi', fontsize=12.5, fontweight='bold', color='#4338CA', pad=12)

    # 1. RoundRectangle 4 corners card
    c_stroke = patches.FancyBboxPatch((0.5, 5.6), 9.0, 4.0, boxstyle="round,pad=0.2", fc='#EEF2FF', ec='#6366F1', lw=2)
    ax2.add_patch(c_stroke)
    ax2.text(0.8, 9.2, '1. StrokeShape="RoundRectangle SolÜst, SağÜst, SağAlt, SolAlt":', fontsize=9.5, fontweight='bold', color='#3730A3')
    
    # Visual asymmetric box
    asym_box = patches.FancyBboxPatch((1.0, 6.2), 3.0, 2.4, boxstyle="round,pad=0.1", fc='#C7D2FE', ec='#4338CA', lw=2.5)
    ax2.add_patch(asym_box)
    ax2.text(2.5, 7.4, 'RoundRectangle\n"40, 0, 40, 0"', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1E1B4B')

    ax2.text(4.4, 8.4, '• StrokeThickness="3" (Çizgi kalınlığı)\n• StrokeDashArray="4, 1" (Kesikli çizgi)\n• StrokeLineCap: Flat | Round | Square\n• StrokeLineJoin: Miter | Bevel | Round', 
             fontsize=8.5, color='#1F2937')
    ax2.text(4.4, 6.1, '*(Android/iOS eksiksiz çizerken Windows\'ta render farkı olabilir)*', fontsize=7.5, color='#6B7280', style='italic')

    # 2. BoxView Geometry Card (Circle & Capsule)
    c_geom = patches.FancyBboxPatch((0.5, 0.4), 9.0, 4.8, boxstyle="round,pad=0.2", fc='#F0FDF4', ec='#22C55E', lw=2)
    ax2.add_patch(c_geom)
    ax2.text(0.8, 4.8, '2. BoxView CornerRadius ile Geometrik Şekil Üretimi:', fontsize=9.5, fontweight='bold', color='#14532D')

    # Draw perfect circle
    circle_patch = patches.Circle((2.5, 2.4), 1.2, fc='#86EFAC', ec='#15803D', lw=2)
    ax2.add_patch(circle_patch)
    ax2.text(2.5, 2.4, 'Kusursuz Daire\nWidth=100\nHeight=100\nCornerRadius=50', ha='center', va='center', fontsize=7.8, fontweight='bold', color='#064E3B')

    # Draw capsule
    capsule_patch = patches.FancyBboxPatch((4.5, 1.4), 4.6, 2.0, boxstyle="round,pad=0.4", fc='#A7F3D0', ec='#047857', lw=2)
    ax2.add_patch(capsule_patch)
    ax2.text(6.8, 2.4, 'Kapsül / Stadyum Formu\nWidth=200, Height=100\nCornerRadius=50 (Yüksekliğin Yarısı)', ha='center', va='center', fontsize=7.8, fontweight='bold', color='#064E3B')

    ax2.text(0.8, 0.7, '🚨 KRİTİK KURAL: CornerRadius kenarın yarısından büyük verilemez; yarıçaptan sonrası şekli değiştirmez!', 
             fontsize=7.8, fontweight='bold', color='#991B1B')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Border, Stroke and Thickness saved to: {output_path}')

if __name__ == '__main__':
    draw_border_stroke_and_thickness('/home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/assets/border_stroke_thickness.png')
