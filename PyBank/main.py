import os
import csv

budget_data_csv = os.path.join('Resources','budget_data.csv')
analysis_export = os.path.join('analysis', 'analysis.txt')

def average(numbers):
    #return sum(numbers) / len(numbers)
    length = len(numbers)-1
    num = 0.0
    for number in numbers:
        num += number
    return num / length

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

        #calculate change in profit/losses
        diff.append((val[len(val)-1])-(val[len(val)-2]))

        rowcount += 1  
        total += int(row[1])
    
    #determine month index corresponding to min/max profits
    maxdiffinx = diff.index(max(diff))
    mindiffinx = diff.index(min(diff))
    
    #print results to terminal
    print("")
    print("Financial Analysis\n")
    print("----------------------------\n")
    print(f"Total Months: {rowcount}\n")
    print(f"Total: ${total}\n")
    print(f"Average Change: ${round(average(diff), 2)}\n")
    print(f"Greatest Increase in Profits: {mnth[maxdiffinx]} (${max(diff)})\n")
    print(f"Greatest Decrease in Profits: {mnth[mindiffinx]} (${min(diff)})\n")    
    
    #append results for export to text file
    result.append("")
    result.append("Financial Analysis\n")
    result.append("----------------------------\n")
    result.append(f"Total Months: {rowcount}\n")
    result.append(f"Total: ${total}\n")
    result.append(f"Average Change: ${round(average(diff), 2)}\n")
    result.append(f"Greatest Increase in Profits: {mnth[maxdiffinx]} (${max(diff)})\n")
    result.append(f"Greatest Decrease in Profits: {mnth[mindiffinx]} (${min(diff)})\n")

#open text file
with open(analysis_export, 'w', newline='') as txtfile:
    
    #write results text file
    for item in result:
        
        #write each result on a new line (https://pynative.com/python-write-list-to-file/)
        txtfile.write("%s\n" % item)
    
    #close the text file
    txtfile.close

