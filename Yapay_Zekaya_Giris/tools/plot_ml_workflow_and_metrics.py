import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('Yapay_Zekaya_Giris/assets', exist_ok=True)

def generate_data_split_and_leakage():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7.5), dpi=300)
    
    # --- Üst Panel: Doğru Veri Bölümleme (Train / Validation / Test) ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 4)
    ax1.axis('off')
    ax1.set_title("A. Standart Veri Bölümleme Oranları ve Amaçları", fontsize=12, fontweight='bold', color='#1E293B', pad=10)

    # Bar: Training (%70)
    ax1.add_patch(patches.Rectangle((0.5, 1.8), 5.0, 1.2, facecolor='#3B82F6', edgecolor='#1D4ED8', lw=1.5))
    ax1.text(3.0, 2.4, 'Eğitim Kümesi (Training Set - %70)\nModel ağırlıklarını öğrenir (fit)', 
             ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)

    # Bar: Validation (%15)
    ax1.add_patch(patches.Rectangle((5.6, 1.8), 2.0, 1.2, facecolor='#F59E0B', edgecolor='#D97706', lw=1.5))
    ax1.text(6.6, 2.4, 'Doğrulama (Val - %15)\nHiperparametre ayarı', 
             ha='center', va='center', color='white', fontweight='bold', fontsize=8.5)

    # Bar: Test (%15)
    ax1.add_patch(patches.Rectangle((7.7, 1.8), 1.8, 1.2, facecolor='#10B981', edgecolor='#047857', lw=1.5))
    ax1.text(8.6, 2.4, 'Test Seti (%15)\nNihai genelleme', 
             ha='center', va='center', color='white', fontweight='bold', fontsize=8.5)

    ax1.text(0.5, 0.9, 'Kural 1: Olcekleme (StandardScaler/MinMax) YALNIZCA Egitim kumesi uzerinden fit edilir: scaler.fit(X_train)\n'
                        'Kural 2: Dogrulama ve Test kumeleri sadece transform edilir: scaler.transform(X_test)', 
             fontsize=9, color='#1E40AF', bbox=dict(boxstyle='round,pad=0.5', facecolor='#EFF6FF', edgecolor='#BFDBFE'))

    # --- Alt Panel: Veri Sızıntısı (Data Leakage) Tehlikesi ---
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 4)
    ax2.axis('off')
    ax2.set_title("B. Veri Sizintisi (Data Leakage) Tehlikesi ve Sonuclari", fontsize=12, fontweight='bold', color='#991B1B', pad=10)

    # Yanlış Uygulama Kutusu
    ax2.add_patch(patches.FancyBboxPatch((0.5, 1.3), 4.2, 2.2, boxstyle="round,pad=0.3", facecolor='#FEF2F2', edgecolor='#EF4444', lw=1.8))
    ax2.text(2.6, 3.1, 'YANLIS: Veri Bolunmeden Once Olcekleme', ha='center', fontsize=9.5, fontweight='bold', color='#B91C1C')
    ax2.text(2.6, 2.1, 'Tum veri setinden ortalama ve varyans\nhesaplanirsa TEST verisinin bilgisi\nmodele gizlice sizdirilmis olur!', 
             ha='center', fontsize=8.5, color='#7F1D1D')

    # Sonuç Kutusu
    ax2.add_patch(patches.FancyBboxPatch((5.3, 1.3), 4.2, 2.2, boxstyle="round,pad=0.3", facecolor='#FFFBEB', edgecolor='#F59E0B', lw=1.8))
    ax2.text(7.4, 3.1, 'SAHTE BASARI TUZAGI', ha='center', fontsize=9.5, fontweight='bold', color='#B45309')
    ax2.text(7.4, 2.1, 'Model testte sahte bicimde %99-%100 basari\ngosterir; ancak sahaya ciktiginda gercek\ndunya verisinde COKER (Ezberleme / Overfitting).', 
             ha='center', fontsize=8.5, color='#92400E')

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/ml_workflow_data_split_leakage.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

