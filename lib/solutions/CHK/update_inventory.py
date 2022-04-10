'''
Updates the number of items used in the inventory. This is based on offers that
provide free items
'''

# ===========================TWO ITEM OFFERS========================# 
def update_number_of_B_items(number_of_items_in_inventory: dict) -> int:
    '''
    2E gives free B
    '''
    return _update_number_of_items_based_on_two_item_offer(number_of_items_in_inventory=number_of_items_in_inventory,
                                                           offering_item="E",
                                                           offered_item="B",
                                                           amount_of_offer=2)
def update_number_of_M_items(number_of_items_in_inventory: dict) -> int:
    '''
    3N get one M free
    '''
    return _update_number_of_items_based_on_two_item_offer(number_of_items_in_inventory=number_of_items_in_inventory,
                                                           offering_item="N",
                                                           offered_item="M",
                                                           amount_of_offer=3)
def update_number_of_Q_items(number_of_items_in_inventory: dict) -> int:
    '''
    3R get one Q free
    '''
    return _update_number_of_items_based_on_two_item_offer(number_of_items_in_inventory=number_of_items_in_inventory,
                                                           offering_item="R",
                                                           offered_item="Q",
                                                           amount_of_offer=3)

# ===========================SINGLE ITEM OFFERS========================# 
def update_number_of_F_items(number_of_items_in_inventory: dict) ->int:
    '''
    2F gets another F free: Offer requires 3Fs in basket. For cases such as 8Fs, customer shall pay
    for 6Fs
    value_of_offer-> 2F + 1F(free) = 3(Did some calculations to determine this logic)
    '''
    return _update_number_of_items_based_on_single_item_offer(number_of_items_in_inventory=number_of_items_in_inventory,
                                                              offering_item="F",
                                                              value_of_offer=3)

def update_number_of_U_items(number_of_items_in_inventory: dict) ->int:
    '''
    3U get one U free 
    '''
    return _update_number_of_items_based_on_single_item_offer(number_of_items_in_inventory=number_of_items_in_inventory,
                                                              offering_item="U",
                                                              value_of_offer=4)

# ===========================HELPER FUNCTIONS========================# 
def _update_number_of_items_based_on_two_item_offer(number_of_items_in_inventory: dict, offering_item: str, offered_item: str, amount_of_offer: int) ->int:
    '''
    Updates the number of x items customer is required to pay based on the number
    of free x items they get. This assumes that if x alread in inventory, then it will not be charged. 
    If x not in inventory, it will be given as free rather than price of x being reduced 
    from the final checkout value
    Note: Number of x items are changed to manage this requirement rather than the checkout price
    '''
    number_of_free_offered_items= number_of_items_in_inventory[offering_item] // amount_of_offer
    number_of_offered_items = number_of_items_in_inventory[offered_item]
    # Checks if customer has more B items than the free B items
    if number_of_offered_items > number_of_free_offered_items:
            return number_of_offered_items - number_of_free_offered_items
    # If less bought items than free, then they pay zero for the B items
    else:
        return 0

def _update_number_of_items_based_on_single_item_offer(number_of_items_in_inventory: dict, offering_item: str, value_of_offer: int) ->int:
    '''
    2F gets another F free: Offer requires 3Fs in basket. For cases such as 8Fs, customer shall pay
    for 6Fs
    '''
    return number_of_items_in_inventory[offering_item] - (number_of_items_in_inventory[offering_item] // value_of_offer)



    # number_of_free_B_items= number_of_items_in_inventory["E"] // 2
    # number_of_items_of_B = number_of_items_in_inventory["B"]
    # # Checks if customer has more B items than the free B items
    # if number_of_items_of_B > number_of_free_B_items:
    #         return number_of_items_of_B - number_of_free_B_items
    # # If less bought items than free, then they pay zero for the B items
    # else:
    #     return 0
    
    
    # return number_of_items_in_inventory["F"] - (number_of_items_in_inventory["F"] // 3)
