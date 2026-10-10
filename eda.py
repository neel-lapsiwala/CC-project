# -*- coding: utf-8 -*-
"""
eda.py — Automated EDA System
==============================
Accepts any CSV file and generates two HTML EDA reports:
  1. ydata-profiling report  → reports/profiling_report.html
  2. SweetViz report         → reports/sweetviz_report.html

Usage:
    python eda.py <csv_path> [--out-dir reports] [--minimal]

Author: Automated EDA System
"""

import argparse
import io
import os
import sys

# Force UTF-8 output on Windows so Unicode characters print correctly
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import pandas as pd


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Automated EDA: generate ydata-profiling and SweetViz reports from a CSV file."
    )
    parser.add_argument(
        "csv_path",
        type=str,
        help="Path to the input CSV file.",
    )
    parser.add_argument(
        "--out-dir",
        type=str,
        default="reports",
        help="Directory where HTML reports will be saved (default: reports).",
    )
    parser.add_argument(
        "--minimal",
        action="store_true",
        help="Enable minimal mode in ydata-profiling (faster, for large datasets).",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# CSV loading & basic console summary
# ---------------------------------------------------------------------------

def load_csv(csv_path: str) -> pd.DataFrame:
    """
    Load the CSV into a DataFrame.
    Raises FileNotFoundError or ValueError for invalid / empty files.
    """
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"CSV file not found: '{csv_path}'")

    df = pd.read_csv(csv_path)

    if df.empty:
        raise ValueError(f"The CSV file '{csv_path}' is empty or has no rows.")

    return df


def print_summary(df: pd.DataFrame, csv_path: str) -> None:
    """Print dataset shape, column dtypes, and missing-value counts."""
    print("\n" + "=" * 60)
    print(f"  Dataset: {csv_path}")
    print("=" * 60)
    print(f"  Shape : {df.shape[0]:,} rows × {df.shape[1]} columns")

    print("\n  Column Data Types:")
    print("  " + "-" * 40)
    for col, dtype in df.dtypes.items():
        print(f"    {col:<30} {str(dtype)}")

    print("\n  Missing Value Counts:")
    print("  " + "-" * 40)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    for col in df.columns:
        count = missing[col]
        pct = missing_pct[col]
        flag = " ⚠" if count > 0 else ""
        print(f"    {col:<30} {count:>6} ({pct:>5.1f}%){flag}")

    print("=" * 60 + "\n")


# ---------------------------------------------------------------------------
# ydata-profiling report
# ---------------------------------------------------------------------------

def generate_profiling_report(df: pd.DataFrame, out_dir: str, minimal: bool, base_name: str) -> None:
    """
    Generate a ydata-profiling (formerly pandas-profiling) HTML report.

    Parameters
    ----------
    df      : input DataFrame
    out_dir : destination directory for the report
    minimal : if True, use minimal mode (faster for large datasets)
    base_name : base name of the csv file to use as prefix
    """
    try:
        # Import here so a missing package doesn't crash the whole script
        from ydata_profiling import ProfileReport

        mode_label = "minimal" if minimal else "explorative"
        print(f"  [ydata-profiling] Generating {mode_label} report …")

        profile = ProfileReport(
            df,
            title="Automated EDA — Profiling Report",
            explorative=not minimal,   # explorative=False when minimal=True
            minimal=minimal,
        )

        out_path = os.path.join(out_dir, f"{base_name}_profiling_report.html")
        profile.to_file(out_path)
        print(f"  [ydata-profiling] ✓ Report saved → {out_path}")

    except ImportError:
        print("  [ydata-profiling] ✗ Package not installed. Run: pip install ydata-profiling")
    except Exception as exc:
        # Log the error but continue so the SweetViz report can still be generated
        print(f"  [ydata-profiling] ✗ Report generation failed: {exc}")


# ---------------------------------------------------------------------------
# SweetViz report
# ---------------------------------------------------------------------------

def generate_sweetviz_report(df: pd.DataFrame, out_dir: str, base_name: str) -> None:
    """
    Generate a SweetViz HTML report.

    Parameters
    ----------
    df      : input DataFrame
    out_dir : destination directory for the report
    base_name : base name of the csv file to use as prefix
    """
    try:
        import sweetviz as sv

        print("  [SweetViz] Generating report …")

        report = sv.analyze(df)

        out_path = os.path.join(out_dir, f"{base_name}_sweetviz_report.html")
        report.show_html(
            filepath=out_path,
            open_browser=False,   # do not auto-open the browser
            layout="widescreen",
            scale=1.0,
        )
        print(f"  [SweetViz] ✓ Report saved → {out_path}")

    except ImportError:
        print("  [SweetViz] ✗ Package not installed. Run: pip install sweetviz")
    except Exception as exc:
        # Log the error but continue so the other report is unaffected
        print(f"  [SweetViz] ✗ Report generation failed: {exc}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()

    # ---- 1. Resolve output directory ----------------------------------------
    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)
    print(f"\n  Output directory: {out_dir}")

    # ---- 2. Load CSV ---------------------------------------------------------
    try:
        df = load_csv(args.csv_path)
    except FileNotFoundError as exc:
        print(f"\n  ✗ Error: {exc}")
        sys.exit(1)
    except ValueError as exc:
        print(f"\n  ✗ Error: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"\n  ✗ Unexpected error while reading CSV: {exc}")
        sys.exit(1)

    # ---- 3. Print console summary --------------------------------------------
    print_summary(df, args.csv_path)

    # ---- 4. Generate reports (each handles its own errors internally) --------
    print("  Generating reports …\n")
    base_name = os.path.splitext(os.path.basename(args.csv_path))[0]
    generate_profiling_report(df, out_dir, minimal=args.minimal, base_name=base_name)
    print()
    generate_sweetviz_report(df, out_dir, base_name=base_name)

    print("\n  All done! Open the HTML files in reports/ to view your EDA.\n")


if __name__ == "__main__":
    main()
