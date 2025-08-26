def portfolio_performance_analyzer(portfolio_data):
    total_invested = 0
    total_current_value = 0
    total_profit_or_loss = 0
    insights = []
    # Loop through each investment in the portfolio
    for investment in portfolio_data:
        asset_type, quantity, purchase_price, current_price, purchase_date = investment['assetType'], investment[
            'quantity'], investment['purchasePrice'], investment['currentPrice'], investment['purchaseDate']
        if quantity <= 0 or purchase_price <= 0 or current_price <= 0:
            raise ValueError("Quantity, purchase price and current price should be greater than 0.")
        # Calculate total amounts
        invested_amount = purchase_price * quantity
        current_amount = current_price * quantity
        profit_or_loss = current_amount - invested_amount
        # Update total values
        total_invested += invested_amount
        total_current_value += current_amount
        total_profit_or_loss += profit_or_loss
        # Push the insights for individual investment
        insights.append({
            'assetType': asset_type,
            'purchaseDate': purchase_date,
            'investedAmount': invested_amount,
            'currentAmount': current_amount,
            'profitOrLoss': round(profit_or_loss, 2)  # Rounding off to 2 decimal places
        })
        # Calculate overall insights
    percentage_change = round((total_profit_or_loss / total_invested) * 100, 2) if total_invested != 0 else 0
    overall_performance = {
        'totalInvested': round(total_invested, 2),
        'totalCurrentValue': round(total_current_value, 2),
        'totalProfitOrLoss': round(total_profit_or_loss, 2),
        'percentageChange': percentage_change,
        'individualInsights': insights

    }
    return overall_performance
