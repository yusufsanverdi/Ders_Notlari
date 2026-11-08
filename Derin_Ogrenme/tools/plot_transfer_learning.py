import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_transfer_learning(output_path):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5), dpi=300)
    
    # Strategy 1: Feature Extraction (Frozen Backbone)
    ax = axes[0]
    ax.axis('off')
    ax.set_title('1. Strateji: Öznitelik Çıkarımı (Katman Dondurma)\nKüçük Veri Setleri İçin', fontsize=11, fontweight='bold', color='#1E40AF')

    # Frozen Backbone
    b1 = patches.FancyBboxPatch((0.15, 0.35), 0.7, 0.5, boxstyle="round,pad=0.08",
                                fc='#E5E7EB', ec='#4B5563', lw=2, ls='--')
    ax.add_patch(b1)
    ax.text(0.5, 0.65, 'Önceden Eğitilmiş Omurga\n(Pre-trained Backbone: ResNet/EfficientNet)',
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#374151')
    ax.text(0.5, 0.48, 'DONDURULDU (FROZEN)\nrequires_grad = False\nAğırlıklar Güncellenmez',
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#DC2626')

    # New Head
    b2 = patches.FancyBboxPatch((0.2, 0.1), 0.6, 0.18, boxstyle="round,pad=0.05",
                                fc='#DCFCE7', ec='#10B981', lw=2)
    ax.add_patch(b2)
    ax.text(0.5, 0.19, 'Yeni Sınıflandırıcı Başlığı\n(Örn: 4 Sınıflı Dense Katman)',
            ha='center', va='center', fontsize=9, fontweight='bold', color='#065F46')
    ax.text(0.5, 0.05, 'EĞİTİLİR (Trainable)\nAğırlıklar güncellenir',
            ha='center', va='center', fontsize=8, color='#047857')

    # Strategy 2: Fine-Tuning
    ax = axes[1]
    ax.axis('off')
    ax.set_title('2. Strateji: İnce Ayar (Fine-Tuning)\nOrta/Büyük Veri Setleri İçin', fontsize=11, fontweight='bold', color='#991B1B')

    # Lower Backbone (Frozen)
    b3 = patches.FancyBboxPatch((0.15, 0.6), 0.7, 0.25, boxstyle="round,pad=0.05",
                                fc='#E5E7EB', ec='#4B5563', lw=2, ls='--')
    ax.add_patch(b3)
    ax.text(0.5, 0.75, 'Alt Katmanlar (Düşük Seviye Özellikler: Kenar, Çizgi)\nDONDURULDU (FROZEN)',
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#4B5563')

    # Upper Backbone (Unfrozen)
    b4 = patches.FancyBboxPatch((0.15, 0.32), 0.7, 0.22, boxstyle="round,pad=0.05",
                                fc='#FEF3C7', ec='#D97706', lw=2)
    ax.add_patch(b4)
    ax.text(0.5, 0.45, 'Üst Katmanlar (Yüksek Seviye Özellikler)\nKİLİDİ AÇILDI (Unfrozen)',
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B45309')
    ax.text(0.5, 0.36, 'Çok düşük öğrenme oranı ile eğitilir (lr = 1e-5)',
            ha='center', va='center', fontsize=7.5, color='#78350F', style='italic')

    # New Head (Unfrozen)
    b5 = patches.FancyBboxPatch((0.2, 0.1), 0.6, 0.18, boxstyle="round,pad=0.05",
                                fc='#DCFCE7', ec='#10B981', lw=2)
    ax.add_patch(b5)
    ax.text(0.5, 0.19, 'Yeni Sınıflandırıcı Başlığı\nEĞİTİLİR (Trainable)',
            ha='center', va='center', fontsize=9, fontweight='bold', color='#065F46')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Transfer learning saved to: {output_path}')

if __name__ == '__main__':
    draw_transfer_learning('Derin_Ogrenme/assets/transfer_learning_finetuning.png')
