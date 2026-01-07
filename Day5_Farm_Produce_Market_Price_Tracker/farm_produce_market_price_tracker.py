naira = "₦"

# Define produce information
produce_name = "Tomatoes"
market_name = "Mile 12 Market"

# List of the prices
daily_prices = [8000, 10000, 10500, 9800]

# Add today's price

today_price = int(input(f"Enter today's price for Tomatoes {naira}: "))
daily_prices.append(today_price)

# Calculate Market Insights

total_price = sum(daily_prices)
average_price = total_price / len(daily_prices)
highest_price = max(daily_prices)
lowest_price = min(daily_prices)

# display the result
print("FARM PRODUCE PRICE REPORT")
print("- " * 12)
print("Produce: ", produce_name)
print("Market: ", market_name)
print("Recorded Prices: ", daily_prices)
print("Average Price: ", average_price)
print("Highest Price: ", highest_price)
print("Lowest Price: ", lowest_price)
