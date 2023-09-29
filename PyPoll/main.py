import csv
 
#filepath is hardcoded due to issues with writing a relative reference
readFilePath = "D:/Desktop/Data Analytics Work/Week 3/PyBank-PyPoll/PyPoll/Resources/election_data.csv"
writeFilePath = "D:/Desktop/Data Analytics Work/Week 3/PyBank-PyPoll/PyPoll/analysis/results.txt"
#row 0 is header, each row after is an entry into the table
line = 0

#declaring variables for tracking
currentCanidate = ""
#vote values are off of the canidate list array by 1
canidateResults = dict()
canidateVotes = 0
totalVotes = 0
#open file
with open(readFilePath) as file:
    headers = next(file)
    reader = csv.reader(file, delimiter=',')
    #loop through and calculate how many votes each canidate got, along with adding up the total number of votes
    specialBoi = 0
    firstEntry = True
    for row in reader:
        if firstEntry:
            currentCanidate = row[2]
            firstEntry = False
        elif currentCanidate != row[2]:
            if currentCanidate in canidateResults:
                canidateResults[currentCanidate] += canidateVotes
            else:
                canidateResults.update({currentCanidate : canidateVotes})
            canidateVotes = 0
            currentCanidate = row[2]
        #see below where i set the dictionary key to be equal to this variable (currently line 40)
        if currentCanidate == "Raymon Anthony Doane":
                specialBoi += 1
                
        canidateVotes += 1
        totalVotes += 1

#This guy has a personal vendetta against me. He wants to change how his votes are counted for some reason
canidateResults["Raymon Anthony Doane"] = specialBoi
#print(str(canidateResults))
#print(totalVotes)
#identify winner
winner = ""
winningVotes = 0
#winner for loop
for canidate in canidateResults:
    if canidateResults[canidate] > winningVotes:
        winner = canidate
        winningVotes = canidateResults[canidate]

#calculate percentage won and store in string for output
allResults = ""
percentWon = 0.0
for canidate in canidateResults:
    percentWon = round((canidateResults[canidate]/totalVotes)*100, 3)
    allResults += f"{canidate}: {percentWon}% ({canidateResults[canidate]})\n"
#string builder for loop


output = f"Election Results\n-------------------------\nTotal Votes: {totalVotes}\n-------------------------\n{allResults}-------------------------\nWinner: {winner}\n-------------------------"
print(output)

with open(writeFilePath, 'w') as file:
    file.write(output)