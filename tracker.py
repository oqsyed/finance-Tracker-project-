def calculate_balance(incomes, expenses):
    total_income = sum(incomes)
    total_expenses = sum(item["amount"] for item in expenses)
    balance = total_income - total_expenses
    return total_income, total_expenses, balance

def group_expenses_by_category(expenses):
    grouped = {}
    for item in expenses:
        cat = item["category"]
        grouped[cat] = grouped.get(cat, 0) + item["amount"]
    return grouped
