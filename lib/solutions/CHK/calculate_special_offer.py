'''
Calculates the special offers for items which help customers save money when purchased in bulk
'''
# ===========================COMBINED OFFERS========================# 
def calculate_special_offer_for_A(number_of_item: int, price_of_item: int) -> int:
    '''
    3A for 130
    5A for 200
    '''
    return _calculate_combined_offer(number_of_item=number_of_item,
                                     price_of_item=price_of_item,
                                     number_of_larger_offer=5,
                                     number_of_smaller_offer=3,
                                     value_of_larger_offer=200,
                                     value_of_smaller_offer=130)

def calculate_special_offer_for_H(number_of_item: int, price_of_item: int) -> int:
    '''
    5H for 45
    10H for 80
    '''
    return _calculate_combined_offer(number_of_item=number_of_item,
                                    price_of_item=price_of_item,
                                    number_of_larger_offer=10,
                                    number_of_smaller_offer=5,
                                    value_of_larger_offer=80,
                                    value_of_smaller_offer=45)

def calculate_special_offer_for_V(number_of_item: int, price_of_item: int) -> int:
    '''
    2V for 90
    3V for 130
    '''
    return _calculate_combined_offer(number_of_item=number_of_item,
                                    price_of_item=price_of_item,
                                    number_of_larger_offer=3,
                                    number_of_smaller_offer=2,
                                    value_of_larger_offer=130,
                                    value_of_smaller_offer=90)

# ================================================================# 

# ===========================SINGLE OFFERS========================# 

def calculate_special_offer_for_B(number_of_item: int, price_of_item: int) -> int:
    '''
    2B for 45
    '''
    return _calculate_single_offer(number_of_item= number_of_item, 
                            price_of_item= price_of_item, 
                            number_of_items_for_offer=2, 
                            value_of_offer=45)
    
def calculate_special_offer_for_K(number_of_item: int, price_of_item: int) -> int:
    '''
    2K for 120
    '''
    return _calculate_single_offer(number_of_item= number_of_item, 
                            price_of_item= price_of_item, 
                            number_of_items_for_offer=2, 
                            value_of_offer=120)

def calculate_special_offer_for_P(number_of_item: int, price_of_item: int) -> int:
    '''
    5P for 200  
    '''
    return _calculate_single_offer(number_of_item= number_of_item, 
                            price_of_item= price_of_item, 
                            number_of_items_for_offer=5, 
                            value_of_offer=200)

def calculate_special_offer_for_Q(number_of_item: int, price_of_item: int) -> int:
    '''
    3Q for 80
    '''
    return _calculate_single_offer(number_of_item= number_of_item, 
                            price_of_item= price_of_item, 
                            number_of_items_for_offer=3, 
                            value_of_offer=80)

#========================HELPER FUNCTIONS FOR OFFER CALCULATION========================================#
def _calculate_single_offer(number_of_item: int, price_of_item: int, number_of_items_for_offer: int, value_of_offer: int):
    number_of_items_out_of_offer = number_of_item % number_of_items_for_offer
    number_of_items_in_offer = number_of_item // number_of_items_for_offer
    return (number_of_items_out_of_offer*price_of_item) + (number_of_items_in_offer*value_of_offer)
    
def _calculate_combined_offer(number_of_item: int, price_of_item: int, number_of_larger_offer: int, number_of_smaller_offer: int, value_of_larger_offer: int, value_of_smaller_offer: int):
    number_of_items_in_the_larger_offer = number_of_item // number_of_larger_offer
    number_of_items_not_in_the_larger_offer = number_of_item % number_of_larger_offer
    number_of_items_in_the_smaller_offer = number_of_items_not_in_the_larger_offer // number_of_smaller_offer
    number_of_items_out_of_offer = number_of_items_not_in_the_larger_offer % number_of_smaller_offer
    return (number_of_items_in_the_larger_offer*value_of_larger_offer) + (number_of_items_in_the_smaller_offer*value_of_smaller_offer) + (number_of_items_out_of_offer*price_of_item)
#========================================================================================================#

