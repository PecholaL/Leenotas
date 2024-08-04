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
