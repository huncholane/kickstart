candidates = [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34]
target = 27

candidates = list(candidates)
slate, result = [], []
candidates.sort()
n = len(candidates)


def helper(i, target):
    # Backtrack case
    if target == 0:
        result.append(slate[:])
        return
    # Base case
    if target < 0 or i == n:
        return
    # Recursive case
    j, count = i, 0
    while j < n and candidates[i] == candidates[j]:
        count += 1
        j += 1
    helper(i + count, target)
    for c in range(1, count + 1):
        slate.append(candidates[i])
        helper(i + count, target - candidates[i] * c)
    for _ in range(count):
        slate.pop()


helper(0, target)
for l in result:
    print(l)
