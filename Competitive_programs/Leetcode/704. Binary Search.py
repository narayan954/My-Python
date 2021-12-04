class Solution:
    def binary_search(arr,l,r,key):
        mid = (l+r)//2
        if r >= l:
            if arr[mid]==key:
                return mid
            elif arr[mid]>key:
                return Solution.binary_search(arr,l,mid-1,key)
            else:
                return Solution.binary_search(arr,mid+1,r,key)
        else:
            return -1
    
    
    def search(self, nums: List[int], target: int) -> int:
        ans = Solution.binary_search(nums,0,len(nums)-1,target)
        return ans
