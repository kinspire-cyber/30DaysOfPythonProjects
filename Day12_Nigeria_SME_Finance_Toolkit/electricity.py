# Bill Analyzer
def analyze_bill(consumption, tariff = 60):
    bill = consumption * tariff

    if bill <= 5000:
        category = "Low"
    elif bill <= 15000:
        category = "Medium"
    else:
        category = "High"
    return bill, category