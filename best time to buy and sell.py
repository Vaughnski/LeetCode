profit = 0
        max_sell = prices[len(prices)-1]
        for buy in prices[::-1]:
            if(max_sell - buy > profit):
                profit = max_sell - buy
            if(buy > max_sell):
                max_sell = buy
        return profit
