def calculate_balance(income, expenses):
    return income - expenses

def balance(income, expenses):
    total = calculate_balance(income, expenses)
    if total > 0:
        return True
    else:
        return False