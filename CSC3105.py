import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('UWB-LOS-NLOS-Dataset.csv')

# Step 2: Basic exploration
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nClass distribution:")
print(df['Class'].value_counts())

# Step 3: Visualize LOS vs NLOS distribution
plt.figure(figsize=(8, 5))
df['Class'].value_counts().plot(kind='bar')
plt.title('LOS vs NLOS Distribution')
plt.xlabel('Class (0=LOS, 1=NLOS)')
plt.ylabel('Count')
plt.show()