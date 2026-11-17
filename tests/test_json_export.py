import json
from datetime import date
from decimal import Decimal
from unittest.mock import patch

from expense_tracker_python.main import (
    Category,
    Expense,
    export_expenses_to_json,
    main,
)


def test_export_single_expense(tmp_path):
    expenses = [
        Expense(Decimal("25.50"), Category.FOOD, "Lunch", date(2026, 11, 17))
    ]
    file_path = tmp_path / "expenses.json"

    export_expenses_to_json(expenses, file_path)

    with file_path.open(encoding="utf-8") as file:
        data = json.load(file)

    assert data == [
        {
            "amount": "25.50",
            "category": "food",
            "description": "Lunch",
            "expense_date": "2026-11-17",
        }
    ]


def test_export_multiple_expenses(tmp_path):
    expenses = [
        Expense(Decimal("25.50"), Category.FOOD, "Lunch", date(2026, 11, 17)),
        Expense(Decimal("40.00"), Category.TRANSPORT, "Fuel", date(2026, 11, 18)),
    ]
    file_path = tmp_path / "expenses.json"

    export_expenses_to_json(expenses, file_path)

    with file_path.open(encoding="utf-8") as file:
        data = json.load(file)

    assert data == [
        {
            "amount": "25.50",
            "category": "food",
            "description": "Lunch",
            "expense_date": "2026-11-17",
        },
        {
            "amount": "40.00",
            "category": "transport",
            "description": "Fuel",
            "expense_date": "2026-11-18",
        },
    ]


def test_save_and_exit_without_expenses(capsys):
    with patch("builtins.input", return_value="5"):
        with patch("expense_tracker_python.main.export_expenses_to_json") as export:
            main()

    export.assert_not_called()
    assert "No expenses to save. Exiting..." in capsys.readouterr().out
