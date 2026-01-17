# Create function to calculate monthly payment

def calculate_loan(principal, annual_rate, months):
    """
    Docstring for calculate_loan
    
    :param principal: loan amount in Naira
    :param annual_rate: annual interest rate in percentage
    :param months: repayment duration in months
    """
    monthly_rate = annual_rate / 12 / 100
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    total_payment = monthly_payment * months
    return monthly_payment, total_payment

# Use fuctions for different loans

loans = [
    {"name": "Aisha Stores", "principal": 150000, "rate": 12, "months": 6},
    {"name": "Chinedu Electronics", "principal": 300000, "rate": 10, "months": 12},
    {"name": "Sadiq Ventures", "principal": 200000, "rate": 15, "months": 9}
]

for loan in loans:
    monthly, total = calculate_loan(loan["principal"], loan["rate"], loan["months"])
    print(f"\n{loan['name']}: Monthly ₦{monthly:.2f}, Total ₦{total:.2f}\n")