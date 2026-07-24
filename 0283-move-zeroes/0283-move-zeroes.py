class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = []
        zeroes = []
        for i in nums:
            if i == 0:
                zeroes.append(i)
            else:
                a.append(i)
        nums[:] = a + zeroes
        