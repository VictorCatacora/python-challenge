import os
import csv
import statistics

# Path and read
budget_csv = os.path.join('budget_data.csv')
with open(budget_csv, 'r') as csvfile:

	# Split the data on commas and skip header
	csvreader = csv.reader(csvfile, delimiter=',')
	header=next(csvreader,None)

	months=0
	total=0
	change_array=[]
	init=0
	dates_array=[]

	# Getting total month, total , changes and dates
	for row in csvreader:
		months=months+1
		total=total+int(row[1])
		change_array.append(int(row[1])-init)
		init=int(row[1])
		dates_array.append(row[0])

	# Total months and total amount
	print("Total months: " + str(months))
	print("Total: $" + str(total))


	# Remove the first value of the list of changes, because that one has not changed
	del change_array[0]
	
	# Using statistics library
	av_changes=statistics.mean(change_array)
	print("Average  Change: $" + str(round(av_changes,2)))
	# Maximum change
	max_change=max(change_array)
	# Get the index where that max change occurred
	max_index=change_array.index(max(change_array))

	# Remove te first value of the list of dates, because that one has not changed
	del dates_array[0]

	# Get the date when the max change occurred
	max_date=dates_array[max_index]
	print("Greatest Increase in Profits: " + max_date +" ($" + str(max_change) + ")")

	# Minimum change
	min_change=min(change_array)
	# Get the index where that min change occurred
	min_index=change_array.index(min(change_array))

	# Get the date when the min change occurred
	min_date=dates_array[min_index]
	print("Greatest Decrease in Profits: " + min_date + " ($" + str(min_change) + ")")

file = './output_budget.txt'

# Open and write output file
with open(file, 'w') as text:
	text.write("Financial Analysis")
	text.write('\n' + "----------------------------")
	text.write('\n' + "Total Months: " + str(months))
	text.write('\n' + "Total: $" + str(total))
	text.write('\n' + "Average  Change: $" + str(round(av_changes,2)))
	text.write('\n' + "Greatest Increase in Profits: " + max_date + ' ($' + str(max_change) + ')')
	text.write('\n' + "Greatest Decrease in Profits: " + min_date + ' ($' + str(min_change) + ')')




	