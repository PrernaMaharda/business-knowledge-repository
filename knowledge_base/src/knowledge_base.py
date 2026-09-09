import json


def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


products = load_data("knowledge_base/products.json")
inventory = load_data("knowledge_base/inventory.json")
rules = load_data("knowledge_base/business_rules.json")


def get_product(product_id):
    for product in products:
        if product["product_id"] == product_id:
            return product
    return None


def check_stock(product_id, order_quantity):

    for item in inventory:

        if item["product_id"] == product_id:

            stock = item["quantity"]
            reorder_level = item["reorder_level"]

            if stock >= order_quantity:
                decision = "Order can be accepted"
            else:
                decision = "Order should be placed on hold"

            if stock <= reorder_level:
                restock = "Restocking recommendation required"
            else:
                restock = "Stock level is sufficient"

            return {
                "available_stock": stock,
                "order_quantity": order_quantity,
                "decision": decision,
                "inventory_status": restock
            }

    return {"error": "Product not found"}


# Example query
product_id = "P002"
order_quantity = 5

product = get_product(product_id)

if product:
    print("Product:", product["name"])
    print("Price:", product["price"])

    result = check_stock(product_id, order_quantity)

    print("Available Stock:", result["available_stock"])
    print("Decision:", result["decision"])
    print("Inventory Status:", result["inventory_status"])
else:
    print("Product not found")
