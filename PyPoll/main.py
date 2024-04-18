#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# Your analysis should align with the following results:
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------


#import modules necessary to read csv
import os
import csv

total_votes, candidates = [], []
candidate1, candidate2, candidate3 = [], [], []

##read csv
path = os.path.join('C:\\', 'Users', '54qb3', 'Documents', 'python-challenge', 'PyPoll', "Resources", "election_data.csv")

with open(path, mode="r") as election:
    ## place csv into csvreader
    csvreader = csv.reader(election, delimiter=',')

    ## Read the header row first
    csv_header = next(election)
    ## checking that its right
    print(f"Header: {csv_header}")

    ##all the rows after the header
    for row in csvreader:
        total_votes.append(row[0])
        row[2] = str(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == candidates[0]:
            candidate1.append(row[0]),
        elif row[2] == candidates[1]:
            candidate2.append(row[0])
        else:
            candidate3.append(row[0])

print(candidates)

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

file = open("analysis.txt", "w")
file.write(f"Total Votes: {len(total_votes)}")
file.write("\n" + f"Candidates: {candidates}")
file.write("\n" + f"{candidates[0]} won {len(candidate1) / len(total_votes): .3%} of the vote, {len(candidate1)} votes")
file.write("\n" + f"{candidates[1]} won {len(candidate2) / len(total_votes): .3%} of the vote, {len(candidate2)} votes")
file.write("\n" + f"{candidates[2]} won {len(candidate3) / len(total_votes): .3%} of the vote, {len(candidate3)} votes")
file.write("\n" + f"Winner: {candidates[1]}")
file.close()
