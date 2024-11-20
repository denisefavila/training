class MyDictionary:
    def __init__(self, capacity=10, load_factor=0.75):
        self.capacity = capacity
        self.size = 0
        self.load_factor = load_factor
        self.table = [[] for _ in range(capacity)]  # n buckets

    def _hash(self, key):
        """
        [[], [], []]
        0 -> 0, 1 -> 1, 2 -> 2, 3 -> 0 ...
        """
        #
        return hash(key) % self.capacity

    def _resize(self):
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]

        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_capacity
                new_table[new_index].append((key, value))

        self.table = new_table
        self.capacity = new_capacity

    def set(self, key, value):
        bucket_idx = self._hash(key)
        bucket = self.table[bucket_idx]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def get(self, key):
        bucket_idx = self._hash(key)
        bucket = self.table[bucket_idx]
        for item_key, item_value in bucket:
            if item_key == key:
                return item_value

        return None

    def delete(self, key):
        bucket_idx = self._hash(key)
        bucket = self.table[bucket_idx]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.size -= 1
                return True

        return False
