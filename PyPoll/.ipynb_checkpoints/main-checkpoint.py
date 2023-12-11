import os
import csv 

election_data = os.path.join("..", "Resources", "election_data.csv")

#set variables
def summary (election_data):
     
votes= 0
candidates =[]
Percentage_of_Votes = 0
Total_votes_per_candidate = 0
Popular_Vote = ""

with open(election_data,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    Total_votes += 1


