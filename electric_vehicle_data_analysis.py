# Libraries for this Data Science project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Hardcoded file path
file_path = r"Electric_Vehicle_Population_Data.csv"

try:
    # Read the dataset
    data = pd.read_csv(file_path)
    print("\nDataset successfully loaded!")
except FileNotFoundError:
    print("Error: The file was not found at the specified path. Please check the file path and try again.")
    exit()
except OSError as e:
    print(f"Error: {e}")
    exit()

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Display the shape of the dataset
print("\nShape of the dataset (rows, columns):")
print(data.shape)

# Display basic information about the dataset
print("\nDataset Info:")
data.info()

# Display column-wise summary statistics
print("\nSummary Statistics:")
print(data.describe(include='all'))

# Check for missing values
print("\nMissing Values per Column:")
print(data.isnull().sum())

# Display the total size of the dataset
print("\nTotal Size of the Dataset:")
print(f"{data.size} elements (rows × columns)")

# Display the column names
print("\nColumn Names:")
print(list(data.columns))

# Optional: Display the first 50 rows
print("\nFirst 50 rows of the dataset:")
print(data.head(50))

# Checking for missing data 
print("\nIdentifying columns with missing values and their proportions:")
print(data.isnull().sum())
print(data.isnull().mean() * 100)  # Percentage of missing values

# Previewing the Data: 
print(data.head())
print(data.tail())

# List all column names
print("Column Names:")
print(data.columns.tolist())

# Identify and remove duplicate rows based on VIN, City, State, and Postal Code
print("\nCleaning rows with duplicate VINs where City, State, and Postal Code match...")

# Drop duplicates and keep the first occurrence
cleaned_data = data.drop_duplicates(subset=['VIN (1-10)', 'City', 'State', 'Postal Code'], keep='first')

print(f"Number of rows before cleaning: {data.shape[0]}")
print(f"Number of rows after cleaning: {cleaned_data.shape[0]}")

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(cleaned_data.describe())

# Bar chart: Most common vehicle makes
plt.figure(figsize=(12, 6))
cleaned_data['Make'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Vehicle Makes', fontsize=16)
plt.xlabel('Make')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

