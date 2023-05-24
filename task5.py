import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample meteorological data
temperature_data = np.array([[25, 23, 26, 24, 28, 27, 26],
                            [21, 20, 22, 23, 19, 20, 21],
                            [18, 17, 19, 16, 17, 18, 20]])

humidity_data = np.array([[70, 75, 68, 72, 65, 67, 70],
                         [62, 64, 61, 63, 59, 58, 61],
                         [55, 57, 58, 53, 56, 54, 60]])

# Calculate average temperature and humidity at different altitudes
average_temperature = np.mean(temperature_data)
average_humidity = np.mean(humidity_data)

# Create a DataFrame using Pandas
altitude_labels = ['0m', '500m', '1000m']
data = {'Temperature': average_temperature, 'Humidity': average_humidity}
df = pd.DataFrame(data, index=altitude_labels)

print(df)

# Generate a graph
df.plot(kind='bar')
plt.xlabel('Altitude')
plt.ylabel('Average Value')
plt.title('Average Temperature and Humidity at Different Altitudes')
plt.show()