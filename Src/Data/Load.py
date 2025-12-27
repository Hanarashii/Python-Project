import pandas as pd
from pathlib import Path


#Loading dữ liệu từ file
def loadData(path: str):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy: {path}")
    
    df = pd.read_csv(path)
    return df
