# PyRamen

This Repository provides some financial analysis on a restaurant business where by comparing the sales data with the menu items
it works by iterating through a list created by loading in two csv files:

- Revenue Data from each sale item
- Menu items with prices

The program would iterate through a dictionary object where this information is stored and would match the orders with the menu item prices to find the sum of the revenue , cost and profit along with the quantity ordered for each item and stores the information in a text file. Below is an example of this output

> spicy miso ramen {'count': 9238, 'revenue': 110856.0, 'cogs': 46190.0, 'profit': 64666.0}

> tori paitan ramen {'count': 9156, 'revenue': 119028.0, 'cogs': 54936.0, 'profit': 64092.0}

> truffle butter ramen {'count': 8982, 'revenue': 125748.0, 'cogs': 62874.0, 'profit': 62874.0}

> tonkotsu ramen {'count': 9288, 'revenue': 120744.0, 'cogs': 55728.0, 'profit': 65016.0}

> vegetarian spicy miso {'count': 9216, 'revenue': 110592.0, 'cogs': 46080.0, 'profit': 64512.0}

> shio ramen {'count': 9180, 'revenue': 100980.0, 'cogs': 45900.0, 'profit': 55080.0}

> miso crab ramen {'count': 8890, 'revenue': 106680.0, 'cogs': 53340.0, 'profit': 53340.0}

> nagomi shoyu {'count': 9132, 'revenue': 100452.0, 'cogs': 45660.0, 'profit': 54792.0}

> soft-shell miso crab ramen {'count': 9130, 'revenue': 127820.0, 'cogs': 63910.0, 'profit': 63910.0}

> burnt garlic tonkotsu ramen {'count': 9070, 'revenue': 126980.0, 'cogs': 54420.0, 'profit': 72560.0}

> vegetarian curry + king trumpet mushroom ramen {'count': 8824, 'revenue': 114712.0, 'cogs': 61768.0, 'profit': 52944.0}
