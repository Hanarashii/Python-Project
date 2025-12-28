from src.user_interface import App
from src.data_ingestor import DataIngestor
from src.data_loader import load_csv_dataframe
from src.data_cleaner import CarDataCleaner

def main():
    #This part handles download data
    kaggle_path = "nehalbirla/vehicle-dataset-from-cardekho"
    ingestor = DataIngestor(kaggle_path)
    ingestor.data_downloader()

if __name__ == '__main__':
    main()