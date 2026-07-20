# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
from email import generator
from typing import List
lis = List[List[int]]
dic = {'r':'d', 'd':'l', 'l':'u'}
class Solution:
    def solve(self, now, nums, x, y, zs, bl) -> None:
        if now == 0:
            return
        match zs:
            case 'r':
                for i in range(x, x + now):
                    nums += 1
                    lis[y][i] = nums
                x = x + now - 1
            case 'd':
                for i in range(y, y + now):
                    nums += 1
                    lis[i][x] = nums
                y = y + now - 1
            case 'l':
                for i in range(x, x - now, -1):
                    nums += 1
                    lis[y][i] = nums
                x = x - now + 1
            case 'u':
                for i in range(y, y - now, -1):
                    nums += 1
                    lis[i][x] = nums
                y = y - now + 1
        if bl:
            self.solve(now - 1, nums, x, y, dic[zs], False)
        else:
            self.solve(now , nums, x, y, dic[zs], True)
        return

    def generateMatrix(self, n: int) -> List[List[int]]:
        lis = [[0 for _ in range(n)] for _ in range(n)]
        self.solve(n, 0, 0, 0, 'r', True)
        return lis

if __name__ == '__main__':
    generateMatrix = Solution().generateMatrix(5)
    print(generateMatrix)

