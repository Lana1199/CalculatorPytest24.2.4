import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,2,2) == 4

    def test_multiply_success(self):
        assert self.calc.multiply(self,4,2) == 8

    def test_division_success(self):
        assert self.calc.division(self,10,2) == 5

    def test_zero_division(selfs):
        with pytest.raises(ZeroDivisionError):
            selfs.calc.division(selfs,2,0)

    def test_subtraction_success(self):
        assert self.calc.subtraction(self,6,4) == 2

    def teardown(self):
        print('Выполнение метода Teardown')



