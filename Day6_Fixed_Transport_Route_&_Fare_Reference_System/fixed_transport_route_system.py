# define the transport routes
routes = (
    ("Ojota", "Yaba", 500),
    ("CMS", "Lekki", 700),
    ("Wuse", "Garki", 300),
    ("Airport", "Ikeja", 1500)
)

# Display all routes
print("\nAVAILABLE TRANSPORT ROUTES")
print("---------------------------")

for route in routes:
    start, end, fare = route
    print(f"{start} → {end} : ₦{fare}")

# Show the number of Routes
print("\nTotal Routes Available: ", len(routes), "\n")

# Access Specific Route pricing
specific_route = int(input("Enter The Sepcific Route You Want To View [0-3]: "))
print("\nSample Route Reference:")
print(routes[specific_route],"\n")
