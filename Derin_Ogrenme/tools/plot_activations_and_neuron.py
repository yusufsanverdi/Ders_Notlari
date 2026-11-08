import matplotlib.pyplot as plt
import numpy as np

def plot_activation_functions(output_path):
    z = np.linspace(-5, 5, 500)
    
    # Activations
    sigmoid = 1 / (1 + np.exp(-z))
    tanh = np.tanh(z)
    relu = np.maximum(0, z)
    leaky_relu = np.where(z >= 0, z, 0.1 * z)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=300)
    
    # 1. Sigmoid
    ax = axes[0, 0]
    ax.plot(z, sigmoid, color='#2563EB', lw=2.5, label=r'$\sigma(z) = \frac{1}{1 + e^{-z}}$')
    ax.axhline(0, color='gray', lw=0.8, ls='--')
    ax.axhline(1, color='gray', lw=0.8, ls='--')
    ax.axvline(0, color='gray', lw=0.8, ls='--')
    ax.set_title('Sigmoid Fonksiyonu', fontsize=12, fontweight='bold', color='#1E40AF')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_xlabel('z')
    ax.set_ylabel(r'$\sigma(z)$')

    # 2. Tanh
    ax = axes[0, 1]
    ax.plot(z, tanh, color='#059669', lw=2.5, label=r'$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$')
    ax.axhline(0, color='gray', lw=0.8, ls='--')
    ax.axhline(1, color='gray', lw=0.8, ls='--')
    ax.axhline(-1, color='gray', lw=0.8, ls='--')
    ax.axvline(0, color='gray', lw=0.8, ls='--')
    ax.set_title('Tanh (Hiperbolik Tanjant)', fontsize=12, fontweight='bold', color='#065F46')
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_xlabel('z')
    ax.set_ylabel(r'$\tanh(z)$')

    # 3. ReLU
    ax = axes[1, 0]
    ax.plot(z, relu, color='#DC2626', lw=2.5, label=r'$\mathrm{ReLU}(z) = \max(0, z)$')
    ax.axhline(0, color='gray', lw=0.8, ls='--')
    ax.axvline(0, color='gray', lw=0.8, ls='--')
    ax.set_title('ReLU (Rectified Linear Unit)', fontsize=12, fontweight='bold', color='#991B1B')
    ax.set_ylim(-0.5, 5.2)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_xlabel('z')
    ax.set_ylabel(r'$f(z)$')

    # 4. Leaky ReLU
    ax = axes[1, 1]
    ax.plot(z, leaky_relu, color='#7C3AED', lw=2.5, label=r'$\mathrm{LeakyReLU}(z) = \max(\alpha z, z)$')
    ax.axhline(0, color='gray', lw=0.8, ls='--')
    ax.axvline(0, color='gray', lw=0.8, ls='--')
    ax.set_title(r'Leaky ReLU ($\alpha = 0.1$)', fontsize=12, fontweight='bold', color='#5B21B6')
    ax.set_ylim(-1.0, 5.2)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_xlabel('z')
    ax.set_ylabel(r'$f(z)$')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Activation functions plot saved to: {output_path}')

def draw_single_neuron(output_path):
    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    # Inputs
    inputs = ['$x_1$', '$x_2$', '$x_3$', '$x_n$']
    weights = ['$w_1$', '$w_2$', '$w_3$', '$w_n$']
    y_pos = [5.0, 3.8, 2.6, 1.2]

    # Draw inputs & weights
    for i in range(4):
        # input circle
        c = plt.Circle((1.5, y_pos[i]), 0.4, color='#EFF6FF', ec='#2563EB', lw=2)
        ax.add_patch(c)
        ax.text(1.5, y_pos[i], inputs[i], ha='center', va='center', fontsize=12, fontweight='bold', color='#1E40AF')
        
        # arrow to sum
        ax.annotate('', xy=(4.6, 3.2), xytext=(1.9, y_pos[i]),
                    arrowprops=dict(arrowstyle="->", color='#4B5563', lw=1.8))
        # weight text
        mid_x = 1.9 + (4.6 - 1.9)*0.45
        mid_y = y_pos[i] + (3.2 - y_pos[i])*0.45
        ax.text(mid_x, mid_y + 0.18, weights[i], fontsize=11, color='#DC2626', fontweight='bold')

    # Bias
    c_b = plt.Circle((4.8, 5.2), 0.35, color='#FEF3C7', ec='#D97706', lw=2)
    ax.add_patch(c_b)
    ax.text(4.8, 5.2, '$b$ (Bias)', ha='center', va='center', fontsize=10, fontweight='bold', color='#B45309')
    ax.annotate('', xy=(5.0, 3.7), xytext=(4.8, 4.85),
                arrowprops=dict(arrowstyle="->", color='#D97706', lw=1.8))

    # Summation circle
    c_sum = plt.Circle((5.0, 3.2), 0.65, color='#F3F4F6', ec='#374151', lw=2)
    ax.add_patch(c_sum)
    ax.text(5.0, 3.2, r'$\sum + b$', ha='center', va='center', fontsize=13, fontweight='bold')
    ax.text(5.0, 2.2, r'$Z = W \cdot X + b$', ha='center', va='center', fontsize=10, color='#1F2937')

    # Arrow from sum to activation
    ax.annotate('', xy=(6.8, 3.2), xytext=(5.65, 3.2),
                arrowprops=dict(arrowstyle="->", color='#4B5563', lw=2))

    # Activation circle
    c_act = plt.Circle((7.4, 3.2), 0.6, color='#ECFDF5', ec='#059669', lw=2)
    ax.add_patch(c_act)
    ax.text(7.4, 3.2, r'$f(Z)$', ha='center', va='center', fontsize=13, fontweight='bold', color='#065F46')
    ax.text(7.4, 2.2, 'Aktivasyon\n(Sigmoid, ReLU)', ha='center', va='center', fontsize=8.5, color='#047857')

    # Output arrow
    ax.annotate('', xy=(9.2, 3.2), xytext=(8.0, 3.2),
                arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.5))
    ax.text(9.5, 3.2, r'$\hat{y}$ (Çıktı)', ha='center', va='center', fontsize=12, fontweight='bold', color='#1E40AF')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'Single neuron diagram saved to: {output_path}')

if __name__ == '__main__':
    plot_activation_functions('Derin_Ogrenme/assets/activation_functions.png')
    draw_single_neuron('Derin_Ogrenme/assets/single_neuron_math.png')
