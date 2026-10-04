class Solution:
    def twoSum(self, nums, target):
        register={}
        for i in range(len(nums)):
            partner=target-nums[i]
            if partner in register:
                return[register[partner],i]
            register[nums[i]]=i        