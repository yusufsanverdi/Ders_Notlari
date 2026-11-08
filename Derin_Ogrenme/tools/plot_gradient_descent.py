import matplotlib.pyplot as plt
import numpy as np

def plot_learning_rates(output_path):
    x = np.linspace(-4, 4, 200)
    y = x**2  # Simple quadratic bowl

    fig, axes = plt.subplots(1, 3, figsize=(13, 4), dpi=300)
    
    # 1. Learning Rate Too Small
    ax = axes[0]
    ax.plot(x, y, color='#374151', lw=2)
    # small steps
    steps_x = [3.5]
    for _ in range(7):
        steps_x.append(steps_x[-1] - 0.15 * steps_x[-1])
    steps_y = [val**2 for val in steps_x]
    ax.plot(steps_x, steps_y, 'o-', color='#2563EB', lw=1.5, markersize=5)
    ax.set_title(r'Öğrenme Oranı Çok Küçük ($\alpha \ll 1$)' + '\nÇok yavaş öğrenir, takılır', fontsize=10, fontweight='bold', color='#1E40AF')
    ax.set_xlabel('Parametre (Ağırlık W)')
    ax.set_ylabel('Kayıp (Loss)')
    ax.grid(True, alpha=0.3)

    # 2. Optimal Learning Rate
    ax = axes[1]
    ax.plot(x, y, color='#374151', lw=2)
    steps_x = [3.5]
    for _ in range(5):
        steps_x.append(steps_x[-1] - 0.45 * steps_x[-1])
    steps_y = [val**2 for val in steps_x]
    ax.plot(steps_x, steps_y, 'o-', color='#059669', lw=1.8, markersize=6)
    ax.set_title(r'Optimal Öğrenme Oranı ($\alpha$ Dengeli)' + '\nHızlı ve kararlı yakınsar', fontsize=10, fontweight='bold', color='#065F46')
    ax.set_xlabel('Parametre (Ağırlık W)')
    ax.grid(True, alpha=0.3)

    # 3. Learning Rate Too Large
    ax = axes[2]
    ax.plot(x, y, color='#374151', lw=2)
    steps_x = [1.2, -1.9, 2.7, -3.8]
    steps_y = [val**2 for val in steps_x]
    ax.plot(steps_x, steps_y, 'o--', color='#DC2626', lw=1.8, markersize=6)
    ax.set_title(r'Öğrenme Oranı Çok Büyük ($\alpha \gg 1$)' + '\nSıçrar, ıraksar (Divergence)', fontsize=10, fontweight='bold', color='#991B1B')
    ax.set_xlabel('Parametre (Ağırlık W)')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Learning rates plot saved to: {output_path}')

if __name__ == '__main__':
    plot_learning_rates('Derin_Ogrenme/assets/learning_rate_comparison.png')
