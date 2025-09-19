# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# For reproducibility of Seaborn style
sns.set(style="whitegrid")

# Load dataset (Iris example from seaborn)
try:
    df = sns.load_dataset("iris")   # You can also use pd.read_csv("yourfile.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Dataset file not found. Please check the file path.")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Info about dataset
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# (If missing values exist: fill or drop)
df = df.dropna()   # or df.fillna(method='ffill')

# Task 2: Basic Data Analysis
print("\nSummary Statistics:")
print(df.describe())

# Grouping: average petal length per species
grouped = df.groupby("species")["petal_length"].mean()
print("\nAverage Petal Length by Species:")
print(grouped)

# Task 3: Data Visualization

# 1. Line chart (using cumulative petal length to simulate time series trend)
df["cum_petal_length"] = df["petal_length"].cumsum()
plt.figure(figsize=(8,5))
plt.plot(df.index, df["cum_petal_length"], label="Cumulative Petal Length", color="purple")
plt.title("Line Chart - Cumulative Petal Length Trend")
plt.xlabel("Index (simulated time)")
plt.ylabel("Cumulative Petal Length")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal_length", data=df, palette="viridis", ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length")
plt.show()

# 3. Histogram of sepal length
plt.figure(figsize=(6,4))
plt.hist(df["sepal_length"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram - Sepal Length Distribution")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - Sepal length vs Petal length
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="deep")
plt.title("Scatter Plot - Sepal vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title="Species")
plt.show()