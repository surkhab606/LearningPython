def display_invoice(username, amount, due_date):
    return f"Hello, {username}. You have ${amount:.2f} due in {due_date} days."

test = display_invoice("Surkhab", 10, 4)
print(test)

