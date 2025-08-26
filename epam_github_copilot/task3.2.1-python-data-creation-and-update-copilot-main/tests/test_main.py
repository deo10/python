import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'portfolio_analyzer')))
from main import portfolio_performance_analyzer

def test_single_stock_positive_return():
	portfolio = [
		{
			'assetType': 'Stock',
			'quantity': 10,
			'purchasePrice': 100.0,
			'currentPrice': 120.0,
			'purchaseDate': '2022-01-01'
		}
	]
	result = portfolio_performance_analyzer(portfolio)
	assert result['totalInvested'] == 1000.0
	assert result['totalCurrentValue'] == 1200.0
	assert result['totalProfitOrLoss'] == 200.0
	assert result['percentageChange'] == 20.0
	assert result['individualInsights'][0]['profitOrLoss'] == 200.0

def test_multiple_assets_mixed_returns():
	portfolio = [
		{
			'assetType': 'Stock',
			'quantity': 5,
			'purchasePrice': 200.0,
			'currentPrice': 180.0,
			'purchaseDate': '2021-06-15'
		},
		{
			'assetType': 'Bond',
			'quantity': 20,
			'purchasePrice': 50.0,
			'currentPrice': 55.0,
			'purchaseDate': '2020-03-10'
		},
		{
			'assetType': 'ETF',
			'quantity': 8,
			'purchasePrice': 150.0,
			'currentPrice': 160.0,
			'purchaseDate': '2023-02-20'
		}
	]
	result = portfolio_performance_analyzer(portfolio)
	assert result['totalInvested'] == 3200.0
	assert result['totalCurrentValue'] == 3280.0
	assert result['totalProfitOrLoss'] == 80.0
	assert result['percentageChange'] == pytest.approx(2.5, 0.01)
	assert len(result['individualInsights']) == 3

def test_zero_quantity_raises():
	portfolio = [
		{
			'assetType': 'Stock',
			'quantity': 0,
			'purchasePrice': 100.0,
			'currentPrice': 120.0,
			'purchaseDate': '2022-01-01'
		}
	]
	with pytest.raises(ValueError):
		portfolio_performance_analyzer(portfolio)

def test_negative_price_raises():
	portfolio = [
		{
			'assetType': 'Bond',
			'quantity': 10,
			'purchasePrice': -50.0,
			'currentPrice': 55.0,
			'purchaseDate': '2020-03-10'
		}
	]
	with pytest.raises(ValueError):
		portfolio_performance_analyzer(portfolio)

def test_empty_portfolio():
	portfolio = []
	result = portfolio_performance_analyzer(portfolio)
	assert result['totalInvested'] == 0
	assert result['totalCurrentValue'] == 0
	assert result['totalProfitOrLoss'] == 0
	assert result['percentageChange'] == 0
	assert result['individualInsights'] == []

def test_realistic_portfolio_varied_dates():
	portfolio = [
		{
			'assetType': 'Stock',
			'quantity': 15,
			'purchasePrice': 80.0,
			'currentPrice': 90.0,
			'purchaseDate': '2019-11-11'
		},
		{
			'assetType': 'Crypto',
			'quantity': 2,
			'purchasePrice': 30000.0,
			'currentPrice': 25000.0,
			'purchaseDate': '2021-04-01'
		},
		{
			'assetType': 'REIT',
			'quantity': 50,
			'purchasePrice': 20.0,
			'currentPrice': 22.0,
			'purchaseDate': '2018-07-23'
		}
	]
	result = portfolio_performance_analyzer(portfolio)
	assert result['totalInvested'] == 62200.0
	assert result['totalCurrentValue'] == 52450.0
	assert result['totalProfitOrLoss'] == -9750.0
	assert result['percentageChange'] == pytest.approx(-15.68, 0.01)

