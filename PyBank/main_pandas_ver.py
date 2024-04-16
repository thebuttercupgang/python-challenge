# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period


# Your analysis should align with the following results:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

#import modules necessary to read csv
import os
import csv
import pandas as pd

#create path, syntax is weird bc windows is weird
path = os.path.join('C:\\', 'Users', '54qb3', 'Documents', 'python-challenge', 'PyBank', "Resources", "budget_data.csv")

budget_df = pd.read_csv(path)
budget_df.head

#results -- SO MUCH EASIER
budget_df.shape[0]
budget_df["Profit/Losses"].sum()
budget_df["Changes"] = budget_df["Profit/Losses"].diff()
budget_df["Changes"].mean()
budget_df["Changes"].max()
budget_df["Changes"].min()