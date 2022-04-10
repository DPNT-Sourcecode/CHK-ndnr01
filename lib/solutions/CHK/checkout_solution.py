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
    
    return calculate_final_checkout_value(number_of_items_in_inventory, price_of_items)

# Assumption: Any illegal input will be ignored and not counted in the checkout. It is not clear
# from requirements if the -1 has any affect on checkout value and hence this assumption
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
                number_of_items_out_of_offer = number_of_items_in_inventory[item] % 3
                number_of_items_in_offer = number_of_items_in_inventory[item] // 3
                final_checkout_value = final_checkout_value + (number_of_items_out_of_offer*price_of_items[item]) + (number_of_items_in_offer*130)
            elif item == "B":
                number_of_items_out_of_offer = number_of_items_in_inventory[item] % 2
                number_of_items_in_offer = number_of_items_in_inventory[item] // 2
                final_checkout_value = final_checkout_value + (number_of_items_out_of_offer*price_of_items[item]) + (number_of_items_in_offer*45)
            else:
                final_checkout_value = final_checkout_value + number_of_items_in_inventory[item]*price_of_items[item]
    return final_checkout_value


