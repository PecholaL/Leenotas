from typing import List


class Solution:

    # 1.两数之和
    # 略

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

    # 206.反转链表
    def reverseList(self, head):
        # 值得注意的是ptr1(左指针)的初始化
        ptr1, ptr2 = None, head
        while ptr2 != None:
            tmp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = tmp
        return ptr1

    # 141.142.判断链表存在环，存在环则返回环的起始结点
    def hasCycle(self, head) -> bool:
        if head is None or head.next is None:
            return False
        ptr1, ptr2 = head, head  # ptr1,2分别为慢,快指针
        while ptr2 is not None:
            ptr1 = ptr1.next
            if ptr2.next is None:
                break
            ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                return True
                # 当需要返回环的起始结点时
                # 从两个指针相遇的时刻开始，新建一个指针从头结点开始同步移动
                #   直到和慢指针相遇，相遇处即为环的起始结点
                # 推导过程可通过对头结点到环起点、环起点到快慢指针相遇点赋参数进行关系推导
                # ptr3 = head
                # while ptr1 != ptr3:
                #     ptr1, ptr3 = ptr1.next, ptr3.next
                # return ptr3
        return False  # return None

    # 21.合并有序链表
    # 递归方法
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:  # l2.val<=l1.val
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 2.链表中的两数相加
    # 略

    # 19.删除链表倒数第n个结点
    def removeNthFromEnd(self, head, n: int):
        # 在头结点之前加入一个辅助结点可以避免对特殊情况（删除头结点）的单独处理
        pre = ListNode()  # type: ignore
        pre.next = head
        ptr1, ptr2 = pre, pre
        # 这里注意快慢指针应该相距n+1
        # 使得快指针移动到末尾None时，慢指针指向待删除结点的前一个结点
        for _ in range(n + 1):
            ptr2 = ptr2.next
        while ptr2 is not None:
            ptr1, ptr2 = ptr1.next, ptr2.next
        ptr1.next = ptr1.next.next
        return pre.next

    # 24.两两交换链表中的结点
    # 递归方法
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

    # 25.K个一组翻转链表
    # 优美的递归，居然一次过了
    def reverseKGroup(self, head, k):
        ptrH = head
        for _ in range(k):
            if ptrH:
                ptrH = ptrH.next
            else:
                return head
        newHead, newTail = self.reverseK(head, k)
        newTail.next = self.reverseKGroup(ptrH, k)
        return newHead

    def reverseK(self, head, k):
        ptr1, ptr2 = None, head
        for _ in range(k):
            ptr3 = ptr2.next
            ptr2.next = ptr1
            ptr1, ptr2 = ptr2, ptr3
        return ptr1, head

    # 138.随机链表的复制
    # 略，用哈希表存储旧-新链表结点对应关系

    # 148.排序链表
    # 略，归并排序

    # 146.LRU缓存
    # 略

    # 23.合并K个升序链表
    # 略，两两合并即可

    # 3.无重复字符的最长子串

    # 438.找到字符串中所有字母异位词
    # 滑动窗口，自己用dict写的题解不够简洁，官方题解用长为26的数组记录当前窗口和pattern串
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return res
        # 相比用Counter()创建字典计数不用判断是否存在key
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        if s_count == p_count:
            res.append(0)
        # 注意这里的循环次数，不是s_len - p_len + 1
        # 因为这个循环的意思是第i次循环抛弃s中的第i位而往后移一位
        # 结果也是相应的i+1
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                res.append(i + 1)
        return res

    # 53.最大子数组和
    # 略，动态规划，dp[i]=max(dp[i-1]+nums[i],nums[i])

    # 56.合并区间
    # 略，先要对区间排序，intervals.sort(key=lambda x: x[0])

    # 41.缺失的第一个正整数
    # 略，答案的取值范围为[1,len+1]，可借助一个数组进行标记

    # 73.矩阵置零
    # 略

    # 54.螺旋矩阵
    # 略

    # 48.旋转图像
    # 略

    # 240.搜索二维矩阵
    # 矩阵每一行左往右升序，每一列上往下升序
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 从矩阵右上角开始搜索，搜索区域为左下角的矩阵
        sx, sy = 0, n - 1
        while sx < m and sy > -1:
            if matrix[sx][sy] == target:
                return True
            # 如果当前位置比目标小，搜索区域最上边的行可排除
            elif matrix[sx][sy] < target:
                sx += 1
            # 如果当前位置比目标大，搜索区域最右边的列可排除
            else:  # matrix[sx][sy]>target
                sy -= 1
        return False

    # 136.只出现一次的数字
    # 用异或运算可以做到O(1)的空间
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce

        # reduce()第一次将集合前两个元素运算，之后每次将上一次的结果和下一个元素运算
        return reduce(lambda x, y: x ^ y, nums)

    # 169.多数元素
    # 略，夺旗见基本操作

    # 75.颜色分类
    # 略

    # 94.二叉树的中序遍历
    # 略

    # 104.二叉树的最大深度
    # 略

    # 226.翻转二叉树
    # 略

    # 101.对称二叉树
    # 递归的起始调用比较巧妙，将根结点传入两次
    def isSymmetric(self, root) -> bool:
        return self.equalLR(root, root)

    def equalLR(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (
            node1.val == node2.val
            and self.equalLR(node1.left, node2.right)
            and self.equalLR(node1.right, node2.left)
        )

    # 543.二叉树的直径
    # 略，在二叉树最大深度的递归方法中加入最大直径的记录

    # 102.二叉树的层序遍历
    # 略，Python队列：queue = collections.deque()，left = queue.popleft()

    # 108.将有序数组转换为二叉搜索树
    # 略

    # 98.验证二叉搜索树
    # 用递归注意结点的值应该在一个区间，而不是只用和父结点比较
    def isValidBST(self, root) -> bool:
        def helper(node, lower=float("-inf"), upper=float("inf")) -> bool:
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            # 分别判定左右子树是否符合，而不用再单独比较左右子结点的值
            # 每次递归更新左子树结点的上界和右子树结点的下界
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    # 230.二叉搜索树中第k小的元素
    # 略

    # 199.二叉树的右视图
    # 略

    # 114.二叉树展开为链表
    # 按前序遍历顺序，链表使用结点的右指针链接
    # 按右子树-左子树-根结点的顺序进行递归遍历
    def __init__(self):
        self.pre = None

    def flatten(self, root) -> None:
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        # 将递归的访问部分改为对指针的修改
        root.right = self.pre
        root.left = None
        self.pre = root
        return

    # 105.从前序与中序遍历序列构造二叉树
    # 略

    # 236.二叉树的最近公共祖先
    def lowestCommonAncestor(self, root, p, q):
        # 如果找到p或q，或找到末尾找不到，则返回当前结点或None
        if root is None or root == p or root == q:
            return root
        # 在左子树中寻找p或q
        left = self.lowestCommonAncestor(root.left, p, q)
        # 在右子树中寻找p或q
        right = self.lowestCommonAncestor(root.right, p, q)
        # 在左子树中找不到p或q，则公共祖先结点在右子树中
        if left is None:
            return right
        # 在右子树中找不到p或q，则公共祖先结点在左子树中
        if right is None:
            return left
        # p和q分别在两边子树中，则当前结点为最近公共祖先
        return root

    # 200.岛屿数量
    # 略

    # 994.腐烂的橘子
    # 略

    # 208.实现Trie（前缀树）
    # 略

    # 20.有效的括号
    # 略

    # 155.最小栈
    # 略

    # 394.字符串编码
    # 略

    # 215.数组中的第K个最大元素
    # 基于快排或堆排

    # 295.数据流中的中位数
    # 略

    # 35.搜索插入位置
    # 略

    # 74.搜索二维矩阵
    # 略

    # 34.在排序数组中查找元素的第一个和最后一个位置
    # 略

    # 33.搜索旋转排序数组
    # 旋转排序数组是指有序数组在某个位置断开并前后两段交换位置
    # 仍然按照二分搜索的思路来处理
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 判断前半段是否有序
            if nums[0] <= nums[mid]:
                # 目标在有序部分中，继续按二分查找的方法进行
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                # 目标在后半段无序部分，重复之前的思路
                else:
                    l = mid + 1
            # 前半段无序，则后半段是有序的
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    # 153.寻找旋转排序数组中的最小值
    # 略

    # 121.买卖股票的最佳时机
    # 略

    # 55.跳跃游戏
    # 贪心算法，遍历过程中记录能到达的最远距离
    def canJump(self, nums: List[int]) -> bool:
        n, far = len(nums), 0
        for i in range(n):
            if i <= far:
                # 当前能到达的距离：i+nums[i]
                far = max(far, i + nums[i])
                if far >= n - 1:
                    return True
        return False

    # 45.跳跃游戏II
    # 贪心算法有点绕，从前往后走
    def jump(self, nums: List[int]) -> int:
        # far是在当前步数的基础上、预期下一步能走到的最远距离
        # end是当前已走过的所有步数能走到最远距离
        far, end, res = 0, 0, 0
        for i in range(len(nums) - 1):
            # 下一步范围内的每一步能走到的最远距离
            if i <= far:
                far = max(far, i + nums[i])
                # 走到了当前这些步数中能走到的最远距离
                # 此时能确定需要再走一步，end更新为
                if i == end:
                    end = far
                    res += 1
        return res

    # 70.爬楼梯
    # 略，dp[n]=dp[n-1]+dp[n-2]

    # 118.杨辉三角
    # 略

    # 198.打家劫舍
    # 略，dp[i]=max(dp[i-1],dp[i-2]+nums[i])

    # 279.完全平方数
    # 求最少需要多少个完全平方数的加和等于n
    # dp[i]=1+min(dp[i-j**2]), j in [1,square(i)]
    # 相当于每次从i中减去一个完全平方数j**2得到子问题dp[i-j**2]
    # 结果为子问题的结果加1（即起初抛开的j**2）
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            tmp = float("inf")
            j = 1
            while j**2 <= i:
                tmp = min(tmp, dp[i - j**2])
                j += 1
            dp[i] = tmp + 1
        return dp[n]

    # 322.零钱交换
    # 略，dp[i]=min(dp[i-coins[j]]+1), j in [0,len(coins))

    # 139.单词拆分
    # 略，dp[i]=dp[i-j] and s[i-j:i] in wordDict. j in [minWordLen,maxWordLen]
