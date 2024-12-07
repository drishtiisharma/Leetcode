class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        leftArray = nums[left:mid + 1]
        rightArray = nums[mid + 1:right + 1]

        i, j, k = 0, 0, left
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                nums[k] = leftArray[i]
                i += 1
            else:
                nums[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            nums[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            nums[k] = rightArray[j]
            j += 1
            k += 1
