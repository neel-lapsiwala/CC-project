# 🔍 Automated EDA System

A lightweight Python script that takes any CSV file and automatically generates
two rich, interactive HTML EDA reports — using **ydata-profiling** and **SweetViz** —
for quick insight generation and data-quality checks.

---

## 📁 Project Structure

```
CC project/
├── data/
│   └── titanic.csv          # Sample dataset (Titanic passenger data)
├── reports/
│   ├── profiling_report.html  # ydata-profiling report (generated)
│   └── sweetviz_report.html   # SweetViz report (generated)
├── venv/                    # Python virtual environment (not committed)
├── eda.py                   # Core EDA script
├── requirements.txt         # Pinned dependencies
└── README.md                # This file
```

---

## ⚙️ Setup

### 1. Clone / Navigate to the project folder

```bash
cd "CC project"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** SweetViz can be sensitive to numpy / pandas versions. The pinned
> versions in `requirements.txt` have been tested for compatibility.

---

## 🚀 Usage

### Basic run (Titanic dataset)

```bash
python eda.py data/titanic.csv
```

### Custom output directory

```bash
python eda.py data/titanic.csv --out-dir my_reports
```

### Minimal mode (faster for large datasets)

```bash
python eda.py data/large_dataset.csv --minimal
```

> `--minimal` enables minimal mode in ydata-profiling, skipping expensive
> correlation calculations and interaction plots. Useful for datasets with
> thousands of columns or millions of rows.

### Full help

```bash
python eda.py --help
```

---

## 📊 Generated Reports

### 1. `profiling_report.html` — ydata-profiling

| Section | What it shows |
|---|---|
| **Overview** | Dataset dimensions, memory usage, duplicate rows |
| **Variables** | Per-column statistics: min/max, mean, histogram, common values |
| **Interactions** | Scatter plots for numeric column pairs |
| **Correlations** | Pearson, Spearman, Kendall, and Cramér's V matrices |
| **Missing Values** | Matrix, heatmap, and dendrogram of nulls |
| **Samples** | First and last rows of the dataset |

Use **explorative mode** (default) for a thorough analysis, or `--minimal` for a
quick scan of large files.

---

### 2. `sweetviz_report.html` — SweetViz

| Section | What it shows |
|---|---|
| **Feature Summary** | High-level strip for every column at a glance |
| **Associations** | Pairwise correlation heatmap (numeric + categorical) |
| **Numeric Features** | Distribution histogram, quartile box, mean/std/min/max |
| **Categorical / Boolean** | Bar chart of top categories, unique counts |
| **Text Features** | Word count, character count, most frequent words |
| **Missing data** | Shown inline per feature as a red stripe |

SweetViz is optimized for **comparing two datasets** (e.g. train vs test), making
it ideal for machine-learning workflows as well.

---

## 🛡️ Error Handling

| Scenario | Behaviour |
|---|---|
| CSV file not found | Exits with a clear error message |
| CSV is empty | Exits with a clear error message |
| ydata-profiling fails | Logs the error; SweetViz still runs |
| SweetViz fails | Logs the error; profiling report still saves |
| Package not installed | Prints a `pip install` hint and continues |

---

## 📌 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `pandas` | 2.0.3 | Data loading and manipulation |
| `numpy` | 1.24.4 | Numerical computations |
| `ydata-profiling` | 4.6.4 | Comprehensive profiling report |
| `sweetviz` | 2.3.1 | Visual EDA comparison report |

See `requirements.txt` for the full pinned dependency list.

---

## 💡 Tips

- Open the HTML reports directly in any modern browser — no server needed.
- For very large CSVs (> 100 MB), always use `--minimal` to keep profiling fast.
- SweetViz supports train/test comparison — extend `eda.py` with `sv.compare()`
  for ML dataset auditing.
- To use a different dataset, just swap the CSV path:
  ```bash
  python eda.py data/my_data.csv
  ```
