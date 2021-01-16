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
    profit=[]
    profit_date=[]
    change_profit=[]
  
    for row in csvreader:
        count_of_months +=1 # gives the count of records except header
        float_profit=float(row[row_index_profit]) # profit/loss column
        total_profit += float_profit #total profit/loss is the increment 
        profit.append(float_profit) #create the list of proft/loss     
        profit_date.append(row[row_index_date]) #create the list of date
        
    for n in range(1,len(profit)):
        value=profit[n]- profit[n-1] #calculate the differences
        change_profit.append(float(value)) #create the list of differences
    
    for n in range(0, len(change_profit)):
        total_change_profit +=change_profit[n] #calculate the total changes
        average_change_profit=round((total_change_profit/(len(change_profit))),2) #calculate the average of changes
       
    for ch_prof in change_profit:
        if ch_prof > greatest_inc:
            greatest_inc = ch_prof #find the greatest increase in the list of change
            
        if ch_prof < greatest_dec:
            greatest_dec = ch_prof #find the greatest decrease in the list of change
            
greatest_inc_index = change_profit.index(greatest_inc)
greatest_inc_date=profit_date[greatest_inc_index+1]
greatest_dec_index = change_profit.index(greatest_dec)
greatest_dec_date=profit_date[greatest_dec_index+1]

print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {count_of_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change_profit}")
print(f"Greatest Increase in Profits: {greatest_inc_date}(${greatest_inc})")
print(f"Greatest Decrease in Profits: {greatest_dec_date}(${greatest_dec})")

output_path = os.path.join( "Analysis", "Analysis_PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:

    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {count_of_months} \n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${average_change_profit}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc_date}(${greatest_inc}))\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec_date}(${greatest_dec}))\n")

