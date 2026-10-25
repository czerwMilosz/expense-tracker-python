from dataclasses import dataclass
from decimal import Decimal
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
    date: date


def display_menu():
    print("=== EXPENSE TRACKER ===\n"
          "1. Add expense\n"
          "2. List expenses\n"
          "3. Show total\n"
          "4. Summary by category\n"
          "5. Save and exit\n")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter option number (1-5): "))

            if choice in range(1, 6):
                return choice
            else:
                print("Invalid choice. Please select an option between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        display_menu()
        user_choice = get_user_choice()
        if user_choice == 1:
            print("Feature not implemented yet.")
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