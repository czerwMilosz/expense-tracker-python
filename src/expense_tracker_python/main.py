from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from datetime import date
from enum import IntEnum, auto
import math

USER_NUMBER_SHIFT = 1

class Category(IntEnum):
    """Available expense categories."""
    FOOD = 1
    TRANSPORT = 2
    BILLS = 3
    ENTERTAINMENT = 4


class MenuOption(IntEnum):
    """Available menu options."""
    ADD_EXPENSE = 1
    LIST_EXPENSE = 2
    SHOW_TOTAL = 3
    SUMMARY_BY_CATEGORY = 4
    SAVE_AND_EXIT = 5

    def __str__(self) -> str:
        return f"{self.value} - {self.name.replace('_', ' ').title()}"



class Navigation(IntEnum):
    PREVIOUS = auto()
    NEXT = auto()
    EXIT = auto()

    @property
    def description(self) -> str:
        return {
            Navigation.PREVIOUS: "Poprzednia strona",
            Navigation.NEXT: "Nastepna strona",
            Navigation.EXIT: "Wyjscie",
        }[self]



@dataclass
class Expense:
    """An expense with its amount, category, description, and date."""
    amount: Decimal
    category: Category
    description: str
    expense_date: date

    def __str__(self) -> str:
        """Format an expense as a multiline string."""

        return (f"amount: {self.amount:.2f}\n"
                f"category: {self.category.name.lower()}\n"
                f"description: {self.description}\n"
                f"expense_date: {self.expense_date}\n")



def display_menu() -> None:
    """Display the main menu."""
    print("=== EXPENSE TRACKER ===\n")
    for option in MenuOption:
        print(option)

def get_user_choice() -> MenuOption:
    """Prompt until the user selects a valid menu option."""
    while True:
        try:
            choice = MenuOption(int(input(F"Enter option number ({USER_NUMBER_SHIFT}-{len(MenuOption)}): ")))
            return choice
        except ValueError:
            print("Invalid input. Please enter option from the list.")


def get_amount() -> Decimal:
    """Prompt for a positive amount with at most two decimal places."""
    while True:
        try:
            user_amount = Decimal(input("Enter amount: "))

            if not user_amount.is_finite() or user_amount <= 0:
                print("Invalid amount. Please enter a valid amount greater than zero.")
                continue

            if user_amount.as_tuple().exponent < -2:
                print("Invalid amount. Please enter a maximum of 2 decimal places.")
                continue

            return user_amount

        except InvalidOperation:
            print("Invalid input. Please enter a number.")



def get_category() -> Category:
    """Prompt until the user enters a valid expense category."""
    while True:
        print("Available categories:")
        for category in Category:
            print(f"{category.value}: {category.name}")
        try:
            user_category = Category(int(
                input(f"Enter category number ({min(Category).value}-{max(Category).value}): ")))
            return user_category
        except ValueError:
            print("Invalid input. Please enter category from the list.")


def get_description() -> str:
    """Prompt for a non-empty expense description."""
    while True:
        user_description = input("Enter description: ").strip()

        if user_description == "":
            print("Description is empty. Please enter a description.")
            continue

        return user_description


def get_expense_date() -> date:
    """Prompt until the user enters a valid expense date."""
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
    """Create and return an expense."""
    return Expense(amount=amount,
                   category=category,
                   description=description,
                   expense_date=expense_date)


def display_expenses(expenses: list[Expense], per_page: int = 10) -> None:
    """Display all expenses or a message if the list is empty."""
    if not expenses:
        print("No expenses added.")

    current_page = 1
    total_pages = math.ceil(len(expenses) / per_page)

    while True:
        start_index = (current_page - 1) * per_page
        end_index = start_index + per_page

        print(f"\nStrona {current_page}/{total_pages}")

        for e in expenses[start_index:end_index]:
             print(e)

        for nav in Navigation:
            print(nav.description)

        try:
            user_navigation = Navigation(int(input("Enter a number: ")))

        except ValueError:
            print("Invalid input. Please enter option from the list.")
            continue
        if user_navigation == Navigation.PREVIOUS:
            current_page = max(1,current_page - 1) #wybieranie ktory jest wiekszy
        elif user_navigation == Navigation.NEXT:
            current_page = min(total_pages,current_page + 1)
        elif user_navigation == Navigation.EXIT:
            break

    # wyswietlic 10 i klikac enter dalej i wyswietlac kolejne 10 rezultatow
    # paginacja


def calculate_category_totals(expenses: list[Expense]) -> dict[Category, Decimal]:
    """Calculate expense totals grouped by category."""
    category_totals: dict[Category, Decimal] = {}
    for e in expenses: #suma po kluczu
        category_totals[e.category] = category_totals.get(e.category, Decimal("0")) + e.amount
    return category_totals


def calculate_total(category_totals: dict[Category, Decimal]) -> Decimal:
    """Calculate the overall total from category totals."""
    return sum(category_totals.values(), Decimal("0"))


def display_category_totals(category_totals: dict[Category, Decimal]) -> None:
    """Display category totals and the overall total, or a message if empty."""
    if not category_totals:
        print("\nNo expenses added.\n")
        return

    print("\n=== SUMMARY BY CATEGORY ===")
    for category, amount in category_totals.items():
        print(f"{category.name.lower()}: {amount:.2f} PLN")
    print("---------------------------")
    print(f"TOTAL: {calculate_total(category_totals):.2f} PLN\n")



def main():
    """Run the expense tracker menu loop."""
    #jedna funkcja jedna odpowiedzialnosc

    expenses: list[Expense] = []

    while True:
        display_menu()
        user_choice = get_user_choice()
        match user_choice:
            case MenuOption.ADD_EXPENSE: #INT ENUM, MATCHING PATTERN
                amount = get_amount()
                category = get_category()
                description = get_description()
                expense_date = get_expense_date()
                expense = add_expense(amount, category, description, expense_date)
                expenses.append(expense)
                print("Expense added successfully.")

            case MenuOption.LIST_EXPENSE:
                display_expenses(expenses)

            case MenuOption.SHOW_TOTAL:
                category_totals = calculate_category_totals(expenses)
                print(f"\nTotal: {calculate_total(category_totals):.2f} PLN\n")

            case MenuOption.SUMMARY_BY_CATEGORY:
                category_totals = calculate_category_totals(expenses)
                display_category_totals(category_totals)

            case MenuOption.SAVE_AND_EXIT:
                print("Exiting...")
                break


if __name__ == "__main__":
    main()

#przy eksporterach popracowach z abstrakcyjnymi klasami
# wzorzec abstrakcyjnej fabryki