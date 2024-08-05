""" 排序算法
"""


# 插入排序
# （希尔排序对插入排序改进，每次依gap对数组分组后插入排序，直到gap逐渐减小到1）
def insertionSort(nums):
    for i in range(len(nums)):
        # 每一次循环保证前i-1个数是有序的（不一定是最终位置）
        # 再将第i个数插入到前i个数中的正确位置
        num = nums[i]
        pre = i - 1
        while pre >= 0 and nums[pre] > num:
            nums[pre + 1] = nums[pre]
            pre -= 1
        nums[pre + 1] = num
    return nums


# 选择排序
def selectionSort(nums):
    for i in range(len(nums) - 1):
        # 每一次循环从nums[i+1:]中选择最小的元素放到nums[i]的位置
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        if i != minIndex:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


# 冒泡排序
def bubbleSort(nums):
    # 每一次循环将确定前n-i个元素中的最大元素，并放到尾部
    for i in range(1, len(nums)):
        for j in range(0, len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 归并排序
# 分治思想
def mergeSort(nums):
    import math

    if len(nums) <= 1:
        return nums
    mid = math.floor(len(nums) / 2)
    left, right = nums[0:mid], nums[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(leftNums, rightNums):
    res = []
    while leftNums and rightNums:
        if leftNums[0] <= rightNums[0]:
            res.append(leftNums.pop(0))
        else:
            res.append(rightNums.pop(0))
    if leftNums:
        res.extend(leftNums)
    if rightNums:
        res.extend(rightNums)
    return res


# 快速排序
# 分治思想
def quickSort(nums, left, right):
    if left < right:
        p = partition(nums, left, right)
        quickSort(nums, left, p - 1)
        quickSort(nums, p + 1, right)
    return nums


# 取区间的第一个元素作为pivot，使pivot左边元素均比其小，右边元素均比其大
def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left


# 桶排序：
"""确定数据中的min和max后划分min到max的k个区间(桶)
   将每个元素放入区间
   对每个桶内的数据进行排序
   将各桶中的元素合并
   适用于数据均匀分布
"""


# 计数排序
"""确定数据中的min和max后, new一个长度为max-min+1的计数数组
   分配: 统计排序数据中的每个值的个数, 填入计数数组
   收集: 根据计数数组从前往后写出排序序列
   适用于数据跨度小(max-min小)
"""


# 基数排序
"""将所有正数补全到相同位数, 一般用十进制
   从个位开始排序(必须使用稳定排序算法)
   在上一位排序的基础上对十位/百位/...进行排序
"""
