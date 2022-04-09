from solutions.HLO import hello_solution

class TestSum():
    
    def test_hello_friend(self):
        assert hello_solution.hello("John") == "Hello, John!"


