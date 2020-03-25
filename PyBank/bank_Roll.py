import os
import csv

cereal_csv = os.path.join("budget_data.csv")
#cereal_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#def bank_roll(financial_data):
pass
# Open and read csv

Title_Total_Months = "Financial Analysis \n ______________________________"
label_Total = "Total: "
label_Average = "Average: "
label_greatest_Increase = " Greatest Increase in profits: "
label_greatest_Decrease = " Greatest Decrease in profits: "
#Define variables
#months = financial_data[0]
#profit_loss = financial_data[1]

months = cereal_csv[0]
profit_loss = cereal_csv[1]
Total_months = 0
net_total = 0
month_count = 0
greatest_increase = 0
greatest_decrease = 0
profit = []


with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
# Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")    
    # Read through each row of data after the header
    for row in csvreader:
    #print(col) #for troubleshooting
        net_total += int(row[1])
        print(net_total)
        month_count += 1
        profit.append(row[1])
        greatest_increase = max(profit)
        greatest_decrease = min(profit)

             # if i > greatest_increase:
           #         greatest_increase = i
            #    print(f"Greatest increase {greatest_increase}")    
    
    # for row in csvreader:
    #     print(row[0],row[1])
    #     profit.append(row[1])
    #     print ("min value element : ", min(profit))
    #     print ("max value element : ", max(profit))
    #     greatest_increase = max(profit)
    #     greatest_decrease = min(profit)

#calculations  
#The total number of months included in the dataset   
    #data = list(csvreader)
    #month_count = len(data)
    #print(f"month count {month_count}")
    
    #for row in csvreader:
        # print(row)
    
#The net total amount of "Profit/Losses" over the entire period
            
print(row)

#The average of the changes in "Profit/Losses" over the entire period
average_the_changes = net_total/month_count

#Greatest Increase in Profits: Feb-2012 ($1926159)

#Greatest Decrease in Profits: Sep-2013 ($-2196167)


 # Print out the Financial Analysis
print(f"Total months:  {month_count}")
print(f"Total:  {net_total}")
print(f"Average  Change:  {average_the_changes}")
print(f"Greatest Increase in Profits:  {greatest_increase}")
print(f"Greatest Decrease in Profits:  {greatest_decrease}")