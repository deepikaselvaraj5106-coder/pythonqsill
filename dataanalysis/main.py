import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv("students.csv")

# Display first few rows
print("Dataset Preview:")
print(data.head())

# Basic analysis
print("\nAverage Marks:")
print(data[['MATHS', 'SCIENCE', 'ENG']].mean())

# Bar chart for average marks
average_marks = data[['MATHS', 'SCIENCE', 'ENG']].mean()
average_marks.plot(kind='bar')
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# Scatter plot (Maths vs Science)
plt.scatter(data['MATHS'], data['SCIENCE'])
plt.title("Maths vs Science Marks")
plt.xlabel("Maths")
plt.ylabel("Science")
plt.show()

# Heatmap for correlation
plt.figure(figsize=(6,4))
sns.heatmap(data[['MATHS', 'SCIENCE', 'ENG']].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()