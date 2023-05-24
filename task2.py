import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'Name': ['John', 'Jane', 'Mike', 'Lisa'],
    'Age': [25, 30, 28, 35],
    'Salary': [50000, 60000, 55000, 70000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Analyze data
average_age = df['Age'].mean()

# Present results in graphs
df.plot(x='Name', y='Age', kind='bar', title='Age')

plt.show()