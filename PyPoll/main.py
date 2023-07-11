import os
import csv
from collections import defaultdict, Counter

election_data_csv = os.path.join('Resources','election_data.csv')
analysis_export = os.path.join('analysis', 'analysis_export.txt')

#lines 9, 14, 17-19, 22-31, sourced and adapted from (https://stackoverflow.com/questions/52012798/python3-dictionary-from-csv-file-to-count-frequency-of-words)
columns = defaultdict(list)

with open(election_data_csv, 'r') as csvfile:

    #read in csv to dictionary format
    reader = csv.DictReader(csvfile)

    #append csv to columns
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

    #define target column for list 
    candidate_list = columns['Candidate']

    #create empty list 
    candidate_list_clean = []

    #append candidates to the empty list 
    for cand in candidate_list:
        candidate_list_clean.append(cand)

    output = dict(Counter(candidate_list_clean)) 

    #sum the total votes
    total = sum(output.values())

    #create empty list for results
    result = []

    #print results to terminal and append to list for export to txt file
    print("")
    result.append("")
    print("Election Results\n")
    result.append("Election Results\n")
    print("----------------------------\n")
    result.append("----------------------------\n")
    print(f"Total Votes: {total}\n")
    result.append(f"Total Votes: {total}\n")
    print("----------------------------\n")
    result.append("----------------------------\n")

    #calculate percentage of votes per candicate (https://stackoverflow.com/questions/43084138/calculate-the-percentage-for-python-dictionary)
    for c, t in output.items():
        perc = round(t *100/total, 3)
        print(f"{c}: {perc}% ({t})\n")
        result.append(f"{c}: {perc}% ({t})\n")

    #determin candidate with the most votes (https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/)
    winner = max(zip(output.values(), output.keys()))[1]

    print("----------------------------\n")
    result.append("----------------------------\n")
    print(f"Winniner: {winner}\n")
    result.append(f"Winniner: {winner}\n")
    print("----------------------------\n")
    result.append("----------------------------\n")

#open text file
with open(analysis_export, 'w', newline='') as txtfile:
    
    #write each item in the results list to the text file
    for item in result:
        txtfile.write("%s\n" % item)
    
    #close the text file
    txtfile.close




