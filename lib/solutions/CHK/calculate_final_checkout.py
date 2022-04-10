'''
Validates inventory and calculates the final checkout value based on updated inventory and special offers
'''

from solutions.CHK.update_inventory import update_number_of_B_items, update_number_of_F_items
from solutions.CHK.calculate_special_offer import calculate_special_offer_for_A, calculate_special_offer_for_B, calculate_special_offer_for_K, calculate_special_offer_for_H

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
    if ("E" and "B") in number_of_items_in_inventory:
        number_of_items_in_inventory["B"] = update_number_of_B_items(number_of_items_in_inventory)
    
    if number_of_items_in_inventory["F"] >=3:
        number_of_items_in_inventory["F"] = update_number_of_F_items(number_of_items_in_inventory)

    for item in number_of_items_in_inventory:    
        if item in price_of_items:
            if item == "A": # Special Offer A
                final_checkout_value+=calculate_special_offer_for_A(number_of_items_in_inventory[item], price_of_items[item])
            elif item == "B": # Special Offer B
                final_checkout_value+=calculate_special_offer_for_B(number_of_items_in_inventory[item], price_of_items[item])
            # elif item == "H":
            #     final_checkout_value+=calculate_special_offer_for_H(item, number_of_items_in_inventory, price_of_items)
            # elif item == "K":
            #     final_checkout_value+=calculate_special_offer_for_K(number_of_items_in_inventory[item], price_of_items[item])
            # elif item == "P":
            #     final_checkout_value+=calculate_special_offer_for_P(item, number_of_items_in_inventory, price_of_items)
            # elif item == "Q":
            #     final_checkout_value+=calculate_special_offer_for_Q(item, number_of_items_in_inventory, price_of_items)
            # elif item == "V":
            #     final_checkout_value+=calculate_special_offer_for_V(item, number_of_items_in_inventory, price_of_items)           
            else:
                final_checkout_value = final_checkout_value + number_of_items_in_inventory[item]*price_of_items[item]
    return final_checkout_value
