'''
Updates the number of items used in the inventory. This is based on 
'''
def update_number_of_B_items(number_of_items_in_inventory: dict) -> int:
    '''
    2E gives free B

    Updates the number of B items customer is required to pay based on the number
    of free B items they get. This assumes that if B alread in inventory, then it will not be charged. 
    If B not in inventory, it will be given as free rather than price of B being reduced 
    from the final checkout value
    Note: Number of B items are changed to manage this requirement rather than the checkout price
    '''
    number_of_free_B_items= number_of_items_in_inventory["E"] // 2
    number_of_items_of_B = number_of_items_in_inventory["B"]
    # Checks if customer has more B items than the free B items
    if number_of_items_of_B > number_of_free_B_items:
            return number_of_items_of_B - number_of_free_B_items
    # If less bought items than free, then they pay zero for the B items
    else:
        return 0

def update_number_of_F_items(number_of_items_in_inventory: dict) ->int:
    '''
    2F gets another F free: Offer requires 3Fs in basket. For cases such as 8Fs, customer shall pay
    for 6Fs
    '''
    return number_of_items_in_inventory["F"] - (number_of_items_in_inventory["F"] // 3)