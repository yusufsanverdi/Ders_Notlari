import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('Yapay_Zekaya_Giris/assets', exist_ok=True)

def generate_gradient_descent():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4.8), dpi=300)
    
    w = np.linspace(-1, 7, 200)
    loss = (w - 3)**2

    # 1. Aşırı Küçük Öğrenme Oranı (Çok Yavaş)
    ax1.plot(w, loss, color='#334155', lw=2)
    w_curr = 0.2
    pts = [w_curr]
    for _ in range(7):
        w_curr = w_curr - 0.04 * 2 * (w_curr - 3)
        pts.append(w_curr)
    pts = np.array(pts)
    ax1.plot(pts, (pts - 3)**2, 'o--', color='#F59E0B', lw=1.5, markersize=5, label=r'Adimlar ($\eta = 0.04$)')
    ax1.set_title(r"A. Asiri Kucuk $\eta$ (Yavas Yakinssama)", fontsize=11, fontweight='bold', color='#B45309')
    ax1.set_xlabel('Agirlik (w)')
    ax1.set_ylabel('Kayip L(w)')
    ax1.grid(True, linestyle=':', alpha=0.5)
    ax1.legend(loc='upper center', fontsize=8.5)
    ax1.text(3, -2, 'Binlerce adim gerektirir,\nyerel minimumda takilabilir', ha='center', fontsize=8, color='#78350F')

    # 2. Optimum Öğrenme Oranı (Kararlı ve Hızlı)
    ax2.plot(w, loss, color='#334155', lw=2)
    w_curr = 0.2
    pts = [w_curr]
    for _ in range(5):
        w_curr = w_curr - 0.25 * 2 * (w_curr - 3)
        pts.append(w_curr)
    pts = np.array(pts)
    ax2.plot(pts, (pts - 3)**2, 'o--', color='#10B981', lw=1.8, markersize=6, label=r'Optimum ($\eta = 0.25$)')
    ax2.set_title(r"B. Optimum $\eta$ (Kararli ve Hizli)", fontsize=11, fontweight='bold', color='#047857')
    ax2.set_xlabel('Agirlik (w)')
    ax2.grid(True, linestyle=':', alpha=0.5)
    ax2.legend(loc='upper center', fontsize=8.5)
    ax2.text(3, -2, 'Kisa surede ideal minimum\nnoktasina ($w^*=3$) ulasir', ha='center', fontsize=8, color='#065F46')

    # 3. Aşırı Büyük Öğrenme Oranı (Iraksama / Patlama)
    ax3.plot(w, loss, color='#334155', lw=2)
    pts = [0.2, 5.8, -1.2, 7.5]
    pts = np.array(pts)
    ax3.plot(pts, (pts - 3)**2, 'o--', color='#EF4444', lw=1.5, markersize=5, label=r'Iraksama ($\eta = 1.05$)')
    ax3.set_title(r"C. Asiri Buyuk $\eta$ (Iraksama / Salinim)", fontsize=11, fontweight='bold', color='#B91C1C')
    ax3.set_xlabel('Agirlik (w)')
    ax3.grid(True, linestyle=':', alpha=0.5)
    ax3.legend(loc='upper center', fontsize=8.5)
    ax3.text(3, -2, 'Minimumun uzerinden atlar,\nkayip sonsuza dogru patlar', ha='center', fontsize=8, color='#7F1D1D')

    for ax in [ax1, ax2, ax3]:
        ax.set_ylim(-4, 25)

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/gradient_descent_learning_rate.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

def generate_perceptron_and_xor():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    
    # --- Sol Panel: AND / OR Problemi (Doğrusal Ayrılabilir - Perceptron) ---
    ax1.set_xlim(-0.5, 1.5)
    ax1.set_ylim(-0.5, 1.5)
    ax1.set_title("A. Dogrusal Ayrilabilir: AND Problemi (Tek Noron)", fontsize=11, fontweight='bold', color='#1E293B')
    
    # Noktalar: AND (0,0)=0, (0,1)=0, (1,0)=0, (1,1)=1
    ax1.scatter([0, 0, 1], [0, 1, 0], color='#EF4444', s=120, edgecolors='black', lw=1.5, zorder=5, label='Sinif 0 (Cikti: 0)')
    ax1.scatter([1], [1], color='#10B981', s=150, marker='^', edgecolors='black', lw=1.5, zorder=5, label='Sinif 1 (Cikti: 1)')
    
    # Karar Sınırı: w1*x1 + w2*x2 + b = 0 -> x1 + x2 - 1.5 = 0 -> x2 = 1.5 - x1
    x_line = np.linspace(-0.2, 1.4, 100)
    ax1.plot(x_line, 1.5 - x_line, color='#2563EB', lw=2.2, linestyle='--', label=r'Karar Siniri ($x_1 + x_2 - 1.5 = 0$)')
    ax1.fill_between(x_line, 1.5 - x_line, 2.0, color='#10B981', alpha=0.1)
    ax1.fill_between(x_line, -1.0, 1.5 - x_line, color='#EF4444', alpha=0.1)

    ax1.set_xlabel('Girdi $x_1$')
    ax1.set_ylabel('Girdi $x_2$')
    ax1.legend(loc='lower left', fontsize=8.5)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.text(0.5, -0.4, "Tek bir Perceptron tek bir dogru cizerek\nAND ve OR problemlerini basariyla ayirir.", 
             ha='center', fontsize=8.5, color='#1E40AF', bbox=dict(boxstyle='round,pad=0.3', facecolor='#EFF6FF', edgecolor='#93C5FD'))

    # --- Sağ Panel: XOR Problemi (Doğrusal Ayrılamaz - Gizli Katman / MLP Şart) ---
    ax2.set_xlim(-0.5, 1.5)
    ax2.set_ylim(-0.5, 1.5)
    ax2.set_title("B. Dogrusal Ayrilamaz: XOR Problemi (MLP / Gizli Katman)", fontsize=11, fontweight='bold', color='#991B1B')
    
    # Noktalar: XOR (0,0)=0, (1,1)=0, (0,1)=1, (1,0)=1
    ax2.scatter([0, 1], [0, 1], color='#EF4444', s=120, edgecolors='black', lw=1.5, zorder=5, label='Sinif 0 (Cikti: 0)')
    ax2.scatter([0, 1], [1, 0], color='#10B981', s=150, marker='^', edgecolors='black', lw=1.5, zorder=5, label='Sinif 1 (Cikti: 1)')

    # 2 Karar Doğrusu (Gizli katmandaki 2 nöron)
    ax2.plot(x_line, 0.5 - x_line, color='#7C3AED', lw=1.8, linestyle=':', label='Gizli Noron 1 Siniri')
    ax2.plot(x_line, 1.5 - x_line, color='#D97706', lw=1.8, linestyle=':', label='Gizli Noron 2 Siniri')

    ax2.set_xlabel('Girdi $x_1$')
    ax2.set_ylabel('Girdi $x_2$')
    ax2.legend(loc='lower left', fontsize=8.5)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.text(0.5, -0.4, "XOR tek bir dogru ile asla ayrilamaz!\nCozum: En az 1 gizli katman ve dogrusal olmayan\naktivasyon (ReLU/Sigmoid) kullanmaktir (MLP).", 
             ha='center', fontsize=8.5, color='#991B1B', bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF2F2', edgecolor='#FCA5A5'))

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/perceptron_xor_mlp_decision_boundary.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

if __name__ == '__main__':
    generate_gradient_descent()
    generate_perceptron_and_xor()
