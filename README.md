# Python Challenge

## Background

* Create a new repository for this project called `python-challenge`.

* Clone the new repository to your computer.

* Inside the local git repository, create a directory for each Python Challenge. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder just created, add the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A "Resources" folder contains the CSV files used. 
  * An "analysis" folder that contains a text file that has the results from the analysis.


## PyBank


* In this challenge, create a Python script that analyzes the financial records of your company. We will be using financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, the final script will both print the analysis to the terminal and export a text file with the results in the Analysis folder.

## PyPoll


* In this challenge, we are tasked with helping a small, rural town modernize its vote counting process.

* We will use a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, the final script will both print the analysis to the terminal and export a text file with the results in the Analysis folder.
