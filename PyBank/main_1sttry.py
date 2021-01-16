import os
import csv

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

csvpath=os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    count_of_months=0
    total_profit=0
    row_index_date=0
    row_index_profit=1
    prev_profit=0
    greatest_inc=0
    greatest_inc_date="date1"
    greatest_dec=0
    greatest_dec_date="date2"
    total_change_profit=0
    average_change_profit=0
    change_profit=0
  
    for row in csvreader:
        count_of_months +=1 # gives the count of records except header
        float_profit=float(row[row_index_profit]) # profit/loss column
        total_profit += float_profit #total profit/loss is the increment 
        change_profit=float_profit-prev_profit 
        prev_profit=float(row[row_index_profit])
        total_change_profit += change_profit

        if change_profit > greatest_inc:
            greatest_inc = change_profit
            greatest_inc_date = row[row_index_date]
        

        if change_profit < greatest_dec:
            greatest_dec = change_profit
            greatest_dec_date = row[row_index_date]           
    
average_change_profit=round(total_change_profit/count_of_months,2)

print(count_of_months)
print(total_profit)
print(average_change_profit)
print(greatest_inc)
print(greatest_inc_date)
print(greatest_dec)
print(greatest_dec_date)
print(change_profit)