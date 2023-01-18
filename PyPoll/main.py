import os
import csv

pollPath = os.path.join("Resources","election_data.csv")

totalVotes = 0
canVotes = 0
candidates = []
newCandidates = []
candidateNum = 0
candidateName = ''
winVotes = 0
winner = ''
counting = False

with open(pollPath, encoding = 'utf-8') as poll:
    pollReader = csv.reader(poll, delimiter = ',')
    next(pollReader, None)
    
    for row in pollReader:  
        totalVotes += 1
        candidateName = row[2]
        if len(candidates) > 0:
            for can in candidates:
                if candidateName == can["Name"]:
                    can["Votes"] += 1
                    counting = True
            if counting == False:
                candidates.append({"Name":candidateName,"Votes":1})
            elif counting == True:
                counting = False
        else:
            candidates.append({"Name":candidateName,"Votes":1})

print("Election Results")
print("-------------------------------")
print(f"TotalVotes: {totalVotes}")
print("-------------------------------")
for can in candidates:
    percentage = can['Votes']/totalVotes
    formatPercentage = "{:.3%}".format(percentage)
    print(f"{can['Name']}: {formatPercentage} ({can['Votes']})")
    if can['Votes'] > winVotes:
        winner = can['Name']
        winVotes = can['Votes']
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

with open('analysis/analysis.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------------\n")
    f.write(f"TotalVotes: {totalVotes}\n")
    f.write("-------------------------------\n")
    for can in candidates:
        percentage = can['Votes']/totalVotes
        formatPercentage = "{:.3%}".format(percentage)
        f.write(f"{can['Name']}: {formatPercentage} ({can['Votes']})\n")
        if can['Votes'] > winVotes:
            winner = can['Name']
            winVotes = can['Votes']
    f.write("-------------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------------\n")