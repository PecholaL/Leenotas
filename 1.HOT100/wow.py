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

    # 160.相交链表
    def getIntersectionNode(self, headA, headB):
        # 重点在于消除两链表的长度差
        # 两个指针分别从两个链表头开始移动，使短链表指针移到末尾后又指向长链表的头
        # 指向长链表的指针移长度差个结点后到达末尾又指向短链表头，由此消除长度差
        # 两个指针在两个链表上继续移动直到指向相同结点
        # 不存在相同结点时则都指向尾部None后相等退出循环并返回
        ptrA = headA
        ptrB = headB
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA != None else headB
            ptrB = ptrB.next if ptrB != None else headA
        return ptrA

    # 234.回文链表
    # 虽然是简单题，但递归方法的递归过程有点意思，空间复杂度还是和粗暴方法同O(N)
    # 简单的粗暴方法：将链表前半部分存储到数组中再比较
    # 这个递归比较震撼，递归到最后一个结点，出栈回退时头结点指针同步后移
    def isPalindrome(self, head) -> bool:
        self.ptr = head

        def palindromeCheck(cnode=head):
            if cnode is not None:
                if not palindromeCheck(cnode.next):
                    return False
                if self.ptr.val != cnode.val:
                    return False
                self.ptr = self.ptr.next
            return True

        return palindromeCheck()
