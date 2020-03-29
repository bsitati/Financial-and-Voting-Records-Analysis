import os, sys
import csv

cereal_csv = os.path.join("Resources/budget_data.csv")
#cereal_csv = os.path.join('..', 'Resources', 'budget_data.csv')

def bank_roll(financial_data):
#pass
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
profit = []


with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
# Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")    
    # Read through each row of data after the header
    greatest_increase = 0
    greatest_decrease = 0
    max = 0
    min = 0

    for row in csvreader:
        #print(col) #for troubleshooting
        net_total += int(row[1])
        month_count += 1
        #greatest profit
        #r = row.split(",")
        if float(row[1]) > max:
            max=float(row[1])
            print(f"Max Value {max}")
            max_month = row[0]
            print(f"Max month {max_month}")

        if float(row[1]) < min:
            min=float(row[1])
            min_month = row[0]
            print(f"Min Value {min}")
            print(f"Min month {min_month}")

    print(f"Net total {net_total}")
    
#The average of the changes in "Profit/Losses" over the entire period
average_the_changes = round((net_total/month_count), 2)


# Print out the Financial Analysis
print("\n____________________________________________________")
print("Financial Analysis \n____________________________________________")
print(f"Total months:  {month_count}")
print(f"Total:  ${net_total}")
print(f"Average  Change: ${average_the_changes}")
print(f"Greatest Increase in Profits: {max_month}  ${max}")
print(f"Greatest Decrease in Profits: {min_month} ${min}")
print("\n____________________________________________________\n")

#open file and read
finance_file = open("Analysis_file.txt", "r")
print(finance_file.read())
sys.stdout.close()