from typing import List


class Solution:

    # 42.接雨水
    def trap(self, height: List[int]) -> int:
        # 对于每一个坐标，其上的最大盛水量为(min(左边最高高度,右边最大高度)-自身高度)
        # 用两个数组分别存放每个点的左边最高高度和右边最高高度
        if len(height) <= 1:
            return 0
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        res = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return res
