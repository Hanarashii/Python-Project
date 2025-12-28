import matplotlib.pyplot as plt

class CarDataVisualizer:
    def __init__(self, df):
        self.df = df
    def plot(self):
        self.df = self.df.plot()
        plt.show()