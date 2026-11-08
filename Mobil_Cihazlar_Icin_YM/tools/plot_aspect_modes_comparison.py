import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_aspect_modes_comparison(output_path):
    fig, axes = plt.subplots(1, 4, figsize=(16, 5), dpi=300)
    fig.suptitle('🚨 [HOCANIN KESİN SINAV UYARISI] .NET MAUI Image.Aspect En-Boy Oranı Modları Karşılaştırması', 
                 fontsize=14, fontweight='bold', color='#B91C1C', y=1.02)

    titles = [
        ('AspectFit', '#1E40AF', '#DBEAFE', 
         '• En-boy oranını KORUR.\n• Resmin TAMAMINI kutuya sığdırır.\n• Oran uyuşmazsa kenarlarda\n  boşluk (bant/letterbox) kalır.'),
        ('AspectFill', '#065F46', '#D1FAE5', 
         '• En-boy oranını KORUR.\n• Kutuyu TAMAMEN doldurur.\n• Asla boşluk kalmaz;\n  ancak taşan kısımlar KIRPILIR (crop).'),
        ('Fill', '#991B1B', '#FEE2E2', 
         '• En-boy oranını BOZAR!\n• Resmi kutunun enine ve boyuna esnetir.\n• Görsel basık/yayvanlaşır.\n• Fotoğraflar için tavsiye edilmez.'),
        ('Center', '#6B21A8', '#F3E8FF', 
         '• 1:1 orijinal piksel boyutu.\n• Resmi kutunun merkezine ortalar.\n• Yeniden boyutlandırmaz;\n  kutudan taşan alanlar görünmez.')
    ]

    for idx, ax in enumerate(axes):
        ax.set_xlim(-0.2, 4.2)
        ax.set_ylim(-1.5, 4.5)
        ax.axis('off')
        
        mode_name, head_color, bg_card, explanation = titles[idx]

        # Container Frame (Target Box: 4x3 ratio or Square)
        box_w, box_h = 3.6, 2.7
        box_x, box_y = 0.2, 1.2
        
        # Outer card background
        card = patches.FancyBboxPatch((-0.1, -1.3), 4.2, 5.5, boxstyle="round,pad=0.15", 
                                      fc=bg_card, ec=head_color, lw=1.8)
        ax.add_patch(card)
        
        # Header title
        ax.text(2.0, 3.9, f'{idx+1}. {mode_name}', ha='center', va='center', 
                fontsize=13, fontweight='bold', color=head_color)

        # Draw target container box (Canvas)
        box_rect = patches.Rectangle((box_x, box_y), box_w, box_h, 
                                     fc='#F3F4F6', ec='#374151', lw=2.5, linestyle='--')
        ax.add_patch(box_rect)
        ax.text(box_x + 0.1, box_y + box_h - 0.2, 'Ayrılan Kutu (Width / Height)', 
                fontsize=7.5, color='#4B5563', style='italic')

        # Draw the image according to mode
        if mode_name == 'AspectFit':
            # Image is 16:9, fits horizontally, vertical empty bars
            img_w = 3.6
            img_h = 2.025
            img_x = box_x
            img_y = box_y + (box_h - img_h) / 2
            
            # Empty margins (top/bottom)
            top_bar = patches.Rectangle((box_x, img_y + img_h), box_w, (box_h - img_h)/2, fc='#9CA3AF', alpha=0.5)
            bot_bar = patches.Rectangle((box_x, box_y), box_w, (box_h - img_h)/2, fc='#9CA3AF', alpha=0.5)
            ax.add_patch(top_bar)
            ax.add_patch(bot_bar)
            
            # The image
            img_rect = patches.Rectangle((img_x, img_y), img_w, img_h, fc='#3B82F6', alpha=0.85, ec='#1D4ED8', lw=1.5)
            ax.add_patch(img_rect)
            ax.text(2.0, img_y + img_h/2, 'Orijinal Görsel\n(Oran Korundu - Tam Görünür)', ha='center', va='center', 
                    fontsize=8, fontweight='bold', color='white')
            ax.text(2.0, box_y + 0.15, 'Boşluk (Bant)', ha='center', va='center', fontsize=7, color='#1F2937')
            ax.text(2.0, box_y + box_h - 0.15, 'Boşluk (Bant)', ha='center', va='center', fontsize=7, color='#1F2937')

        elif mode_name == 'AspectFill':
            # Image fills vertical (2.7), so width becomes 2.7 * (16/9) = 4.8, overflows horizontally by 1.2
            img_w = 4.8
            img_h = 2.7
            img_x = box_x - (img_w - box_w) / 2
            img_y = box_y
            
            # Cropped outer area (overflow)
            overflow_left = patches.Rectangle((img_x, img_y), (img_w - box_w)/2, img_h, 
                                              fc='#EF4444', alpha=0.4, linestyle=':', ec='#B91C1C')
            overflow_right = patches.Rectangle((box_x + box_w, img_y), (img_w - box_w)/2, img_h, 
                                               fc='#EF4444', alpha=0.4, linestyle=':', ec='#B91C1C')
            ax.add_patch(overflow_left)
            ax.add_patch(overflow_right)
            
            # Visible image area
            img_rect = patches.Rectangle((box_x, box_y), box_w, box_h, fc='#10B981', alpha=0.85, ec='#047857', lw=1.5)
            ax.add_patch(img_rect)
            ax.text(2.0, box_y + box_h/2, 'Kutuyu Tam Doldurur\n(Oran Korundu - Boşluk Yok)', ha='center', va='center', 
                    fontsize=8, fontweight='bold', color='white')
            ax.text(box_x - 0.3, box_y + box_h/2, 'Kırpıldı\n(Crop)', ha='center', va='center', fontsize=6.5, color='#991B1B', rotation=90)
            ax.text(box_x + box_w + 0.3, box_y + box_h/2, 'Kırpıldı\n(Crop)', ha='center', va='center', fontsize=6.5, color='#991B1B', rotation=270)

        elif mode_name == 'Fill':
            # Distorted directly to box size
            img_rect = patches.Rectangle((box_x, box_y), box_w, box_h, fc='#EF4444', alpha=0.85, ec='#B91C1C', lw=1.5)
            ax.add_patch(img_rect)
            ax.text(2.0, box_y + box_h/2, 'ORAN BOZULDU!\n(Enine / Boyuna Esnetildi)\nBasık & Deforme Görünüm', 
                    ha='center', va='center', fontsize=8, fontweight='bold', color='white')

        elif mode_name == 'Center':
            # 1:1 original pixel scale (assume larger than box)
            img_w = 4.2
            img_h = 3.2
            img_x = box_x - (img_w - box_w)/2
            img_y = box_y - (img_h - box_h)/2
            
            # Ghost overflow
            ghost = patches.Rectangle((img_x, img_y), img_w, img_h, fc='none', ec='#9333EA', lw=1.5, linestyle=':')
            ax.add_patch(ghost)
            
            # Visible center
            img_rect = patches.Rectangle((box_x, box_y), box_w, box_h, fc='#A855F7', alpha=0.85, ec='#7E22CE', lw=1.5)
            ax.add_patch(img_rect)
            ax.text(2.0, box_y + box_h/2, 'Merkez Odaklı\n(1:1 Orijinal Piksel Boyutu)\nTaşan Alanlar Gizlenir', 
                    ha='center', va='center', fontsize=8, fontweight='bold', color='white')

        # Bottom explanatory text
        ax.text(2.0, -0.6, explanation, ha='center', va='center', fontsize=8.2, color='#1F2937')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Aspect modes comparison saved to: {output_path}')

if __name__ == '__main__':
    draw_aspect_modes_comparison('/home/antigravity/yusufsanverdi/Ders_Notlari/Mobil_Cihazlar_Icin_YM/assets/aspect_modes_comparison.png')
