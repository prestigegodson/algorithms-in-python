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
        key = str(key)
        hashed_key = self.hash_key(key)

        if not self.data[hashed_key]:
            self.data[hashed_key] = []

        self.data[hashed_key].append([key,value])
        return self.data

    def get(self, key):
        key = str(key)
        hashed_key = self.hash_key(key)

        data = self.data[hashed_key]

        if len(data) > 0:
            for record in data:
                if record[0].lower() == key.lower():
                    return record[1]

        return None


hashTable = HashTable(100)
hashTable.set('Language', 'Python')
hashTable.set('Version', '3.0')
hashTable.set(1, 'Number')
print(hashTable.get('1'))
