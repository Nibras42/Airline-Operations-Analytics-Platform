import os
import pandas as pd
import matplotlib.pyplot as plt

PROCESSED_DIR = "data_processed"
PROCESSED_PATH = os.path.join(PROCESSED_DIR, "processed_data.csv")
SUMMARY_PATH = os.path.join(PROCESSED_DIR, "summary.txt")
CORR_PATH = os.path.join(PROCESSED_DIR, "correlations.txt")
VIS_DIR = "visuals"


def load_processed_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Processed data not found at: {path}\n"
            f"Run wf_dataprocessing.py or wf_core.py first."
        )
    return pd.read_csv(path)


def write_summary_statistics(df: pd.DataFrame):
    quantitative = ["PASSENGERS", "SEATS", "DEPARTURES_PERFORMED", "LOAD_FACTOR"]
    qualitative = ["AIRCRAFT_TYPE"]

    lines = []
    lines.append("SUMMARY STATISTICS (T-100 Domestic Segment)\n")

    for col in quantitative:
        series = df[col].dropna()
        lines.append(f"{col}:")
        lines.append(f"  min: {series.min():.4f}")
        lines.append(f"  max: {series.max():.4f}")
        lines.append(f"  median: {series.median():.4f}\n")

    for col in qualitative:
        series = df[col].dropna()
        value_counts = series.value_counts()
        n_categories = value_counts.shape[0]

        most_freq = value_counts[value_counts == value_counts.max()].index.tolist()
        least_freq = value_counts[value_counts == value_counts.min()].index.tolist()

        lines.append(f"{col}:")
        lines.append(f"  number of categories: {n_categories}")
        lines.append(f"  most frequent: {most_freq[:5]} (showing up to 5)")
        lines.append(f"  least frequent: {least_freq[:5]} (showing up to 5)\n")

    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[wf_visualization] Wrote summary to: {SUMMARY_PATH}")


def write_correlations(df: pd.DataFrame):
    cols = ["PASSENGERS", "SEATS", "DEPARTURES_PERFORMED", "LOAD_FACTOR"]
    corr = df[cols].corr(method="pearson")

    with open(CORR_PATH, "w", encoding="utf-8") as f:
        f.write("PAIRWISE CORRELATIONS (Pearson)\n\n")
        f.write(corr.to_string())

    print(f"[wf_visualization] Wrote correlations to: {CORR_PATH}")


def make_plots(df: pd.DataFrame):
    os.makedirs(VIS_DIR, exist_ok=True)

    pairs = [
        ("SEATS", "PASSENGERS"),
        ("DEPARTURES_PERFORMED", "PASSENGERS"),
        ("SEATS", "DEPARTURES_PERFORMED"),
        ("LOAD_FACTOR", "PASSENGERS"),
        ("LOAD_FACTOR", "SEATS"),
        ("LOAD_FACTOR", "DEPARTURES_PERFORMED"),
    ]

    for x, y in pairs:
        plt.figure()
        plt.scatter(df[x], df[y], s=5)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f"{y} vs {x}")
        out_path = os.path.join(VIS_DIR, f"{y}_vs_{x}.png")
        plt.tight_layout()
        plt.savefig(out_path, dpi=150)
        plt.close()

    top_counts = df["AIRCRAFT_TYPE"].value_counts().head(20)
    plt.figure(figsize=(10, 5))
    plt.bar(top_counts.index.astype(str), top_counts.values)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Aircraft Type (Top 20)")
    plt.ylabel("Count")
    plt.title("Aircraft Type Distribution (Top 20)")
    out_path = os.path.join(VIS_DIR, "AircraftType_hist.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

    print(f"[wf_visualization] Saved plots to: {VIS_DIR}/")


def main():
    df = load_processed_data(PROCESSED_PATH)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    write_summary_statistics(df)
    write_correlations(df)
    make_plots(df)


if __name__ == "__main__":
    main()