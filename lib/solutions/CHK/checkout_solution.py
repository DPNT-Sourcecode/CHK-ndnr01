

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    skus: 
        skus[0] = String containing the SKUs of all the products in the basket
        skus[1] = ?
        skus [..N] = ?
    @return: Total checkout value
    '''
    #---Debug Code-----#
    # for i in range(len(skus)):
    print(skus)
    # -------------#
    
    # if is_illegal_argument(skus):
    #     return 1
    # return 0

# def is_illegal_argument(skus):
#     ''' Check for illegal argument'''
#     return skus[0].isalpha()
