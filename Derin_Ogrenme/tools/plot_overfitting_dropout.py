import matplotlib.pyplot as plt
import numpy as np

def plot_overfitting_curves(output_path):
    epochs = np.arange(1, 41)
    
    # Synthetic curves
    train_loss = 2.5 * np.exp(-0.12 * epochs) + 0.1
    # Val loss drops until epoch 15, then starts rising (overfitting)
    val_loss = 2.5 * np.exp(-0.12 * epochs) + 0.1 + 0.0015 * np.maximum(0, epochs - 14)**2

    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    ax.plot(epochs, train_loss, 'b-', lw=2.5, label='Eğitim Kaybı (Train Loss)')
    ax.plot(epochs, val_loss, 'r--', lw=2.5, label='Doğrulama Kaybı (Val Loss)')
    
    # Optimal point
    ax.axvline(14, color='green', ls=':', lw=2, label='Optimal Nokta (Erken Durdurma)')
    
    # Regions
    ax.axvspan(1, 14, color='green', alpha=0.08)
    ax.axvspan(14, 40, color='red', alpha=0.08)
    
    ax.text(7, 2.0, 'İyi Öğrenme Bölgesi\n(Genelleme)', ha='center', fontsize=10, fontweight='bold', color='#065F46')
    ax.text(27, 1.8, 'AŞIRI ÖĞRENME\n(Overfitting / Ezberleme)', ha='center', fontsize=11, fontweight='bold', color='#991B1B')
    
    ax.set_title('Aşırı Öğrenme (Overfitting) Belirtisi ve Erken Durdurma', fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel('Epoch Sayısı', fontsize=10)
    ax.set_ylabel('Kayıp Değeri (Loss)', fontsize=10)
    ax.legend(fontsize=10, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 2.7)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Overfitting curves saved to: {output_path}')

def draw_dropout_mechanism(output_path):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
    
    # Standard Network
    ax = axes[0]
    ax.axis('off')
    ax.set_title('Standart Katman\n(Tüm Nöronlar Aktif)', fontsize=11, fontweight='bold', color='#1E40AF')
    for y in [1, 2, 3, 4]:
        c1 = plt.Circle((0.2, y), 0.25, color='#DBEAFE', ec='#2563EB', lw=2)
        ax.add_patch(c1)
        for y2 in [1, 2, 3, 4]:
            ax.plot([0.45, 0.75], [y, y2], color='#9CA3AF', lw=1)
        c2 = plt.Circle((1.0, y), 0.25, color='#DBEAFE', ec='#2563EB', lw=2)
        ax.add_patch(c2)
    ax.set_xlim(-0.1, 1.3)
    ax.set_ylim(0.5, 4.5)

    # Dropout Network
    ax = axes[1]
    ax.axis('off')
    ax.set_title('Dropout Uygulanmış Katman\n(Rastgele Kapatılan Nöronlar - p=0.5)', fontsize=11, fontweight='bold', color='#991B1B')
    inactive_left = [2]
    inactive_right = [1, 4]
    
    for y in [1, 2, 3, 4]:
        if y in inactive_left:
            c1 = plt.Circle((0.2, y), 0.25, color='#FEE2E2', ec='#DC2626', lw=2, ls='--')
            ax.add_patch(c1)
            ax.text(0.2, y, 'X', color='#DC2626', fontweight='bold', ha='center', va='center', fontsize=12)
        else:
            c1 = plt.Circle((0.2, y), 0.25, color='#DBEAFE', ec='#2563EB', lw=2)
            ax.add_patch(c1)
            
        for y2 in [1, 2, 3, 4]:
            if y not in inactive_left and y2 not in inactive_right:
                ax.plot([0.45, 0.75], [y, y2], color='#4B5563', lw=1.5)
                
        if y in inactive_right:
            c2 = plt.Circle((1.0, y), 0.25, color='#FEE2E2', ec='#DC2626', lw=2, ls='--')
            ax.add_patch(c2)
            ax.text(1.0, y, 'X', color='#DC2626', fontweight='bold', ha='center', va='center', fontsize=12)
        else:
            c2 = plt.Circle((1.0, y), 0.25, color='#DBEAFE', ec='#2563EB', lw=2)
            ax.add_patch(c2)

    ax.set_xlim(-0.1, 1.3)
    ax.set_ylim(0.5, 4.5)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Dropout mechanism saved to: {output_path}')

if __name__ == '__main__':
    plot_overfitting_curves('Derin_Ogrenme/assets/overfitting_curve.png')
    draw_dropout_mechanism('Derin_Ogrenme/assets/dropout_mechanism.png')
