class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.dict1 = Counter(nums1)
        self.dict2 = Counter(nums2)
        self.nums2 = nums2
        
    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.dict2[prev] -= 1
        new = prev+val
        if new not in self.dict2:
            self.dict2[new] = 1
        else:
            self.dict2[new] += 1
        self.nums2[index] = new

    def count(self, tot: int) -> int:
        ans = 0
        for k in self.dict1.keys():
            t = tot - k
            if t in self.dict2:
                ans += self.dict1[k]*self.dict2[t]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)