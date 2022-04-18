### Best time to buy and sell stock (LeetCode 121)

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

answer:

https://enlear.academy/leetcode-algorithm-challenges-best-time-to-buy-and-sell-stock-4114caffb5e7

There can be different approaches. However, simple one is this:

We need to traverse the given array of integers linearly and find
- the minimum price
- the maximum profit we can make

```python
def calculate_profit(stock_prices):

    minimum = stock_prices[0]
    max_profit = 0

    for value in stock_prices:
        if value < minimum:
            minimum = value
        if (value - minimum) > max_profit:
            max_profit = value - minimum
        
    return max_profit

print(calculate_profit([7,1,5,3,6,4])) # 5
print(calculate_profit([7, 6, 4, 3, 1])) # 0
```

question id: f4dc2be1-cb6b-4ff2-9813-18c7ac3f5df7