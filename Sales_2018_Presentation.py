# # 1. Read the data from the spreadsheet - see examples below
#
# # 2. Collect all of the sales from each month into a single list
#
# # using csv for month and sales lists
import csv

with open('sales.csv', newline='') as csvfile:
    monthly_sales = csv.DictReader(csvfile)
    print('Monthly Sales')

    for row in monthly_sales:
        print(row['month'], row['sales'])

# # 3.Output the total sales across all months
import csv

with open('sales.csv','r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    sales = []

    for row in spreadsheet:
        sales_data = row['sales']
        sales.append(sales_data)

total_sales = 0

for total in sales:
    total_sales = total_sales + int(total)

print('Total Sales in 2018 = £', total_sales)


##Extending the project - Bar graph code
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

plt.bar(y_pos, column_sales, color=['indianred', 'coral', 'orange', 'yellow', 'palegreen', 'skyblue',
                            'cyan', 'pink', 'violet', 'palevioletred', 'magenta', 'mediumorchid'])

# Create names on the x-axis
plt.xticks(y_pos, column_month)
plt.title('Sales by month')
plt.xlabel('Month')
plt.ylabel('Sales')

# Show graphic
plt.show()

## Extending the project - scatter plot
##libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a dataset:
df = pd.read_csv('sales.csv')
# x = 'sales'
# y = 'expenditure'
plt.plot('sales','expenditure', data=df, linestyle='none', marker='o')
plt.title('sales vs expenditure')
plt.xlabel('sales')
plt.ylabel('expenditure')

sns.regplot(df['sales'], df['expenditure'])

# # Show graphic
plt.show()
print('Sales/Expenditure')
