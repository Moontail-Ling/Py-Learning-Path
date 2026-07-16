# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。
#
# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：
#
# 0 <= j <= nums[i] 且
# i + j < n
# 返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 1
        lth = len(nums)
        ans = 10000000
        now = nums[0]
        while True:
            if r == lth and target > now:
                break
            if now >= target:
                ans = min(ans, r-l)
                now -= nums[l]
                l += 1
            else:
                now += nums[r]
                r += 1
        if ans != 10000000:
            return ans
        return 0

# 采取快慢指针的策略，通过sum与target的比较，决定是前项舍弃还是后项补充。
# 时间复杂度为O(2n)