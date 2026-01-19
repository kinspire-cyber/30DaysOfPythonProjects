# Loan Calculations
def calculate_loans(principal, annual_rate, months):
    monthly_rate = annual_rate / 12 / 100
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate)** -months)
    total_payment = monthly_payment * months
    return monthly_payment, total_payment