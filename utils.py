from decimal import Decimal

def convert_to_decimal(number: float) -> Decimal:
    result = str(number)
    total = Decimal(result)
    return total


def conver_to_chance(number: Decimal, event: str) -> str:
    current_number = float(number)
    count = None
    for multiplier in range(1, 10**9):
        if int(multiplier * current_number) == 1:
            count = multiplier
            break
    message = f'Шанс события "{event}" равен:\n1 к {count} или {number}'
    return message
