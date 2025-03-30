num_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    slate, res = [], []
    s = [num for num in phone_number if num not in ["0", "1"]]

    def helper(i):
        if i == len(s):
            res.append("".join(slate))
            return
        letters = num_map[s[i]]
        for letter in letters:
            slate.append(letter)
            helper(i + 1)
            slate.pop()

    if len(s) == 0:
        res.append("")
    else:
        helper(0)
    return res
