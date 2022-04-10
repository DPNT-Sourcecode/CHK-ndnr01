from solutions.CHK.calculate_final_checkout import is_valid_item, calculate_final_checkout_value

from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''
    skus: String of items 
    @return: Total checkout value
    '''
    # Item price list
    price_of_items = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    
    # Dictionary of frequency of items in inventory
    number_of_items_in_inventory = Counter(skus)
    
    if is_valid_item(price_of_items, number_of_items_in_inventory):
        return calculate_final_checkout_value(number_of_items_in_inventory, price_of_items)
    return -1

#============ IMPROVEMENTS=========#
'''
3. Create config file.py to load all hardcoded values calclate_special offer and other modules
3. Write unit tests for separated modules
'''
