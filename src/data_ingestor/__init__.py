import os
import kagglehub

class DataIngestor:
    def __init__(self, path):
        self.path = path
    def data_downloader(self):
        if not os.path.exists("./downloads"):
            os.mkdir("./downloads")
            os.environ["KAGGLEHUB_CACHE"] = "./downloads"
            path = kagglehub.dataset_download(self.path)
            print(f"Dataset downloaded: {path}")
        else:
            return