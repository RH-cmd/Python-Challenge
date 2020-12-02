#Import os and csv modules
import os
import csv

#Set path for file
budget_path = os.path.join("Resources", "budget_data.csv")

#Set variables 
total_months = 0
total_profitlosses = 0

#Open budget_data as a csv file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Read the header row first
    csv_header = next(csvfile)

#Read through each row of data after the header
    for row in csvreader:


