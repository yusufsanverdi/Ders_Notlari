import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_iou_diagram(output_path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)
    
    # 1. Overlapping Boxes
    ax = axes[0]
    ax.axis('off')
    ax.set_title('Gerçek Kutu (Ground Truth) vs Tahmin Kutusu (Prediction)', fontsize=10.5, fontweight='bold', color='#1E40AF')
    
    # Ground Truth Box (Green)
    gt = plt.Rectangle((0.15, 0.25), 0.5, 0.5, fc='#DCFCE7', ec='#10B981', lw=2.5, alpha=0.6)
    ax.add_patch(gt)
    ax.text(0.18, 0.78, 'Ground Truth (A)', fontsize=10, fontweight='bold', color='#047857')

    # Prediction Box (Blue)
    pred = plt.Rectangle((0.35, 0.35), 0.5, 0.5, fc='#DBEAFE', ec='#2563EB', lw=2.5, alpha=0.6)
    ax.add_patch(pred)
    ax.text(0.55, 0.88, 'Prediction (B)', fontsize=10, fontweight='bold', color='#1D4ED8')

    # Intersection (Darker fill)
    intersect = plt.Rectangle((0.35, 0.35), 0.3, 0.4, fc='#FCD34D', ec='#D97706', lw=1.5, alpha=0.8)
    ax.add_patch(intersect)
    ax.text(0.5, 0.55, 'Kesişim\n(A ∩ B)', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#92400E')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 2. IoU Mathematical Formula Box
    ax2 = axes[1]
    ax2.axis('off')
    ax2.set_title('IoU (Kesişim / Birleşim Oranı) Formülü', fontsize=11, fontweight='bold', color='#991B1B')

    # Formula text and illustration
    formula_box = patches.FancyBboxPatch((0.05, 0.1), 0.9, 0.8, boxstyle="round,pad=0.08",
                                         fc='#FEF2F2', ec='#EF4444', lw=2)
    ax2.add_patch(formula_box)

    formula_str = (
        r"$\mathbf{IoU = \frac{Kesisim\ Alani}{Birlesim\ Alani} = \frac{Area(A \cap B)}{Area(A \cup B)}}$" + "\n\n"
        r"$Birlesim\ Alani = Area(A) + Area(B) - Area(A \cap B)$" + "\n\n"
        r"• $\mathrm{IoU} \geq 0.50 \rightarrow \mathbf{True\ Positive\ (TP)}$" + "\n"
        r"• $\mathrm{IoU} < 0.50 \rightarrow \mathbf{False\ Positive\ (FP)}$" + "\n"
        r"• Deger Araligi: $[0.0, 1.0]$"
    )
    ax2.text(0.5, 0.5, formula_str, ha='center', va='center', fontsize=11, color='#7F1D1D', linespacing=1.6)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'IoU diagram saved to: {output_path}')

def draw_precision_recall_curve(output_path):
    fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
    
    # Synthetic PR curve
    recall = np.linspace(0, 1, 200)
    precision = 1.0 - 0.7 * (recall**2.2) + 0.05 * np.sin(recall * 10)
    precision = np.clip(precision, 0, 1)
    # Monotonic decreasing smoothing (VOC standard)
    precision_smooth = np.maximum.accumulate(precision[::-1])[::-1]

    ax.plot(recall, precision_smooth, color='#2563EB', lw=2.5, label='Precision-Recall Eğrisi')
    ax.fill_between(recall, precision_smooth, color='#DBEAFE', alpha=0.5, label='AP: Eğri Altındaki Alan (AUC)')

    ax.set_title('Precision-Recall Eğrisi ve Ortalama Kesinlik (AP)', fontsize=11, fontweight='bold', pad=12)
    ax.set_xlabel('Duyarlılık (Recall)', fontsize=10, fontweight='bold')
    ax.set_ylabel('Kesinlik (Precision)', fontsize=10, fontweight='bold')
    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9.5, loc='lower left')

    # Annotate Trade-off
    ax.annotate('Yüksek Eşik: Az Tespit,\nYüksek Precision, Düşük Recall',
                xy=(0.15, 0.98), xytext=(0.25, 0.85),
                arrowprops=dict(arrowstyle="->", color='#DC2626', lw=1.5),
                fontsize=8.5, color='#991B1B')
    ax.annotate('Düşük Eşik: Çok Tespit,\nDüşük Precision, Yüksek Recall',
                xy=(0.92, 0.35), xytext=(0.6, 0.5),
                arrowprops=dict(arrowstyle="->", color='#059669', lw=1.5),
                fontsize=8.5, color='#065F46')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'PR curve saved to: {output_path}')

if __name__ == '__main__':
    draw_iou_diagram('Derin_Ogrenme/assets/iou_mathematical_diagram.png')
    draw_precision_recall_curve('Derin_Ogrenme/assets/precision_recall_map_curve.png')
