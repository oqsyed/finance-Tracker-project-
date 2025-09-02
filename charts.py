import matplotlib.pyplot as plt

def plot_expenses_bar(expenses_by_category):
    if not expenses_by_category:
        print("No expense data to plot.")
        return
    categories = list(expenses_by_category.keys())
    amounts = list(expenses_by_category.values())

    plt.figure(figsize=(8, 4))
    plt.bar(categories, amounts)
    plt.title("Expenses by Category (Bar)")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.tight_layout()
    plt.show()

def plot_expenses_pie(expenses_by_category):
    if not expenses_by_category:
        print("No expense data to plot.")
        return
    categories = list(expenses_by_category.keys())
    amounts = list(expenses_by_category.values())

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expense Distribution (Pie)")
    plt.tight_layout()
    plt.show()
