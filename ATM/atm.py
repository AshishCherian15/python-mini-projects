# ============================================
#   ATM Simulation Program
#   Made by: CSE Final Year Student
# ============================================

# hardcoded PIN and starting balance
CORRECT_PIN = "1234"
balance = 5000.0

# ---- LOGIN ----
print("=" * 35)
print("      Welcome to Simple ATM")
print("=" * 35)

attempts = 0
logged_in = False

while attempts < 3:
    pin = input("\nEnter your PIN: ")
    if pin == CORRECT_PIN:
        logged_in = True
        print("\n✅ Login successful! Welcome.")
        break
    else:
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"❌ Wrong PIN. {remaining} attempt(s) left.")
        else:
            print("❌ Too many wrong attempts. Card blocked.")

# if login failed, stop the program
if not logged_in:
    exit()

# ---- MAIN MENU LOOP ----
while True:
    print("\n" + "-" * 35)
    print("         ATM Main Menu")
    print("-" * 35)
    print("  1. Check Balance")
    print("  2. Deposit Money")
    print("  3. Withdraw Money")
    print("  4. Exit")
    print("-" * 35)

    choice = input("Enter your choice (1-4): ")

    # ---- CHECK BALANCE ----
    if choice == "1":
        print(f"\n💰 Your current balance is: ₹{balance:.2f}")

    # ---- DEPOSIT ----
    elif choice == "2":
        try:
            amount = float(input("\nEnter amount to deposit: ₹"))
            if amount <= 0:
                print("⚠️  Please enter a valid amount greater than 0.")
            else:
                balance += amount
                print(f"✅ ₹{amount:.2f} deposited successfully.")
                print(f"   Updated Balance: ₹{balance:.2f}")
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")

    # ---- WITHDRAW ----
    elif choice == "3":
        try:
            amount = float(input("\nEnter amount to withdraw: ₹"))
            if amount <= 0:
                print("⚠️  Please enter a valid amount greater than 0.")
            elif amount > balance:
                print(f"❌ Insufficient balance! Your balance is only ₹{balance:.2f}")
            else:
                balance -= amount
                print(f"✅ ₹{amount:.2f} withdrawn successfully.")
                print(f"   Updated Balance: ₹{balance:.2f}")
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")

    # ---- EXIT ----
    elif choice == "4":
        print("\n👋 Thank you for using Simple ATM. Goodbye!")
        break

    # ---- INVALID CHOICE ----
    else:
        print("⚠️  Invalid choice. Please enter 1, 2, 3, or 4.")
