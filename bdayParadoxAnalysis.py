import pandas as pd
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt

# Load the first DataFrame from a CSV file and rename it as 'nba_data'
nba_data = pd.read_csv('nba.csv')

# Load the second DataFrame from a CSV file and rename it as 'nfl_data'
nfl_data = pd.read_csv('nfl.csv')

# Remove rows with missing values in the 'date_of_birth' column in the 'nfl_data' DataFrame
nfl_data.dropna(subset=['date_of_birth'], inplace=True)

# Rename the 'Birth Date' column to 'Birth Date' and format date in 'nba_data'
nba_data['Birth Date'] = pd.to_datetime(nba_data['Birth Date'], errors='coerce').dt.strftime('%m-%d')

# Rename the 'date_of_birth' column to 'Birth Date' and format date in 'nfl_data'
nfl_data['Birth Date'] = pd.to_datetime(nfl_data['date_of_birth'], format='%m/%d/%Y', errors='coerce').dt.strftime('%m-%d')

# Concatenate the two DataFrames into a new DataFrame called 'combined_data'
combined_data = pd.concat([nba_data, nfl_data], ignore_index=True)

# Initialize a list to store different group sizes for the birthday paradox analysis
total_group_sizes = []
current_size = 460  # Setting the initial size for the texting group

# Generate group sizes to be analyzed until it's less than 6831
while current_size < 6831:
    total_group_sizes.append(current_size)
    current_size += 23

# Initialize a list to store the percentage of groups with shared birthdays for each group size
percentage_shared_list = []

# Loop through different group sizes
for total_group_size in total_group_sizes:
    count_shared_birthday = 0

    # Loop through the 'combined_data' DataFrame in groups of 23 people
    group_size = 23
    for i in range(0, total_group_size, group_size):
        group = combined_data[i:i + group_size]

        # Generate combinations of birth dates within the group
        birthday_pairs = list(combinations(group['Birth Date'], 2))

        # Check if there's at least one shared birthday in the group
        if any(bday1 == bday2 for bday1, bday2 in birthday_pairs):
            count_shared_birthday += 1

    # Calculate the percentage of groups with shared birthdays
    percentage_shared = (count_shared_birthday / (total_group_size / 23)) * 100
    percentage_shared_list.append(percentage_shared)


# Calculate the mean of the percentages
mean_percentage = sum(percentage_shared_list) / len(percentage_shared_list)

# Calculate the variance of the percentages
mean_square_diff = sum((percentage - mean_percentage) ** 2 for percentage in percentage_shared_list) / (len(percentage_shared_list) - 1)

# Output the results
print("Mean Percentage:", mean_percentage)
print("Variance:", mean_square_diff)

# Calculate the absolute error (positive values only) compared to the original mean (50.73%)
expected_probability = 50.73
error_list = [abs(mean_percentage - percentage) for percentage in percentage_shared_list]

# Create the first plot for Absolute Error
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(total_group_sizes, error_list, marker='o', linestyle='-', markersize=2)
plt.xlabel('Total People')
plt.ylabel('Absolute Error (%)')
plt.title('Absolute Error in Birthday Paradox Analysis')
plt.grid(True)

# Create the second plot for Percentage of Shared Birthdays
plt.subplot(2, 1, 2)
plt.plot(total_group_sizes, percentage_shared_list, marker='o', linestyle='-', markersize=2, label='Percentage of Shared Birthdays')
plt.axhline(y=expected_probability, color='red', linestyle='--', label='Expected Probability')
plt.axhline(y=mean_percentage, color='green', linestyle='--', label='Mean Percentage')
plt.xlabel('Total People')
plt.ylabel('Percentage')
plt.title('Percentage of Shared Birthdays in Birthday Paradox Analysis')
plt.grid(True)
plt.legend()

# Adjust spacing between the two plots
plt.tight_layout()

# Show the plots
plt.show()