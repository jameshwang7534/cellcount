import pandas as pd

def convert_cell_counts(input_file, output_file):

    data = pd.read_csv(input_file)

    population_columns = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

    melted = data.melt(id_vars=['sample'], value_vars=population_columns, var_name='population', value_name='count')

    total_counts = melted.groupby('sample')['count'].sum().reset_index()
    total_counts.rename(columns={'count': 'total_count'}, inplace=True)

    merged = pd.merge(melted, total_counts, on='sample')

    merged['percentage'] = (merged['count'] / merged['total_count']) * 100

    output_data = merged[['sample', 'total_count', 'population', 'count', 'percentage']]

    output_data.to_csv(output_file, index=False)
    print(f"Saved output to {output_file}")


if __name__ == "__main__":
    input_path = "cell-count.csv"
    output_path = "relative_frequency.csv"
    convert_cell_counts(input_path, output_path)