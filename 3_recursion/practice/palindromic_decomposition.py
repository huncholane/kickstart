def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    slate, res = [], []

    def helper(i, last_split):
        if i == len(s):
            a, b = last_split, len(slate) - 1
            while a < b:
                if slate[a] != slate[b]:
                    return
                a += 1
                b -= 1
            res.append("".join(slate))
            return
        slate.append(s[i])
        helper(i + 1, last_split)
        slate.pop()
        if len(slate) == 0:
            return
        a, b = last_split, len(slate) - 1
        while a < b:
            if slate[a] != slate[b]:
                return
            a += 1
            b -= 1
        slate.extend(["|", s[i]])
        helper(i + 1, len(slate) - 1)
        slate.pop()
        slate.pop()

    helper(0, 0)
    return res


res = generate_palindromic_decompositions("abaa")
print(res)
