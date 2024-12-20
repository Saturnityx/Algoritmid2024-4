class Node:
    def __init__(self, key):
        self.key = key  # Võti
        self.next = None  # Järgmine sõlm

class HashTable:
    def __init__(self, size):
        self.table_size = size
        self.table = [None] * self.table_size  # Räsitabel (massiiv, mis sisaldab linked list'e)
    
    def hash_function(self, key):
        # Lihtne räsifunktsioon: võtme mod tabeli suurusega
        return key % self.table_size
    
    def insert(self, key):
        index = self.hash_function(key)
        new_node = Node(key)
        
        # Kui koht on tühi, lisame uue sõlme
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Kui koht on juba täidetud, lisame sõlme loendi algusesse
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        
        # Otsime väärtust linked list'ist
        while current:
            if current.key == key:
                return True  # Võti leiti
            current = current.next
        
        return False  # Võti ei leitud
    
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        
        # Eemaldame võtme linked list'ist
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        
        return False  # Võti ei leitud
        

# Näide kasutamisest:
hash_table = HashTable(10)

hash_table.insert(10)
hash_table.insert(20)
hash_table.insert(30)
hash_table.insert(42)

print(hash_table.search(20))  # True
print(hash_table.search(15))  # False

hash_table.delete(20)
print(hash_table.search(20))  # False
