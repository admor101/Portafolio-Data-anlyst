import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

DATA_URL = "https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
DATA_PATH = "data/ag_exports.csv"
PLOT_PATH = "data/top10_total_exports.png"


def download_data(url: str = DATA_URL) -> pd.DataFrame:
    """Download CSV data from a URL and return as DataFrame."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return pd.read_csv(StringIO(resp.text))


def compute_top_exports(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Return the top `n` states by total exports."""
    return df.nlargest(n, "total exports")


def plot_exports(df: pd.DataFrame, path: str = PLOT_PATH) -> None:
    """Generate a bar plot for total exports by state and save to disk."""
    plt.figure(figsize=(10, 6))
    plt.bar(df["state"], df["total exports"], color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Total Exports (millions USD)")
    plt.title("Top States by Total Agricultural Exports (2011)")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def main() -> None:
    df = download_data()
    df.to_csv(DATA_PATH, index=False)
    top_df = compute_top_exports(df)
    plot_exports(top_df)
    print(top_df)


if __name__ == "__main__":
    main()
