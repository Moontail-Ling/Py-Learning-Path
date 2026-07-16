# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
ans = []
class Solution:
    def khsc(self, now: int, n: int, r: int, k: str) -> None:
        if n == now:
            ans.append(k+")"*(n-r))
            return
        self.khsc(now + 1, n, r, k + '(')
        if r < now:
            self.khsc(now, n, r + 1, k + ')')
        return
    def generateParenthesis(self, n: int) -> List[str]:
        ans.clear()
        self.khsc(0, n, 0, '')
        return ans
        
# 简单
# 由于n=8，所以理论上直接打表就可以了，时间复杂度O(1)
# 但懒，所以用递归，时间复杂度为O(2**n)