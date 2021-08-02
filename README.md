# 5 Phase Workflow

1. Think simple + mini EDA (lihat Prep, Prep 2)
2. Feature Importance / Correlation Matrix / asosiasi matrix
3. Poly/Transform/Scaling, Gridsearch, BayesSearchCV Randomized Search/Fine Tuning
4. Evaluation
5. EDA

# Prep
1. Cek target, imbalance atau engga
2. Cek missing value, drop kalo banyak.
3. Korelasi/Asosiasi matrix, kalo fiturnya banyak, gunain yg berkorelasi kuat aja.
4. Splitting

# Prep 2
1. Plot X vs target
2. Cari Insight, nambah fitur bisa pake binning

# Modeling
1. xxxxxxxxxx
2. Poly/Transform/Scaling, Randomized Search/Fine Tuning
3. Feature Importance

# Evaluation Klasifikasi
1. Correlation_matrix untuk fitur yg numerik
2. Fokus ke precision atau recall.
    - Fokus ke recall ketika ingin mengurangi false negatif, dan pake f2-score
    - Fokus ke precision ketika ingin mengurangi false positif, dan pake f0.5-score
    - F1 Score ketika dua2nya penting

4. Liat data yang error, cek deh ada salah input data atau engga, kalo ada drop ae
5. Classification Report
6. plot_pr_curve
7. plot_roc_curve

# Evaluation Regresi
1. Correlation_matrix untuk fitur yg numerik
2. plot_actual_vs_prediction
3. plot_residual, cek apa problem datanya.
4. Setelah diplot residual, Cari Data yang Errornya paling besar

