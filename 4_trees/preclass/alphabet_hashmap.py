def hash_function(key):
    return ord(key) - 97


class HashMap:
    """A hashmap with a simple function using the first letter for hash function.
    This is terrible and causes collisions.
    Only works with a-z"""

    def __init__(self):
        """m is the size of the hashmap"""
        self.m = 26
        self.arr = [None] * self.m

    def search(self, key):
        key = hash_function(key[0])
        if self.arr[key]:
            return self.arr[key][1]

    def insert(self, key, val):
        self.arr[hash_function(key[0])] = (key, val)

    def delete(self, key, val):
        self.arr[hash_function(key[0])] = None

    def __str__(self):
        s = "{\n"
        for i in range(self.m):
            if self.arr[i]:
                s += f'  "{self.arr[i][0]}": "{self.arr[i][1]}"\n'
        s += "}"
        return s


m = HashMap()
m.insert("hi", "hey")
m.insert("im", "Huncho")
m.insert("hashmap", "hashmap is really cool")
m.insert("uhh", "what happened to hi: hey?")
print(m)
