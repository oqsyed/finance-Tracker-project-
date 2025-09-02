from input_handler import get_income_from_user, get_expenses_from_user, get_expenses_from_csv
from tracker import calculate_balance, group_expenses_by_category
from charts import plot_expenses_bar, plot_expenses_pie

def main():
    print("=== Finance Tracker ===")
    mode = input("Enter 'csv' to load expenses from file or 'manual' to enter manually: ").strip().lower()

    print("\n-- Enter incomes --")
    incomes = get_income_from_user()

    if mode == "csv":
        expenses = get_expenses_from_csv("expenses.csv")
    else:
        print("\n-- Enter expenses --")
        expenses = get_expenses_from_user()

    total_income, total_expenses, balance = calculate_balance(incomes, expenses)

    print("\n=== Summary ===")
    print(f"Total income: ${total_income:.2f}")
    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

    by_cat = group_expenses_by_category(expenses)
    if by_cat:
        print("\nExpenses by category:")
        for cat, amt in by_cat.items():
            print(f"  - {cat}: ${amt:.2f}")
    else:
        print("\nNo expenses recorded.")

    show = input("\nShow charts? (y/n): ").strip().lower()
    if show == "y":
        plot_expenses_bar(by_cat)
        plot_expenses_pie(by_cat)

if __name__ == "__main__":
    main()
