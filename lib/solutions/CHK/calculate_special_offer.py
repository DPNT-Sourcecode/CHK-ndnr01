'''
Calculates the special offers for items which help customers save money when purchased in bulk
'''
# ===========================COMBINED OFFERS========================# 
def calculate_special_offer_for_A(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    3A for 130
    5A for 200
    '''
    number_of_items_in_offer_of_five = number_of_items_in_inventory[item] // 5
    number_of_items_not_in_offer_of_five = number_of_items_in_inventory[item] % 5
    number_of_items_in_offer_of_three = number_of_items_not_in_offer_of_five // 3
    number_of_items_out_of_offer = number_of_items_not_in_offer_of_five % 3
    return (number_of_items_in_offer_of_five*200) + (number_of_items_in_offer_of_three*130) + (number_of_items_out_of_offer*price_of_items[item])

def calculate_special_offer_for_H(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    3A for 130
    5A for 200
    '''
    number_of_items_in_offer_of_ten = number_of_items_in_inventory[item] // 10
    number_of_items_not_in_offer_of_ten = number_of_items_in_inventory[item] % 10
    number_of_items_in_offer_of_five = number_of_items_not_in_offer_of_ten // 5
    number_of_items_out_of_offer = number_of_items_not_in_offer_of_ten % 5
    return (number_of_items_in_offer_of_ten*80) + (number_of_items_in_offer_of_five*45) + (number_of_items_out_of_offer*price_of_items[item])
# ================================================================# 

# ===========================SINGLE OFFERS========================# 

def calculate_special_offer_for_B(number_of_item: int, price_of_item: int) -> int:
    '''
    2B for 45
    '''
    _calculate_single_offer(number_of_item= number_of_item, 
                            price_of_item= price_of_item, 
                            number_of_items_for_offer=2, 
                            value_of_offer=45)
    
def calculate_special_offer_for_K(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    2B for 45
    '''
    _calculate_single_offer(number_of_item= number_of_items_in_inventory[item], 
                            price_of_item= price_of_items, 
                            number_of_items_for_offer=2, 
                            value_of_offer=45)

#================================================================#
def calculate_special_offer_for_E(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    This assumes that if B alread in inventory, then it will not be charged. If B not in inventory, it
    will be given as free rather than price of B being reduced from the final checkout value
    '''
    return (number_of_items_in_inventory[item]*price_of_items[item])



def _calculate_single_offer(number_of_item: int, price_of_item: int, number_of_items_for_offer: int, value_of_offer: int):
    number_of_items_out_of_offer = number_of_item % number_of_items_for_offer
    number_of_items_in_offer = number_of_item // number_of_items_for_offer
    return (number_of_items_out_of_offer*price_of_item) + (number_of_items_in_offer*value_of_offer)
    
def _calculate_combined_offer():
    number_of_items_in_offer_of_ten = number_of_items_in_inventory[item] // 10
    number_of_items_not_in_offer_of_ten = number_of_items_in_inventory[item] % 10
    number_of_items_in_offer_of_five = number_of_items_not_in_offer_of_ten // 5
    number_of_items_out_of_offer = number_of_items_not_in_offer_of_ten % 5
    return (number_of_items_in_offer_of_ten*80) + (number_of_items_in_offer_of_five*45) + (number_of_items_out_of_offer*price_of_items[item])
