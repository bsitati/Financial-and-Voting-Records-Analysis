import os
import csv

# Path to collect data from the Resources folder
#finance_csv = os.path.join('..', 'Resources', 'budget_datacsv')
finance_csv = os.path.join('budget_datacsv')


# Define the function and have it accept the 'wrestler_data' as its sole parameter
def print_percentages(financial_data):

    Title_Total_Months = "Financial Analysis \n ______________________________"
    label_Total = "Total: "
    label_Average = "Average: "
    label_greatest_Increase = " Greatest Increase in profits: "
    label_greatest_Decrease = " Greatest Decrease in profits: "
#Define variables
    months = financial_data[0]
    profit_loss = financial_data[1]



