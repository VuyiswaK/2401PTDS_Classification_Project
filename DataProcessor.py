import pandas as pd
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self, csv_files, test_size=0.2, random_seed=42):
        """
        Initializes the DataProcessor with a list of CSV files, test set size, and random seed.

        :param csv_files: List of paths to CSV files.
        :param test_size: Proportion of the dataset to include in the test split.
        :param random_seed: Seed used by the random number generator.
        """
        self.csv_files = csv_files
        self.test_size = test_size
        self.random_seed = random_seed
        self.data = None
        self.train_df = None
        self.test_df = None

    def load_and_concatenate(self):
        """
        Loads and concatenates the CSV files into a single DataFrame.
        """
        df_list = [pd.read_csv(file) for file in self.csv_files]
        self.data = pd.concat(df_list, ignore_index=True)

    def split_data(self):
        """
        Splits the data into training and testing sets.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_and_concatenate() first.")
        
        self.train_df, self.test_df = train_test_split(
            self.data, test_size=self.test_size, random_state=self.random_seed, 
            stratify=self.data['category']
        )

    def get_splits(self):
        """
        Returns the training and testing DataFrames.

        :return: A tuple (train_df, test_df) containing the training and testing splits.
        """
        if self.train_df is None or self.test_df is None:
            self.process()
        
        return self.train_df, self.test_df

    def process(self):
        """
        Executes the full data processing pipeline: loading, concatenating, and splitting the data.
        """
        self.load_and_concatenate()
        self.split_data()


