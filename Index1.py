import json
from datetime import datetime


'''import random
num1= input("enter user number")
num2= random.randint(1,100)

if num1 >= num2:
    print("user number is greater")

else:
    print("user number smaller")'''

'''def calculate_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


def count_frequency(items):
    frequency = {}

    for item in items:
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


numbers = [12, 45, 23, 12, 67, 34, 45, 89, 23, 12]

total, average, maximum, minimum = calculate_statistics(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", round(average, 2))
print("Maximum:", maximum)
print("Minimum:", minimum)

print("\nFrequency:")
for number, count in count_frequency(numbers).items():
    print(number, "->", count)


names = ["Aanya", "jade", "max", "sean", "oliver"]

print("\nStudents:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")


'''

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    title = input("Expense name: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['title']} | "
            f"₹{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def show_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\n--- Summary ---")
    print("Total spent:", total)

    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_summary(expenses)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()