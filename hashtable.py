class HashTable:

    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def hash_key(self, key):
        hashed_key = 0
        for i in range(len(key)):
            hashed_key = (hashed_key + (ord(key[i]) * i)) % self.size

        return hashed_key

    def set(self, key, value):
        hashed_key = self.hash_key(key)

        if not self.data[hashed_key]:
            self.data[hashed_key] = []

        self.data[hashed_key].append([key,value])
        return self.data

    def get(self, key):
        hashed_key = self.hash_key(key)

        data = self.data[hashed_key]

        if len(data) > 0:
            for record in data:
                if record[0] == key:
                    return record[1]

        return None

