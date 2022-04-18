###  Best time to buy and sell stock II (LeetCode 122)

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
Examples:

[8, 2, 5, 1, 6]

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Write a function that returns the maximum profit you can achieve buying stocks on a dip
and selling on high.

Expected results:
[1, 2, 3, 4, 5, 6, 7, 8, 9]  # maximum profit is 8
[9, 8, 7, 6, 5, 4, 3, 2, 1] # maximum profit is 0
[8, 2, 5, 1, 6]   # 8 (buy on 2, sell on 5, then buy on 1 and sell on 6) 
[1, 5, 7, 3, 8] # 11 (buy on 1, sell on 7, then buy on 3 and sell on 8)

answer:

All you really need to do is iterate over the array,
compare i and i+1 values, and if i+1 is bigger than i,
you add this difference to previous stored differences.

```python
import typing as tp

def calculate_profit(stock_prices: tp.List[int]) -> int:
    
    total_profit = 0
    for i, left in enumerate(stock_prices):
        try:
            right = stock_prices[i+1]
        except IndexError:
            return total_profit
        if right > left:
            total_profit += right - left
    return total_profit

print(calculate_profit([1, 2, 3, 4, 5, 6, 7, 8, 9])) # maximum profit is 8
print(calculate_profit([9, 8, 7, 6, 5, 4, 3, 2, 1])) # maximum profit is 0
print(calculate_profit([8, 2, 5, 1, 6])) # 8 (buy on 2, sell on 5, then buy on 1 and sell on 6) 
print(calculate_profit([1, 5, 7, 3, 8])) # 11 (buy on 1, sell on 7, then buy on 3 and sell on 8) 
```

question id: e237f0fc-4ca8-453d-bcbd-00e19fee6440