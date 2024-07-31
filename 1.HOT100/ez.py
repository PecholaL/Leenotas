from typing import List


class Solution:

    # 1.两数之和
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [i, dict[target - nums[i]]]
            dict[nums[i]] = i
        return []

    # 49.字母异位词分组
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dict = {}
        for str in strs:
            # 关键在于用组成字母的有序排列作为key
            k = "".join(sorted(list(str)))
            if k not in dict:
                dict[k] = [str]
            else:
                dict[k].append(str)
        for key in dict:
            res.append(dict[key])
        return res

    # 283.双指针移动0
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 0:
            return
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

    # 11.盛最多水的容器
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while i != j:
            s = (j - i) * min(height[i], height[j])
            if s > res:
                res = s
            (i, j) = (i + 1, j) if height[i] < height[j] else (i, j - 1)
        return res
