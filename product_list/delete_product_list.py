

product_list = ["laptop", "mouse", "keyboard", "monitor", "printer", "headphones", "phone", "charger"]

def delete_product(product_list, product_name):
    if product_name in product_list:
        product_list.remove(product_name)
        print(f"Removed {product_name} from the list.")
    else:
        print(f"{product_name} not found in the list.")

def delete_last_product(product_list):
    if product_list:
        product_list.pop()
        print(f"Removed last product from the list.")

# Example usage
delete_product(product_list, "mouse")
delete_last_product(product_list)
