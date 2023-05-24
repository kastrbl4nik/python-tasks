import numpy as np

image = np.array([[50, 100, 150],
                  [75, 125, 200],
                  [25, 175, 225]])

# Calculate the minimum pixel value
min_value = np.min(image)

# Calculate the maximum pixel value
max_value = np.max(image)

# Calculate the average pixel value
average_value = np.mean(image)

print("Minimum value:", min_value)
print("Maximum value:", max_value)
print("Average value:", average_value)