# Step 1: Create dictionary for users
bank_users = {
    'alice': 5000,
    'bob': 2000,
    'emeka': 0
}

# Step 2: Function to Check Balance
def check_balance(user):
    try:
        return bank_users[user]
    except KeyError:
        return f"User '{user}' not found!"


# Step 3: Deposit Money
def deposit(user, amount):
    try:
        bank_users[user] += amount
        return f"{amount} deposited. New balance: {bank_users[user]}"
    except KeyError:
        return f"User '{user}' not found!"
    except TypeError:
        return "Deposit amount must be a number"


# Step 4: Withdraw Money

def withdraw(user, amount):
    try:
        if amount > bank_users[user]:
            return "Insufficient funds"
        bank_users[user] -= amount
        return f"{amount} withdrawn. Remaining balance: {bank_users[user]}"
    except KeyError:
        return f"User '{user}' not found!"
    except TypeError:
        return "Withdrawal amount must be a number"


# Making the app user friendly
while True:
    action = input("Enter action (deposit/withdraw/balance/exit): ").lower()
    if action == "exit":
        break
    user = input("Enter username: ").lower()
    if action == "balance":
        print(check_balance(user))
    else:
        amount = input("Enter amount: ")
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid number!")
            continue
        if action == "deposit":
            print(deposit(user, amount))
        elif action == "withdraw":
            print(withdraw(user, amount))
        else:
            print("Unknown action!")
