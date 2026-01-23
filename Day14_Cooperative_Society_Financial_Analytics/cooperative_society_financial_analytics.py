# Sample Data
members = [
    {"name": "Chinedu", "contribution": 5000, "loan": 1000, "repaid": 500},
    {"name": "Aisha", "contribution": 7000, "loan": 2000, "repaid": 2000},
    {"name": "Emeka", "contribution": 3000, "loan": 1500, "repaid": 500},
    {"name": "Fatima", "contribution": 8000, "loan": 0, "repaid": 0},
]

# calculate total contributions
total_contributions = sum(map(lambda m: m["contribution"], members))
print("\nTotal Contributions: ", total_contributions)

# Identify Defaulters 
defaulters = list(filter(lambda m: m["loan"] > m["repaid"], members))
print([m["name"] for m in defaulters])

# Compute Net Loan Outstanding
outstanding_loans = list(map(lambda m: m["loan"] - m["repaid"], members))
print(outstanding_loans)

# Apply Interest Dynamically (Higer Order Function)
def interest_applier(rate):
    def apply(amount):
        return amount + (amount * rate)
    return apply

apply_5_percent = interest_applier(0.05)
loan_with_interest = list(map(lambda m: apply_5_percent(m["loan"] - m["repaid"]), members))
print(loan_with_interest)


#Summarize Contributions and Outstanding Loans
from functools import reduce

total_outstanding = reduce(lambda x, y: x + y, loan_with_interest)
print("Total Outstanding:", total_outstanding)


def audit_log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[Audit] Function {func.__name__} executed")
        return result
    return wrapper

@audit_log
def total_contributions_fn(members):
    return sum(map(lambda m: m["contribution"], members))

print(total_contributions_fn(members))
