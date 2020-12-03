#Import os and csv modules
import os
import csv

#Set path for file
election_data = os.path.join("Resources", "election_data.csv")

#Create lists to hold data for candidate names, number of votes for each candidate, and total percentage of votes for each candidate
candidate_names = []
number_of_votes = []
percentage_of_votes = []

#Set counter for the total number of votes
total_number_of_votes = 0

#Open election_data as a csv file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Read the header row first
    csv_header = next(csvfile)

    #Loop through each row 
    for row in csvreader:

        #Add votes to the counter
        total_number_of_votes += 1

        #Complete list of canidates who recieved votes by adding names to our list as they occur as well their vote count
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            index = candidate_names.index(row[2])
            number_of_votes.append(1)
        
        else:
            index = candidate_names.index(row[2])
            number_of_votes[index] += 1

        #Calculate the percentage of votes each candidate won and format to 3 decimal place for percentage
        for votes in number_of_votes:
            percentage = (round(votes/total_number_of_votes) * 100)
            percentage = "{:.3%}".format(percentage)
            percentage_of_votes.append(percentage)

        
