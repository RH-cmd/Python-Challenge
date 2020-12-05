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
    csv_header = next(csvreader)

    #Loop through each row of data after the header
    for row in csvreader:

        #Calculate the total number of months included on the dataset
            total_months.append(row[0])

        #Calculate the net total amount of "Profit/Losses"
            net_profit_and_loss.append(int(row[1]))

    #Iterate through the profit to calculate the changes in "Profit/Losses" over the entire period
    for i in range(len(net_profit_and_loss)-1):

    #Calculate the differences between each month and append it to the list
        monthly_profit_loss_change.append(net_profit_and_loss[i+1]-net_profit_and_loss[i])

    #Calculate the greatest increase and decrease in profits over the entire period
    greatest_increase_amount = max(monthly_profit_loss_change)
    greatest_decrease_amount = min(monthly_profit_loss_change)

    #To find the greatest increase and decrease in months, use the monthly change list and add 1 to denote the next month
    greatest_increase_month = monthly_profit_loss_change.index(max(monthly_profit_loss_change)) + 1
    greatest_decrease_month = monthly_profit_loss_change.index(min(monthly_profit_loss_change)) + 1 

# Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_profit_and_loss)}")
print(f"Average Change: {round(sum(monthly_profit_loss_change)/len(monthly_profit_loss_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_amount))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_amount))})")




       