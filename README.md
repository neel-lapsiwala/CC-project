<div align="center">
  <h1>📊 Automated EDA System</h1>
  
  <p>
    <strong>A lightweight, zero-configuration Python tool to generate rich Exploratory Data Analysis reports.</strong>
  </p>

  <p>
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Versions" />
    <img src="https://img.shields.io/badge/pandas-2.0+-green.svg" alt="Pandas version" />
    <img src="https://img.shields.io/badge/ydata--profiling-4.6.4-orange.svg" alt="ydata-profiling" />
    <img src="https://img.shields.io/badge/sweetviz-2.3.1-ff69b4.svg" alt="SweetViz" />
  </p>
</div>

<br />

> Takes any CSV file and automatically generates **two interactive HTML reports** using `ydata-profiling` and `SweetViz` for rapid insight generation and data-quality audits.

## 📋 Table of Contents

- [✨ Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🛠️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📊 Generated Reports](#-generated-reports)
- [📦 Dependencies](#-dependencies)

## ✨ Features

- 🚀 **One-command execution:** Pass any CSV file and get full reports instantly.
- 📉 **Two Powerful Engines:** Get the statistical depth of `ydata-profiling` and the visual comparative power of `SweetViz`.
- ⚡ **Minimal Mode:** Optimized for large datasets (millions of rows) by skipping heavy correlation matrix computations.
- 🛡️ **Robust Error Handling:** Gracefully falls back if one of the profiling engines encounters an issue.

## 📂 Project Structure

```text
CC project/
├── data/
│   └── titanic.csv            # Sample dataset 
├── reports/
│   ├── profiling_report.html  # Generated ydata-profiling report
│   └── sweetviz_report.html   # Generated SweetViz report
├── eda.py                     # 🧠 Core EDA script
├── requirements.txt           # Pinned dependencies
└── README.md                  # This file
```
*(Note: The `venv` directory is ignored via `.gitignore`)*

## 🛠️ Installation

### 1. Clone & Navigate
```bash
git clone https://github.com/neel-lapsiwala/CC-project.git
cd "CC project"
```

### 2. Set Up Virtual Environment

<details>
<summary><b>Windows (PowerShell)</b></summary>

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
</details>

<details>
<summary><b>Windows (CMD)</b></summary>

```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```
</details>

<details>
<summary><b>macOS / Linux</b></summary>

```bash
python3 -m venv venv
source venv/bin/activate
```
</details>

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
> **⚠️ Note:** SweetViz can be sensitive to specific `numpy`/`pandas` versions. The pinned versions in `requirements.txt` are tested for stability.

## 🚀 Usage

### Basic Run
Run the script on the provided sample dataset:
```bash
python eda.py data/titanic.csv
```

### Advanced Options

| Command | Description |
| :--- | :--- |
| `python eda.py data/titanic.csv --out-dir my_reports` | Specify a custom folder for saving output reports. |
| `python eda.py data/large_dataset.csv --minimal` | **Minimal Mode:** Skips expensive correlations for massive datasets. |
| `python eda.py --help` | View all available command-line arguments. |

## 📊 Generated Reports

### 1️⃣ `ydata-profiling` Report
A detailed statistical overview saved as `profiling_report.html`.

- **Overview:** Row/column counts, memory usage, duplicate rates.
- **Variables:** Distribution histograms, missing values, descriptive stats.
- **Interactions & Correlations:** Pearson/Spearman matrices and pair scatters.

### 2️⃣ `SweetViz` Report
A visually stunning, high-level summary saved as `sweetviz_report.html`.

- **Feature Summary:** High-level strips for every column.
- **Associations:** Heatmaps combining numeric and categorical data.
- **Missing Data:** Inline red-stripes indicating null density per feature.

*(Tip: Open the `.html` files directly in any modern browser—no server required!)*

## 📦 Dependencies

| Package | Version | Purpose |
| :--- | :--- | :--- |
| `pandas` | `2.0.3` | Data loading and preprocessing |
| `numpy` | `1.24.4` | Matrix and numerical operations |
| `ydata-profiling` | `4.6.4` | Statistical analysis & profiling |
| `sweetviz` | `2.3.1` | Visual EDA and feature comparison |

---

<div align="center">
  <i>Built with ❤️ for rapid data analysis.</i>
</div>
