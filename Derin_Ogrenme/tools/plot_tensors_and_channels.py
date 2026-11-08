import matplotlib.pyplot as plt
import numpy as np

def draw_tensors(output_path):
    fig, axes = plt.subplots(1, 4, figsize=(14, 4), dpi=300)
    
    # 0D Scalar
    ax = axes[0]
    ax.axis('off')
    ax.set_title('0D Tensör: Skaler (Scalar)', fontsize=11, fontweight='bold', pad=15)
    circle = plt.Circle((0.5, 0.5), 0.25, color='#3B82F6', alpha=0.3, ec='#1D4ED8', lw=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, '42', fontsize=20, ha='center', va='center', fontweight='bold', color='#1E3A8A')
    ax.text(0.5, 0.1, 'Tek bir sayı (Boyut = 0)\nÖrn: Kayıp değeri (Loss)', ha='center', fontsize=9, color='#4B5563')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 1D Vector
    ax = axes[1]
    ax.axis('off')
    ax.set_title('1D Tensör: Vektör (Vector)', fontsize=11, fontweight='bold', pad=15)
    for i in range(5):
        rect = plt.Rectangle((0.15 + i*0.14, 0.4), 0.12, 0.25, color='#10B981', alpha=0.3, ec='#047857', lw=1.5)
        ax.add_patch(rect)
        ax.text(0.21 + i*0.14, 0.525, f'x_{i+1}', ha='center', va='center', fontsize=9, fontweight='bold', color='#064E3B')
    ax.text(0.5, 0.1, '1B Dizi (Shape: [5])\nÖrn: Öznitelik Vektörü', ha='center', fontsize=9, color='#4B5563')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 2D Matrix
    ax = axes[2]
    ax.axis('off')
    ax.set_title('2D Tensör: Matris (Matrix)', fontsize=11, fontweight='bold', pad=15)
    for r in range(3):
        for c in range(3):
            rect = plt.Rectangle((0.2 + c*0.2, 0.65 - r*0.2), 0.18, 0.18, color='#F59E0B', alpha=0.3, ec='#B45309', lw=1.5)
            ax.add_patch(rect)
            ax.text(0.29 + c*0.2, 0.74 - r*0.2, f'{r},{c}', ha='center', va='center', fontsize=8, color='#78350F')
    ax.text(0.5, 0.1, '2B Tablo (Shape: [3, 3])\nÖrn: Grayscale Resim / Ağırlıklar', ha='center', fontsize=9, color='#4B5563')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 3D/4D Tensor
    ax = axes[3]
    ax.axis('off')
    ax.set_title('3D / 4D Tensör', fontsize=11, fontweight='bold', pad=15)
    colors = ['#EF4444', '#10B981', '#3B82F6']
    labels = ['Kırmızı (R)', 'Yeşil (G)', 'Mavi (B)']
    for i in range(3):
        offset = (2 - i) * 0.1
        rect = plt.Rectangle((0.15 + offset, 0.35 + offset), 0.45, 0.35, 
                             color=colors[i], alpha=0.35, ec=colors[i], lw=2)
        ax.add_patch(rect)
        ax.text(0.18 + offset, 0.65 + offset, labels[i], fontsize=8, fontweight='bold', color='#111827')
    ax.text(0.5, 0.1, 'RGB Resim (Shape: [H, W, 3])\nBatch Resim (Shape: [B, H, W, C])', ha='center', fontsize=9, color='#4B5563')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Tensors diagram saved to: {output_path}')

def draw_rgb_channels(output_path):
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.5), dpi=300)
    
    # Synthetic RGB image
    np.random.seed(42)
    h, w = 40, 40
    rgb = np.zeros((h, w, 3), dtype=np.uint8)
    # Circle in center (reddish/yellow)
    Y, X = np.ogrid[:h, :w]
    dist = np.sqrt((X - 20)**2 + (Y - 20)**2)
    rgb[dist < 12] = [230, 80, 50]
    rgb[dist >= 12] = [40, 140, 200]
    
    axes[0].imshow(rgb)
    axes[0].set_title('Renkli Görüntü (RGB)\n[H x W x 3]', fontsize=10, fontweight='bold')
    axes[0].axis('off')
    
    # R channel
    axes[1].imshow(rgb[:, :, 0], cmap='Reds')
    axes[1].set_title('Kırmızı Kanalı (R)\n[H x W x 1]', fontsize=10, fontweight='bold')
    axes[1].axis('off')
    
    # G channel
    axes[2].imshow(rgb[:, :, 1], cmap='Greens')
    axes[2].set_title('Yeşil Kanalı (G)\n[H x W x 1]', fontsize=10, fontweight='bold')
    axes[2].axis('off')
    
    # B channel
    axes[3].imshow(rgb[:, :, 2], cmap='Blues')
    axes[3].set_title('Mavi Kanalı (B)\n[H x W x 1]', fontsize=10, fontweight='bold')
    axes[3].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'RGB channels saved to: {output_path}')

if __name__ == '__main__':
    draw_tensors('Derin_Ogrenme/assets/tensors_overview.png')
    draw_rgb_channels('Derin_Ogrenme/assets/rgb_channels_breakdown.png')
