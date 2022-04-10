'''
Calculates the group discount
'''

from calendar import prcal


def calculate_group_discounts(number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    total_number_of_items_in_group_discount, list_of_prices_of_group_discount_items = _total_number_items_and_prices_applicable_for_group_discounts(number_of_items_in_inventory, price_of_items)
    
    
def _total_number_items_and_prices_applicable_for_group_discounts(number_of_items_in_inventory:dict, price_of_items: dict):
    list_of_items_for_group_discount = ["S","T","X","Y","Z"]
    list_of_prices_of_group_discount_items = []
    total_number_of_items_in_group_discount = 0
    for item in list_of_items_for_group_discount:
        if item in number_of_items_in_inventory:
            total_number_of_items_in_group_discount +=total_number_of_items_in_group_discount+number_of_items_in_inventory[item]
            list_of_prices_of_group_discount_items.append(price_of_items[item])
    return (total_number_of_items_in_group_discount, list_of_prices_of_group_discount_items)
