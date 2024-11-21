

product_prices = [800, 25, 50, 400, 150, 200, 50, 30]

def max_price(product_prices):
    max_cost = 0
    for price in product_prices:
        if price > max_cost:
            max_cost = price
    return max_cost

def min_price(product_prices):
    min_cost = float('inf')
    for price in product_prices:
        if price < min_cost:
            min_cost = price
    return min_cost

# Example usage
print(f"The maximum price is: {max_price(product_prices)}")
print(f"The minimum price is: {min_price(product_prices)}")

# Built-in function
print(f"The max price using built-in: {max(product_prices)}")
print(f"The min price using built-in: {min(product_prices)}")
