
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_calculator.main import calculate_discounted_price_with_tax

class TestCalculateDiscountedPriceWithTax:
	def test_valid_discount_no_tax(self):
		assert calculate_discounted_price_with_tax(100, 10) == 90.0
		assert calculate_discounted_price_with_tax(200, 25) == 150.0
		assert calculate_discounted_price_with_tax(50.0, 20) == 40.0

	def test_valid_discount_with_tax(self):
		# 100 - 10% = 90; tax 10% = 9; total = 99
		assert calculate_discounted_price_with_tax(100, 10, 10) == 99.0
		# 200 - 25% = 150; tax 5% = 7.5; total = 157.5
		assert calculate_discounted_price_with_tax(200, 25, 5) == 157.5

	def test_zero_discount(self):
		assert calculate_discounted_price_with_tax(100, 0) == 100.0
		assert calculate_discounted_price_with_tax(100, 0, 10) == 110.0

	def test_full_discount(self):
		assert calculate_discounted_price_with_tax(100, 100) == 0.0
		assert calculate_discounted_price_with_tax(100, 100, 10) == 0.0

	def test_float_inputs(self):
		# 99.99 - (99.99 * 0.155) = 84.49155
		assert calculate_discounted_price_with_tax(99.99, 15.5) == pytest.approx(84.49155)
		# with tax: 84.49155 + 8.449155 = 92.940705
		assert calculate_discounted_price_with_tax(99.99, 15.5, 10) == pytest.approx(92.940705)

	def test_invalid_type_original_price(self):
		with pytest.raises(TypeError):
			calculate_discounted_price_with_tax("100", 10)

	def test_invalid_type_discount_percentage(self):
		with pytest.raises(TypeError):
			calculate_discounted_price_with_tax(100, "10")

	def test_invalid_type_tax_rate(self):
		with pytest.raises(TypeError):
			calculate_discounted_price_with_tax(100, 10, "5")

	def test_negative_discount(self):
		with pytest.raises(ValueError):
			calculate_discounted_price_with_tax(100, -5)

	def test_discount_above_100(self):
		with pytest.raises(ValueError):
			calculate_discounted_price_with_tax(100, 150)

	def test_zero_price(self):
		assert calculate_discounted_price_with_tax(0, 50) == 0.0
		assert calculate_discounted_price_with_tax(0, 50, 10) == 0.0

	def test_negative_price(self):
		assert calculate_discounted_price_with_tax(-100, 10) == -90.0
		# -100 - 10% = -90; tax 10% = -9; total = -99
		assert calculate_discounted_price_with_tax(-100, 10, 10) == -99.0

	def test_negative_tax(self):
		with pytest.raises(ValueError):
			calculate_discounted_price_with_tax(100, 10, -5)

	def test_tax_above_100(self):
		with pytest.raises(ValueError):
			calculate_discounted_price_with_tax(100, 10, 150)


