from typing import List


class Solution:

    # 最长连续序列
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
