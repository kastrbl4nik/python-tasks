import pandas as pd
import matplotlib.pyplot as plt

# Read sample data from data.csv
data = pd.read_csv('res/data.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Analyze data
max_salary = df['Salary'].max()

# Present results in graphs
df.plot(x='Name', y='Salary', kind='bar', title='Salary')

plt.show()