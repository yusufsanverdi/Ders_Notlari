import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_gan_architecture(output_path):
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6)

    # 1. Latent Noise (z)
    c_z = plt.Circle((1.2, 4.5), 0.5, color='#E0E7FF', ec='#4338CA', lw=2)
    ax.add_patch(c_z)
    ax.text(1.2, 4.5, 'Rastgele\nGürültü (z)', ha='center', va='center', fontsize=9, fontweight='bold', color='#3730A3')

    # Arrow from noise to Generator
    ax.annotate('', xy=(2.6, 4.5), xytext=(1.8, 4.5),
                arrowprops=dict(arrowstyle="->", color='#374151', lw=2))

    # 2. Generator Box
    g_box = patches.FancyBboxPatch((2.7, 3.6), 2.2, 1.8, boxstyle="round,pad=0.1",
                                   fc='#FEF3C7', ec='#D97706', lw=2.5)
    ax.add_patch(g_box)
    ax.text(3.8, 4.8, 'ÜRETEÇ (Generator - G)', ha='center', va='center', fontsize=10, fontweight='bold', color='#B45309')
    ax.text(3.8, 4.1, 'Analoji: Sahte Para\nBasan Kalpazan', ha='center', va='center', fontsize=8.5, color='#78350F', style='italic')

    # Arrow from Generator to Fake Image
    ax.annotate('', xy=(5.8, 4.5), xytext=(5.0, 4.5),
                arrowprops=dict(arrowstyle="->", color='#D97706', lw=2))

    # Fake Image Box
    fake_box = patches.FancyBboxPatch((5.9, 3.9), 1.2, 1.2, boxstyle="round,pad=0.05",
                                      fc='#FEE2E2', ec='#DC2626', lw=2)
    ax.add_patch(fake_box)
    ax.text(6.5, 4.5, 'Sahte\nGörsel\nG(z)', ha='center', va='center', fontsize=9, fontweight='bold', color='#991B1B')

    # Real Images Box (bottom)
    real_box = patches.FancyBboxPatch((4.0, 1.0), 1.6, 1.3, boxstyle="round,pad=0.08",
                                      fc='#DCFCE7', ec='#10B981', lw=2)
    ax.add_patch(real_box)
    ax.text(4.8, 1.8, 'Gerçek Görseller', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#065F46')
    ax.text(4.8, 1.3, 'Veri Seti (x)', ha='center', va='center', fontsize=8.5, color='#047857')

    # Arrows into Discriminator
    ax.annotate('', xy=(7.7, 3.8), xytext=(7.2, 4.3),
                arrowprops=dict(arrowstyle="->", color='#DC2626', lw=2))
    ax.annotate('', xy=(7.7, 3.2), xytext=(5.7, 1.8),
                arrowprops=dict(arrowstyle="->", color='#10B981', lw=2))

    # 3. Discriminator Box
    d_box = patches.FancyBboxPatch((7.8, 2.5), 2.2, 2.0, boxstyle="round,pad=0.1",
                                   fc='#EFF6FF', ec='#2563EB', lw=2.5)
    ax.add_patch(d_box)
    ax.text(8.9, 3.9, 'AYIRT EDİCİ\n(Discriminator - D)', ha='center', va='center', fontsize=10, fontweight='bold', color='#1E40AF')
    ax.text(8.9, 3.0, 'Analoji: Sahteyi\nYakalamaya Çalışan Polis', ha='center', va='center', fontsize=8.5, color='#1E3A8A', style='italic')

    # Output Arrow
    ax.annotate('', xy=(10.7, 3.5), xytext=(10.1, 3.5),
                arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.5))
    ax.text(10.8, 3.8, 'Gerçek (1)', fontsize=9, fontweight='bold', color='#059669')
    ax.text(10.8, 3.2, 'Sahte (0)', fontsize=9, fontweight='bold', color='#DC2626')

    # Feedback loop arrow (Backprop into G)
    ax.plot([8.9, 8.9, 3.8, 3.8], [2.4, 0.4, 0.4, 3.5], color='#7C3AED', lw=2, ls='--')
    ax.annotate('', xy=(3.8, 3.5), xytext=(3.8, 3.0),
                arrowprops=dict(arrowstyle="->", color='#7C3AED', lw=2))
    ax.text(6.3, 0.65, 'Çekişmeli Geri Bildirim (Geri Yayılım ile G Gelişir)',
            ha='center', fontsize=9, fontweight='bold', color='#6D28D9')

    ax.set_title('Çekişmeli Üretici Ağlar (GAN) Mimarisi ve Minimax Eğitimi', fontsize=12, fontweight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'GAN architecture saved to: {output_path}')

if __name__ == '__main__':
    draw_gan_architecture('Derin_Ogrenme/assets/gan_architecture_diagram.png')
