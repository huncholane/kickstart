import random
from typing import List


def partition(d: List[tuple], l, r):
    pi = random.randint(l, r)
    d[l], d[pi] = d[pi], d[l]
    i = l
    for j in range(l + 1, r + 1):
        if d[j][0] < d[l][0]:
            i += 1
            d[i], d[j] = d[j], d[i]
    d[l], d[i] = d[i], d[l]
    return i


def helper(d, l, r):
    if l > r:
        return
    pi = partition(d, l, r)
    helper(d, l, pi - 1)
    helper(d, pi + 1, r)


def lomuto_sort(d):
    helper(d, 0, len(d) - 1)
    return d


class Dict:
    def __init__(self, arr: List[tuple] = []):
        self.arr = lomuto_sort(arr)

    def __str__(self):
        s = "{\n"
        for node in self.arr:
            s += f'  "{node[0]}": "{node[1]}"\n'
        s += "}"
        return s

    def search(self, key):
        i, tup = self.lsearch(key)
        if tup:
            return tup

    def lsearch(self, key):
        """Lower bound binary search"""

        def helper(l, r):
            if l > r:
                return r, None
            mid = (l + r) // 2
            if self.arr[mid][0] == key:
                return mid, self.arr[mid]
            elif key < self.arr[mid][0]:
                return helper(l, mid - 1)
            else:
                return helper(mid + 1, r)

        return helper(0, len(self.arr) - 1)

    def insert(self, key, val):
        i, tup = self.lsearch(key)
        if tup:
            self.arr[i] = (key, val)
        else:
            self.arr.append(None)
            for j in range(len(self.arr) - 1, i + 1, -1):
                self.arr[j] = self.arr[j - 1]
            self.arr[i + 1] = (key, val)

    def delete(self, key):
        i, node = self.search(key)
        if i:
            for j in range(i, len(self.arr) - 1):
                self.arr[j] = self.arr[j + 1]
            self.arr.pop()
            return i, node


d = Dict([])
d.insert("b", "wwced")
d.insert("r", "avcsd")
d.insert("e", "iuob")
print(d)
d.insert("g", "ibui")
d.insert("h", "ibuu")
print(d)
print(d.lsearch("a"))
d.insert("z", "ewf")
print(d)
