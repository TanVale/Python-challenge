import os
import csv 

election_data = os.path.join("..", "Resources", "election_data.csv")
Output_data = os.path.join("..", "Analysis", "election_analysis.txt")
#Setting variables
Total_Votes = 0
candidate_names = []
candidate_votes = {}
winner = 0 
winner_name = ""

with open(election_data,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        Total_Votes += 1
        Candidates = row[2]
        if Candidates not in candidate_names:
            candidate_names.append(Candidates)
            candidate_votes[Candidates] = 0
        candidate_votes[Candidates] += 1


# Find the winner
#winner = candidate_votes[Candidates]
with open(Output_data, 'w') as txt_file:

# Print the results

    Vote_data = f"""
Election Results
-------------------------
Total Votes: {Total_Votes}
-------------------------
"""
    print(Vote_data)
    txt_file.write (Vote_data)
    # Print the percentage of votes and total votes for each candidate
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentage = (votes / Total_Votes) * 100
        if votes > winner :
            winner = votes 
            winner_name = candidate
        candidate_results =  (f"{candidate}: {percentage:.3f}% ({votes})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    winning_candidate = f"""
-------------------------
Winner: {winner_name}
-------------------------
"""
    print(winning_candidate)
    txt_file.write(winning_candidate)