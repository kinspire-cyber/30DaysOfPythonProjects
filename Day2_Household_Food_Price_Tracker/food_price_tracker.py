# Collect Household Info
naira = "\u20A6"
print("")
household_name = input("Enter household name: ")
market_name = input("Enter market name: ")
print("")

# Collect Food Prices and Store Prices in Variables
rice_price = float(input(f"Price of Rice ({naira}): "))
beans_price = float(input(f"Price of Beans ({naira}): "))
garri_price = float(input(f"Price of Garri ({naira}): "))
tomatoes_price = float(input(f"Price of Tomatoes ({naira}): "))
oil_price = float(input(f"Price of Cooking Oil ({naira}): "))

# Store the items in a list
food_items = [rice_price, beans_price, garri_price, tomatoes_price, oil_price]

# Total cost of the food items
total_cost = sum(food_items)

# Calculate the number of food items
number_of_items = len(food_items)

# Calculate the average
item_average = (total_cost / number_of_items)

# Most expensive item price
costly_item = max(food_items)

# Cheapest item price
cheap_item = min(food_items)

# Display a Clean Report
print("")
print("HOUSEHOLD FOOD PRICE REPORT")
print("-" * 20)
print("Household: ", household_name)
print("Market: ", market_name)

print("")

print(f"Total Food Cost: {naira}{total_cost:.2f}")
print(f"Number of Items: {number_of_items:.2f}")
print(f"Average Item Price: {naira}{item_average}")
print("\n")
print(f"Most Expensive Item Price: {naira}{costly_item:.2f}")
print(f"Cheapest Item Price: {cheap_item}")
print("")