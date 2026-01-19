from loan import calculate_loans
from sale import calculate_daily_sales
from electricity import analyze_bill


monthly, total = calculate_loans(150000, 12, 6)
print(f"\n Loan → Monthly: {monthly:.2f} Total: {total:.2f}")

sales = [2500, 4000, 1500]
total_sales, avg_sales = calculate_daily_sales(sales)
print(f"Sales → Total: {total_sales:.2f}, Average: {avg_sales:.2f}")

bill, category = analyze_bill(280)
print("Electricity → Bill:", bill, "Category:", category, "\n")