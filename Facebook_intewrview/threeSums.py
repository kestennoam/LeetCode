class Solution:
    def threeSum(self, nums):
        dic_pairs = {}
        # n choose 2 options to make the hash map
        for i, valI in enumerate(nums):
            for j in range(i + 1, len(nums)):
                temp = valI + nums[j]
                if temp in dic_pairs:
                    dic_pairs[temp].append([i, j])
                else:
                    dic_pairs[temp] = [[i, j]]

        lst_triples = []
        for i, val in enumerate(nums):
            if (val * -1) in dic_pairs:
                for pair in dic_pairs[val * -1]:
                    if i in pair:
                        continue
                    sorted_triple = [nums[pair[0]], nums[pair[1]], val]
                    sorted_triple.sort()
                    if sorted_triple not in lst_triples:
                        lst_triples.append(sorted_triple)

        return lst_triples


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
