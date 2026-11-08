import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_cv_tasks(output_path):
    fig, axes = plt.subplots(1, 3, figsize=(13, 4), dpi=300)
    
    # Task 1: Classification
    ax = axes[0]
    ax.axis('off')
    ax.set_title('1. Sınıflandırma (Classification)\n"Resimde Ne Var?"', fontsize=10.5, fontweight='bold', color='#1E40AF')
    rect = plt.Rectangle((0.1, 0.1), 0.8, 0.8, fc='#EFF6FF', ec='#3B82F6', lw=2)
    ax.add_patch(rect)
    c = plt.Circle((0.5, 0.5), 0.25, color='#F87171', ec='#DC2626', lw=2)
    ax.add_patch(c)
    ax.text(0.5, 0.5, 'Araba', ha='center', va='center', fontweight='bold', fontsize=11, color='white')
    ax.text(0.5, 0.15, 'Çıktı: "Araba" (Tek Etiket)', ha='center', fontsize=9.5, fontweight='bold', color='#1E40AF')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Task 2: Localization
    ax = axes[1]
    ax.axis('off')
    ax.set_title('2. Sınıflandırma + Konumlandırma\n"Nerede ve Ne?" (Tek Nesne)', fontsize=10.5, fontweight='bold', color='#065F46')
    rect = plt.Rectangle((0.1, 0.1), 0.8, 0.8, fc='#ECFDF5', ec='#10B981', lw=2)
    ax.add_patch(rect)
    c = plt.Circle((0.45, 0.55), 0.2, color='#F87171', ec='#DC2626', lw=2)
    ax.add_patch(c)
    # Bounding box
    bb = plt.Rectangle((0.23, 0.33), 0.44, 0.44, fill=False, ec='#059669', lw=2.5, ls='--')
    ax.add_patch(bb)
    ax.text(0.25, 0.8, 'Araba: [x, y, w, h]', fontsize=9, fontweight='bold', color='#065F46')
    ax.text(0.5, 0.15, 'Çıktı: 1 Sınıf + 1 Kutu Koordinatı', ha='center', fontsize=9.5, fontweight='bold', color='#064E3B')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Task 3: Object Detection
    ax = axes[2]
    ax.axis('off')
    ax.set_title('3. Nesne Tespiti (Object Detection)\n"Nerede ve Ne?" (Çoklu Nesne)', fontsize=10.5, fontweight='bold', color='#991B1B')
    rect = plt.Rectangle((0.1, 0.1), 0.8, 0.8, fc='#FEF2F2', ec='#EF4444', lw=2)
    ax.add_patch(rect)
    # Car
    c = plt.Circle((0.35, 0.4), 0.18, color='#F87171', ec='#DC2626', lw=2)
    ax.add_patch(c)
    bb1 = plt.Rectangle((0.15, 0.2), 0.4, 0.4, fill=False, ec='#DC2626', lw=2.2)
    ax.add_patch(bb1)
    ax.text(0.16, 0.62, 'Araba: %96', fontsize=8, fontweight='bold', color='#991B1B')
    # Pedestrian
    p = plt.Rectangle((0.7, 0.45), 0.12, 0.35, color='#60A5FA', ec='#2563EB', lw=1.5)
    ax.add_patch(p)
    bb2 = plt.Rectangle((0.68, 0.42), 0.16, 0.42, fill=False, ec='#2563EB', lw=2.2)
    ax.add_patch(bb2)
    ax.text(0.68, 0.86, 'Yaya: %91', fontsize=8, fontweight='bold', color='#1E40AF')
    ax.text(0.5, 0.15, 'Çıktı: Çoklu Sınıf + Çoklu Kutu', ha='center', fontsize=9.5, fontweight='bold', color='#7F1D1D')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'CV tasks saved to: {output_path}')

def draw_yolo_grid(output_path):
    fig, ax = plt.subplots(figsize=(6, 6), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)

    # Grid
    for i in range(8):
        ax.axhline(i, color='#9CA3AF', lw=1.2, ls=':')
        ax.axvline(i, color='#9CA3AF', lw=1.2, ls=':')

    # Background image simulation
    ax.text(0.5, 6.5, 'S x S Izgara (Grid)', fontsize=10, fontweight='bold', color='#4B5563')

    # Object 1 (Car in center)
    car_box = patches.FancyBboxPatch((2.2, 1.8), 2.6, 2.4, boxstyle="round,pad=0.05",
                                     fc='#FEE2E2', ec='#DC2626', lw=2.5)
    ax.add_patch(car_box)
    ax.text(2.3, 4.4, 'Araba (Conf: 0.94)', fontsize=9, fontweight='bold', color='#DC2626')

    # Center of object
    cx, cy = 3.5, 3.0
    ax.plot(cx, cy, 'ko', markersize=8)
    ax.text(cx + 0.15, cy - 0.25, 'Merkez (xc, yc)', fontsize=9, fontweight='bold', color='#111827')

    # Highlight responsible grid cell (cell (3, 3))
    resp_cell = plt.Rectangle((3, 2), 1, 1, fill=True, color='#FEF08A', alpha=0.5, ec='#CA8A04', lw=2)
    ax.add_patch(resp_cell)
    ax.text(3.5, 2.2, 'Sorumlu\nHücre', ha='center', fontsize=8, fontweight='bold', color='#854D0E')

    ax.set_title('YOLO Izgara (Grid) ve Sorumlu Hücre Mantığı', fontsize=11, fontweight='bold', pad=12)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'YOLO grid saved to: {output_path}')

if __name__ == '__main__':
    draw_cv_tasks('Derin_Ogrenme/assets/cv_tasks_comparison.png')
    draw_yolo_grid('Derin_Ogrenme/assets/yolo_grid_bounding_box.png')
