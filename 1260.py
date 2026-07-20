# 给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。
#
# 每次「迁移」操作将会引发下述活动：
#
# 位于 grid[i][j]（j < n - 1）的元素将会移动到 grid[i][j + 1]。
# 位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
# 位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
# 请你返回 k 次迁移操作后最终得到的 二维网格。
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = []
        k %= m * n
        for i in range(m):
            temp = []
            for j in range(n):
                s = (i * n + j - k + m * n) % (m * n)
                temp.append(grid[int(s / n)][s % n])
            ans.append(temp)
        return ans

一道很简单的模拟题
只需要整出正确的移动关系就好了
时间复杂度为O(m*n)