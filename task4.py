import pandas as pd
import matplotlib.pyplot as plt

# Read sample data from data.csv
data1 = pd.read_csv('res/data.csv')
data2 = {
    'Name': ['John', 'Jane', 'Mike', 'Sarah'],
    'Department': ['IT', 'IT', 'HR', 'Marketing']
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df_merged = df1.join(df2.set_index('Name'), on='Name')

# Analyze data
employee_count = df_merged.groupby('Department').size()

# Present results in graphs
employee_count.plot(kind='bar', title='Number of Employees in Each Department')

plt.show()