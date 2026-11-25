import math


def validate_expense(expense: dict, participants: list[str]) -> bool:
    """Validate an expense dictionary against allowed participants and numeric rules."""
    if not isinstance(expense, dict):
        raise ValueError("Expense must be a dictionary.")

    amount = expense.get("amount")
    payer = expense.get("payer")

    # 1 & 4: Check type first so text or booleans fail cleanly before numeric comparisons
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Expense amount must be a valid number.")

    if math.isnan(amount) or math.isinf(amount):
        raise ValueError("Expense amount must be a finite number.")

    # 1 & 2: Reject negative or zero amounts
    if amount <= 0:
        raise ValueError("Expense amount must be greater than zero.")

    # 3: Ensure payer is part of the group
    if payer not in participants:
        raise ValueError(f"Payer '{payer}' is not in the participant list.")

    return True