# # 1. Read the data from the spreadsheet - see examples below
#
# # 2. Collect all of the sales from each month into a single list
#
# # using csv for month and sales lists
import csv
# use with statement and open to read csv file and create a list of monthly_sales
with open('sales.csv', newline='') as csvfile:
    monthly_sales = csv.DictReader(csvfile)
    print('Monthly Sales')
# for loop to iterate through each line in csv for month and sales column
    for row in monthly_sales:
        print(row['month'], row['sales'])

# # 3.Output the total sales across all months
import csv
# use with statement and open to read csv file
with open('sales.csv','r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
#create a sales list from the csv by parsing the info using DictReader
    sales = []
#for loop to iterate through sales column
    for row in spreadsheet:
        sales_data = row['sales']
        sales.append(sales_data)
#starting at zero and adding to previous value through each row in sales column
total_sales = 0

for total in sales:
    total_sales = total_sales + int(total)
#print total sales in 2018
print('Total Sales in 2018 = £', total_sales)


##Extending the project - Bar graph code
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#use pandas to read csv file sales and month columns to plot graph
ds = pd.read_csv('sales.csv',sep = ",", header=0)
column_month = ds["month"]
print(column_month)
y_pos = np.arange(len(column_month))

ds = pd.read_csv('sales.csv',sep = ",", header=0)
column_sales = ds["sales"]
print(column_sales)
plt.bar(y_pos, column_sales)

# Create names on the x-axis
plt.xticks(y_pos, column_month)
# create colours for the bars
plt.bar(y_pos, column_sales, color=['indianred', 'coral', 'orange', 'yellow', 'palegreen', 'skyblue',
                            'cyan', 'pink', 'violet', 'palevioletred', 'magenta', 'mediumorchid'])

# Create names on the x-axis
plt.xticks(y_pos, column_month)
plt.title('Sales by month')
plt.xlabel('Month')
plt.ylabel('Sales')

# Show graph
plt.show()

## Extending the project - scatter plot
##import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a dataset:
df = pd.read_csv('sales.csv')
# axis - x = 'sales', y = 'expenditure'
plt.plot('sales','expenditure', data=df, linestyle='none', marker='o')
plt.title('sales vs expenditure')
plt.xlabel('sales')
plt.ylabel('expenditure')

#to plot line of best fit inport seaborn
sns.regplot(df['sales'], df['expenditure'])

# # Show graph
plt.show()
print('Sales/Expenditure')
