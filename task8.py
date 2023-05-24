import numpy as np

results = np.array([[4, 3, 5],
                   [3.5, 4.5, 2],
                   [4, 3.5, 3]])

pass_threshold = 3
total_students = results.shape[0]
total_tests = results.shape[1]

# Calculate the percentage share of students who passed the test
passed_students = np.count_nonzero(np.sum(results >= pass_threshold, axis=0) >= total_tests)
pass_percentage = (passed_students / total_students) * 100

# Calculate the average score for each test
average_scores = np.mean(results, axis=0)

print("Percentage of students who passed the test:", pass_percentage)
print("Average scores for each test:", average_scores)