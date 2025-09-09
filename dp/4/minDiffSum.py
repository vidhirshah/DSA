from itertools import combinations
import bisect

def minAbsDifference(nums):
    n = len(nums) // 2
    total = sum(nums)
    left, right = nums[:n], nums[n:]
    
    def get_sums(arr):
        sums = [[] for _ in range(len(arr)+1)]
        for k in range(len(arr)+1):
            for comb in combinations(arr, k):
                sums[k].append(sum(comb))
            sums[k].sort()
        return sums
    
    left_sums = get_sums(left)
    right_sums = get_sums(right)    
    ans = abs(total - 2 * sum(left)) 
    
    for i in range(n+1):
        left_part = left_sums[i]
        right_part = right_sums[n-i]
        
        for sl in left_part:
            target = total//2 - sl
            idx = bisect.bisect_left(right_part, target)
            for j in [idx, idx-1]:
                if 0 <= j < len(right_part):
                    sr = right_part[j]
                    diff = abs(total - 2*(sl+sr))
                    ans = min(ans, diff)
    return ans

nums = [2,-1,0,4,-2,-9]

print(minAbsDifference(nums))