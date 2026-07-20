# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。
#
# 你必须编写一个具有 O(log n) 时间复杂度的算法。

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while True :
            temp = (r + l) // 2
            if nums[temp] == target:
                return temp
            if temp == l:
                return -1
            if nums[temp] > target:
                r = temp
            else:
                l = temp

# 太easy了，略