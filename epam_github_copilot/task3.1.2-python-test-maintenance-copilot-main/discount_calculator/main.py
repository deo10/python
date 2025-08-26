def calculate_discounted_price_with_tax(original_price: int | float, discount_percentage: int | float,
                                        tax_rate: int | float = 0) -> float:
    if not isinstance(original_price, (int, float)) or not isinstance(discount_percentage,
                                                                      (int, float)) or not isinstance(tax_rate,
                                                                                                      (int, float)):
        raise TypeError("Invalid input type")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage should be between 0 and 100")
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Tax rate should be between 0 and 100")
    discount = original_price * (discount_percentage / 100)
    after_discount_price = original_price - discount
    tax = after_discount_price * (tax_rate / 100)
    return after_discount_price + tax
