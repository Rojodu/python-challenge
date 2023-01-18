import os
import csv

budgetPath = os.path.join("Resources","budget_data.csv")

monthCount = 1
totalProfitLoss = 0
previousMonth = 0
currentMonth = 0
totalChanges = 0
avgChangesProfitLoss = 0
greatIncMonth = ""
greatestIncrease = 0
greatDecMonth = ""
greatestDecrease = 0

with open(budgetPath, encoding = "utf-8") as budget:
    budgetReader = csv.reader(budget, delimiter = ',')
    
    next(budgetReader, None)
    previousMonth = int(next(budgetReader)[1])
    totalProfitLoss += previousMonth
    
    for row in budgetReader:
        monthCount += 1
        totalProfitLoss += int(row[1])
        currentMonth = int(row[1])
        change = currentMonth - previousMonth
        totalChanges += change
        if (change > greatestIncrease):
            greatIncMonth = row[0]
            greatestIncrease = change
        elif (change < greatestDecrease):
            greatDecMonth = row[0]
            greatestDecrease = change
        previousMonth = currentMonth
    
    avgChangesProfitLoss = totalChanges/(monthCount-1)

output = f"Financial Analysis\n\n----------------------------------\n\nTotalMonths: {monthCount}\n\nTotal: ${totalProfitLoss}\n\nAverage Change: ${avgChangesProfitLoss}\n\nGreatest Increase in Profits: {greatIncMonth} (${greatestIncrease})\n\nGreatest Decrease in Profits: {greatDecMonth} (${greatestDecrease})"
print(output)

with open('analysis/analysis.txt', 'w') as f:
    f.write(output)