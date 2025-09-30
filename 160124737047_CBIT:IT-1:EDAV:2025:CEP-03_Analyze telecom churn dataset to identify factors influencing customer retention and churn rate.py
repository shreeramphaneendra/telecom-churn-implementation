import pandas as pd
import platform
# Replace 'path_to_your_file.csv' with the actual path to your CSV file
file_path = '/Users/shreeramssp/Desktop/programming/python programs/churn-bigml-20.csv'

# Read the CSV file
data = pd.read_excel(file_path)

# Display the first few rows of the dataset
print(data.head())