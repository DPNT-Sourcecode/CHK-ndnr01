

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
    # Check illegal argument
    if skus[0].isalpha():
        return True
    return False

def check_illegal_argument(skus):
    '''
    '''
    if skus[0].isalpha():
        return True
    return False


