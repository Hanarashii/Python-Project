import pandas as pd
#Các trường dữ liệu bắt buộc phải có
REQUIRED_COLUMNS = [
    "selling_price",
    "fuel",
    "year",
    "transmission"
]

#Kiểm tra trường nào thiếu 
def check_requied_col(df: pd.DataFrame):
    missing = [i for i in REQUIRED_COLUMNS if i not in df.columns]
    return missing

#Kiểm về mặt logic
def check_price(df: pd.DataFrame):
    return (df["selling_price"] <= 0).sum()

#Đánh giá mức độ trùng của dữ liệu
def check_duplicate(df: pd.DataFrame):
    return df.duplicated().sum()

#Kiểm tra các dòng thiếu dữ liệu
def check_na(df: pd.DataFrame):
    return df.isna().any(axis = 1).sum()

#Rà soát dữ liệu
def validate(df: pd.DataFrame):
    reports = {}
    reports["total_rows"] = len(df)
    reports["rows_na"] = check_na(df)
    reports["rows_duplicate"] = check_duplicate(df)
    reports["required_columns"] = check_requied_col(df)
    reports["invalid_price"] = check_price(df)
    return reports
