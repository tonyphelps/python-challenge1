
import os

# Module for reading CSV files
import csv
import numpy as np
# Initialize CSV file to be read, and text file to be writen to
BudgetCSV = os.path.join('budget_data.csv')

ResultsTXT = os.path.join('Financial_Results.txt')

ResultsTXT = open("Financial_Results.txt", "w")

# Open CSV file to analyze
with open(BudgetCSV, newline='') as csvfile:

    # Declare csvreader & delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    next(csvreader)

    # Delcare lists to be populated by csvreader for easy analysis/iterating through
    revenue = []
    date = []
    revenue_change = []

    inde = 0

    # Loop through rows of csvreader to populate/append the lists
    for row in csvreader:
     
        revenue.append(float(row[1]))
        date.append(row[0])

    # Print initial results
    print("Financial Analysis")
    print("Financial Analysis", file=ResultsTXT)
    print("------------------------------------------------")
    print("------------------------------------------------", file=ResultsTXT)
    print("Total Months:", len(date), file=ResultsTXT)
    print("Total Revenue: $", sum(revenue))
    print("Total Revenue: $", sum(revenue),file=ResultsTXT)

    # Loop through the range to find monthly revenue changes to average
    for i in range(1,len(date)):
    
        revenue_change.append(revenue[i] - revenue[i-1])   
        average_change = sum(revenue_change)/len(revenue_change)
        max_rev_change = max(revenue_change)
        min_rev_change = min(revenue_change)

        #grab index value of max & min values w/ numpy function
        inde_max = np.argmax(revenue_change)
        inde_min = np.argmin(revenue_change)

        #correct index to get month with greatest increase & decrease
        max_rev_change_date = str(date[inde_max + 1])
        min_rev_change_date = str(date[inde_min + 1])

    # Print averages of monthly revenue changes
    print("Average Revenue Change: $", int(average_change))
    print("Average Revenue Change: $", int(average_change),file=ResultsTXT)
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")",file=ResultsTXT)
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")",file=ResultsTXT)
    #print(revenue_change)

