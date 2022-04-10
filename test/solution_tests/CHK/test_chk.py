from solutions.CHK import checkout_solution

class TestCheckout():
    
    def test_checkout_value_when_no_special_offer_and_valid_items(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_value_when_multiple_special_offers_and_valid_items(self):
        assert checkout_solution.checkout("AABBCDABA") == 290

    def test_checkout_value_when_invalid_items(self):
        assert checkout_solution.checkout("ABCD1234") == -1
    
    
    def test_checkout_value_when_multiple_offers_for_A(self):
        assert checkout_solution.checkout("AAAAAAAAAAAAAA") == 580
        

