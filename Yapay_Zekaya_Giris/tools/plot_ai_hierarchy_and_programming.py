import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('Yapay_Zekaya_Giris/assets', exist_ok=True)

def generate_ai_hierarchy_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5), dpi=300)
    
    # --- Sol Panel: AI Hiyerarşisi (İç İçe Kümeler) ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title("A. Yapay Zekâ Ekosistemi ve Hiyerarşisi", fontsize=13, fontweight='bold', pad=15, color='#1E293B')

    # AI (En dış)
    c_ai = plt.Circle((5, 4.8), 4.5, color='#EFF6FF', ec='#2563EB', lw=2.2)
    ax1.add_patch(c_ai)
    ax1.text(5, 8.8, 'YAPAY ZEKÂ (AI)', ha='center', fontsize=12, fontweight='bold', color='#1E40AF')
    ax1.text(5, 8.4, 'İnsan zekasını taklit eden tüm sistemler (Kural tabanlı + Uzman sistemler)', 
             ha='center', fontsize=7.5, color='#3B82F6', style='italic')

    # ML
    c_ml = plt.Circle((5, 4.2), 3.4, color='#ECFDF5', ec='#059669', lw=2)
    ax1.add_patch(c_ml)
    ax1.text(5, 7.1, 'MAKİNE ÖĞRENMESİ (ML)', ha='center', fontsize=11, fontweight='bold', color='#065F46')
    ax1.text(5, 6.7, 'Açıkça kodlanmadan veriden örüntü öğrenen algoritmalar\n(Regresyon, k-NN, Karar Ağaçları, SVM)', 
             ha='center', fontsize=7.2, color='#047857')

    # DL
    c_dl = plt.Circle((5, 3.5), 2.2, color='#FEF2F2', ec='#DC2626', lw=1.8)
    ax1.add_patch(c_dl)
    ax1.text(5, 5.2, 'DERİN ÖĞRENME (DL)', ha='center', fontsize=10, fontweight='bold', color='#991B1B')
    ax1.text(5, 4.7, 'Çok katmanlı yapay sinir ağları\n(Otomatik öznitelik çıkarımı - CNN, MLP)', 
             ha='center', fontsize=7, color='#B91C1C')

    # GenAI & LLM
    c_gen = plt.Circle((5, 2.7), 1.1, color='#FAF5FF', ec='#9333EA', lw=1.6)
    ax1.add_patch(c_gen)
    ax1.text(5, 3.1, 'ÜRETKEN YZ & LLM', ha='center', fontsize=8.5, fontweight='bold', color='#6B21A8')
    ax1.text(5, 2.6, 'Metin, görüntü ve kod üretimi\n(ChatGPT, Gemini, Claude)', 
             ha='center', fontsize=6.2, color='#7E22CE')

    # --- Sağ Panel: Geleneksel Programlama vs Makine Öğrenmesi Paradigması ---
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title("B. Programlama Paradigmaları Karşılaştırması", fontsize=13, fontweight='bold', pad=15, color='#1E293B')

    # 1. Geleneksel Programlama Kutusu
    box_trad = patches.FancyBboxPatch((0.5, 5.5), 9.0, 3.8, boxstyle="round,pad=0.3", 
                                      facecolor='#F8FAFC', edgecolor='#94A3B8', lw=1.5)
    ax2.add_patch(box_trad)
    ax2.text(5, 8.8, '1. GELENEKSEL PROGRAMLAMA (Kural Tabanlı)', ha='center', fontsize=11, fontweight='bold', color='#334155')

    # Input items
    ax2.text(1.8, 7.6, '[ VERİ ]\n(Sayılar, Metin)', ha='center', va='center', fontsize=8.5, 
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#E2E8F0', edgecolor='#64748B'))
    ax2.text(1.8, 6.3, '[ KURALLAR ]\n(Mühendisin Kodları)', ha='center', va='center', fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#E2E8F0', edgecolor='#64748B'))

    ax2.annotate('', xy=(4.5, 7.0), xytext=(3.0, 7.0),
                 arrowprops=dict(facecolor='#64748B', edgecolor='#64748B', width=1.5, headwidth=6))

    ax2.text(5.2, 7.0, '[ BİLGİSAYAR / DERLEYİCİ ]\n(Kuralları veriye uygular)', ha='center', va='center', fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#DBEAFE', edgecolor='#2563EB', lw=1.2))

    ax2.annotate('', xy=(7.8, 7.0), xytext=(6.9, 7.0),
                 arrowprops=dict(facecolor='#64748B', edgecolor='#64748B', width=1.5, headwidth=6))

    ax2.text(8.7, 7.0, '[ CEVAPLAR ]\n(Sonuç / Çıktı)', ha='center', va='center', fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#DCFCE7', edgecolor='#16A34A', lw=1.2))

    # 2. Makine Öğrenmesi Kutusu
    box_ml = patches.FancyBboxPatch((0.5, 0.8), 9.0, 3.8, boxstyle="round,pad=0.3", 
                                    facecolor='#F0FDF4', edgecolor='#10B981', lw=1.8)
    ax2.add_patch(box_ml)
    ax2.text(5, 4.1, '2. MAKİNE ÖĞRENMESİ (Veri Güdümlü)', ha='center', fontsize=11, fontweight='bold', color='#065F46')

    ax2.text(1.8, 2.9, '[ VERİ ]\n(Öznitelikler - X)', ha='center', va='center', fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#E0F2FE', edgecolor='#0284C7'))
    ax2.text(1.8, 1.6, '[ CEVAPLAR ]\n(Etiketler - Y)', ha='center', va='center', fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEF3C7', edgecolor='#D97706'))

    ax2.annotate('', xy=(4.5, 2.25), xytext=(3.0, 2.25),
                 arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.5, headwidth=6))

    ax2.text(5.2, 2.25, '[ ML ÖĞRENME MOTORU ]\n(Örüntüleri keşfeder)', ha='center', va='center', fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#D1FAE5', edgecolor='#059669', lw=1.2))

    ax2.annotate('', xy=(7.8, 2.25), xytext=(6.9, 2.25),
                 arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.5, headwidth=6))

    ax2.text(8.7, 2.25, '[ KURALLAR ]\n(Eğitilmiş MODEL)', ha='center', va='center', fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEE2E2', edgecolor='#DC2626', lw=1.2))

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/ai_hierarchy_and_programming_paradigms.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

if __name__ == '__main__':
    generate_ai_hierarchy_diagram()
