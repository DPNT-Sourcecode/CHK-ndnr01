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
    
        
    # if is_illegal_argument(skus):
    #     return 1
    # return 0

# def is_illegal_argument(skus):
#     ''' Check for illegal argument'''
#     return skus[0].isalpha()

def calculate_final_checkout_value(number_of_items_in_inventory: dict,
                                   price_of_items: dict) -> int:
    final_checkout_value = 0
    checkout_value =- 0
    for item in number_of_items_in_inventory:    
        if item in price_of_items:
            
            # Special Offer A
            if item == "A":
                number_of_items_out_of_offer = number_of_items_in_inventory[item] % 3
                number_of_items_in_offer = number_of_items_in_inventory[item] // 3
                checkout_value = 
    

