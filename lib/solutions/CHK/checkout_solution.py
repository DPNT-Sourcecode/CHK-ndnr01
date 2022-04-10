from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''
    skus: String of items 
    @return: Total checkout value
    '''
    # Item price list
    dict_of_items = {"A": 50, "B": 30, "C": 20, "D": 15}
    
    # Dictionary of frequency of items in inventory
    number_of_items_in_inventory = Counter(skus)
    
        
    # if is_illegal_argument(skus):
    #     return 1
    # return 0

# def is_illegal_argument(skus):
#     ''' Check for illegal argument'''
#     return skus[0].isalpha()

def calculate_final_checkout_value(number_of_items_in_inventory: dict) -> int:
    for item in number_of_items_in_inventory:
        
    






