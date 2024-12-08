import pandas as pd
import numpy as np

# Create a series of 10 random integers between 1 and 50
random_series = pd.Series(np.random.randint(1, 51, size=10))

# Display the series
print("Random Series:")
print(random_series)

# Display some basic statistics
print("\nBasic Statistics:")
print(f"Mean: {random_series.mean():.2f}")
print(f"Minimum: {random_series.min()}")
print(f"Maximum: {random_series.max()}")
print(f"Standard Deviation: {random_series.std():.2f}")

# Sort the series
print("\nSorted Series:")
print(random_series.sort_values())

# Calculate and display percentages
total_sum = random_series.sum()
percentages = (random_series / total_sum * 100).round(2)
print("\nPercentages of Total:")
for i in range(len(random_series)):
    print(f"Value {random_series[i]}: {percentages[i]}%")

# Create a combined series with values and their percentages
combined_series = pd.DataFrame({
    'Value': random_series,
    'Percentage': percentages
})
print("\nCombined Statistics:")
print(combined_series)
