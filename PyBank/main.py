# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#----------------------------------------------------------------------------------------

#import modules necessary to read csv
import os
import csv

##read csv
path = os.path.join('C:\\', 'Users', '54qb3', 'Documents', 'python-challenge', 'PyBank', "Resources", "budget_data.csv")

#create lists to hold the values:
months = []
profits = []
changes = []

##making it readable
with open(path, mode="r") as budget:
    ## place csv into csvreader
    csvreader = csv.reader(budget, delimiter=',')

    ## Read the header row first
    csv_header = next(budget)
    ## checking that its right
    print(f"Header: {csv_header}")

    #need this for changes list
    prev = 0
    ##all the rows after the header
    for row in csvreader:
        row[1] = int(row[1])
        months.append(row[0])
        profits.append(row[1])
        #storing the differences in changes
        changes.append(row[1] - prev)
        prev = row[1]

#pop off the inital value bc it's not a difference
#find the index of the min and max values to pull from Date list
    #this is honestly bulky, but i don't think we're supposed to do this pandas
del changes[0]
max_index = changes.index(max(changes))
min_index = changes.index(min(changes))

#okay results now, exporting to .txt file

file = open("analysis.txt", "w")
file.write(f'Total Months: {len(months)}')
file.write("\n" + f'Total: {sum(profits)}')
file.write("\n" + f'Average Change: {sum(changes) / len(changes)}')
file.write("\n" + f'Greatest Increase in Profits: {max(changes)} on {months[max_index]}')
file.write("\n" + f'Greatest Decrease in Profits: {min(changes)} on {months[min_index]}')
file.close()