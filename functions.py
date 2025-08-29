original_price = float(input("Enter the original price: "))
discount = float(input("Enter discount percentage: "))

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = price - ((discount_percent/100) * price)

    return price


print(calculate_discount(original_price, discount))
