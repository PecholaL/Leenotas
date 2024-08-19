# 堆
# 一直对堆熟悉又陌生

# 由于堆是*完全二叉树*，可以存储在一个数组中，
# 可以快速计算左右孩子的下标：
#   leftChild, rightChild = cur*2+1, cur*2+2

""" 堆
    * 建堆：从下往上（即数组中从后往前）对每一个有子结点的结点进行整堆
    * 整堆：通过交换使当前结点比两个子结点都大
        ** 如果发生交换，需要对发生变化的子结点进行整堆（因为交换后子结点比原先的小，子树可能被破坏）
"""


# 建堆
def buildMaxHeap(nums, heapSize):
    for i in range(heapSize // 2, -1, -1):
        maxHeapify(nums, i, heapSize)


# 整堆
def maxHeapify(nums, i, heapSize):
    l, r, largest = i * 2 + 1, i * 2 + 2, i
    # largest保存当前结点与左右子结点中最大者下标
    if l < heapSize and nums[l] > nums[largest]:
        largest = l
    if r < heapSize and nums[r] > nums[largest]:
        largest = r
    # 如果发生交换，对子结点整堆
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        maxHeapify(nums, largest, heapSize)


# 应用
# 每次能从堆顶获取最大的元素
# 将堆顶元素和堆中最后一个元素交换
# （注意不是数组中最后一个元素，因为堆越来越小，而数组可能要求保持不变，仅用下标标识数组中堆的范围）
# 从堆顶开始整堆
