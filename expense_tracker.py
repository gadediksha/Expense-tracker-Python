# Expense Tracker Project

expenseslist = []  
print("Welcome to Expense Tracker")

while True:
    print("\n******* Menu ********")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    try:
        choice = int(input("Please Enter Your Choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # 1. Add Expense
    if choice == 1:
        date = input("Date of cost (DD-MM-YYYY): ")
        
        print("Categories:- Food, Travel, Makeup, Books")
        category = input("Type of cost: ")
        
        description = input("More details: ")
        
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Amount must be a number!")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseslist.append(expense)
        print("Expense added successfully!")

    # 2. View All Expenses
    elif choice == 2:
        if len(expenseslist) == 0:
            print("No Expenses Added.")
        else:
            print("\n******** Your All Expenses ********")
            for i, each_cost in enumerate(expenseslist, start=1):
                print(
                    f"Cost {i} -> "
                    f"{each_cost['date']}, "
                    f"{each_cost['category']}, "
                    f"{each_cost['description']}, "
                    f"₹{each_cost['amount']}"
                )

    # 3. View Total Spending
    elif choice == 3:
        total = sum(each_cost["amount"] for each_cost in expenseslist)
        print("TOTAL COST = ₹", total)

    # 4. Exit
    elif choice == 4:
        print("Thank you for using my system...")
        break

    else:
        print("INVALID CHOICE, TRY AGAIN")
