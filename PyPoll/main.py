import os
import csv

election_data_csv = os.path.join('PyPoll','Resources','election_data.csv')
analysis_export = os.path.join('PyPoll','analysis', 'analysis.txt')

with open(election_data_csv, 'r') as csvfile:

    #split the columns on comma
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    header = next(csvfile,None)

    #define inital variable values
    rowcount = 0

    #define lists
    cand = []

    #append unique values to list (https://stackoverflow.com/questions/24441606/how-to-create-a-list-in-python-with-the-unique-values-of-a-csv-file)
    for row in csvreader:
        if row[2] not in cand:
            cand.append(row[2])
        rowcount += 1
 

    print("")
    print("Election Results\n")
    print("----------------------------\n")
    print(f"Total Votes: {rowcount}\n")
    print("----------------------------\n")

    for can in range(len(cand)):
        print(f"{can} {cand[can]}:\n")

    print("----------------------------\n")
    print(f"Winniner: \n")
    print("----------------------------\n")
