import csv
from pathlib import Path
from tqdm import tqdm  # used to create a progress bar while doing the for loop

# Setting the file paths for the data files to be analyzed
menu_filepath = Path("Resources/menu_data.csv")
sales_filepath = Path("Resources/sales_data.csv")

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menu_filepath, "r") as csv_file:
    menu_data = csv.reader(csv_file, delimiter=",")
    menu_data_header = next(csv_file)
    # loop through the lines in the csv to store in to the menu list
    for row in menu_data:
        menu.append(row)

# Read in the sales data into the menu list
with open(sales_filepath, "r") as csv_file:
    sales_data = csv.reader(csv_file, delimiter=",")
    sales_data_header = next(csv_file)
    # loop through the lines in the csv to store in to the menu list
    for row in sales_data:
        sales.append(row)

# Initialize dict object to hold our key-value pairs of items and metrics
result = {}

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object

for row in tqdm(sales):

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # Initialize sales data variables
    quantity = int(row[3])
    menu_item = row[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in result.keys():
        result[menu_item] = {"count": 0, "revenue": 0, "cogs": 0, "profit": 0}

    # For every row in our sales data, loop over the menu records to determine a match
    for row in menu:
        # Item,Category,Description,Price,Cost
        # Initialize menu data variables
        item = row[0]
        price = float(row[3])
        cost = float(row[4])

        # Calculate profit of each item in the menu data
        profit = price - cost
        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == item:
            # Print out matching menu data
            # save a dict of the matched items to be printed in summary
            matched_items = {
                "item": item,
                "price": price,
                "cost": cost,
                "profit": profit,
            }
            print(
                f"Found a match /n Item: {item} /n Price: {price} /n Cost: {cost} /n Profit: {profit}"
            )
            # Cumulatively add up the metrics for each item key
            result[menu_item]["count"] += quantity
            result[menu_item]["revenue"] += price * quantity
            result[menu_item]["cogs"] += cost * quantity
            result[menu_item]["profit"] += profit * quantity

        # Else, the sales item does not equal any fo the item in the menu data, therefore no match
        # else:
        # print(f"{item} does not match any item in the menu ")

    # Increment the row counter by 1
    row_count += 1

# Print total number of records in sales data
# printing the summary after the progress bar completes
print(f"the total number of records are {row_count}")


# Write out report to a text file (won't appear on the command line output)

results_path = Path("results/output.txt")
with open(results_path, "w") as csvout:
    for key, value in result.items():
        row = "%s %s \n" % (key, value)
        csvout.write(row)

