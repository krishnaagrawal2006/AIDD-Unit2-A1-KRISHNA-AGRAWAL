participants = ["Asha", "Rahul", "Priya"]

# Valid expense
valid_expense = {"description": "Dinner", "amount": 900, "payer": "Asha"}
assert validate_expense(valid_expense, participants) is True

# Invalid edge cases
edge_case_expenses = [
    ("Negative amount", {"description": "Snack", "amount": -100, "payer": "Asha"}),
    ("Zero amount", {"description": "Water", "amount": 0, "payer": "Rahul"}),
    ("Unknown payer", {"description": "Taxi", "amount": 300, "payer": "Vikram"}),
    ("Text amount", {"description": "Groceries", "amount": "125.50", "payer": "Priya"}),
    ("Boolean amount", {"description": "Coffee", "amount": True, "payer": "Asha"}),
]

for label, bad_expense in edge_case_expenses:
    try:
        validate_expense(bad_expense, participants)
        print(f"[FAIL] {label}: expected ValueError")
    except ValueError as exc:
        print(f"[PASS] {label}: {exc}")