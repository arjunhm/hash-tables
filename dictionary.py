from linear_probing_hashmap import LinearProbingHashMap


class Dictionary(LinearProbingHashMap):
    def __init__(self, bucket_size=2):
        super().__init__(bucket_size)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __repr__(self):
        print("{")
        for bucket in self.buckets:
            print()
