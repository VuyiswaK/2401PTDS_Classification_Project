from DataProcessor import DataProcessor
import pandas as pd
import os

csv_files = ['Data/raw/business_data.csv', 'Data/raw/education_data.csv', 'Data/raw/entertainment_data.csv',
              'Data/raw/sports_data.csv', 'Data/raw/technology_data.csv']
processor = DataProcessor(csv_files, test_size=0.2, random_seed=42)
train_df, test_df = processor.get_splits()

print(train_df.head())
print(test_df.head())

processed_data_file_path = "Data/processed"
if not os.path.exists(processed_data_file_path):
    os.makedirs(processed_data_file_path)

# save train and test csv files
train_df.to_csv("Data/processed/train.csv")
test_df.to_csv("Data/processed/test.csv")

