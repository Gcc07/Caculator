import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()


class TestAdd:
    def test_add_method(self, calc):
        assert calc.add(2, 3) == 5

    def test_add_negatives(self, calc):
        assert calc.add(-4, -5) == -9

    def test_add_floats(self, calc):
        assert calc.add(3.1, 4.3) == pytest.approx(7.4)

    def test_add_small_number(self, calc):
        assert calc.add(0.000000000000000000000000000001, 1.0) == pytest.approx(1.000000000000000000000000000001)

class TestSubtract:
    def test_subtract_method(self, calc):
        assert calc.subtract(2, 3) == -1

    def test_subtract_negatives(self, calc):
        assert calc.subtract(-4, -5) == 1

    def test_subtract_floats(self, calc):
        assert calc.subtract(3.1, 4.3) == pytest.approx(-1.2)

class TestMultiply:
    def test_multiply_method(self, calc):
        assert calc.multiply(2, 3) == 6

    def test_multiply_floats(self, calc):
        assert calc.multiply(3.14, 2.8) == pytest.approx(8.792)

class TestDivide:
    def test_even_division(self, calc):
        assert calc.divide(4, 2) == 2

    def test_float_division(self, calc):
        assert calc.divide(3.14, 2.8) == pytest.approx(1.12142857143)

    def test_zero_divisor_raises(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(3, 0)

    def test_negative_divide(self, calc):
        assert calc.divide(3, -1) == -3

class TestPower:
    def test_power_method(self, calc):
        assert calc.power(2, 3) == 8

    def test_power_zero(self, calc):
        assert calc.power(2, 0) == 1

    def test_power_one_half(self, calc):
        assert calc.power(2, 0.5) == pytest.approx(1.41421356237)

    def test_negative_base(self, calc):
        with pytest.raises(ValueError):
            calc.power(-2, 0.5)

class TestSquareRoot:
    def test_square_root_method(self, calc):
        assert calc.square_root(4) == 2

    def test_square_root_negative_one(self, calc):
        with pytest.raises(ValueError):
            calc.square_root(-1)

    def test_square_root_zero(self, calc):
        assert calc.square_root(0) == 0

    def test_square_root_float(self, calc):
        assert calc.square_root(3.14) == pytest.approx(1.77200451467)

class TestModulus:
    def test_modulus_method(self, calc):
        assert calc.modulus(5, 2) == 1

    def test_modulus_negative(self, calc):
        assert calc.modulus(5, -3) == -1

    def test_zero_modulus_divisor(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.modulus(2, 0)

class TestFloorDivide:
    def test_floor_divide_method(self, calc):
        assert calc.floor_divide(4, 3) == 1

    def test_zero_floor_divide_divisor(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.floor_divide(2, 0)

class TestIntegration:
    def test_integration_add(self, calc):
            assert calc.add(calc.subtract(2, 1), 3) == 4

    def test_integration_with_power(self, calc):
        assert calc.power(calc.subtract(3, 1), 2) == 4

