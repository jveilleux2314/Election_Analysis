# The data we need to retrieve
# 1. the total number of votes cast
# 2. A complete list on candidates who received votes
# 3. the percentage of votes each candidiate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Add our dependencies

import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources" , "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    file_reader = csv.reader(election_data)

# Read and print header row so we can skip the first row to look at data
    headers = next(file_reader)
    print(headers)

# Print each row in the csv file.
    for row in file_reader:
            print(row)

    print(election_data)
# Close the file.
    election_data.close()

with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Hello World\n")
    txt_file.write("Counties in the Election\n\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
