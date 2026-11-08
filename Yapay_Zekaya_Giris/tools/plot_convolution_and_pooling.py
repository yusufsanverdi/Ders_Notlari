import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('Yapay_Zekaya_Giris/assets', exist_ok=True)

def generate_convolution_step_by_step():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.2), dpi=300)
    
    # --- Sol Panel: 2D Evrişim Hesaplama Mantığı ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title("A. 2D Evrisim (Convolution) Islemi ve Matris Carpimi", fontsize=11.5, fontweight='bold', color='#1E293B', pad=12)

    # Girdi Matrisi (5x5) Temsili
    input_mat = np.array([
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0]
    ])

    # Kernel (3x3)
    kernel_mat = np.array([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ])

    # Çıktı Sol Üst Değeri:
    # 1*1 + 1*0 + 1*1 + 0*0 + 1*1 + 1*0 + 0*1 + 0*0 + 1*1 = 1 + 0 + 1 + 0 + 1 + 0 + 0 + 0 + 1 = 4!
    
    # Matris Görselleştirme Kutuları
    # 1. Girdi Matrisi Çizimi
    ax1.text(2.0, 8.8, "Girdi Matrisi (5x5)", ha='center', fontsize=9.5, fontweight='bold', color='#2563EB')
    for r in range(5):
        for c in range(5):
            val = input_mat[r, c]
            # Sol üst 3x3 bölgeyi vurgula
            is_active = (r < 3 and c < 3)
            bg = '#DBEAFE' if is_active else '#F1F5F9'
            border = '#2563EB' if is_active else '#94A3B8'
            lw = 1.8 if is_active else 0.8
            rect = patches.Rectangle((0.5 + c*0.6, 5.5 + (4-r)*0.6), 0.55, 0.55, facecolor=bg, edgecolor=border, lw=lw)
            ax1.add_patch(rect)
            ax1.text(0.5 + c*0.6 + 0.275, 5.5 + (4-r)*0.6 + 0.275, str(val), ha='center', va='center', fontsize=8.5,
                     fontweight='bold' if is_active else 'normal', color='#1E40AF' if is_active else '#475569')

    # 2. Kernel (Filtre) Çizimi
    ax1.text(5.5, 8.8, "Kernel (3x3)", ha='center', fontsize=9.5, fontweight='bold', color='#DC2626')
    ax1.text(4.2, 7.0, "*", ha='center', va='center', fontsize=22, fontweight='bold', color='#64748B')
    for r in range(3):
        for c in range(3):
            val = kernel_mat[r, c]
            rect = patches.Rectangle((4.6 + c*0.6, 6.1 + (2-r)*0.6), 0.55, 0.55, facecolor='#FEE2E2', edgecolor='#DC2626', lw=1.5)
            ax1.add_patch(rect)
            ax1.text(4.6 + c*0.6 + 0.275, 6.1 + (2-r)*0.6 + 0.275, str(val), ha='center', va='center', fontsize=8.5,
                     fontweight='bold', color='#991B1B')

    # 3. Çıktı (Öznitelik Haritası)
    ax1.text(8.3, 8.8, "Cikti (3x3)", ha='center', fontsize=9.5, fontweight='bold', color='#059669')
    ax1.text(6.9, 7.0, "=", ha='center', va='center', fontsize=20, fontweight='bold', color='#64748B')
    
    out_mat = np.array([
        [4, 3, 4],
        [2, 4, 3],
        [2, 3, 4]
    ])
    for r in range(3):
        for c in range(3):
            val = out_mat[r, c]
            is_active = (r == 0 and c == 0)
            bg = '#DCFCE7' if is_active else '#F8FAFC'
            border = '#16A34A' if is_active else '#CBD5E1'
            lw = 2.0 if is_active else 0.8
            rect = patches.Rectangle((7.3 + c*0.6, 6.1 + (2-r)*0.6), 0.55, 0.55, facecolor=bg, edgecolor=border, lw=lw)
            ax1.add_patch(rect)
            ax1.text(7.3 + c*0.6 + 0.275, 6.1 + (2-r)*0.6 + 0.275, str(val), ha='center', va='center', fontsize=9,
                     fontweight='bold' if is_active else 'normal', color='#166534' if is_active else '#475569')

    # Açıklama Kutusu
    calc_text = (
        "Adim Adim Sol Ust Eleman Hesabi (Noktasal Carpim ve Toplam):\n"
        "(1*1 + 1*0 + 1*1) + (0*0 + 1*1 + 1*0) + (0*1 + 0*0 + 1*1)\n"
        "= 1 + 0 + 1 + 0 + 1 + 0 + 0 + 0 + 1 = 4 (Oznitelik Degeri)"
    )
    ax1.text(5.0, 4.2, calc_text, ha='center', fontsize=8.2, color='#1E293B',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0FDF4', edgecolor='#86EFAC', lw=1.2))

    # Formül Kutusu
    formula_text = (
        "Temel Cikti Boyutu Formulu:\n"
        r"$\mathbf{W_{out}} = \left\lfloor \frac{W_{in} - K + 2P}{S} \right\rfloor + 1$" + "\n\n"
        "W_in: Girdi boyutu (5)  | K: Kernel boyutu (3)\n"
        "P: Dolgu / Padding (0)  | S: Adim / Stride (1)\n"
        r"W_out = (5 - 3 + 0)/1 + 1 = 3  (3x3 Matris)"
    )
    ax1.text(5.0, 1.8, formula_text, ha='center', fontsize=8.5, color='#1E40AF',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#EFF6FF', edgecolor='#93C5FD', lw=1.2))

    # --- Sağ Panel: Padding ve Stride Mantığı ---
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title("B. Dolgulama (Padding) ve Adim (Stride) Rolu", fontsize=11.5, fontweight='bold', color='#1E293B', pad=12)

    # 1. Zero-Padding (Same Padding) Şeması
    box_pad = patches.FancyBboxPatch((0.5, 5.2), 9.0, 4.3, boxstyle="round,pad=0.3", facecolor='#F8FAFC', edgecolor='#64748B', lw=1.2)
    ax2.add_patch(box_pad)
    ax2.text(5, 9.1, "1. DOLGULAMA (PADDING): Neden Kenarlara Sifir Eklenir?", ha='center', fontsize=9.5, fontweight='bold', color='#334155')

    ax2.text(5, 7.8, 
             "A. Bilgi Kaybini Onler: Kenar ve kose pikselleri filitreden az gecer.\n"
             "   Dolgulama yapilmazsa kose pikselleri modele ogretilemez.\n"
             "B. Boyut Erimisini Durdurur: Padding olmazsa (Valid Padding)\n"
             "   her katmanda matris kuculur ve derin aglarda goruntu 1x1'e erir!\n"
             "C. Same Padding ($P = (K-1)/2$): Cikti boyutu girdiyle ayni kalir ($W_{out} = W_{in}$).", 
             ha='center', fontsize=8.2, color='#1E293B')

    # 2. Stride (Adım) Şeması
    box_stride = patches.FancyBboxPatch((0.5, 0.4), 9.0, 4.3, boxstyle="round,pad=0.3", facecolor='#FFFBEB', edgecolor='#F59E0B', lw=1.2)
    ax2.add_patch(box_stride)
    ax2.text(5, 4.3, "2. ADIM (STRIDE - S): Filtrenin Kayma Miktari", ha='center', fontsize=9.5, fontweight='bold', color='#B45309')

    ax2.text(5, 2.7, 
             "S = 1: Filtre 1 piksel kayarak tum pikselleri detaylica tarar.\n"
             "S = 2: Filtre 2 piksel atlayarak kayar; cikti uzamsal boyutunu\n"
             "       yaklasik yariya indirir (Boyut indirgeme / Downsampling).\n"
             "S > 1 Durumu: Buyuk resimlerde hesaplama maliyetini azaltmak icin\n"
             "              ilk katmanlarda tercih edilir.", 
             ha='center', fontsize=8.2, color='#78350F')

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/convolution_stride_padding_matrix.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

def generate_pooling_and_flatten():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.2), dpi=300)
    
    # --- Sol Panel: Max vs Average Pooling ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title("A. Havuzlama (Pooling): Max Pooling vs Average Pooling", fontsize=11.5, fontweight='bold', color='#1E293B', pad=12)

    # 4x4 Matris
    mat_4x4 = np.array([
        [12, 20, 30,  0],
        [ 8, 12,  2,  4],
        [ 1,  5,  9, 15],
        [ 3,  7,  8,  4]
    ])

    # 4 bölgeyi renklendir:
    colors = [['#DBEAFE', '#FEE2E2'], ['#FEF3C7', '#DCFCE7']]
    borders = [['#2563EB', '#DC2626'], ['#D97706', '#16A34A']]

    ax1.text(2.6, 9.0, "Girdi Oznitelik Haritasi (4x4)", ha='center', fontsize=9, fontweight='bold', color='#334155')
    for r in range(4):
        for c in range(4):
            val = mat_4x4[r, c]
            br = r // 2
            bc = c // 2
            rect = patches.Rectangle((0.6 + c*0.9, 4.6 + (3-r)*0.9), 0.85, 0.85, 
                                     facecolor=colors[br][bc], edgecolor=borders[br][bc], lw=1.5)
            ax1.add_patch(rect)
            ax1.text(0.6 + c*0.9 + 0.425, 4.6 + (3-r)*0.9 + 0.425, str(val), 
                     ha='center', va='center', fontsize=10, fontweight='bold', color='#1E293B')

    # Max Pooling (2x2) Sonucu
    ax1.text(7.2, 9.0, "Max Pooling (2x2, S=2)", ha='center', fontsize=9, fontweight='bold', color='#1E40AF')
    max_res = np.array([[20, 30], [7, 15]])
    for r in range(2):
        for c in range(2):
            rect = patches.Rectangle((5.8 + c*1.1, 6.6 + (1-r)*1.1), 1.0, 1.0, 
                                     facecolor=colors[r][c], edgecolor=borders[r][c], lw=2.0)
            ax1.add_patch(rect)
            ax1.text(5.8 + c*1.1 + 0.5, 6.6 + (1-r)*1.1 + 0.5, str(max_res[r, c]), 
                     ha='center', va='center', fontsize=11, fontweight='bold', color='#1E40AF')

    # Average Pooling (2x2) Sonucu
    ax1.text(7.2, 5.8, "Average Pooling (2x2, S=2)", ha='center', fontsize=9, fontweight='bold', color='#047857')
    avg_res = np.array([[13.0, 9.0], [4.0, 9.0]])
    for r in range(2):
        for c in range(2):
            rect = patches.Rectangle((5.8 + c*1.1, 3.4 + (1-r)*1.1), 1.0, 1.0, 
                                     facecolor=colors[r][c], edgecolor=borders[r][c], lw=2.0)
            ax1.add_patch(rect)
            ax1.text(5.8 + c*1.1 + 0.5, 3.4 + (1-r)*1.1 + 0.5, f"{avg_res[r, c]:.0f}", 
                     ha='center', va='center', fontsize=11, fontweight='bold', color='#047857')

    ax1.text(5.0, 1.6, 
             "Max Pooling: Bolgedeki EN BASKIN ozelligi alir; nesne kenarlarini korur.\n"
             "Average Pooling: Bolgenin ORTALAMASINI alir; yumusak arka plan ozeti sunar.\n"
             "Hayati Not: Pooling katmaninin OGRENEBILIR PARAMETRESI YOKTUR (W ve b = 0)!", 
             ha='center', fontsize=8.2, color='#1E40AF',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#EFF6FF', edgecolor='#93C5FD'))

    # --- Sağ Panel: Flatten Katmanı ve Parametre Patlaması Uyarısı ---
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title("B. Duzlestirme (Flatten) ve Parametre Yonetimi", fontsize=11.5, fontweight='bold', color='#1E293B', pad=12)

    # 3D Tensor Temsili (2x2x2)
    ax2.text(2.2, 9.0, "3D Tensor (2x2x2)", ha='center', fontsize=9, fontweight='bold', color='#7C3AED')
    ax2.add_patch(patches.Rectangle((0.8, 6.2), 2.8, 2.4, facecolor='#EDE9FE', edgecolor='#7C3AED', lw=1.8))
    ax2.text(2.2, 7.4, "Kanal 1:\n[ [1, 2],\n  [3, 4] ]\n\nKanal 2:\n[ [5, 6],\n  [7, 8] ]", 
             ha='center', va='center', fontsize=7.5, color='#5B21B6')

    # Ok
    ax2.annotate('', xy=(4.6, 7.4), xytext=(3.8, 7.4),
                 arrowprops=dict(facecolor='#6D28D9', edgecolor='#6D28D9', width=2, headwidth=7))
    ax2.text(4.2, 7.8, "Flatten", ha='center', fontsize=8.5, fontweight='bold', color='#6D28D9')

    # 1D Vektör Temsili (8x1)
    ax2.text(5.5, 9.0, "1D Vektor (8 eleman)", ha='center', fontsize=9, fontweight='bold', color='#059669')
    vec_vals = [1, 2, 3, 4, 5, 6, 7, 8]
    for i, v in enumerate(vec_vals):
        rect = patches.Rectangle((5.2, 5.0 + (7-i)*0.45), 0.7, 0.4, facecolor='#DCFCE7', edgecolor='#16A34A', lw=1.2)
        ax2.add_patch(rect)
        ax2.text(5.55, 5.0 + (7-i)*0.45 + 0.2, str(v), ha='center', va='center', fontsize=8, fontweight='bold', color='#14532D')

    # Ok FC Katmanına
    ax2.annotate('', xy=(7.2, 6.5), xytext=(6.2, 6.5),
                 arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=2, headwidth=7))

    # Dense Katmanı
    ax2.add_patch(patches.FancyBboxPatch((7.4, 5.2), 2.2, 3.2, boxstyle="round,pad=0.2", facecolor='#FEE2E2', edgecolor='#DC2626', lw=1.5))
    ax2.text(8.5, 7.8, "Tam Bagli\n(Dense / FC)\nKatman", ha='center', fontsize=8.5, fontweight='bold', color='#991B1B')
    ax2.text(8.5, 6.2, "Ogrendigi tum\noznitelikleri\nbirlestirir ve\nsiniflandirir.", ha='center', fontsize=7.2, color='#7F1D1D')

    # Hocanın Sınav Uyarısı Kutusu
    alert_text = (
        "HOCANIN KESIN SINAV UYARISI:\n"
        "Soru: 'Bir CNN modelinden Pooling katmanini kaldirirsak ne olur?'\n"
        "Cevap: Boyut indirgeme yapilamayacagi icin Flatten sonrasi vektor\n"
        "boyutu ve baglanti agirliklari DEVASE boyutta artar (Parametre patlamasi).\n"
        "Bellek tukenir, GPU kitlenir ve model asiri ezberlemeye (Overfitting) duser!"
    )
    ax2.text(5.0, 2.0, alert_text, ha='center', fontsize=8.2, color='#991B1B',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEF2F2', edgecolor='#EF4444', lw=1.5))

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/pooling_max_vs_average_flatten.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

if __name__ == '__main__':
    generate_convolution_step_by_step()
    generate_pooling_and_flatten()
