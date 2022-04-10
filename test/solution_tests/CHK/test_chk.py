from solutions.CHK import checkout_solution

# Integration Testing
class TestCheckout():
    
    def test_checkout_value_when_no_special_offer_and_valid_items(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_value_when_multiple_special_offers_and_valid_items(self):
        assert checkout_solution.checkout("AABBCDABA") == 290

    def test_checkout_value_when_invalid_items(self):
        assert checkout_solution.checkout("ABCD1234") == -1
    
    # Create a parameterised test to check all combinations
    def test_checkout_value_when_multiple_offers_for_A(self):
        assert checkout_solution.checkout("AAAAAAAAAAAAAA") == 580
    
    def test_checkout_value_when_free_B_and_B_not_in_inventory(self):
        assert checkout_solution.checkout("ACDEEE") == 205
        
    def test_checkout_value_when_free_B_less_than_B_in_inventory(self):
        assert checkout_solution.checkout("ABCDEEE") == 205

    # def test_checkout_value_when_free_B_greater_than_B_in_inventory(self):
    #     assert checkout_solution.checkout("ABCD") == 580