class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            pair = target - num
            if pair in arr:
                index = arr.index(pair)
                return [index, i]
            else:
                arr.append(num)
        return [0, 0]



        