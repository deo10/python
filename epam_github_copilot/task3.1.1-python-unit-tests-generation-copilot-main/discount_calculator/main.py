def calculate_discounted_price(original_price: int | float, discount_percentage: int | float) -> float:
    if not isinstance(original_price, (int, float)) or not isinstance(discount_percentage, (int, float)):
        raise TypeError("Invalid input type")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage should be between 0 and 100")
    discount = original_price * (discount_percentage / 100)
    return original_price - discount
