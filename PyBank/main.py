import os
import csv

my_csvpath = os.path.join('Resources', 'budget_data.csv')

#set initial values for variables
num_months = 0
net_pl = 0
delta = 0
delta_avg = 0
total_delta = 0
alpha_delta_pos = 0
alpha_delta_pos_date = ''
alpha_delta_neg = 0
alpha_delta_neg_date = ''
this_pl = 0
previous_pl = 0

#open the csv file
with open(my_csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #total number of months
        num_months += 1

        #net total profit/loss
        net_pl += int(row[1])

        #compute current delta and cumulative delta
        if num_months >=2:
            previous_pl = this_pl
        this_pl = int(row[1])
        if num_months >=2:
            delta = this_pl - previous_pl
        total_delta += delta

        #compute greatest positive delta and identify the associated month
        if delta > 0:
            if delta > alpha_delta_pos:
                alpha_delta_pos = delta
                alpha_delta_pos_date = row[0]

        #compute greatest negative delta and identify the associated month
        elif delta < 0:
            if delta < alpha_delta_neg:
                alpha_delta_neg = delta
                alpha_delta_neg_date = row[0]

    #compute average delta
    delta_avg = "{0:.2f}".format(total_delta/(num_months-1))


#write data to text file
os.path.join("PyBank.txt")
f = open("PyBank.txt","w")
f.write(f"```\n")
f.write(f"Financial Analysis\n")
f.write(f"----------------------------\n")
f.write(f"Total Months: {num_months}\n")
f.write(f"Total ${net_pl}\n")
f.write(f"Average Change: ${delta_avg}\n")
f.write(f"Greatest Increase In Profits: {alpha_delta_pos_date} (${alpha_delta_pos})\n")
f.write(f"Greatest Decrease In Profits: {alpha_delta_neg_date} (${alpha_delta_neg})\n")
f.write(f"```\n")
f.close()

#open the text file we created and print text to console
file = "PyBank.txt"
f = open(file, 'r+')
print(f.read())
f.close()
