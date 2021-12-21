class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        result = []
        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                start = m
                end = m
                print(start, end)
                for i in range(len(nums)):
                    print(start, end)
                    if nums[start-1] == target and start-1>=0:
                        start -= 1
                    elif end+1<len(nums) and nums[end+1] == target:
                        end += 1
                result.append(start)
                result.append(end)
                return result
        return [-1, -1]
