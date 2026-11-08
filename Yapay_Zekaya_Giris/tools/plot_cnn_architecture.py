import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('Yapay_Zekaya_Giris/assets', exist_ok=True)

def generate_cnn_architecture():
    fig, ax = plt.subplots(figsize=(15, 6), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.set_title("Evrisimli Sinir Agi (CNN) Ucuca Mimari Akisi ve Katman Donusumleri (LeNet-5 Standarti)", 
                 fontsize=13, fontweight='bold', pad=15, color='#1E293B')

    # 1. Girdi Görüntüsü
    rect_in = patches.Rectangle((0.6, 2.5), 1.6, 3.0, facecolor='#E2E8F0', edgecolor='#475569', lw=1.5)
    ax.add_patch(rect_in)
    ax.text(1.4, 4.0, "Girdi\nGorseli\n32x32\n(1 veya 3 kanal)", ha='center', va='center', fontsize=8, fontweight='bold', color='#1E293B')

    # Ok 1
    ax.annotate('', xy=(2.6, 4.0), xytext=(2.2, 4.0),
                arrowprops=dict(facecolor='#2563EB', edgecolor='#2563EB', width=1.5, headwidth=5))
    ax.text(2.4, 4.5, "Conv 5x5\n(6 filtre)", ha='center', fontsize=7, color='#2563EB', fontweight='bold')

    # 2. Conv Katmanı 1 (Feature Maps)
    for i in range(4):
        rect_c1 = patches.Rectangle((2.7 + i*0.15, 2.7 - i*0.15), 1.4, 2.6, facecolor='#DBEAFE', edgecolor='#2563EB', lw=1.2)
        ax.add_patch(rect_c1)
    ax.text(3.6, 3.8, "C1 Haritalari\n28x28\n(6 kanal)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1E40AF')

    # Ok 2
    ax.annotate('', xy=(4.8, 3.8), xytext=(4.4, 3.8),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.5, headwidth=5))
    ax.text(4.6, 4.3, "Havuzlama\n(2x2, S=2)", ha='center', fontsize=7, color='#059669', fontweight='bold')

    # 3. Pooling Katmanı 1 (S2)
    for i in range(4):
        rect_s1 = patches.Rectangle((4.9 + i*0.12, 3.0 - i*0.12), 1.1, 1.8, facecolor='#DCFCE7', edgecolor='#059669', lw=1.2)
        ax.add_patch(rect_s1)
    ax.text(5.6, 3.7, "S2 Havuz\n14x14\n(6 kanal)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#065F46')

    # Ok 3
    ax.annotate('', xy=(6.7, 3.7), xytext=(6.3, 3.7),
                arrowprops=dict(facecolor='#D97706', edgecolor='#D97706', width=1.5, headwidth=5))
    ax.text(6.5, 4.2, "Conv 5x5\n(16 filtre)", ha='center', fontsize=7, color='#D97706', fontweight='bold')

    # 4. Conv Katmanı 2 (C3)
    for i in range(5):
        rect_c2 = patches.Rectangle((6.8 + i*0.12, 3.2 - i*0.12), 1.0, 1.4, facecolor='#FEF3C7', edgecolor='#D97706', lw=1.2)
        ax.add_patch(rect_c2)
    ax.text(7.4, 3.7, "C3 Haritalari\n10x10\n(16 kanal)", ha='center', va='center', fontsize=7, fontweight='bold', color='#92400E')

    # Ok 4
    ax.annotate('', xy=(8.5, 3.7), xytext=(8.1, 3.7),
                arrowprops=dict(facecolor='#7C3AED', edgecolor='#7C3AED', width=1.5, headwidth=5))
    ax.text(8.3, 4.2, "Havuzlama\n(2x2, S=2)", ha='center', fontsize=7, color='#7C3AED', fontweight='bold')

    # 5. Pooling Katmanı 2 (S4)
    for i in range(5):
        rect_s2 = patches.Rectangle((8.6 + i*0.1, 3.4 - i*0.1), 0.7, 0.9, facecolor='#EDE9FE', edgecolor='#7C3AED', lw=1.2)
        ax.add_patch(rect_s2)
    ax.text(9.05, 3.7, "S4 Havuz\n5x5 (16)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#5B21B6')

    # Ok 5
    ax.annotate('', xy=(10.0, 3.7), xytext=(9.6, 3.7),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.5, headwidth=5))
    ax.text(9.8, 4.2, "Flatten\n(Duzlestir)", ha='center', fontsize=7, color='#DC2626', fontweight='bold')

    # 6. Flatten Vektörü (400 eleman)
    rect_flat = patches.Rectangle((10.1, 2.0), 0.35, 4.0, facecolor='#FEE2E2', edgecolor='#DC2626', lw=1.5)
    ax.add_patch(rect_flat)
    ax.text(10.27, 4.0, "F\nL\nA\nT\nT\nE\nN", ha='center', va='center', fontsize=6.5, fontweight='bold', color='#991B1B')
    ax.text(10.27, 1.6, "1D Vektor\n(400 eleman:\n5x5x16)", ha='center', fontsize=7, color='#7F1D1D')

    # Ok 6
    ax.annotate('', xy=(11.3, 4.0), xytext=(10.6, 4.0),
                arrowprops=dict(facecolor='#475569', edgecolor='#475569', width=1.5, headwidth=5))

    # 7. Dense (Tam Bağlantılı) Katmanlar
    rect_fc1 = patches.Rectangle((11.4, 2.4), 0.5, 3.2, facecolor='#F1F5F9', edgecolor='#64748B', lw=1.2)
    ax.add_patch(rect_fc1)
    ax.text(11.65, 4.0, "FC 1\n(120)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#334155')

    ax.annotate('', xy=(12.4, 4.0), xytext=(12.0, 4.0),
                arrowprops=dict(facecolor='#475569', edgecolor='#475569', width=1.5, headwidth=5))

    rect_fc2 = patches.Rectangle((12.5, 2.8), 0.5, 2.4, facecolor='#F1F5F9', edgecolor='#64748B', lw=1.2)
    ax.add_patch(rect_fc2)
    ax.text(12.75, 4.0, "FC 2\n(84)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#334155')

    ax.annotate('', xy=(13.5, 4.0), xytext=(13.1, 4.0),
                arrowprops=dict(facecolor='#16A34A', edgecolor='#16A34A', width=1.5, headwidth=5))

    # 8. Softmax Çıkış Katmanı (10 Sınıf)
    rect_out = patches.Rectangle((13.6, 3.2), 1.6, 1.8, facecolor='#DCFCE7', edgecolor='#16A34A', lw=2.0)
    ax.add_patch(rect_out)
    ax.text(14.4, 4.3, "Cikis: Softmax", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#166534')
    ax.text(14.4, 3.6, "10 Sinif Olasiligi\nToplam = 1.0", ha='center', va='center', fontsize=7.5, color='#14532D')

    # Alt Bilgilendirme Kutusu: Mimari Soru Bankası Hatırlatması
    info_text = (
        "DERSTE VE QUIZLERDE SORULAN MATRIS / BOYUT HESAPLAMA STANDARTI:\n"
        "Quiz Sorusu: 64x64 RGB girdi -> Conv2D (16 filtre, 3x3, Same Padding, S=1) -> 64x64x16\n"
        "-> MaxPool2D (2x2, S=2) -> 32x32x16 -> Flatten Sonrasi Eleman Sayisi: 32 x 32 x 16 = 16384 (veya 16x16x32 = 8192)\n"
        "Hayati Kural: Conv ve Pooling katmanlari OZNITELIK CIKARIR; Flatten ve FC katmanlari SINIFLANDIRMAYI yapar!"
    )
    ax.text(8.0, 0.7, info_text, ha='center', fontsize=8, color='#1E40AF',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#EFF6FF', edgecolor='#93C5FD', lw=1.2))

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/cnn_full_architecture_lenet5.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

if __name__ == '__main__':
    generate_cnn_architecture()
