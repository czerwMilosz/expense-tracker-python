from datetime import date
from decimal import Decimal
from expense_tracker_python.main import (
    Category,
    Expense,
    calculate_total,
    calculate_category_totals
)

def test_calculate_total():
    category_totals = {
        Category.FOOD: Decimal("100"),
        Category.BILLS: Decimal("50")
    }
    result = calculate_total(category_totals)
    assert result == Decimal("150")

def test_calculate_category_totals():
    expenses: list[Expense] = [
        Expense(Decimal("25.50"), Category.FOOD, "Groceries", date(2026, 10, 20)),
        Expense(Decimal("40.00"), Category.TRANSPORT, "Fuel", date(2026, 10, 21)),
        Expense(Decimal("15.99"), Category.FOOD, "Lunch", date(2026, 10, 22)),
        Expense(Decimal("120.00"), Category.BILLS, "Electricity", date(2026, 10, 23)),
        Expense(Decimal("35.50"), Category.TRANSPORT, "Bus tickets", date(2026, 10, 24)),
    ]
    result = calculate_category_totals(expenses)
    assert result == {
        Category.FOOD: Decimal("41.49"),
        Category.TRANSPORT: Decimal("75.50"),
        Category.BILLS: Decimal("120.00"),
    }

def test_calculate_total_empty():
    result = calculate_total({})

    assert result == Decimal("0")

def test_calculate_category_totals_empty():
    result = calculate_category_totals([])

    assert result == {}

def test_calculate_category_totals_single_expense():
    expenses: list[Expense] = [Expense(Decimal("26.50"), Category.FOOD, "Restaurant", date(2026, 10, 25))]

    result = calculate_category_totals(expenses)

    assert result == {Category.FOOD: Decimal("26.50")}