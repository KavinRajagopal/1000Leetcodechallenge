class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        temp =0
        for i in range (0, len(nums)):
            temp += nums[i]
            answer.append(temp)
        return answer
