from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''
    skus: String of items 
    @return: Total checkout value
    '''
    # Item price list
    price_of_items = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    
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
            # Special Offer E
            elif item == "E":
                checkout_value_E, number_of_B_items=calculate_special_offer_for_E(item, number_of_items_in_inventory, price_of_items)
                final_checkout_value+=checkout_value_E
                number_of_items_in_inventory["B"] = number_of_B_items
            # Special Offer B
            elif item == "B":
                final_checkout_value+=calculate_special_offer_for_B(item, number_of_items_in_inventory, price_of_items)
            else:
                final_checkout_value = final_checkout_value + number_of_items_in_inventory[item]*price_of_items[item]
    return final_checkout_value

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

def calculate_special_offer_for_B(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    2B for 45
    '''
    print(number_of_items_in_inventory)
    number_of_items_out_of_offer = number_of_items_in_inventory[item] % 2
    number_of_items_in_offer = number_of_items_in_inventory[item] // 2
    return (number_of_items_out_of_offer*price_of_items[item]) + (number_of_items_in_offer*45)

def calculate_special_offer_for_E(item: str, number_of_items_in_inventory: dict, price_of_items: dict) -> int:
    '''
    2E gives free B
    This assumes that if B alread in inventory, then it will not be charged. If B not in inventory, it
    will be given as free rather than price of B being reduced from the final checkout value
    '''
    number_of_free_B_items= number_of_items_in_inventory[item] // 2
    number_of_B_items = update_number_of_B_items(number_of_items_in_inventory, number_of_free_B_items)
    return (number_of_items_in_inventory[item]*price_of_items[item], number_of_B_items)

def update_number_of_B_items(number_of_items_in_inventory: dict, number_of_free_B_items: dict) -> int:
    '''
    Updates the number of B items customer is required to pay based on the number
    of free B items they get. This assumes that if B alread in inventory, then it will not be charged. 
    If B not in inventory, it will be given as free rather than price of B being reduced 
    from the final checkout value
    Note: Number of B items are changed to manage this requirement rather than the checkout price
    '''
    # If item B exists in inventory
    if "B" in number_of_items_in_inventory:
        number_of_items_of_B = number_of_items_in_inventory["B"]
        # Checks if customer has more B items than the free B items
        if number_of_items_of_B > number_of_free_B_items:
             return number_of_items_of_B - number_of_free_B_items
        # If less bought items than free, then they pay zero for the B items
        else:
            return 0

checkout("ABCDEEE")
#============ IMPROVEMENTS=========#
'''
1a. Rearchitecture the code into separate files etc
1b. Allows to write better unit tests
2. Extract the common functionality i.e. // and % into separate function as repeated
'''





