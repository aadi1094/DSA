prices=[7,1,5,3,6,4]

def max_profit(prices):
    max_profit = 0
    start=prices[0]
    for i in range(1,len(prices)):
        if prices[i]<start:
            start=prices[i]
        else:
            max_profit=max(max_profit,prices[i]-start)
    return max_profit

print(max_profit(prices))  # Output: 5
           