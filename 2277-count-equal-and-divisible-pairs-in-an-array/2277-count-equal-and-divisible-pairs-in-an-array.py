class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # cnt = 0
        # n = len(nums)

        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j] and (i*j)%k == 0:
        #             cnt += 1

        # return cnt

        # index_map = defaultdict(list)
        # for idx, num in enumerate(nums):
        #     index_map[num].append(idx)

        # cnt = 0
        # for indicies in index_map.values():
        #     for i in range(len(indicies)):
        #         for j in range(i+1, len(indicies)):
        #             if (indicies[i]*indicies[j])%k == 0:
        #                 cnt += 1 

        # return cnt

        index_map = defaultdict(list)
        cnt = 0
        n = len(nums)

        for i in range(n):
            for j in index_map[nums[i]]:
                if (i*j)%k == 0:
                    cnt += 1
            index_map[nums[i]].append(i)

        return cnt
        