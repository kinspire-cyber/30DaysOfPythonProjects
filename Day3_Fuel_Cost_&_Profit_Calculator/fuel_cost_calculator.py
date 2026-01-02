# Step 1 Prompt the User for input
naira = "\u20A6"

fuel_price = float(input(f"Fuel price per litre ({naira}): "))
litres = float(input("Litres bought: "))
trips = int(input("Numbers of trips: "))
fare_per_trip  = float(input(f"Average fare per trip ({naira}): "))

#print(fuel_price,"\n", litres,"\n", trips,"\n", fare_per_trip)

# Step 2 Run calculations for the data
total_fuel_cost = fuel_price * litres
total_revenue = trips * fare_per_trip
profit = total_revenue - total_fuel_cost
cost_per_trip = total_fuel_cost / trips

# Step 3 Display Results Clearly
print("\n--- DAILY TRANSPORT SUMMARY ---\n")
print(f"Total Fuel Cost: {naira}{total_fuel_cost}")
print(f"Total Revenue: {naira}{total_revenue}")
print(f"Cost Per Trip: {naira}{cost_per_trip}")


# Step 4 Add Logical Decision
if profit > total_fuel_cost:
    print("✅ You made a profit today.")
elif profit == total_fuel_cost:
    print("⚠️ You broke even today.")
else:
    print("❌ You ran at a loss today. Review your fares or fuel usage.")
print("\n")