def generate_classification_and_roc():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
    
    # --- Sol Panel: Karışıklık Matrisi (Confusion Matrix) ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title("A. Karisiklik Matrisi ve Temel Metrikler", fontsize=12, fontweight='bold', color='#1E293B', pad=12)

    # 2x2 Matrix Grid
    # TP (Sol Üst)
    ax1.add_patch(patches.Rectangle((2.5, 5.5), 2.8, 2.8, facecolor='#DCFCE7', edgecolor='#16A34A', lw=2))
    ax1.text(3.9, 7.3, 'DOGRU POZITIF (TP)', ha='center', fontsize=10, fontweight='bold', color='#166534')
    ax1.text(3.9, 6.4, 'Gercek: 1 | Model: 1\n(Hastalik var, tespit edildi)', ha='center', fontsize=8, color='#14532D')

    # FN (Sağ Üst - Tip II Hata)
    ax1.add_patch(patches.Rectangle((5.5, 5.5), 2.8, 2.8, facecolor='#FEE2E2', edgecolor='#DC2626', lw=2))
    ax1.text(6.9, 7.3, 'YANLIS NEGATIF (FN)', ha='center', fontsize=10, fontweight='bold', color='#991B1B')
    ax1.text(6.9, 6.4, 'Gercek: 1 | Model: 0\n(Tip II Hata - Kacirilan vaka)', ha='center', fontsize=8, color='#7F1D1D')

    # FP (Sol Alt - Tip I Hata)
    ax1.add_patch(patches.Rectangle((2.5, 2.5), 2.8, 2.8, facecolor='#FEF3C7', edgecolor='#D97706', lw=2))
    ax1.text(3.9, 4.3, 'YANLIS POZITIF (FP)', ha='center', fontsize=10, fontweight='bold', color='#B45309')
    ax1.text(3.9, 3.4, 'Gercek: 0 | Model: 1\n(Tip I Hata - Yanlis alarm)', ha='center', fontsize=8, color='#78350F')

    # TN (Sağ Alt)
    ax1.add_patch(patches.Rectangle((5.5, 2.5), 2.8, 2.8, facecolor='#E0F2FE', edgecolor='#0284C7', lw=2))
    ax1.text(6.9, 4.3, 'DOGRU NEGATIF (TN)', ha='center', fontsize=10, fontweight='bold', color='#075985')
    ax1.text(6.9, 3.4, 'Gercek: 0 | Model: 0\n(Saglikli, saglam dendi)', ha='center', fontsize=8, color='#0C4A6E')

    # Formüller
    ax1.text(5.0, 1.2, r"$\mathrm{Precision} = \frac{TP}{TP + FP}$  |  "
                       r"$\mathrm{Recall} = \frac{TP}{TP + FN}$" + "\n" +
                       r"$\mathrm{F1} = 2 \times \frac{\mathrm{Precision} \times \mathrm{Recall}}{\mathrm{Precision} + \mathrm{Recall}}$  |  " +
                       r"$\mathrm{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$",
             ha='center', fontsize=9.5, color='#1E293B',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#F8FAFC', edgecolor='#CBD5E1'))

    # --- Sağ Panel: ROC Eğrisi ve AUC ---
    fpr = np.linspace(0, 1, 100)
    tpr_ideal = 1 - (1 - fpr)**3.5
    
    ax2.plot(fpr, tpr_ideal, color='#2563EB', lw=2.5, label='Model ROC Eğrisi (AUC ≈ 0.92)')
    ax2.fill_between(fpr, tpr_ideal, alpha=0.15, color='#3B82F6')
    ax2.plot([0, 1], [0, 1], color='#94A3B8', lw=1.8, linestyle='--', label='Rastgele Tahmin Köşegeni (AUC = 0.50)')
    
    ax2.set_xlim(-0.02, 1.02)
    ax2.set_ylim(-0.02, 1.05)
    ax2.set_xlabel('Yanlış Pozitif Oranı (FPR = FP / (FP + TN))', fontsize=9.5, fontweight='bold', color='#334155')
    ax2.set_ylabel('Doğru Pozitif Oranı / Duyarlılık (TPR = TP / (TP + FN))', fontsize=9.5, fontweight='bold', color='#334155')
    ax2.set_title("B. ROC Eğrisi ve Alan (AUC) Değerlendirmesi", fontsize=12, fontweight='bold', color='#1E293B', pad=12)
    ax2.legend(loc='lower right', fontsize=8.5)
    ax2.grid(True, linestyle=':', alpha=0.6)

    ax2.text(0.35, 0.45, "Mükemmel Model: AUC = 1.0\nKabul Edilebilir: AUC ≥ 0.80\nRastgele / İşe Yaramaz: AUC = 0.50", 
             fontsize=8.5, color='#1E40AF', bbox=dict(boxstyle='round,pad=0.4', facecolor='#EFF6FF', edgecolor='#93C5FD'))

    plt.tight_layout()
    output_file = 'Yapay_Zekaya_Giris/assets/classification_metrics_roc_curve.png'
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_file}")

if __name__ == '__main__':
    generate_data_split_and_leakage()
    generate_classification_and_roc()
