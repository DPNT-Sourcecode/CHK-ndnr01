from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''
    skus: String of items 
    @return: Total checkout value
    '''
    # Item price list
    price_of_items = {"A": 50, "B": 30, "C": 20, "D": 15}
    
    # Dictionary of frequency of items in inventory
    number_of_items_in_inventory = Counter(skus)
    
    if is_valid_item(price_of_items, number_of_items_in_inventory):
        return calculate_final_checkout_value(number_of_items_in_inventory, price_of_items)
    return -1

def is_valid_item(price_of_items: dict, number_of_items_in_inventory: dict) -> bool:
    '''
    Checks for any invalid items
    '''
    set_of_valid_items = set(price_of_items.keys())
    set_of_customer_items = set(number_of_items_in_inventory.keys())
    # Items are valid only when there is no set difference between the valid items and customer items
    return len(set_of_customer_items-set_of_valid_items) == 0

# Assumption: Based on the second deployment, its clear that customer expects -1 for any invalid
#  item despite other valid items being present
def calculate_final_checkout_value(number_of_items_in_inventory: dict,
                                   price_of_items: dict) -> int:
    '''
    Using the price of items and any special offers, this calculates the 
    checkout value after the shopping
    @return: int -> final_checkout_value
    '''
    final_checkout_value = 0
    for item in number_of_items_in_inventory:    
        if item in price_of_items: # Checks if item is valid
            # Special Offer A
            if item == "A":
                final_checkout_value+=calculate_special_offer_for_A(item, number_of_items_in_inventory, price_of_items)
            # Special Offer B
            elif item == "B":
                final_checkout_value+=calculate_special_offer_for_B(item, number_of_items_in_inventory, price_of_items)
            # Special Offer E
            # elif item == "E":
            #     calculate_special_offer_for_E(item, number_of_items_in_inventory, price_of_items)
            else:
                final_checkout_value = final_checkout_value + number_of_items_in_inventory[item]*price_of_items[item]
    return final_checkout_value

def calculate_special_offer_for_A(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    3A for 130
    5A for 200
    '''
    number_of_items_in_offer_of_five = number_of_items_in_inventory[item] // 5 
    if number_of_items_in_offer_of_five > 0:
        number_of_items_in_offer_of_five = number_of_items_in_inventory[item] // 5
    
    number_of_items_out_of_offer = number_of_items_in_inventory[item] % 3
    number_of_items_in_offer = number_of_items_in_inventory[item] // 3
    return (number_of_items_out_of_offer*price_of_items[item]) + (number_of_items_in_offer*130)

def calculate_special_offer_for_B(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    2B for 45
    '''
    number_of_items_out_of_offer = number_of_items_in_inventory[item] % 2
    number_of_items_in_offer = number_of_items_in_inventory[item] // 2
    return (number_of_items_out_of_offer*price_of_items[item]) + (number_of_items_in_offer*45)

def calculate_special_offer_for_E(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    2E gives free B
    This assumes that if B alread in inventory, then it will not be charged. If B not in inventory, it
    will be given as free rather than price of B being reduced from the final checkout value
    '''
    number_of_items_out_of_offer = number_of_items_in_inventory[item] % 2
    number_of_items_in_offer = number_of_items_in_inventory[item] // 2
    return (number_of_items_out_of_offer*price_of_items[item]) + (number_of_items_in_offer*45)