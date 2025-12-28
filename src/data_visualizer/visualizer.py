"""
Module: data_visualizer/visualizer.py

Mô tả:
    - Module này chứa các hàm dùng để trực quan hóa dữ liệu cho tập dữ liệu processed.csv
    - Phân tích các yếu tố ảnh hưởng đến giá xe:
        + Năm sản xuất
        + Loại nhiên liệu
        + Hộp số
        + Số km đã chạy
        + Mức tiêu hao nhiên liệu
        + Tuổi xe

Dùng cho dataset: processed.csv (Car details v3.csv đã clean)
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_price_distribution(df):
    """Vẽ biểu đồ Histogram để xem phân bố giá xe trên số lượng"""
    plt.figure(figsize=(8, 5)) 
    plt.hist(
        df['selling_price'], 
        bins = 20,
        edgecolor = 'black'
    )
    plt.title("Distribution of Selling Price")
    plt.xlabel("Selling Price")
    plt.ylabel("Number of Vehicles")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_price_by_year(df):
    """Vẽ biểu đồ Scatter plot để xem mối quan hệ giữa Năm sản xuất và Giá bán"""
    plt.figure(figsize=(8, 5))
    plt.scatter(
        df['year'], 
        df['selling_price'], 
        alpha=0.6
    )
    avg_price_by_year = df.groupby('year')['selling_price'].mean() 
    plt.plot(
        avg_price_by_year.index,
        avg_price_by_year.values
    )
    plt.title('Selling Price by Manufacturing Year')
    plt.xlabel('Year')
    plt.ylabel('Selling Price')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot_vehicle_count_by_fuel(df):
    """Vẽ biểu đồ Bar chart để thống kê số lượng xe theo loại nhiên liệu (Xăng, Dầu, CNG)"""
    fuel_counts = df['fuel'].value_counts() 
    plt.figure(figsize=(7, 5))
    plt.bar(
        fuel_counts.index,
        fuel_counts.values
    )
    plt.title("Number of Vehicles by Fuel Type")
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Vehicles")
    plt.grid(axis='y', linestyle='--', alpha = 0.7)
    plt.tight_layout()
    plt.show()


def plot_price_by_transmission(df):
    """Vẽ biểu đồ Bar chart để so sánh giá xe giữa xe số sàn và số tự động"""
    avg_price = df.groupby("transmission")["selling_price"].mean() 
    plt.figure()
    avg_price.plot(kind="bar")
    plt.xlabel("Transmission Type")
    plt.ylabel("Average Selling Price")
    plt.title("Average Selling Price by Transmission Type")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_kms_vs_price(df):
    """Vẽ biểu đồ Scatter plot để kiểm tra ảnh hưởng của số Km đã chạy đến giá bán"""
    plt.figure()
    plt.scatter(df["km_driven"], df["selling_price"], alpha = 0.5) 
    plt.xlabel("Kilometers Driven") 
    plt.ylabel("Selling Price")
    plt.title("Kilometers Driven vs Selling Price")
    plt.tight_layout()
    plt.show()


def plot_price_vs_mileage(df):
    """Vẽ biểu đồ đường: Giá bán trung bình theo Mức tiêu hao nhiên liệu"""
    plt.figure(figsize=(8, 5))
    avg_price_mileage = df.groupby(df['mileage'].round())['selling_price'].mean()
    
    plt.plot(avg_price_mileage.index, avg_price_mileage.values, color='green', marker='o', linewidth=2)
    plt.title("Average Selling Price by Mileage")
    plt.xlabel("Mileage (km/l)")
    plt.ylabel("Average Selling Price")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_price_by_car_age(df):
    """Vẽ biểu đồ cột: Giá bán trung bình theo Tuổi xe"""
    plt.figure(figsize=(10, 5))
    avg_price_age = df.groupby('car_age')['selling_price'].mean()
    
    plt.bar(avg_price_age.index, avg_price_age.values, color='orange', edgecolor='darkorange')
    plt.title("Average Selling Price by Car Age")
    plt.xlabel("Car Age (Years)")
    plt.ylabel("Average Selling Price")
    plt.xticks(avg_price_age.index)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("processed.csv")
    plot_price_distribution(df)
