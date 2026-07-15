class Solution:
    def jump(self, nums: List[int]) -> int:
        lth = len(nums)
        # bb = [100000 for i in range(lth)]
        # bb[0]=0
        # for i in range(0,lth):
        #     for j in range(i+1,min(i+nums[i]+1,lth)):
        #         bb[j]=min(bb[j],bb[i]+1)
        # return bb[lth-1]
        i=0
        ans=0
        while i < lth - 1:
            maxn = 0
            temp = 0
            if (i + nums[i] >= lth - 1):
                ans+=1
                break
            for j in range(i + 1, min(i + nums[i] + 1, lth - 1)):
                if(j + nums[j] > maxn):
                    temp = j
                    maxn = j + nums[j]
            ans += 1
            i = temp
        return ans
    
# 一道较为简单的动态规划
# 最初做法使用背包算出到每个点的最小步数，时间复杂度为O(n²)
# 但后来思考了一下，可以直接贪心，这里是再多看下一步，看两步之内如何跨度最大（这说明下一步可以落在的下下步可以达到最远的点）
# 时间复杂度理论上也是O(n²),但由于部分的跳步最终实际耗时会较小