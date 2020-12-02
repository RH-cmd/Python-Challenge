#Import os and csv modules
import os
import csv

#Set path for file
budget_path = os.path.join("Resources", "budget_data.csv")

#Set variables 
total_months = 0
total_profit_and_losses = 0


#Open budget_data as a csv file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Read the header row first
    csv_header = next(csvfile)

#Loop through each row of data after the header
    for row in csvreader:

        #Calculate the total number of months included on the dataset
        total_months += 1

        #Calculate the net total amount of "Profit/Losses"
        total_profit_and_losses = total_profit_and_losses + int(row["Profit/Losses"])

        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

        #Calculate the greatest increase in profits

        #Calculate the greatest decreases in losses

#Exporting/writing analysis results to a text file
output = open("output.txt", "w")







