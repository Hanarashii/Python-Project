from Src.Data import *

#Chạy pipline
def main():
    path = "Data/Car details v3.csv"

    df = loadData(path)

    reports_before = validate(df)
    print("Trước khi làm sạch:", reports_before)
    
    df_clean = cleanData(df)

    reports_after = validate(df_clean)
    print("Sau khi làm sạch:", reports_after)

    df_feat = transformData(df_clean)
    print("Đã hoàn tất biến đổi dữ liệu")

    output_path = "Data/processed.csv"
    df_feat.to_csv(output_path,mode = "w", index = False)
    print("Hoàn tất pipline")
if __name__ == "__main__":
    main()
