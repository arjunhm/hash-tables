from hashmap import HashMap
from node import Node


class ChainingHashMap(HashMap):
    def __init__(self, bucket_size=2):
        super().__init__(bucket_size)

    # * Operations

    def insert(self, key, value):
        bucket_index = self.get_bucket_index(key)

        if self.buckets[bucket_index] is None:
            self.buckets[bucket_index] = Node(key, value)
        else:
            bucket = self.buckets[bucket_index]
            bucket.insert(key, value)

    def get(self, key, default=None):
        bucket_index = self.get_bucket_index(key)
        bucket = self.buckets[bucket_index]
        if bucket is None:
            return default

        return bucket.get(key, default)

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        bucket = self.buckets[bucket_index]
        if bucket is None:
            raise KeyError
        bucket.delete(key)

    def display(self):
        for i in range(self.__bucket_size):
            print(i, end=": ")
            bucket = self.buckets[i]
            if bucket is not None:
                bucket.print_list()
        print("----")

