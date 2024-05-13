import csv

    #set path for file
csvpath = "python-challenge/PyBank/Resources/budget_data.csv"
    
    #key variables:
month_count = 0
profit = 0

   #keep track of changes: 
changes = []
month_change = []

    #open CSV using UTF-8 encoding:
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ",")

    #read header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #read each row of data after header
    for row in csvreader:
        print(row)

        #month count
        month_count = month_count + 1

        #total profit -- important to cast row as integer or else code will not work since it is a string
        profit = profit + int(row[1])
    
        #this month proft - last month profit
        if (month_count ==1):
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_change.append(row[0])

            #reset last month profit
            last_month_profit = int(row[1])


    print(month_count)
        #prints: 86 months
    print(profit)
        #prints: 22564198
    print(len(changes))
        #prints: 85 changes

    avg_change = sum(changes) / len(changes)
    print(avg_change)
        #prints: -8311.105882352942

    max_change = max(changes)
    max_month = month_change[changes.index(max_change)]

    print(max_change)
    print(max_month)
        #prints: max change of 1862002 in August 2016

    min_change = min(changes)
    min_month = month_change[changes.index(min_change)]

    print(min_change)
    print(min_month)
        #prints: min change of -1825558 in February 2014

    output = f"""Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${profit}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""
    
    #to round number use round(variable, number of places after decimal) -- see above for example

    print(output)

    #output to text file
    with(open("output_malinowski.txt", 'w') as f):
        f.write(output)