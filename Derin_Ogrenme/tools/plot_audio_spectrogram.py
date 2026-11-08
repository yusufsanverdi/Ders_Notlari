import matplotlib.pyplot as plt
import numpy as np

def draw_audio_spectrogram(output_path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)
    
    # 1. 1D Waveform
    ax = axes[0]
    t = np.linspace(0, 1, 1000)
    # Signal with mixed frequencies
    signal = np.sin(2 * np.pi * 5 * t) * np.exp(-t) + 0.5 * np.sin(2 * np.pi * 20 * t) + 0.2 * np.random.normal(0, 0.2, 1000)
    ax.plot(t, signal, color='#2563EB', lw=1.2)
    ax.set_title('1 Boyutlu Ham Ses Dalgası (Zaman - Genlik)\n[Genlik: A(t)]', fontsize=10, fontweight='bold', color='#1E40AF')
    ax.set_xlabel('Zaman (s)', fontsize=9)
    ax.set_ylabel('Genlik', fontsize=9)
    ax.grid(True, alpha=0.3)

    # 2. 2D Spectrogram
    ax2 = axes[1]
    # Synthetic spectrogram matrix
    np.random.seed(42)
    spec = np.zeros((50, 100))
    for i in range(50):
        for j in range(100):
            spec[i, j] = np.sin(i / 5.0) * np.cos(j / 10.0) + np.random.uniform(0, 0.4)
    spec[15:25, 20:60] += 1.8  # high energy harmonic
    spec[35:40, 40:80] += 1.2
    
    im = ax2.imshow(spec, aspect='auto', origin='lower', cmap='viridis')
    ax2.set_title('2 Boyutlu Spektrogram (Zaman - Frekans - Enerji)\n2D CNN (ResNet / MobileNet) ile İşlenir', fontsize=10, fontweight='bold', color='#065F46')
    ax2.set_xlabel('Zaman Ekseninde Adımlar (X)', fontsize=9)
    ax2.set_ylabel('Frekans Kanalları (Y)', fontsize=9)
    fig.colorbar(im, ax=ax2, label='Ses Şiddeti (dB)')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Audio spectrogram diagram saved to: {output_path}')

def draw_background_bias(output_path):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
    
    # Cat on Green Grass
    ax = axes[0]
    ax.axis('off')
    ax.set_title('Laboratuvardaki Test Görüntüsü:\nYeşil Çimende Oturan Kedi', fontsize=10, fontweight='bold', color='#1E40AF')
    # Green background
    bg = plt.Rectangle((0, 0), 1, 1, color='#86EFAC', alpha=0.8)
    ax.add_patch(bg)
    # Cat face simplified
    cat = plt.Circle((0.5, 0.45), 0.25, color='#F59E0B', ec='#B45309', lw=2)
    ax.add_patch(cat)
    # Ears
    e1 = plt.Polygon([[0.3, 0.6], [0.38, 0.85], [0.45, 0.65]], color='#F59E0B', ec='#B45309')
    e2 = plt.Polygon([[0.7, 0.6], [0.62, 0.85], [0.55, 0.65]], color='#F59E0B', ec='#B45309')
    ax.add_patch(e1)
    ax.add_patch(e2)
    ax.text(0.5, 0.45, 'KEDİ', ha='center', va='center', fontsize=12, fontweight='bold', color='#78350F')
    ax.text(0.5, 0.08, 'Arka Plan: Yoğun Yeşil Çimen', ha='center', fontsize=9.5, fontweight='bold', color='#064E3B')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Model Decision Error
    ax2 = axes[1]
    ax2.axis('off')
    ax2.set_title('Modelin Yanılgısı (Arka Plan Yanlılığı):\n"Kediye Kurbağa Dedi!" Vakası', fontsize=10, fontweight='bold', color='#DC2626')
    
    err_box = plt.Rectangle((0.05, 0.1), 0.9, 0.8, color='#FEF2F2', ec='#EF4444', lw=2)
    ax2.add_patch(err_box)
    
    msg = (
        "MODELİN KARARI:\n"
        "Tahmin: %94 Kurbağa (Frog)! ❌\n\n"
        "NEDEN HATA YAPTI?\n"
        "• Eğitim setindeki tüm kurbağalar yeşil çimendeydi.\n"
        "• Model kedinin kulaklarını veya bıyıklarını değil,\n"
        "  arka plandaki yeşil çimen piksellerini ezberledi!\n\n"
        "ÇÖZÜM:\n"
        "1. Arka planı farklılaştır (Evde, betonda kedi).\n"
        "2. Veri artırma (Renk & parlaklık değişimi).\n"
        "3. Segmentasyon ile nesneyi arka plandan ayır."
    )
    ax2.text(0.5, 0.5, msg, ha='center', va='center', fontsize=9, color='#7F1D1D', linespacing=1.4)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Background bias diagram saved to: {output_path}')

if __name__ == '__main__':
    draw_audio_spectrogram('Derin_Ogrenme/assets/audio_spectrogram_2d_cnn.png')
    draw_background_bias('Derin_Ogrenme/assets/background_bias_cat_frog.png')
