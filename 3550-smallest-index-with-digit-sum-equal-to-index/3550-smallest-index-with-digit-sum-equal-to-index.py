class Solution:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            number = nums[i]
            digit_sum = 0

            while number > 0:
                digit = number % 10
                digit_sum = digit_sum + digit
                number = number // 10

            if digit_sum == i:
                return i

        return -1