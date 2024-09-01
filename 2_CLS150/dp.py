# 面试经典150题中的一些有趣的DP问题
from typing import List


# 122. 买卖股票的最佳时机 II
# 给定一个数组，它的第i个元素是一支给定的股票在第i天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 解：dp[i][j]表示第i天，分别在状态j=0或1时的最大利润（j=0表示不持有股票，j=1表示持有股票）
def maxProfit(prices: List[int]) -> int:
    l = len(prices)
    if l < 2:
        return 0
    dp = [[0] * 2 for _ in range(l)]
    dp[0][1] = -prices[0]  # 持有股票相当于处于亏损状态

    for i in range(1, l):
        # 第i天不持有股票，则最大利润可能是延续前一天不持有股票，或者前一天持有股票并在当天卖出
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # 第i天持有股票，则最大利润可能是延续前一天持有股票，或者前一天不持有股票并在当天买入
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
    return dp[-1][0]
