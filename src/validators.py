def validate_quantity(quantity: int) -> int:
    if type(quantity) is not int or quantity <= 0:
        raise ValueError("Количество должно быть целым положительным числом")
    return quantity