import pandas as pd

#Làm sạch dữ liệu
def cleanData(df: pd.DataFrame):
    df = df.copy()

    df = df.drop_duplicates()
    df = df.dropna()
    #Xóa các cột không cần thiết
    df = df.drop(columns = ["name", "seller_type", "owner"], errors = "ignore")

    #Clean cột mileage
    df["mileage"] = (df["mileage"].astype(str).str.replace("kmpl", "", case = False)
                     .str.replace("km/kg", "", case = False).str.strip())
    df["mileage"] = pd.to_numeric(df["mileage"], errors = "coerce")
    
    #Clean cột engine
    df["engine"] = (df["engine"].astype(str).str.replace("cc", "", case = False).str.strip())
    df["engine"] = pd.to_numeric(df["engine"], errors = "coerce")

    #Clean cột max_power
    df["max_power"] = (df["max_power"].astype(str).str.replace("bhp", "", case = False).str.strip())
    df["max_power"] = pd.to_numeric(df["engine"], errors = "coerce")

    #Clean cột torque
    df["torque"] = df["torque"].astype(str).str.extract(r"(\d+\.?\d*)")[0].astype(float)

    #Clean cột seats
    df["seats"] = df["seats"].astype(float)

    #Đồng bộ kiểu dữ liệu các cột
    df["selling_price"] = df["selling_price"].astype(float)
    df["year"] = df["year"].astype(float)
    df["km_driven"] = df["km_driven"].astype(float)

    return df

