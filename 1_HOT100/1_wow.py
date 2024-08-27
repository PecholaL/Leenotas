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

    # 3.无重复长度的最长子串
    # 双指针滑动窗口，但是注意指针j不用每次回退到i的位置
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hset = set()
        i, j = 0, 0
        while i < len(s) - res:
            # 这里注意，窗口滑到下一个位置，需要取出上一个窗口起点的元素
            if i != 0:
                hset.remove(s[i - 1])
            # j始终不需要回退，如果重复元素在窗口中靠右，窗口也会滑动到这个重复元素处（一直break）
            while j < len(s):
                if s[j] in hset:
                    break
                else:
                    hset.add(s[j])
                    j += 1
            res = max(res, len(hset))
            i += 1
        return res

    # 76.最小覆盖子串
    def minWindow(self, s: str, t: str) -> str:
        import collections

        cnt_t = collections.Counter(t)
        res_i, res_j = 0, 0
        i, j = 0, 0
        flag = 0
        min_length = float("inf")
        # 起步会一直跳过内层while循环而一直执行外层while直到窗口䏻覆盖t
        while j < len(s):
            if s[j] in cnt_t:
                cnt_t[s[j]] -= 1
                if cnt_t[s[j]] == 0:
                    flag += 1
            j += 1
            # 窗口能覆盖t后尝试从左边缩短窗口，直到无法覆盖t
            while flag == len(cnt_t):
                # 先删去左边不在t中的部分（一直跳过if）
                if s[i] in cnt_t:
                    cnt_t[s[i]] += 1
                    if cnt_t[s[i]] > 0:
                        flag -= 1
                    # 记下当前最优解
                    # （当前最优一定是最左边的元素在t中）
                    if j - i < min_length:
                        res_i, res_j = i, j
                        min_length = j - i
                i += 1
        return s[res_i:res_j]

    # 238.除自身以外数组的乘积
    # 要求不能用除法
    # 建立前缀和后缀乘积数组，分别存储第i位左边所有元素的乘积和右边所有元素的乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        leftProductList, rightProductList = [1] * len(nums), [1] * len(nums)
        leftProduct, rightProduct = 1, 1
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            leftProductList[i] = leftProduct
            rightProductList[j] = rightProduct
            if i < len(nums) - 1 and j > 0:  # 减少不必要计算
                leftProduct *= nums[i]
                rightProduct *= nums[j]
        for i in range(len(answer)):
            answer[i] = leftProductList[i] * rightProductList[i]
        return answer

    # 31.下一个排列
    def nextPermutation(self, nums: List[int]) -> None:
        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        # 从尾部开始寻找相邻且前比后小的两数，找到后这两个数之后遍历过的数一定是降序的
        while i >= 0 and nums[i] >= nums[j]:
            i, j = i - 1, j - 1
        # 从尾部的降序序列中从后往前找最小的比nums[i]大的数作为与nums[i]交换的数
        # 这样可以保证变化幅度尽可能小
        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
        # 交换之后的尾部仍然一定是降序的，将其反转以得到下一个序列
        for p, q in zip(range(j, len(nums)), range(len(nums) - 1, i, -1)):
            if p < q:
                nums[p], nums[q] = nums[q], nums[p]
            else:
                break
        return

    # 437.二叉树路径和III
    # 在遍历的过程中记录下当前路径和，并查找是否有与之匹配的前缀路径和使差值为tgt
    def pathSum(self, root, targetSum: int) -> int:
        self.preSum = {}  # 记录遍历过的路径和，每种和的数量
        self.preSum[0] = 1
        self.targetSum = targetSum
        return self.trav(root, 0)

    def trav(self, root, curSum):
        if root is None:
            return 0
        res = 0
        curSum += root.val  # 当前路径和
        res += (
            self.preSum[curSum - self.targetSum]  # 寻找是否有合适的前缀路径和
            if curSum - self.targetSum in self.preSum
            else 0
        )
        # 将当前路径和保存
        if curSum in self.preSum:
            self.preSum[curSum] += 1
        else:
            self.preSum[curSum] = 1
        res += self.trav(root.left, curSum)
        res += self.trav(root.right, curSum)
        # 遍历完左右子树后会退到父结点，记得将当前路径和的记录减去
        self.preSum[curSum] -= 1
        return res

    # 124.二叉树中的最大路径和
    def maxPathSum(self, root):
        self.res = float("-inf")
        self.depth(root)
        return self.res

    # 递归深度遍历二叉树，记录最大路径和
    def depth(self, node):
        if node is None:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        # 记录将当前结点左右两边的子树纳入路径时是否可最大
        self.res = max(self.res, left + right + node.val)
        # 当前结点的价值：将以该结点为根的子树纳入路径中得到的回报
        # 由于可以不纳入，即回报为负数时，故取max(val,0)
        return max(max(left, right) + node.val, 0)

    # 207.课程表
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 建立有向图，使依赖的课程指向当前课程
        ind = [0] * numCourses  # 存储各课程结点的入度（依赖课程数）
        adjac = [[] for _ in range(numCourses)]  # 存储各课程的后置课程
        import collections

        q = collections.deque()
        for cur, pre in prerequisites:
            ind[cur] += 1
            adjac[pre].append(cur)
        # 找到不需要依赖的所有课程（入度为0）
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        # 逐步从图中减去这些不需要依赖的课程（表示可以完成）
        # 并将依赖这门课程的课入度-1（依赖中已完成一个，即依赖少一个）
        while q:
            pre = q.popleft()
            numCourses -= 1
            for cur in adjac[pre]:
                ind[cur] -= 1
                if ind[cur] == 0:
                    q.append(cur)
        return True if numCourses == 0 else False

    # 739.每日温度
    # 记录相对于第i天，下一次更高气温出现在几天后
    # 使用单调栈存储下标，栈顶到栈底下标对应的温度递增
    # res数组延迟更新，直到对应的下标从栈中弹出才能知道表示下一次最高温度出现
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_index = stack.pop()
                res[pre_index] = i - pre_index
            stack.append(i)
        return res

    # 4.寻找两个正序数组的中位数
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.findKth(nums1, nums2, (m + n + 1) // 2)
        else:
            return (
                self.findKth(nums1, nums2, (m + n) // 2)
                + self.findKth(nums1, nums2, (m + n) // 2 + 1)
            ) / 2

    # 从两个正序数组找到第k位
    # 比较两个数组中的第k//2位
    # 由此可排除第k//2位较小的数组的前k//2位（一定比整体的第k位小）
    # 根据排除的数量减小k的值
    def findKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        i1, i2 = 0, 0
        while True:
            if i1 == m:
                return nums2[i2 + k - 1]
            if i2 == n:
                return nums1[i1 + k - 1]
            if k == 1:
                return min(nums1[i1], nums2[i2])

            i1_ = min(i1 + k // 2 - 1, m - 1)
            i2_ = min(i2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[i1_], nums2[i2_]
            if pivot1 <= pivot2:
                k -= i1_ - i1 + 1
                i1 = i1_ + 1
            else:
                k -= i2_ - i2 + 1
                i2 = i2_ + 1

    # 763.划分字母区间
    # 要求：把给定字符串划分为尽可能多的片段，同一字母最多出现在一个片段中
    # 贪心策略
    def partitionLabels(self, s: str) -> List[int]:
        res = 0
        # 记录每个字母在字符串中出现的最后位置
        lastPos = [0] * 26
        for i, ch in enumerate(s):
            lastPos[ord(ch) - ord("a")] = i
        # 开始从头划分
        res = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            # 对于第i个字符ch，其应在当前字符串中
            # 且ch在s中出现的最后位置应该不大于当前字符串的end
            end = max(end, lastPos[ord(ch) - ord("a")])
            # 贪心策略：当处理的字符追上了end，应立即切片，即更新start
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

    # 32.最长有效括号串长度
    # dp[i]表示以s[i]结尾的最长有效括号串长度
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":  # s[i]=='('时则无法作为有效括号串结尾，dp[i]为0
                # 前一位为'('，末尾两位'()'䏻增加2位有效串长度
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                # 前一位为')'，如果前一位结尾的有效串之前一位(s[i-dp[i-1]-1])为'('，则可为有效串长度增加2位
                # （将以s[i-1]结尾的有效串扩起来的情形）
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = (
                        dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        if i - dp[i - 1] >= 2
                        else dp[i - 1] + 2
                    )
        return max(dp)
