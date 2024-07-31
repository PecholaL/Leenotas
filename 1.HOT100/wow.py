from typing import List


class Solution:

    # 128.最长连续序列
    def longestConsecutive(self, nums: List[int]) -> int:
        # 字典用于存储key所在区间的最长子序列长度
        len_dict = {}
        res = 0
        for num in nums:
            # 当num不在字典中时，其左右两个值对应的长度即自己作为端点时
            if num not in len_dict:
                left = len_dict.get(num - 1, 0)
                right = len_dict.get(num + 1, 0)
                tmp_len = left + right + 1
                if tmp_len > res:
                    res = tmp_len
                # 只用更新当前num以及所在区间的端点的长度值，因为区间中的端点已不再会遍历到
                len_dict[num] = tmp_len
                len_dict[num - left] = tmp_len
                len_dict[num + right] = tmp_len
        return res

    # 15.三数之和
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 双指针分别指向nums[i]之后的数组两端
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # 注意即使刚好和为0，还可能存在其他的lr与nums[i]和为0
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # 以下两个while循环将指针分别指向下一个不同的数，为了防止结果出现重复
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l, r = l + 1, r - 1
                # 和小于0则需要将左指针右移
                elif s < 0:
                    l += 1
                # 和大于0则需要将右指针左移
                else:
                    r -= 1
        return res
