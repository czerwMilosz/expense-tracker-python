from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from datetime import date
from enum import Enum


class Category(Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    BILLS = "bills"
    ENTERTAINMENT = "entertainment"


@dataclass
class Expense:
    amount: Decimal
    category: Category
    description: str
    expense_date: date


def display_menu() -> None:
    print("=== EXPENSE TRACKER ===\n"
          "1. Add expense\n"
          "2. List expenses\n"
          "3. Show total\n"
          "4. Summary by category\n"
          "5. Save and exit\n")

def get_user_choice() -> int:
    while True:
        try:
            choice = int(input("Enter option number (1-5): "))

            if choice in range(1, 6):
                return choice
            else:
                print("Invalid choice. Please select an option between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_amount() -> Decimal:
    while True:
        try:
            user_amount = Decimal(input("Enter amount: "))

            if not user_amount.is_finite() or user_amount <= 0:
                print("Invalid amount. Please enter a number greater than zero.")
                continue

            if user_amount.as_tuple().exponent < -2:
                print("Invalid amount. Please enter a maximum of 2 decimal places.")

                continue

            return user_amount

        except InvalidOperation:
            print("Invalid input. Please enter a number.")



def get_category() -> Category:
    while True:
        print("Available categories:")
        print(", ".join(category.value for category in Category))
        try:
            user_category = Category(input("Enter category: ").strip().lower())
            return user_category
        except ValueError:
            print("Invalid input. Please enter category from the list.")


def get_description() -> str:
    while True:
        user_description = input("Enter description: ").strip()

        if user_description == "":
            print("Description is empty. Please enter a description.")
            continue

        return user_description


def get_expense_date() -> date:
    while True:
        try:
            user_date = input("Enter expense date (YYYY-MM-DD): ").strip()
            converted_date = date.fromisoformat(user_date)
            return converted_date
        except ValueError:
            print("Invalid input. Please enter a date in the format YYYY-MM-DD.")


def add_expense(amount: Decimal,
                category: Category,
                description: str,
                expense_date: date) -> Expense:
    return Expense(amount=amount,
                   category=category,
                   description=description,
                   expense_date=expense_date)


def main():
    expenses: list[Expense] = []
    while True:
        display_menu()
        user_choice = get_user_choice()
        if user_choice == 1:
            amount = get_amount()
            category = get_category()
            description = get_description()
            expense_date = get_expense_date()
            expense = add_expense(amount, category, description, expense_date)
            expenses.append(expense)
            print("Expense added successfully.")
        elif user_choice == 2:
            print("Feature not implemented yet.")
        elif user_choice == 3:
            print("Feature not implemented yet.")
        elif user_choice == 4:
            print("Feature not implemented yet.")
        elif user_choice == 5:
            print("Exiting...")
            break



if __name__ == "__main__":
    main()