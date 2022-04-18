import typing as tp


def calculate_profit(stock_prices: tp.List[int]) -> int:
    bought = False
    price_bought = 0
    total_profit = 0

    for i, left in enumerate(stock_prices):
        try:
            right = stock_prices[i + 1]
        except IndexError:
            if bought and left > price_bought:
                # print(f"{left=}")
                # print(f"{price_bought}")
                total_profit += left - price_bought
                return total_profit

        if left < right and not bought:  # then buy
            # print(f'buy for {left}')
            bought = True
            price_bought = left

        elif left > right and bought:  # then sell
            # print(f'sell with profit of {left - price_bought}')
            total_profit += left - price_bought
            price_bought = 0
            bought = False

    return total_profit


def calculate_profit2(stock_prices: tp.List[int]) -> int:
    
    total_profit = 0
    for i, left in enumerate(stock_prices):
        try:
            right = stock_prices[i+1]
        except IndexError:
            return total_profit
        if right > left:
            total_profit += right - left
    return total_profit

# print(calculate_profit2([1, 2, 3, 4, 5, 6, 7, 8, 9])) # maximum profit is 8
# print(calculate_profit2([9, 8, 7, 6, 5, 4, 3, 2, 1])) # maximum profit is 0
# print(calculate_profit2([8, 2, 5, 1, 6])) # 8 (buy on 2, sell on 5, then buy on 1 and sell on 6) 
# print(calculate_profit2([1, 5, 7, 3, 8])) # 11 (buy on 1, sell on 7, then buy on 3 and sell on 8) 

def calculate_profit3(stock_prices):
    stock_prices_sorted = sorted(stock_prices)
    print(stock_prices_sorted)
    
    low = stock_prices_sorted[0]
    for i in range(len(stock_prices)):
        print(f'{low=}')
        high = stock_prices_sorted[0 - (i+1)]
        print(f'{high=}')

        low_index = stock_prices.index(low)
        high_index = stock_prices.index(high)

        if low_index > high_index:
            continue

        if low_index < high_index:
            return high - low

    return 0


def calculate_profit3(stock_prices):

    minimum = stock_prices[0]
    max_profit = 0

    for value in stock_prices:
        if value < minimum:
            minimum = value
        if (value - minimum) > max_profit:
            max_profit = value - minimum
        
    return max_profit


    

# print(calculate_profit3([7,1,5,3,6,4])) # 5
# print(calculate_profit3([7, 6, 4, 3, 2, 1])) # 0
print(calculate_profit3([7,1,5,3,6,4])) # 5
print(calculate_profit3([7, 6, 4, 3, 1])) # 0