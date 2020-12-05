#Import os and csv modules
import os
import csv

#Set path for file
budget_path = os.path.join("Resources", "budget_data.csv")

#Set variables for total months and net profit and loss
total_months = 0
net_profit_and_losses = 0

#Set counter and lists to calculate average monthly change in profit
previous_profit = 0
change_in_month = []
change_in_profit_list = []

#Create variables for greatest increase and decrease amounts
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]

#Open budget_data as a csv file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Read the header row first
    csv_header = next(csvfile)

#Loop through each row of data after the header
    for row in csvreader:

        #Calculate the total number of months included on the dataset
        total_months = total_months + 1

        #Calculate the net total amount of "Profit/Losses"
        net_profit_and_losses = net_profit_and_losses + int(row[1])

        #Calculate the changes in "Profit/Losses" over the entire period
        profit_difference = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        change_in_profit_list = change_in_profit_list + [profit_difference]
        change_in_month = change_in_month + [int(row[0])]

        #Calculate the greatest increase (date and amount) in profits
        if (profit_difference > greatest_increase[1]):
            greatest_increase[0] = int(row[0])
            greatest_increase[1] = profit_difference

        #Calculate the greatest decrease (date and amount) in losses
        if (profit_difference < greatest_decrease[1]):
            greatest_decrease[0] = int(row[0])
            greatest_decrease[1] = profit_difference

#Calculate the average monthly change
profit_change_average = sum(change_in_profit_list) / len(change_in_profit_list)

#Print Financial Analysis
print("Financial Analysis")
print(f"-------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit_and_losses}")
print(f"Average Change: ${profit_change_average}")
print(f"Greatest Increase in Revenue: {greatest_increase[0]}  (${greatest_increase[1]})")
print(f"Greatest Decrease in Revenue: {greatest_decrease[0]}  (${greatest_decrease[1]})")


# f"\nFinancial Analysis\n"
# f"-----------------------------\n"
# f"Total Months:  {total_months}\n"
# f"Total:  ${net_profit_and_losses}\n"
# f"Average Change: ${profit_change_average}\n"
# f"Greatest Increase in Revenue: {greatest_increase[0]}  (${greatest_increase[1]})\n"
# f"Greatest Decrease in Revenue: {greatest_decrease[0]}  (${greatest_decrease[1]})\n"

# #Exporting/writing analysis results to a text file
# output = open("output.txt", "w")







