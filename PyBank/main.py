import csv
 
#filepath is hardcoded due to issues with writing a relative reference
readFilePath = "D:/Desktop/Data Analytics Work/Week 3/PyBank-PyPoll/PyBank/Resources/budget_data.csv"
writeFilePath = "D:/Desktop/Data Analytics Work/Week 3/PyBank-PyPoll/PyBank/analysis/results.txt"
#filePath = 'Resources/budget_data.csv'
#row 0 is header, each row after is an entry into the table
totalMonths = 0
totalChange = 0
bigHigh = ["", 0]
bigLow = ["", 0]
plList = []
with open(readFilePath) as file:
    line = 0
    headers = next(file)
    reader = csv.reader(file, delimiter=',')
    for row in reader:

        totalMonths += 1.0
        #print(row[1])
        totalChange += int(row[1])
        #greatest increase in price
        if int(bigHigh[1]) < int(row[1]):
            bigHigh = [row[0], row[1]]
        #greatest decrease in price
        if int(bigLow[1]) > int(row[1]):
            bigLow = [row[0], row[1]]
        plList.append(row[1])
            

#THIS PORTION MAY BE WRONG, UNKNOWN WHAT IS REQUIRED HERE
averageChange = 0.0
changes = [0]
for entry in plList:
    prevEntry = plList.index(entry) - 1
    if prevEntry < 0:
        continue
    else:
        changes.append(float(entry) - float(plList[prevEntry]))

averageChange = round(sum(changes)/len(changes),2)

output = f"Financial Analysis\n----------------------------\nTotal Months: {totalMonths}\nTotal: ${totalChange}\nAverage Change: ${averageChange}\nGreatest Increase in Profits: {bigHigh[0]} with ${bigHigh[1]}\nGreatest Decrease in Profits: {bigLow[0]} with ${bigLow[1]}"
print(output)

with open(writeFilePath, 'w') as file:
    file.write(output)