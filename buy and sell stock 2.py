for price in prices[::-1]:
    if not sell:
        sell = price
    elif price > sell and buy is None:
        sell = price
    else:
        if buy is None:
            buy = price
        elif buy and price < buy:
            buy = price
        else:
            profit += (sell - buy)
            sell, buy = price, None
if buy is not None:
    profit += (sell - buy)
return profit