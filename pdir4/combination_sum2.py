class Sol():
    def combinationSum2(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if prev != candidates[start]:
                intermediate.append(candidates[start])
                self.combinationSumRecu(candidates, result, start + 1, intermediate, target - candidates[start])
                intermediate.pop()
                prev = candidates[start]
            start += 1

cs = Sol()
print(cs.combinationSum2([2,5,2,1,2],5))

