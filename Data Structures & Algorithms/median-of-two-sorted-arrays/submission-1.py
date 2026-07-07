class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        new_arr = nums1 + nums2
        new_arr.sort()

        total_len = len1 + len2

        mid = total_len // 2
        if total_len % 2 == 0:
            return ((new_arr[mid] + new_arr[mid - 1]) / 2) 
        else:
            return new_arr[mid]