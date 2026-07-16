import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = [0 for i in range(len(nums))]
        mx[0] = nums[0]
        prefixGcd = [0 for i in range(len(nums))]
        prefixGcd[0] = nums[0]
        for i in range(1,len(nums)):
            mx[i] = max(mx[i-1], nums[i])
            prefixGcd[i] = gcd(nums[i], mx[i])
        prefixGcd.sort()
        i = 0
        ans = 0
        while True:
            if 2 * i >= len(nums) - 1:
                break
            ans += gcd(prefixGcd[i], prefixGcd[len(nums) - 1 - i])
            i += 1
        return ans

# 一道很简单的题，按题目要求做即可，理论上的时间复杂度为O(n log n + n log U)
# 其中n指的是数列长度，U指的是nums的最大项，是求其最大公约数算法的时间复杂度