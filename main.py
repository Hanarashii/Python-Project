from src.data_ingestor import DataIngestor
from src.data_loader import load_csv_dataframe
from src.data_cleaner.Validate import validate
from src.data_cleaner.Clean import clean_data
from src.data_cleaner.Transform import transform_data
from src.data_visualizer.visualizer import run_all

def main():
    #This part handles download data
    kaggle_path = "nehalbirla/vehicle-dataset-from-cardekho"
    ingestor = DataIngestor(kaggle_path)
    ingestor.data_downloader()

    #Load data and validate it
    download_path = f"./downloads/datasets/{kaggle_path}"
    raw_data = load_csv_dataframe(download_path)
    validate(raw_data)

    #Clean and transform the data
    cleaned_data = clean_data(raw_data)
    transform_data(cleaned_data)
    run_all(cleaned_data)


if __name__ == '__main__':
    main()