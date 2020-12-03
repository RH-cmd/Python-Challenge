#Import os and csv modules
import os
import csv

#Set path for file
budget_path = os.path.join("Resources", "election_data.csv")

#Create lists to hold data for candidates, number of votes for each candidate, and total percentage of votes for each candidate
candidate_names = []
number_of_votes = []
percentage_of_votes = []
