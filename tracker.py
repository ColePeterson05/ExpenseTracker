import csv
import os
from datetime import datetime
#File in which expenses are stored
FILE_NAME = "expenses.csv"

#Creating the CSV file if it doesn't exist
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "amount", "category", "description"])

# Add a new expense entry to the CSV file
def add_expense(amount, category, description):
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), amount, category, description])
    print("Expense added!")

# Print all expenses from the CSV file
def view_expenses():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Summarize expenses grouped by category
def summary_by_category():
    summary = {}
    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row["category"]
            amount = float(row["amount"])
            # Add amount to the correct category total
            summary[category] = summary.get(category, 0) + amount

    print("\n📊 Expense Summary:")
    for cat, total in summary.items():
        print(f"{cat}: ${total:.2f}")

# Main menu loop
def menu():
    init_file()       # Make sure CSV exists before starting
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary by Category")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount = input("Amount: ")
            category = input("Category: ")
            description = input("Description: ")
            add_expense(amount, category, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

#Running the program
if __name__ == "__main__":
    menu()