import os
import csv

budget_data_csv = os.path.join('Resources','budget_data.csv')
analysis_export = os.path.join('analysis', 'analysis.txt')

#read in the csv file    
with open(budget_data_csv, 'r') as csvfile:

    #split the columns on comma
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    header = next(csvfile,None)

    #define inital variable values
    rowcount = 0
    total = 0

    #define lists
    mnth = []
    val = []
    diff = []
    result = []
    
    #loop through rows to count rows and sum values
    for row in csvreader:
        val.append(int(row[1]))
        mnth.append(row[0])
        diff.append((val[len(val)-1])-(val[len(val)-2]))
        rowcount += 1  
        total += int(row[1])
    
    #determine month index corresponding to min/max profits
    maxdiffinx = diff.index(max(diff))
    mindiffinx = diff.index(min(diff))
    
    #print results to terminal
    print("")
    print("Financial Analysis")
    print("")
    print("----------------------------")
    print("")
    print(f"Total Months: {rowcount}")
    print("")
    print(f"Total: ${total}")
    print("")
    print(f"Average Change: ${round(sum(diff) / len(diff), 2)}")
    print("")
    print(f"Greatest Increase in Profits: {mnth[maxdiffinx]} (${max(diff)})")
    print("")
    print(f"Greatest Decrease in Profits: {mnth[mindiffinx]} (${min(diff)})")    
    
    #append results for export to text file
    result.append("")
    result.append("Financial Analysis")
    result.append("")
    result.append("----------------------------")
    result.append("")
    result.append(f"Total Months: {rowcount}")
    result.append("")
    result.append(f"Total: ${total}")
    result.append("")
    result.append(f"Average Change: ${round(sum(diff) / len(diff), 2)}")
    result.append("")
    result.append(f"Greatest Increase in Profits: {mnth[maxdiffinx]} (${max(diff)})")
    result.append("")
    result.append(f"Greatest Decrease in Profits: {mnth[mindiffinx]} (${min(diff)})")

#open text file
with open(analysis_export, 'w', newline='') as txtfile:
    
    #write each item in the results list to the text file
    for item in result:
        txtfile.write("%s\n" % item)
    
    #close the text file
    txtfile.close

