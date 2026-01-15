# define the tariff rules
bandA_tariff_per_kwh = 209.50
bandB_tariff_per_kwh = 64.07
bandC_tariff_per_kwh = 52.05
bandD_tariff_per_kwh = 43.27
bandE_tariff_per_kwh = 43.27

# Get user input
tariff_ban = input("Enter your Service Band (A-E): ").lower()
consumption = float(input("Enter your monthly electricity consumption in kWh: "))

# Calculate the bill
if tariff_ban == "a":
    bill = bandA_tariff_per_kwh * consumption
elif tariff_ban == "b":
    bill = bandB_tariff_per_kwh * consumption
elif tariff_ban == "c":
    bill = bandC_tariff_per_kwh * consumption
elif tariff_ban == "d":
    bill = bandD_tariff_per_kwh * consumption
elif tariff_ban == "e":
    bill = bandE_tariff_per_kwh * consumption
else:
    print("Enter a Letter A - E")

# Analzing the Bill

if bill <= 5000:
    category = "Low"
    advice = "Your consumption is efficient. Keep it up!"
elif bill <= 15000:
    category = "Medium"
    advice = "Consider saving energy to reduce your bill."
else:
    category = "High"
    advice = "Your bill is high. Check for wastage or faulty appliances."

# DIsplay Result
print("\nELECTRICITY BILL ANALYSIS")
print("------------------------")
print(f"Monthly Consumption: {consumption} kWh")
print(f"Estimated Bill: ₦{bill}")
print(f"Category: {category}")
print(f"Advice: {advice}\n")
