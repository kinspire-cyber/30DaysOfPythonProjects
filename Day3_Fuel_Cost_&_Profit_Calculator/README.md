---
title: "Day 3 – Fuel Cost & Profit Calculator (Nigeria)"
published: true
description: "Calculate fuel cost, revenue, cost per trip, and profit for Nigerian transport operators using Python operators."
tags: python, beginners, debugging, nigeria
series: 30DaysOfPythonProjects
---

# Day 3 – Operators
## Fuel Cost & Profit Calculator for Nigerian Transporters

### 🌍 Problem Background (Nigerian Context)
Fuel price fluctuations directly affect:
- Okada riders
- Keke (tricycle) operators
- Taxi & ride-hailing drivers
- Small logistics/delivery businesses

Most operators don’t calculate:
- Daily fuel cost
- Cost per trip
- Real profit after fuel

They guess — and many run at a loss without knowing.

### 👥 Who This Project Helps
- Okada & Keke riders
- Bolt/Uber drivers
- Dispatch riders
- Small transport SMEs
- Students learning real-world Python

### ❗ Why This Problem Matters in Africa
- Fuel is a major cost driver in African transport
- Rising fuel prices affect food, logistics, and inflation
- Financial literacy at micro-business level is very low
- Simple tools can immediately improve income decisions

### 🧠 Python Concepts (Day 3 Focus)
**Core Operators**
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `//`, `**`
- Assignment: `=`, `+=`, `-=`
- Comparison: `>`, `<`, `>=`, `<=`, `==`
- Logical: `and`, `or`

**Other Basics**
- `input()`, `print()`
- Type conversion: `int()`, `float()`

### ⚙️ Core Features
- Collect daily transport data
- Calculate:
  - Total fuel cost
  - Cost per trip
  - Total revenue
  - Net profit or loss
- Warn driver if operating at a loss

---

## 🪜 Step-by-Step Implementation

### Step 1: Collect Inputs
```python
naira = "\u20A6"  # ₦

fuel_price = float(input(f"Fuel price per litre ({naira}): "))
litres = float(input("Litres bought: "))
trips = int(input("Numbers of trips: "))
fare_per_trip = float(input(f"Average fare per trip ({naira}): "))
```

### Step 2: Perform Calculations (Operators in Action)
```python
total_fuel_cost = fuel_price * litres
total_revenue = trips * fare_per_trip
profit = total_revenue - total_fuel_cost
cost_per_trip = total_fuel_cost / trips
```

### Step 3: Display Results Clearly (with Smart ₦ Formatting)
```python
print("\n--- DAILY TRANSPORT SUMMARY ---\n")
print(f"Total Fuel Cost: {naira}{fmt_amount(total_fuel_cost)}")
print(f"Total Revenue: {naira}{fmt_amount(total_revenue)}")
print(f"Cost Per Trip: {naira}{fmt_amount(cost_per_trip)}")
print(f"Profit/Loss: {naira}{fmt_amount(profit)}")
```

### Step 4: Add Logical Decision (Very Important)
```python
if profit > 0:
    print("✅ You made a profit today.")
elif profit == 0:
    print("⚠️ You broke even today.")
else:
    print("❌ You ran at a loss today. Review your fares or fuel usage.")
```

---

## 🔢 Sample Input & Output

**Input**
```
Fuel price per litre: 650
Litres bought: 5
Number of trips: 20
Average fare per trip: 400
```

**Output**
```
--- DAILY TRANSPORT SUMMARY ---

Total Fuel Cost: ₦3250
Total Revenue: ₦8000
Cost Per Trip: ₦162.5
Profit/Loss: ₦4750
✅ You made a profit today.
```

---

## 🛠️ Debugging Tips
- **ValueError on input**: Ensure you enter numbers (e.g., `650`, `5`, `20`, `400`).
- **Trailing .0 amounts**: Use `fmt_amount()` above to hide unnecessary decimals.
- **Divide by zero**: `trips` must be at least `1` to compute `cost_per_trip`.
- **Negative values**: Guard against negatives if needed (e.g., fuel price or litres shouldn’t be negative).
- **Currency accuracy**: For strict currency math, consider `decimal.Decimal`.

---

## ▶️ How to Run (Windows)
From the project folder:
```powershell
python Day3_Fuel_Cost_&_Profit_Calculator\fuel_cost_calculator.py
```
Or if you are already in the Day 3 folder:
```powershell
python fuel_cost_calculator.py
```

---

## 🔗 Project Link
Full source and updates: https://github.com/kinspire-cyber/30DaysOfPythonProjects/tree/main/Day3_Fuel_Cost_%26_Profit_Calculator

If you find this helpful, ⭐ the repo and follow the 30-day series!
