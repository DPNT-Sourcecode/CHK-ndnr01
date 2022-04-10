'''
Validates inventory and calculates the final checkout value based on updated inventory and special offers
'''

from solutions.CHK.update_inventory import update_number_of_B_items, update_number_of_F_items, update_number_of_M_items, update_number_of_Q_items, update_number_of_U_items
from solutions.CHK.calculate_special_offer import calculate_special_offer_for_A, calculate_special_offer_for_B, calculate_special_offer_for_K, calculate_special_offer_for_H, calculate_special_offer_for_P, calculate_special_offer_for_Q, calculate_special_offer_for_V
from solutions.CHK.calculate_group_discount import calculate_group_discounts

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
    
    # --------------------- GROUP DISCOUNTS FOR SPECIAL ITEMS---------------------------#
    
    
    # ------------ FREE ITEMS OFFER WHEN PURCHASED SPECIFIC QUANTITIES-------------------#
    if ("E" and "B") in number_of_items_in_inventory:
        number_of_items_in_inventory["B"] = update_number_of_B_items(number_of_items_in_inventory)
        
    if ("N" and "M") in number_of_items_in_inventory:
        number_of_items_in_inventory["M"] = update_number_of_M_items(number_of_items_in_inventory)
        
    if ("R" and "Q") in number_of_items_in_inventory:
        number_of_items_in_inventory["Q"] = update_number_of_Q_items(number_of_items_in_inventory)
        
    if number_of_items_in_inventory["F"] >=3:
        number_of_items_in_inventory["F"] = update_number_of_F_items(number_of_items_in_inventory)

    if number_of_items_in_inventory["U"] >=4:
        number_of_items_in_inventory["U"] = update_number_of_U_items(number_of_items_in_inventory)

    # ------------ SAVINGS OFFER WHEN PURCHASED ITEMS IN BULK-------------------#
    for item in number_of_items_in_inventory:    
        if item in price_of_items:
            if item == "A": # Special Offer A
                final_checkout_value+=calculate_special_offer_for_A(number_of_items_in_inventory[item], price_of_items[item])
            elif item == "B": # Special Offer B
                final_checkout_value+=calculate_special_offer_for_B(number_of_items_in_inventory[item], price_of_items[item])
            elif item == "H": # Special Offer H
                final_checkout_value+=calculate_special_offer_for_H(number_of_items_in_inventory[item], price_of_items[item])
            elif item == "K": # Special Offer K
                final_checkout_value+=calculate_special_offer_for_K(number_of_items_in_inventory[item], price_of_items[item])
            elif item == "P": # Special Offer P
                final_checkout_value+=calculate_special_offer_for_P(number_of_items_in_inventory[item], price_of_items[item])
            elif item == "Q": # Special Offer Q
                final_checkout_value+=calculate_special_offer_for_Q(number_of_items_in_inventory[item], price_of_items[item])
            elif item == "V": # Special Offer V
                final_checkout_value+=calculate_special_offer_for_V(number_of_items_in_inventory[item], price_of_items[item])          
            else:
                final_checkout_value = final_checkout_value + number_of_items_in_inventory[item]*price_of_items[item]
    return final_checkout_value
