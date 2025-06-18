# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your total expenses: ₹{your_total}")
print(f"Partner's total expenses: ₹{partner_total}")

# Determine who spent more
if your_total > partner_total:
    print("You spent more than your partner.")
elif partner_total > your_total:
    print("Your partner spent more than you.")
else:
    print("Both spent the same amount.")

# find the category with the biggest difference
max_diff = 0
max_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_category = category

print(f"The biggest difference is in '{max_category}' with a difference of ₹{max_diff}.")
