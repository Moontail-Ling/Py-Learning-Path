# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        ans = 0
        if len(s) == 0:
            return 0
        now = {s[0]}
        while r < len(s):
            if s[r] in now:
                ans = max(ans, r - l)
                now.remove(s[l])
                l += 1
            else:
                now.add(s[r])
                r += 1
        ans = max(ans, r - l)
        return ans

# 这道题很阴，有一项测试数据是s="",要求去对该字符串是否有包含内容去做检测。
# 使用快慢指针的策略，通过“存删前，无补后”的策略，便可得出无相同的字符子串
# 时间复杂度为O(2n)