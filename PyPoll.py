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
#set total votes to 0 so the loop starts at the top
total_votes = 0
# declare candidate list
candidate_options =[]
# create empty dictionary
candidate_votes = {}
#calculate winners
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    file_reader = csv.reader(election_data)

# Read and print header row so we can skip the first row to look at data
    headers = next(file_reader)

# make a loop to go through the data
    for row in file_reader:
        #add to toal vote count by 1
        total_votes += 1
        
    #print names
        candidate_name = row[2]
 
    #add names to list
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            # track votes per candidate
            candidate_votes[candidate_name] = 0
        #adding the votes per line
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n ")



        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

            winning_candidate_summary = (
            f"------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"   
            f"-------------------\n")
    print(winning_candidate_summary)
    # Close the file.
election_data.close()

with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Hello World\n")
    txt_file.write("Counties in the Election\n\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
