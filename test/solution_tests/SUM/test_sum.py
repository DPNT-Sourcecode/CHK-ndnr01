from solutions.SUM import sum_solution


class TestSum():
    def test_sum_set_1(self):
        assert sum_solution.compute(1, 2) == 3
        
    def test_sum_set_2(self):
        assert sum_solution.compute(10, 20) == 30


