from hashmap import HashMap
from node import LPNode
from exceptions import KeyError


class LinearProbingHashMap(HashMap):
    def __init__(self, bucket_size=2):
        super().__init__(bucket_size)

    def increment_bucket(self, bucket_index):
        return (bucket_index + 1) % self.get_bucket_size()

    def get_key_index(self, key):
        bucket_index = self.get_bucket_index(key)
        i = 0
        while i < self.get_bucket_size():
            bucket = self.buckets[bucket_index]
            if bucket is None:
                return None

            if bucket.key == key:
                return bucket_index

            bucket_index = self.increment_bucket(bucket_index)
            i += 1
        return None

    def get_bucket(self, key):
        bucket_index = self.get_key_index(key)
        if bucket_index is None:
            return None
        return self.buckets[bucket_index]

    def resize(self, key, value):
        self.set_bucket_size()
        node_list = self.buckets
        self.buckets = [None] * self.get_bucket_size()

        for node in node_list:
            if node is not None and node.is_deleted is False:
                self.insert(node.key, node.value)

        self.insert(key, value)

    def insert(self, key, value):
        bucket_index = self.get_key_index(key)

        # # Find existing key and replace value and set is_deleted to False
        if bucket_index is not None:
            self.buckets[bucket_index].is_deleted = False
            self.buckets[bucket_index].value = value
            return

        bucket_index = self.get_bucket_index(key)
        i = 0
        while i < self.get_bucket_size():
            bucket = self.buckets[bucket_index]
            # # If empty or deleted
            if bucket is None or bucket.is_deleted:
                self.buckets[bucket_index] = LPNode(key, value)
                return

            bucket_index = self.increment_bucket(bucket_index)
            i += 1

        self.resize(key, value)

    def get(self, key, default=None):
        bucket = self.get_bucket(key)
        if bucket is None or bucket.is_deleted:
            return default
        return bucket.value

    def delete(self, key):
        bucket_index = self.get_key_index(key)
        if bucket_index is None or self.buckets[bucket_index].is_deleted:
            raise KeyError
        self.buckets[bucket_index].is_deleted = True

    def return_display(self):
        return f"{self.buckets}"

    def display(self):
        output = self.return_display()
        print(output)
