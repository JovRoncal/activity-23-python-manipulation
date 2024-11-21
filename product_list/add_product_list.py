

product_list = ["laptop", "mouse", "keyboard", "monitor", "printer", "headphones", "phone", "charger"]

def add_product(product_list, product_name):
    product_list.append(product_name)
    print(f"Added {product_name} to the list.")

def add_multiple_products(product_list, products):
    product_list.extend(products)
    print(f"Added products: {', '.join(products)} to the list.")

# Example usage
add_product(product_list, "tablet")
add_multiple_products(product_list, ["webcam", "USB cable"])
