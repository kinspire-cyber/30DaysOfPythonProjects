# Create Loan Records Using Dictionary
loans = {
    "Aisha Stores": {"borrowed": 150000, "repaid": 50000},
    "Chinedu Electronics": {"borrowed": 300000, "repaid": 120000},
    "Sadiq Ventures": {"borrowed": 200000, "repaid": 20000}
}

# Display Loan summaries
print("\n")
print("SME LOAN REPAYMENT STATUS")
print("-" * 24)
for business, record in loans.items():
    borrowed = record["borrowed"]
    repaid = record["repaid"]
    balance = borrowed - repaid

    print(business)
    print(f"    Borrowed: ₦{borrowed}")
    print(f"    Repaid: ₦{repaid}")
    print(f"    Balance: ₦{balance}\n")
