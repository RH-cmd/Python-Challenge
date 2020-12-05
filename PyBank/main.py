#Import os and csv modules
import os
import csv

#Set path for file
budget_path = os.path.join("Resources", "budget_data.csv")

#Set variables for total months and net profit and loss
total_months = []
net_profit_and_loss = []
monthly_profit_loss_change = []

#Open budget_data as a csv file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Read the header row first
csv_header = next(csvfile)

#Loop through each row of data after the header
    for row in csvreader:

        #Calculate the total number of months included on the dataset
        total_months.append(row[0])

        #Calculate the net total amount of "Profit/Losses"
        net_profit_and_loss.append(int(row[1]))

    #Iterate through the profit to calculate the changes in "Profit/Losses" over the entire period
    for i in range(len(net_profit_and_loss)-1):

       