import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_cnn_architecture(output_path):
    fig, ax = plt.subplots(figsize=(14, 5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)

    # Stages data: (name, shape_str, color, x_pos, width, height)
    layers = [
        ("Girdi (Input)", "64 x 64 x 3", "#93C5FD", 1.0, 0.6, 2.4),
        ("Conv2D\n(K=3, S=1, P=1)", "64 x 64 x 16", "#FCA5A5", 2.8, 0.7, 2.4),
        ("MaxPool2D\n(2x2, S=2)", "32 x 32 x 16", "#FDE047", 4.6, 0.6, 1.6),
        ("Conv2D\n(K=3, S=1, P=1)", "32 x 32 x 32", "#F87171", 6.4, 0.9, 1.6),
        ("MaxPool2D\n(2x2, S=2)", "16 x 16 x 32", "#FACC15", 8.2, 0.8, 1.0),
        ("Flatten", "8192", "#86EFAC", 10.0, 0.3, 3.2),
        ("Dense\n(Sınıflandırma)", "10 Sınıf (Softmax)", "#C084FC", 11.8, 0.4, 1.2),
    ]

    for i, (name, shape, col, x, w, h) in enumerate(layers):
        rect = patches.FancyBboxPatch((x - w/2, 2.5 - h/2), w, h,
                                      boxstyle="round,pad=0.08", fc=col, ec='#1F2937', lw=1.5)
        ax.add_patch(rect)
        ax.text(x, 2.5 - h/2 - 0.45, name, ha='center', va='top', fontsize=8.5, fontweight='bold', color='#111827')
        ax.text(x, 2.5 + h/2 + 0.25, shape, ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#1E40AF')

        # Arrow to next
        if i < len(layers) - 1:
            next_x = layers[i+1][3]
            next_w = layers[i+1][4]
            ax.annotate('', xy=(next_x - next_w/2 - 0.05, 2.5), xytext=(x + w/2 + 0.05, 2.5),
                        arrowprops=dict(arrowstyle="->", color='#374151', lw=1.8))

    ax.set_title('Klasik CNN Katman Akışı ve Boyut Dönüşümü (Sınav Sorusunun Mimarisi)',
                 fontsize=12, fontweight='bold', pad=25)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'CNN architecture diagram saved to: {output_path}')

def draw_conv_operation(output_path):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=300)
    
    # 1. Input with Padding
    ax = axes[0]
    ax.axis('off')
    ax.set_title('Girdi Matrisi + Padding (P=1)\n(Mavi: Piksel, Gri: Sıfır Dolgu)', fontsize=9.5, fontweight='bold')
    grid = [
        [0,0,0,0,0],
        [0,1,2,0,0],
        [0,0,1,1,0],
        [0,1,0,2,0],
        [0,0,0,0,0]
    ]
    for r in range(5):
        for c in range(5):
            val = grid[r][c]
            bg = '#DBEAFE' if (0 < r < 4 and 0 < c < 4) else '#F3F4F6'
            rect = plt.Rectangle((c*0.2, 0.8 - r*0.2), 0.18, 0.18, fc=bg, ec='#4B5563', lw=1)
            ax.add_patch(rect)
            ax.text(c*0.2 + 0.09, 0.8 - r*0.2 + 0.09, str(val), ha='center', va='center', fontsize=9)
    # Highlight 3x3 kernel receptive field
    hl = plt.Rectangle((0, 0.4), 0.58, 0.58, fill=False, ec='#DC2626', lw=2.5, ls='--')
    ax.add_patch(hl)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)

    # 2. Kernel (Filter)
    ax = axes[1]
    ax.axis('off')
    ax.set_title('Evrişim Çekirdeği (Kernel)\n(3x3 Filtre Ağırlıkları)', fontsize=9.5, fontweight='bold')
    k_vals = [[1,0,-1], [1,0,-1], [1,0,-1]]
    for r in range(3):
        for c in range(3):
            rect = plt.Rectangle((0.2 + c*0.2, 0.7 - r*0.2), 0.18, 0.18, fc='#FEF3C7', ec='#D97706', lw=1.2)
            ax.add_patch(rect)
            ax.text(0.2 + c*0.2 + 0.09, 0.7 - r*0.2 + 0.09, str(k_vals[r][c]), ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(0.5, 0.05, 'Dikey Kenar Bulucu (Sobel Filtresi)', ha='center', fontsize=8.5, color='#B45309', style='italic')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 3. Output Feature Map
    ax = axes[2]
    ax.axis('off')
    ax.set_title('Çıktı: Öznitelik Haritası\n(Feature Map)', fontsize=9.5, fontweight='bold')
    for r in range(3):
        for c in range(3):
            bg = '#DCFCE7' if (r==0 and c==0) else '#F9FAFB'
            rect = plt.Rectangle((0.2 + c*0.2, 0.7 - r*0.2), 0.18, 0.18, fc=bg, ec='#10B981', lw=1.2)
            ax.add_patch(rect)
            txt = '3' if (r==0 and c==0) else '...'
            ax.text(0.2 + c*0.2 + 0.09, 0.7 - r*0.2 + 0.09, txt, ha='center', va='center', fontsize=10, fontweight='bold', color='#065F46')
    ax.text(0.5, 0.05, 'Yeşil hücre: Çekirdek ile çarpım toplamı', ha='center', fontsize=8.5, color='#047857')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Conv operation diagram saved to: {output_path}')

if __name__ == '__main__':
    draw_cnn_architecture('Derin_Ogrenme/assets/cnn_architecture_flow.png')
    draw_conv_operation('Derin_Ogrenme/assets/convolution_stride_padding.png')
