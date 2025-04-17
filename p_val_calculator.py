from scipy.stats import mannwhitneyu
import pandas as pd

df = pd.read_csv('cell-count.csv') 

filtered = df[(df['sample_type'] == 'PBMC') & (df['treatment'] == 'tr1')]

for col in ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']:
    y_vals = filtered[filtered['response'] == 'y'][col]
    n_vals = filtered[filtered['response'] == 'n'][col]
    stat, p = mannwhitneyu(y_vals, n_vals, alternative='two-sided')
    print(f"{col}: p-value = {p:.4f}")