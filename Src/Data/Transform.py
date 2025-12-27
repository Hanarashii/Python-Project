import pandas as pd

CURRENT_YEAR  = 2025 #Năm hiện tại 

#biển đổi 1 số cột dữ liệu cần thiết cho phân tích
def transformData(df: pd.DataFrame):

    df["mean_price_by_fuel"] = df.groupby("fuel")["selling_price"].transform("mean")
    df["median_price_by_fuel"] = df.groupby("fuel")["selling_price"].transform("median")

    df["car_age"] = CURRENT_YEAR - df["year"]
    
    df["mean_price_by_age"] = df.groupby("car_age")["selling_price"].transform("mean")

    df["mean_price_by_transmission"] = df.groupby("transmission")["selling_price"].transform("mean")
    df["median_price_by_transmission"] = df.groupby("transmission")["selling_price"].transform("median")

    return df