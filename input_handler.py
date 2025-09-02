import csv

def get_income_from_user():
    incomes = []
    while True:
        try:
            val = input("Enter income amount (or press Enter to stop): ")
            if val.strip() == "":
                break
            incomes.append(float(val))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return incomes

def get_expenses_from_user():
    expenses = []
    while True:
        cat = input("Enter expense category (or press Enter to stop): ").strip()
        if cat == "":
            break
        try:
            amt = float(input("Enter amount: "))
            expenses.append({"category": cat, "amount": amt})
        except ValueError:
            print("Invalid amount. Try again.")
    return expenses

def get_expenses_from_csv(filepath="expenses.csv"):
    expenses = []
    try:
        with open(filepath, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not row.get("category") or not row.get("amount"):
                    continue
                expenses.append({
                    "category": row["category"],
                    "amount": float(row["amount"])
                })
    except FileNotFoundError:
        print(f"CSV file '{filepath}' not found.")
    return expenses
