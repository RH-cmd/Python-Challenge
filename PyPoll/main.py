#Import os and csv modules
import os
import csv

#Set path for file
election_data = os.path.join("Resources", "election_data.csv")

#Create a dictionary to hold the candidate names and the number of votes counted for each of them
candidate_to_num_votes = {}

#Set counter for the total number of votes cast
total_number_of_votes = 0

#Open election_data as a csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Read the header row first
    csv_header = next(csvfile)

    #Loop through each row 
    for row in csvreader:
        candidate = row[2]

        #Add votes to the counter
        total_number_of_votes += 1

        #Populate the variable candidate to num votes
        if candidate not in candidate_to_num_votes:
            candidate_to_num_votes[candidate] = 0
        candidate_to_num_votes[candidate] += 1

#Calculate the winner
winner = ""
winner_votes = 0

#Print election results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_number_of_votes)}")
print("-------------------------")
for candidate in candidate_to_num_votes:
    num_votes = candidate_to_num_votes[candidate]
    if num_votes > winner_votes:
        winner_votes = num_votes
        winner = candidate
    percentage_votes = num_votes/total_number_of_votes
    percentage_votes = "{:.3%}".format(percentage_votes)
    print(f"{candidate}: {num_votes}: {percentage_votes}")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

#Export/write results to a text file in the Analysis folder
output = open(f"Analysis/analysis_output.txt", "w")
output.write("Election Results")
output.write("\n")
output.write(f"-------------------------")
output.write("\n")
output.write(f"Total Votes: {str(total_number_of_votes)}")
output.write("\n")
output.write(f"-------------------------")
output.write("\n")
for candidate in candidate_to_num_votes:
    num_votes = candidate_to_num_votes[candidate]
    if num_votes > winner_votes:
        winner_votes = num_votes
        winner = candidate
    percentage_votes = num_votes/total_number_of_votes
    percentage_votes = "{:.3%}".format(percentage_votes)
    output.write(f"{candidate}: {num_votes}: {percentage_votes}\n")
output.write("-------------------------")
output.write("\n")
output.write(f"Winner: {str(winner)}")
output.write("\n")
output.write("-------------------------")
output.write("\n")
output.close()




        
    

        
