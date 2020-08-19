import pandas as pd

csv_file_path01 = 'E:\Sebnewrepo\Data/aisles.csv'
aisles = pd.read_csv(csv_file_path01)
print(aisles.head(5))