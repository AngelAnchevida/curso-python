def calculate_balance(income, expenses):
    return income - expenses

def balance(income, expenses):
    total = calculate_balance(income, expenses)
    if total > 0:
        return "El total es positivo"
    else:
        return "El total es negativo"