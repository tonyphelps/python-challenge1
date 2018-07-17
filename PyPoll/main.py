
import os

# Module for reading CSV files
import csv

# Initialize CSV file to be read, and text file to be writen to
PollingCSV = os.path.join('election_data.csv')

ResultsTXT = os.path.join('Election_Results.txt')

ResultsTXT = open("Election_Results.txt", "w")

# Open CSV file to analyse
with open(PollingCSV, newline='') as csvfile:

    # Declare csvreader
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    next(csvreader)

    # Delcare lists and dictionary to be populated by csvreader for easy analysis/iterating through
    VoterID = []
    county = []
    candidates = []
    results = {}
    votes = 0

    # Loop through rows of csvreader to populate/append the lists
    for row in csvreader:

        VoterID.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # Count the votes
    for votes in candidates:
        results[votes] = results.setdefault(votes,0) +1

    # Declare variables to be counted/formated in results
    total_votes = len(candidates)            
    Khan_percentage = '{:.1%}'.format(candidates.count("Khan") / total_votes)
    Correy_percentage = '{:.1%}'.format(candidates.count("Correy") / total_votes)
    Li_percentage = '{:.1%}'.format(candidates.count("Li") / total_votes)
    OTooley_percentage = '{:.1%}'.format(candidates.count("O'Tooley") / total_votes)

    # Find the dictionary key with the most votes to delare winner
    max_value = max(results.items(), key = lambda x: x[1])

# Print out the results and write to TXT file
print("Election Results")
print("Election Results",file=ResultsTXT)
print("------------------------------------------------")
print("------------------------------------------------",file=ResultsTXT)
print("Total votes:", total_votes)
print("Total votes:", total_votes, file=ResultsTXT)
print("------------------------------------------------")
print("------------------------------------------------", file=ResultsTXT)
print("Candidates:", sorted(results))
print("Candidates:", sorted(results), file=ResultsTXT)
print("------------------------------------------------")
print("------------------------------------------------", file=ResultsTXT)
print("Khan:", Khan_percentage, (candidates.count("Khan")))
print("Khan:", Khan_percentage, (candidates.count("Khan")), file=ResultsTXT)
print("Li:", Correy_percentage, (candidates.count("Li")))
print("Li:", Correy_percentage, (candidates.count("Li")), file=ResultsTXT)
print("Correy:", Li_percentage, (candidates.count("Correy")))
print("Correy:", Li_percentage, (candidates.count("Correy")), file=ResultsTXT)
print("O'Tooley:", OTooley_percentage, (candidates.count("O'Tooley")))
print("O'Tooley:", OTooley_percentage, (candidates.count("O'Tooley")), file=ResultsTXT)
print("------------------------------------------------")
print("------------------------------------------------", file=ResultsTXT)
print("The Winner is:", max_value)
print("The Winner is:", max_value, file=ResultsTXT)
print("------------------------------------------------")
print("------------------------------------------------", file=ResultsTXT)



