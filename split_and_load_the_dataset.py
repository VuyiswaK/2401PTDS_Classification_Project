from DataProcessor import DataProcessor
import pandas as pd
import os

random_seed = 42

csv_files = ['Data/raw/business_data.csv', 'Data/raw/education_data.csv', 'Data/raw/entertainment_data.csv',
              'Data/raw/sports_data.csv', 'Data/raw/technology_data.csv']
processor = DataProcessor(csv_files, test_size=0.2, random_seed=random_seed)
train_df, test_df = processor.get_splits()

print(train_df.head())
print(test_df.head())

processed_data_file_path = "Data/processed"
if not os.path.exists(processed_data_file_path):
    os.makedirs(processed_data_file_path)


class_counts = train_df['category'].value_counts().to_dict()
print(class_counts)
# Create a new DataFrame to hold the imbalanced training set
imbalanced_train_df = pd.DataFrame()

# Define imbalance ratios, for example, reduce class 0 to 50% and class 1 to 30% of their original sizes in the training set
imbalance_ratios = {"business": 0.7, 
                    "sports": 0.4, 
                    "entertainment": 0.6, 
                    "education":0.95,
                    "technology":0.8}

for class_label, ratio in imbalance_ratios.items():
    class_df = train_df[train_df['category'] == class_label]
    n_samples = int(ratio * class_counts[class_label])
    sampled_class_df = class_df.sample(n=n_samples, random_state=random_seed)
    imbalanced_train_df = pd.concat([imbalanced_train_df, sampled_class_df])

# # Assign the imbalanced DataFrame to the train_df
train_df = imbalanced_train_df
print(train_df.columns)
class_counts = train_df['category'].value_counts().to_dict()
print(class_counts)


# save train and test csv files
train_df.to_csv("Data/processed/train.csv", index=False)
test_df.to_csv("Data/processed/test.csv", index=False)

train_df = pd.read_csv("Data/processed/train.csv")

print(train_df.head())
print(train_df.columns)
class_counts = train_df['category'].value_counts().to_dict()
print(class_counts)