# Define Market Information
naira = "\u20A6"

last_record_garri = 1000
last_record_rice = 800

print("")
market_name = input("Market Name: ")
date = input("Date: ")

print("")
garri_price = int(input("Garri (per paint): ₦"))
rice_price = int(input("Rice (per kg): ₦"))
print("")
# Store Food Items and Prices 
food_items = {"garri": garri_price , "rice": rice_price}

# Print Stored Data Clearly

print("  Community Market Price Log \n_______________________________")
print("Market: ", market_name)
print("Date: ", date, "\n")

print("Food Prices: ")
print(f"Garri (per paint): {naira}{food_items["garri"]}")
print(f"Rice (per kg): {naira}{food_items["rice"]}")
print("")

# Simple Price comparaison

price_diff_garri = food_items["garri"] - last_record_garri
price_diff_rice = food_items["rice"] - last_record_rice

print("Price Difference: ")
print(f"Garri increased by {naira}{price_diff_garri} compare to last record")
print(f"Rice increased by {naira}{price_diff_rice} compare to last record")
print("")