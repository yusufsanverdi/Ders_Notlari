import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_ai_hierarchy(output_path):
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # AI Circle
    c_ai = plt.Circle((5, 5), 4.6, color='#2563EB', alpha=0.15, ec='#1D4ED8', lw=2.5, linestyle='-')
    ax.add_patch(c_ai)
    ax.text(5, 8.8, 'YAPAY ZEKA (Artificial Intelligence - AI)', ha='center', va='center', 
            fontsize=13, fontweight='bold', color='#1E40AF')
    ax.text(5, 8.3, 'İnsan zekasını taklit eden tüm sistemler (Kural tabanlı + Öğrenen)', 
            ha='center', va='center', fontsize=9, color='#3B82F6', style='italic')

    # ML Circle
    c_ml = plt.Circle((5, 4.3), 3.3, color='#059669', alpha=0.2, ec='#047857', lw=2.2, linestyle='-')
    ax.add_patch(c_ml)
    ax.text(5, 6.8, 'MAKİNE ÖĞRENMESİ (Machine Learning - ML)', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='#065F46')
    ax.text(5, 6.3, 'Açıkça programlanmadan veriden örüntü çıkaran algoritmalar', 
            ha='center', va='center', fontsize=8.5, color='#059669', style='italic')

    # DL Circle
    c_dl = plt.Circle((5, 3.5), 1.9, color='#DC2626', alpha=0.25, ec='#B91C1C', lw=2.2, linestyle='-')
    ax.add_patch(c_dl)
    ax.text(5, 4.4, 'DERİN ÖĞRENME\n(Deep Learning - DL)', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='#991B1B')
    ax.text(5, 3.1, 'Çok katmanlı yapay sinir ağları,\notomatik öznitelik çıkarımı', 
            ha='center', va='center', fontsize=8, color='#B91C1C', style='italic')

    # Examples/Features
    ax.text(5, 1.9, 'CNN, ResNet, YOLO, Transformer, GAN', ha='center', va='center',
            fontsize=8.5, fontweight='semibold', color='#7F1D1D')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'AI hierarchy saved to: {output_path}')

def draw_ml_types(output_path):
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Supervised Box
    p1 = patches.FancyBboxPatch((0.5, 0.8), 3.4, 4.4, boxstyle="round,pad=0.3",
                                fc='#EFF6FF', ec='#3B82F6', lw=2)
    ax.add_patch(p1)
    ax.text(2.2, 4.8, 'Denetimli Öğrenme\n(Supervised Learning)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#1E40AF')
    ax.text(2.2, 4.0, 'Etiketli Veri (Input X -> Target Y)', ha='center', va='center',
            fontsize=8.5, color='#1E3A8A', style='italic')
    ax.text(2.2, 3.2, '• Sınıflandırma (Classification)\n  - Kedi / Köpek\n  - Spam / Normal Mail\n  - Trafik Işığı Rengi',
            ha='center', va='center', fontsize=8.5, color='#1F2937')
    ax.text(2.2, 1.6, '• Regresyon (Regression)\n  - Ev Fiyatı / Kira Tahmini\n  - Sınav Notu Tahmini\n  - Sıcaklık / Hisse Değeri',
            ha='center', va='center', fontsize=8.5, color='#1F2937')

    # Unsupervised Box
    p2 = patches.FancyBboxPatch((4.3, 0.8), 3.4, 4.4, boxstyle="round,pad=0.3",
                                fc='#ECFDF5', ec='#10B981', lw=2)
    ax.add_patch(p2)
    ax.text(6.0, 4.8, 'Denetimsiz Öğrenme\n(Unsupervised Learning)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#065F46')
    ax.text(6.0, 4.0, 'Etiketsiz Veri (Sadece X)', ha='center', va='center',
            fontsize=8.5, color='#064E3B', style='italic')
    ax.text(6.0, 2.7, '• Kümeleme (Clustering)\n  - Müşteri Segmentasyonu\n  - Benzer Haber Gruplama\n  - Anomali / Sahtekarlık Tespiti\n\n• Boyut İndirgeme (PCA)\n• Yoğunluk Tahmini',
            ha='center', va='center', fontsize=8.5, color='#1F2937')

    # Reinforcement Box
    p3 = patches.FancyBboxPatch((8.1, 0.8), 3.4, 4.4, boxstyle="round,pad=0.3",
                                fc='#FEF2F2', ec='#EF4444', lw=2)
    ax.add_patch(p3)
    ax.text(9.8, 4.8, 'Pekiştirmeli Öğrenme\n(Reinforcement Learning)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#991B1B')
    ax.text(9.8, 4.0, 'Ödül / Ceza Mekanizması', ha='center', va='center',
            fontsize=8.5, color='#7F1D1D', style='italic')
    ax.text(9.8, 2.7, '• Ajan (Agent) ve Çevre (Env)\n• Durum (State) & Eylem (Action)\n• Deneme - Yanılma\n\n- Otonom Araç Sürüşü\n- Satranç / Go (AlphaGo)\n- Robotik Kol Kontrolü',
            ha='center', va='center', fontsize=8.5, color='#1F2937')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f'ML types saved to: {output_path}')

if __name__ == '__main__':
    draw_ai_hierarchy('Derin_Ogrenme/assets/ai_ml_dl_hierarchy.png')
    draw_ml_types('Derin_Ogrenme/assets/ml_types.png')
