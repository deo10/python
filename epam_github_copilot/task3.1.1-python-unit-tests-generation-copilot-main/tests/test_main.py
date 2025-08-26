
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_calculator.main import calculate_discounted_price

class TestCalculateDiscountedPrice:
	def test_valid_discount(self):
		assert calculate_discounted_price(100, 10) == 90.0
		assert calculate_discounted_price(200, 25) == 150.0
		assert calculate_discounted_price(50.0, 20) == 40.0

	def test_zero_discount(self):
		assert calculate_discounted_price(100, 0) == 100.0

	def test_full_discount(self):
		assert calculate_discounted_price(100, 100) == 0.0

	def test_float_inputs(self):
		# 99.99 - (99.99 * 0.155) = 84.49155
		assert calculate_discounted_price(99.99, 15.5) == pytest.approx(84.49155)

	def test_invalid_type_original_price(self):
		with pytest.raises(TypeError):
			calculate_discounted_price("100", 10)

	def test_invalid_type_discount_percentage(self):
		with pytest.raises(TypeError):
			calculate_discounted_price(100, "10")

	def test_negative_discount(self):
		with pytest.raises(ValueError):
			calculate_discounted_price(100, -5)

	def test_discount_above_100(self):
		with pytest.raises(ValueError):
			calculate_discounted_price(100, 150)

	def test_zero_price(self):
		assert calculate_discounted_price(0, 50) == 0.0

	def test_negative_price(self):
		assert calculate_discounted_price(-100, 10) == -90.0

