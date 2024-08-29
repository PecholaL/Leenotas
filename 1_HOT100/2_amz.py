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

    # 84.柱状图中最大矩形
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []  # 单调递增栈
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                # 高度取当前栈顶元素高度
                cur = stack.pop()
                # 右边界即当前元素的前一个元素（一定满足高度大于等于当前所取高度）
                # 因为还无法知道当前元素右边有多少能满足高度高于当前元素，
                # 对右边可能构成更大面积的情况交给后面的遍历访问
                # 不能直接取栈顶（cur），因为这里while可能循环多次，而当前右边界应固定
                right = i - 1
                # 左边界为当前栈顶元素的后一个
                # 因为当前高度为之前被弹出的栈顶，往左能达到该高度的即为当前栈顶所存下标的下一个
                # 如果不存在（即栈空），则左边界为0（最左边）
                left = stack[-1] + 1 if len(stack) > 0 else 0
                res = max(res, (right - left + 1) * heights[cur])
            stack.append(i)
        return res

    # 416.分割等和子串
    # 子串不要求在原数组中连续
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False
        # 动态规划二维数组dp
        # dp[i][j]表示nums[0:i]中是否存在和为j的子串
        # （最终目标是求nums[0:len(nums)]中是否存在和为target的子串）
        # i,j>0时，dp[i][j]=dp[i-1][j]|dp[i-1][j-nums[i]], j>=nums[i]
        # dp[i][j]=dp[i-1][j], j<nums[i]
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]

    # 46.全排列
    # 回溯法
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                # 将当前nums的拷贝存入res，如果不拷贝，后续nums改变会导致res中之前的结果也改变
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

    # 78.子集
    # 求元素各不相同的数组的所有子集
    # 每一位元素对应一个bit的掩码，每位掩码的0或1表示该元素是否在子集中
    # 一共有2^n种掩码（即0~2^n-1的二进制数），对应2^n个子集
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for mask in range(2**n):
            tmp = []
            # 根据当前掩码确定当前子集包含哪些元素
            for i in range(n):
                if mask & (2**i):
                    tmp.append(nums[i])
            res.append(tmp)
        return res

    # 79.单词搜索
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            # 结束条件：当前位置与单词第k个字母不同/已完成单词搜索
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            # 回退
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        # 将所有位置依次作为起点
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False

    # 51.n皇后
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 根据当前row的设置生成符合条件的结果
        def generateBoard():
            board = []
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row):
            # 结束当前搜索的条件：已指定最后一行中皇后的位置
            if row == n:
                board = generateBoard()
                res.append(board)
            else:
                # 对一行中每个位置进行试探，看列和对角是否与其他皇后共线
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    # 对角线冲突判断：
                    # 对角线上row与i之差（左上到右下方向）是相同的
                    diagonal1.add(row - i)
                    # 对角线上row与i之和（左下到右上方向）是相同的
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    diagonal2.remove(row + i)
                    diagonal1.remove(row - i)
                    columns.remove(i)

        res = []
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return res
