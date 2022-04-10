'''
Calculates the group discount. This method assumes that (Z,Z,Z) is also applicable for the discount
Since the policy favours customer, so the customer uses higher price items to form the group discount
and pays for the lowest ones
'''

def calculate_group_discounts(number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    total_number_of_items_in_group_discount, list_of_prices_of_group_discount_items = _total_number_items_and_prices_applicable_for_group_discounts(number_of_items_in_inventory, price_of_items)
    
    number_of_group_discounts = total_number_of_items_in_group_discount // 3
    number_of_items_left_from_group_discounts =  total_number_of_items_in_group_discount % 3
    
    final_price_of_group_discounts = number_of_group_discounts * 45
    
    if number_of_items_left_from_group_discounts == 0:
        return final_price_of_group_discounts
    elif number_of_items_left_from_group_discounts == 1:
        return (min(list_of_prices_of_group_discount_items)+final_price_of_group_discounts)
    else:
        list_of_prices_of_group_discount_items = sorted(list_of_prices_of_group_discount_items)
        return (list_of_prices_of_group_discount_items[0]+list_of_prices_of_group_discount_items[1]+final_price_of_group_discounts)
    
def _total_number_items_and_prices_applicable_for_group_discounts(number_of_items_in_inventory:dict, price_of_items: dict):
    list_of_items_for_group_discount = ["S","T","X","Y","Z"]
    list_of_prices_of_group_discount_items = []
    total_number_of_items_in_group_discount = 0
    for item in list_of_items_for_group_discount:
        if item in number_of_items_in_inventory:
            total_number_of_items_in_group_discount +=total_number_of_items_in_group_discount+number_of_items_in_inventory[item]
            list_of_prices_of_group_discount_items.append(price_of_items[item])
    return (total_number_of_items_in_group_discount, list_of_prices_of_group_discount_items)
