class HashMap:
    """Hashmap that sums the ascii value of word and mods by 1000 which is very collision prone"""

    def __init__(self):
        """m is the size of the hashmap"""
        self.m = 1000
        self.arr = [None] * self.m

    def hash_function(self, key):
        return sum([ord(c) for c in key])

    def search(self, key):
        key = self.hash_function(key)
        if self.arr[key]:
            return self.arr[key][1]

    def insert(self, key, val):
        self.arr[self.hash_function(key)] = (key, val)

    def delete(self, key):
        self.arr[self.hash_function(key)] = None

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
m.insert("ohhh", "dang we upgraded the hash function")
m.delete("uhh")
print(m)
