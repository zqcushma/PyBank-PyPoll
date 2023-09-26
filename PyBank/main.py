import pandas as pdr
 
#filepath is hardcoded due to issues with writing a relative reference
filePath = "D:/Desktop/Data Analytics Work/Week 3/PyBank-PyPoll/PyBank/Resources/budget_data.csv"
data = pdr.read_csv(filePath)

#total months in set
totalMonths = len(data["Date"])
row = 0
bigHigh = ["", 0]
bigLow = ["", 0]

totalChange = sum(data["Profit/Losses"])
averageChange = totalChange/len(data["Profit/Losses"])
for dataPoint in data["Profit/Losses"]:
    
    #greatest increase in price
    if bigHigh[1] < dataPoint:
        bigHigh = [data["Date"][row], dataPoint]
    #greatest decrease in price
    if bigLow[1] > dataPoint:
        bigLow = [data["Date"][row], dataPoint]
    row += 1

    #changes in +/- over full period and the average of those changes
    #changes over the course of the period, with average given
    
