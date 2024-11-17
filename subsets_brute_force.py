nums = [1,2,3]
"""
[] [1] [2] [3] [1,2] [1,3] [2,3] [1,2,3]
"""

def backtrack(index, s):
    if index == len(nums):
        print(s)
        return
    cs = s[:]
    backtrack(index+1, s )
    backtrack(index+1, cs + [nums[index]])

backtrack(0, [])