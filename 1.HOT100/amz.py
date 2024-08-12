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

    # 560.和为k的子数组
    # 将子数组的和转换为两个前缀和之差为k的情形（前缀和：从数组起始到当前位置的总和）
    # 因为数组中可能有负数，同样的前缀和可能有多种情形，用字典记录前缀和出现的次数
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, pre = 0, 0
        dict = {}
        dict[0] = 1
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in dict:
                res += dict[pre - k]
            tmp = dict[pre] if pre in dict else 0
            dict[pre] = tmp + 1
        return res

    # 239.滑动窗口最大值
    # 使用一个双端队列维护窗口，队列需要满足：
    #   队列仅包含窗口内的元素，元素递减
    #   每次窗口移动需要删除队列内对应的元素
    #   每次窗口移动需要向队列添加新元素，并且删除中比新增元素小的元素
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections

        deque = collections.deque()
        res, n = [], len(nums)
        # i,j分别是队列对应的窗口起点和终点，i<0时代表刚开始正在往空队列里添加元素
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res

    # 287.寻找重复数
    # nums长度为n+1，其中的数均在区间[1,n]内，寻找唯一的重复数（可能重复多次）
    # 将 0到n共n+1个数 与 nums中的数 建立映射关系。如：
    # 0 1 2 3 4
    # 1 3 4 2 2，f(0)=1,f(1)=3...
    # 可以形成一个带有环的链：0-1-3-2-4-2
    # 用快慢指针找到相遇点后再找寻环的起点（Floyd判圈算法）
    def findDuplicate(self, nums: List[int]) -> int:
        i, j = nums[0], nums[nums[0]]
        while i != j:
            i = nums[i]
            j = nums[nums[j]]
        res = 0
        while res != i:
            res = nums[res]
            i = nums[i]
        return res
