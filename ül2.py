def index_mapping(keys, table_size):
    # Loo massiiv vastava suurusega
    hash_table = [None] * table_size
    
    for key in keys:
        # Kasutame triviaalset kaardistamist (nt võtme väärtus mod tabeli suurus)
        index = key % table_size
        
        # Kui koht on juba hõivatud, liigu järgmisele vaba kohale (naivne lähenemine)
        while hash_table[index] is not None:
            index = (index + 1) % table_size
        
        # Salvestame väärtuse vastavasse kohta
        hash_table[index] = key
    
    return hash_table

# Näide kasutamisest:
keys = [10, 20, 30, 40, 50]
table_size = 7
hash_table = index_mapping(keys, table_size)
print(hash_table)

# 2. Parim aja jutumus on O(n) ja halvim juht on O(n*m)
# 3. Päris elus kasutatakse indekseerimist andmebaasides
