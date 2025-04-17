# Cell Count to Relative Frequency Converter

This Python script converts raw immune cell counts from a CSV file into relative frequency percentages for each sample and cell population.

## Input

- `cell-count.csv`: A CSV file containing immune cell counts. Must include the following columns:
  - `sample`, `b_cell`, `cd8_t_cell`, `cd4_t_cell`, `nk_cell`, `monocyte`

## Output

- `relative_frequency.csv`: A CSV file with one row per sample × population, including:
  - `sample`, `total_count`, `population`, `count`, `percentage`

## ✅ Requirements

Make sure you have **Python 3.x** installed.

Install the required library using pip:
```bash
pip install pandas