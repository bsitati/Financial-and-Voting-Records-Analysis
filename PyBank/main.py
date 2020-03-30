import os, sys
import csv

cereal_csv = os.path.join("budget_data.csv")
#cereal_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#def bank_roll(financial_data):
#pass
# Open and read csv

with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")    
    # Read through each row of data after the header
    profit_loss=[]
    profit_loss_change=[]
    profit_loss_month=[]

    for row in csvreader:
        profit_loss_month.append(row[0])
        profit_loss.append(int(row[1]))
        

#greatest number   
    for i in range((len(profit_loss) - 1)):
        profit_loss_change.append(profit_loss[i] - profit_loss[i - 1])
        if profit_loss_change[i - 1] < profit_loss_change[i]:
            max_inc_profit_loss = profit_loss_change[i]
            max_inc_profit_loss_month = profit_loss_month[i]
        else:
            max_inc_profit_loss = profit_loss_change[i - 1]
            max_inc_profit_loss_month = profit_loss_month[i - 1]
        
        if profit_loss_change[i - 1] > profit_loss_change[i]:
            max_dec_profit_loss = profit_loss_change[i - 1]
            max_dec_profit_loss_month = profit_loss_month[i - 1]
        else:
            max_dec_profit_loss = profit_loss_change[i-1]
            max_dec_profit_loss_month = profit_loss_month[i-1]



        #print(f"Profit-loss month  {profit_loss_month[i]}")
        #print(f"All profit-loss  {profit_loss[i]}")
        #print(f"Profit-loss change  {profit_loss_change[i]}")

#calc net profit
    profit_sum = 0
    for i in range(0, len(profit_loss)):    
        profit_sum = profit_sum + profit_loss[i];  


    total_profit_loss= sum(profit_loss)
    sum_profit = sum(profit_loss_change)
    total_profit_loss = len(profit_loss)
    average_profit_loss = sum_profit/total_profit_loss

    #print to file
    sys.stdout = open('output_profit_loss.txt','wt')

    print(f"Financial Analysis ")
    print(f"----------------------------------------------")    
    print(f"Total  Months: {total_profit_loss}")
    print(f"Total: ${profit_sum}")
    print(f"Average  Change: ${round(average_profit_loss,2)}")
    print(f"Greatest Increase in Profits: {max_inc_profit_loss_month} (${max_inc_profit_loss})")
    print(f"Greatest Decrease in Profits: {max_dec_profit_loss_month} (${max_dec_profit_loss})")
    print(f"----------------------------------------------")

    
    #print(f"Greatest Increase in Profits: {max_inc_profit_loss_month}")
    #print(f"Max profit increase {max(profit_loss_change)}")
    #print(f"Max profit decrease {min(profit_loss_change)}")
    #print(f"Average profit {round(average_profit_loss,2)}")
        
#print file output
    file = open("output_profit_loss.txt", "r") 
    print(file.read())




       

            

