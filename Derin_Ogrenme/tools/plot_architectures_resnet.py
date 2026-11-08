import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_resnet_block(output_path):
    fig, ax = plt.subplots(figsize=(7, 6), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 9)

    # Input X
    c_in = plt.Circle((3, 8), 0.45, color='#DBEAFE', ec='#2563EB', lw=2)
    ax.add_patch(c_in)
    ax.text(3, 8, 'x (Girdi)', ha='center', va='center', fontsize=11, fontweight='bold', color='#1E40AF')

    # Main path
    ax.annotate('', xy=(3, 6.7), xytext=(3, 7.55),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=2))

    # Weight Layer 1 (Conv)
    r1 = patches.FancyBboxPatch((1.6, 5.8), 2.8, 0.9, boxstyle="round,pad=0.1", fc='#FEF3C7', ec='#D97706', lw=1.8)
    ax.add_patch(r1)
    ax.text(3, 6.25, 'Ağırlık Katmanı (Conv)', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#B45309')

    ax.annotate('', xy=(3, 4.9), xytext=(3, 5.7),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=2))
    ax.text(3.4, 5.3, 'ReLU', fontsize=9, color='#059669', fontweight='bold')

    # Weight Layer 2 (Conv)
    r2 = patches.FancyBboxPatch((1.6, 3.9), 2.8, 0.9, boxstyle="round,pad=0.1", fc='#FEF3C7', ec='#D97706', lw=1.8)
    ax.add_patch(r2)
    ax.text(3, 4.35, 'Ağırlık Katmanı (Conv)', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#B45309')
    ax.text(1.2, 4.35, 'F(x)', fontsize=11, fontweight='bold', color='#DC2626')

    ax.annotate('', xy=(3, 2.7), xytext=(3, 3.8),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=2))

    # Skip Connection (Identity Shortcut)
    # Arc from (3, 7.8) out to x=6 then down to (3.4, 2.3)
    ax.plot([3.45, 6.0, 6.0, 3.55], [8.0, 8.0, 2.3, 2.3], color='#2563EB', lw=2.5, ls='-')
    ax.annotate('', xy=(3.45, 2.3), xytext=(3.9, 2.3),
                arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.5))
    ax.text(6.15, 5.2, 'Artık Bağlantı (Skip Connection)\nx (Kimlik / Identity)', 
            fontsize=10, fontweight='bold', color='#1D4ED8', rotation=270, va='center')

    # Addition Circle
    c_add = plt.Circle((3, 2.3), 0.4, color='#DCFCE7', ec='#10B981', lw=2)
    ax.add_patch(c_add)
    ax.text(3, 2.3, '+', ha='center', va='center', fontsize=18, fontweight='bold', color='#065F46')

    # Output to ReLU
    ax.annotate('', xy=(3, 1.1), xytext=(3, 1.85),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=2))
    ax.text(3.4, 1.45, 'ReLU', fontsize=9, color='#059669', fontweight='bold')

    # Final Output
    c_out = plt.Circle((3, 0.6), 0.45, color='#F3E8FF', ec='#9333EA', lw=2)
    ax.add_patch(c_out)
    ax.text(3, 0.6, 'F(x) + x', ha='center', va='center', fontsize=11, fontweight='bold', color='#6B21A8')

    ax.set_title('ResNet Artık Blok (Residual Block) Mimarisi\nGradyanların Geri Akışını Sağlayan Kısayol',
                 fontsize=11, fontweight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'ResNet block saved to: {output_path}')

def draw_cnn_timeline(output_path):
    fig, ax = plt.subplots(figsize=(11, 4), dpi=300)
    ax.axis('off')
    ax.set_xlim(1996, 2021)
    ax.set_ylim(-1.5, 2.5)

    # Timeline line
    ax.plot([1997, 2020], [0, 0], color='#4B5563', lw=3)

    models = [
        (1998, "LeNet-5", "MNIST Rakam Tanıma\nModern CNN Temeli", 1),
        (2012, "AlexNet", "ImageNet Zaferi\nReLU, Dropout, GPU", -1),
        (2014, "VGGNet", "3x3 Küçük Filtreler\nDerinlik Artışı", 1),
        (2015, "ResNet", "Skip Connection\nVanishing Gradient Çözümü", -1),
        (2017, "MobileNet", "Depthwise Separable Conv\nMobil ve Hafif Cihazlar", 1),
        (2019, "EfficientNet", "Compound Scaling\nOptimum Verim ve Boyut", -1)
    ]

    colors = ['#3B82F6', '#EF4444', '#F59E0B', '#10B981', '#8B5CF6', '#EC4899']

    for i, (year, name, desc, direction) in enumerate(models):
        y_text = 1.3 * direction
        ax.plot([year, year], [0, 0.5 * direction], color=colors[i], lw=2)
        ax.plot(year, 0, 'o', color=colors[i], markersize=9)
        
        # Box
        p = patches.FancyBboxPatch((year - 1.2, y_text - 0.4), 2.4, 0.8,
                                   boxstyle="round,pad=0.1", fc='#F9FAFB', ec=colors[i], lw=1.8)
        ax.add_patch(p)
        ax.text(year, y_text + 0.15, f"{name} ({year})", ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=colors[i])
        ax.text(year, y_text - 0.15, desc, ha='center', va='center',
                fontsize=7.5, color='#374151')

    ax.set_title('CNN Mimarilerinin Tarihsel Evrimi (1998 - 2019)', fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Timeline saved to: {output_path}')

if __name__ == '__main__':
    draw_resnet_block('Derin_Ogrenme/assets/resnet_skip_connection.png')
    draw_cnn_timeline('Derin_Ogrenme/assets/cnn_models_timeline.png')
