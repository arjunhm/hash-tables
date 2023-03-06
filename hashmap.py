from exceptions import KeyError
import math


class HashMap:
    def __init__(self, bucket_size=2):
        if bucket_size <= 1:
            raise ValueError("bucket_size has to be greater than 1")
        self.__bucket_size = bucket_size
        self.buckets = [None] * self.__bucket_size

    def hash(self, key):
        return key % self.__bucket_size

    def get_bucket_size(self):
        return self.__bucket_size

    def set_bucket_size(self, bucket_size=None):
        if bucket_size is None:
            exponent = int(math.log(self.__bucket_size, 2)) + 1
            self.__bucket_size = 2 ** exponent
        else:
            if bucket_size <= 1:
                raise ValueError("bucket_size has to be greater than 1")
            self.__bucket_size = bucket_size

    def get_bucket_index(self, key):
        return self.hash(key) % self.__bucket_size

    def get_bucket(self, key):
        bucket_index = self.hash(key) % self.__bucket_size
        return self.buckets[bucket_index]

    def get(self, key):
        pass

    def insert(self, key, value):
        pass

    def delete(self, key, value):
        pass

