class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
# 这是一道很简单的题，如果不加思考，用两个for循环分别求出奇数和偶数和，再进行GCD，复杂度大约为O(2n)
# 稍加思考，直接套公式求出奇数和和偶数和，再进行GCD，复杂度大约为O(1)
# 但并非最优，奇数和为n²，偶数和为n*(n+1)，因为n+1和n肯定互质，容易得出最大公约是一定是n，即直接return n便是正解
