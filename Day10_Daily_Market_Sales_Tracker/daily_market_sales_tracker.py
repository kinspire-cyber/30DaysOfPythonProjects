# Initalize Variable 
total_sales = 0
transaction_count = 0


# Use Loop to collect sales

print("\n Enter daily sales amounts (enter 0 to finish):")

while True:
    sale = float(input("Sale amount (₦): "))

    if sale == 0:
        break

    total_sales += sale
    transaction_count += 1


# Claculate the Sunmmary

if transaction_count > 0 :
    average_sale = total_sales / transaction_count
else:
    average_sale = 0


# Display Results
print("\nDAILY MARKET SALES SUMMARY")
print("--------------------------")
print(f"Total Transactions: {transaction_count}")
print(f"Total Sales: ₦{total_sales}")
print(f"Average Sale: ₦{average_sale}\n")