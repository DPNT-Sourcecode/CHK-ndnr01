

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    skus: String of items 
    @return: Total checkout value
    '''
    dict_of_items = {"A": 50, "B": 30, "C": 20, "D": 15}
    
    for item in skus:
        if item not in dict_of_items:
            return -1
        
    # if is_illegal_argument(skus):
    #     return 1
    # return 0

# def is_illegal_argument(skus):
#     ''' Check for illegal argument'''
#     return skus[0].isalpha()



