class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Esimene räsifunktsioon
    def primary_hash(self, key):
        return key % self.size

    # Teine räsifunktsioon
    def secondary_hash(self, key):
        return 1 + (key % (self.size - 1))

    # Lisamine tabelisse
    def insert(self, key, value):
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        
        # Kui kokkupõrge toimub, kasuta topelträsimist
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + step_size) % self.size

        self.table[index] = (key, value)

    # Väärtuse leidmine
    def search(self, key):
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        
        # Liigu läbi tabeli topelträsimise järgi
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step_size) % self.size

        return None

# Näide kasutusest
hash_table = DoubleHashingHashTable(7)  # Tabeli suurus 7
hash_table.insert(10, "Value for 10")
hash_table.insert(20, "Value for 20")
hash_table.insert(15, "Value for 15")
hash_table.insert(23, "Value for 23")

# Otsing
print(hash_table.search(10))  # Väljund: Value for 10
print(hash_table.search(23))  # Väljund: Value for 23
print(hash_table.search(99))  # Väljund: None

# 