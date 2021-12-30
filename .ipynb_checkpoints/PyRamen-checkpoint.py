import csv
from pathlib import Path
from tqdm import tqdm

# Setting the file paths for the data files to be analyzed
menu_filepath = Path("Resources/menu_data.csv")
sales_filepath = Path("Resources/sales_data.csv")

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, "r") as csv_file:
    menu_data = csv.reader(csv_file, delimiter=",")
    menu_data_header = next(csv_file)
    # loop through the lines in the csv to store in to the menu list
    for row in menu_data:
        menu.append(row)

# @TODO: Read in the sales data into the menu list
with open(sales_filepath, "r") as csv_file:
    sales_data = csv.reader(csv_file, delimiter=",")
    sales_data_header = next(csv_file)
    # loop through the lines in the csv to store in to the menu list
    for row in sales_data:
        sales.append(row)
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

for row in  tqdm(sales):
    
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(row[3])
    menu_item = row[4]
    
    
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report.keys():
        report[menu_item]= {
            "count":0,
            "revenue":0,
            "cogs":0,
            "profit":0
        }

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for row in (menu):
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = row[0]
        price = float(row[3])
        cost = float(row[4])

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost
        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == item:
            # @TODO: Print out matching menu data
            #print(f"Found a match /n Item: {item} /n Price: {price} /n Cost: {cost} /n Profit: {profit}")
            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_item]["count"]+=quantity
            report[menu_item]["revenue"]+=price * quantity
            report[menu_item]["cogs"]+= cost * quantity
            report[menu_item]["profit"]+= profit * quantity

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        #else:
            #print(f"{item} does not match any item in the menu ")
    # @TODO: Increment the row counter by 1
    row_count+=1

# @TODO: Print total number of records in sales data
print(f"the total number of records are {row_count}")
# @TODO: Write out report to a text file (won't appear on the command line output)



# @TODO: Write out report to a text file (won't appear on the command line output)

results_path = Path('results/output.csv')
with open (results_path,'w') as csvout :
    for key,value in report.items():
        row = "%s %s \n" %(key,value)
        csvout.write(row)
        



