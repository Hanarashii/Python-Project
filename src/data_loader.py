from pathlib import Path
import logging
import pandas as pd

logger = logging.getLogger("__name__")

def load_csv_dataframe(path: str):
    path = Path(path)
    csv_files = list(path.rglob("*csv"))
    if not csv_files:
        logger.error("No csv files found, exiting")
    csv_files.sort(key=lambda df: df.stat().st_mtime, reverse=True)
    return pd.read_csv(csv_files[0])
