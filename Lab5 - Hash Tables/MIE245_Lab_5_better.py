class HashTableWithChaining:
    """
    Implements a hash table using chaining for collision resolution.
    Supports both division and multiplication hashing methods.
    """
    def __init__(self, size: int, hash_type: str = "division"):
        """
        Initializes the hash table.
        :param size: Size of the hash table.
        :param hash_type: Hashing method ("division" or "multiplication").
        """
        self.size = size        
        self.hash_type = hash_type
        self.hash_fn = self.division_method if hash_type == "division" else self.multiplication_method
        self.table = None    
        self.initialize_table()    
    
    def initialize_table(self):
        """Initializes the hash table with empty lists."""
        self.table = [[] for _ in range(self.size)]

    def division_method(self, key: int) -> int:
        """Computes hash using the division method."""
        return key % self.size

    def multiplication_method(self, key: int) -> int:
        """Computes hash using the multiplication method."""
        return int(key * 0.2787 % 1 * self.size // 1)

    def insert(self, key: int):
        """Inserts a key into the hash table."""
        self.table[self.hash_fn(key)].append(key)

    def search(self, key: int) -> int:
        """Searches for a key in the hash table. 
        Return the slot index of the key if it is present in the hash table.
        Return -1 if the key is not found in the hash table.
        """
        idx = self.hash_fn(key)
        return idx if key in self.table[idx] else -1

    def delete(self, key: int):
        """Deletes a key from the hash table."""
        chain = self.table[self.hash_fn(key)]
        if key in chain:
            chain.remove(key)

    def get(self) -> list[list]:
        """Returns the current state of the hash table."""
        return self.table

class HashTableWithOpenAddressing:
    """
    Implements a hash table using open addressing for collision resolution.
    Supports linear probing and double hashing.
    """
    def __init__(self, size: int, hash_type: str = "linear_probing"):
        """
        Initializes the hash table.
        :param size: Size of the hash table.
        :param hash_type: Hashing method ("linear_probing" or "double_hashing").
        """
        self.size = size
        self.hash_type = hash_type
        self.hash_fn = self.linear_probing if hash_type == "linear_probing" else self.double_hashing
        self.table = None
        self.initialize_table()

    def initialize_table(self):
        """Initializes the hash table with empty slots."""
        self.table = [None for _ in range(self.size)]

    def linear_probing(self, key: int, i: int) -> int:
        """Computes hash using linear probing."""
        return (key % self.size + i) % self.size

    def double_hashing(self, key: int, i: int) -> int:
        """Computes hash using double hashing."""
        return (key % self.size + i * (1 + key % (self.size - 2))) % self.size

    def insert(self, key: int) -> int:
        """Inserts a key into the hash table.
        Return the slot index if the key is inserted successfully into hash table.
        Return -1 if hash table is full."""
        for i in range(self.size):
            idx = self.hash_fn(key, i)
            if self.table[idx] is None or self.table[idx] == -1:
                self.table[idx] = key
                return idx
        return -1
    
    def search(self, key: int) -> int:
        """Searches for a key in the hash table.
        Return the slot index of the key if it is present in the hash table.
        Return -1 if the key is not found in the hash table.
        """
        for i in range(self.size):
            idx = self.hash_fn(key, i)
            if self.table[idx] == key:
                return idx
            if self.table[idx] is None:
                break
        return -1
    
    def delete(self, key: int):
        """Deletes a key from the hash table."""
        idx = self.search(key)
        if idx != -1:
            self.table[idx] = -1

    def get(self) -> list:
        """Returns the current state of the hash table."""
        return self.table
