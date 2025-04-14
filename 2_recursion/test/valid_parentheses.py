def valid_parentheses(n):
    slate, res = [], []

    def helper(opens, closes):
        if opens > n or closes > n or closes > opens:
            return
        if opens == n and closes == n:
            res.append("".join(slate))
            return
        slate.append("(")
        helper(opens + 1, closes)
        slate.pop()
        slate.append(")")
        helper(opens, closes + 1)
        slate.pop()

    helper(0, 0)
    print(res)


valid_parentheses(3)
