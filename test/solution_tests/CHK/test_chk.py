from solutions.CHK import checkout_solution

# Integration Testing
class TestCheckout():
    
    # def test_checkout_value_when_no_special_offer_and_valid_items(self):
    #     assert checkout_solution.checkout("ABCD") == 115

    # def test_checkout_value_when_multiple_special_offers_and_valid_items(self):
    #     assert checkout_solution.checkout("AABBCDABA") == 290

    # def test_checkout_value_when_invalid_items(self):
    #     assert checkout_solution.checkout("ABCD1234") == -1
    
    # # Create a parameterised test to check all combinations
    # def test_checkout_value_when_multiple_offers_for_A(self):
    #     assert checkout_solution.checkout("AAAAAAAAAAAAAA") == 580
    
    # def test_checkout_value_when_free_B_and_B_not_in_inventory(self):
    #     assert checkout_solution.checkout("ACDEEE") == 205
        
    # def test_checkout_value_when_free_B_less_than_B_in_inventory(self):
    #     assert checkout_solution.checkout("ABCDEEE") == 205

    # def test_checkout_value_when_free_B_greater_than_B_in_inventory(self):
    #     assert checkout_solution.checkout("ABEEEEE") == 250

    # # Create a parameterised test to check all combinations
    # def test_checkout_value_when_offer_valid_for_F_item(self):
    #     assert checkout_solution.checkout("AFFFFFFFFF") == 110
    
    # def test_checkout_value_when_offer_invalid_for_F_item(self):
    #     assert checkout_solution.checkout("AFF") == 70

    # def test_checkout_value_when_offer_valid_for_F_item(self):
    #     assert checkout_solution.checkout("ANNNMMN") == 225
        
    def test_checkout_value_when_single_group_discounts(self):
        assert checkout_solution.checkout("ASTBXZ") == 146

    # def test_checkout_value_when_multiple_group_discounts(self):
    #     assert checkout_solution.checkout("ASTBXZZY") == 225
    
    # def test_checkout_value_when_two_items_left_after_group_discount(self):
    #     assert checkout_solution.checkout("ASTBX") == 225
    
