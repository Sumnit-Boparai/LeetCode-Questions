class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
            elif i < len(candidates) and total < target:
                path.append(candidates[i])
                total += candidates[i]
                if total <= target:
                    dfs(i, path, total)

                path.pop()
                total -= candidates[i]
                if total <= target:
                    dfs(i+1, path, total)
        dfs(0, [], 0)
        return res
