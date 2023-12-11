import os
import csv  
  
#Path to collect data from folder
budget_data = os.path.join("..","Resources","budget_data.csv")
#setting variables
TotalMonth = 0
NetTotalProfitandLoss = []
TotalChange = 0
GreatestIncrease = [0,""]
GreatestDecrease = [999999999,""] 
Monthofchange = []                          
#Reading the file 
with open(budget_data, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = next(csv_reader)
       #print(f"Header: {csv_header}")
        firstrow = next(csv_reader)
        TotalMonth += 1
        TotalChange += int(firstrow[1])           
        previouschange = int(firstrow[1])

        for line in csv_reader:
                TotalMonth+= 1
                TotalChange += int(line[1])
                NetChange = int(line[1]) - previouschange
                NetTotalProfitandLoss.append(NetChange)
                Monthofchange.append(line[0])
                previouschange= int(line[1])

                if NetChange > GreatestIncrease [0]:
                        GreatestIncrease[0] = NetChange
                        GreatestIncrease[1] = line[1]

                if NetChange < GreatestDecrease [0]:
                        GreatestDecrease[0] = NetChange
                        GreatestDecrease[1] = line[1]
Net_Average = sum(NetTotalProfitandLoss)/len(NetTotalProfitandLoss)
  
Results = f"""
Financial Analysis
----------------------------
Total Months: {TotalMonth}
Total: ${TotalChange}
Average Change: ${Net_Average:.2f}
Greatest Increase in Profits: {GreatestIncrease[1]} (${GreatestIncrease[0]})
Greatest Decrease in Profits: {GreatestDecrease[1]} (${GreatestDecrease[0]})
"""
print(Results)

output_file = os.path.join("..","Analysis","budget_analysis.txt")
with open (output_file, 'w') as text:
        text.write(Results)