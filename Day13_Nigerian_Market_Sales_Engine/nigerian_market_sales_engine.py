# Raw Market Sales Data
daily_sales = [1500, 2300, 800, 4000, 1200, 600, 5000, 300]

# Identify good days sales
good_days = [sale for sale in daily_sales if sale >= 2000]
print("\nGood days: ", good_days)

# Identify poor days sales
poor_days = [sale for sale in daily_sales if sale <= 1000]
print("Poor days: ", poor_days)

# Apply POS Charges Using Lambda POS charge = 1.5%
pos_charge = lambda amount: amount * 0.015

charges = [pos_charge(sale) for sale in daily_sales]
print("POS Charges: ",charges)

# Check net sales after charges 
net_sales = [sale - pos_charge(sale) for sale in daily_sales]
print("Net sales: ", net_sales)

# Categorize Sales
sales_category = [
    "High" if sale >= 3000 else "Medium" if sale >= 1500 else "Low"
    for sale in daily_sales
]

print("Categories: ", sales_category)

# Sales Summary
total_sales = sum(daily_sales)
average_sales = sum(daily_sales) / len(daily_sales)

print("Total:", total_sales)
print("Average:", average_sales)
print("\n")
