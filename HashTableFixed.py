class Bucket:
    def __init__(self, depth):
        self.depth = depth
        self.items = {}

class ExtendibleHashTable:
    def __init__(self, bucket_size=2):
        self.global_depth = 1
        self.bucket_size = bucket_size
        b0 = Bucket(1)
        b1 = Bucket(1)
        self.directory = [b0, b1]

    def hash(self, key):
        return hash(key) & ((1 << self.global_depth) - 1)

    def double_directory(self):
        self.directory += self.directory
        self.global_depth += 1

    def split_bucket(self, idx):
        old_bucket = self.directory[idx]
        new_depth = old_bucket.depth + 1
        b1, b2 = Bucket(new_depth), Bucket(new_depth)
        for k, v in old_bucket.items.items():
            h = hash(k) & ((1 << new_depth) - 1)
            if h & (1 << (new_depth - 1)):
                b2.items[k] = v
            else:
                b1.items[k] = v
        for i in range(len(self.directory)):
            if self.directory[i] == old_bucket:
                if i & (1 << (new_depth - 1)):
                    self.directory[i] = b2
                else:
                    self.directory[i] = b1

    def insert(self, key, value):
        while True:
            idx = self.hash(key)
            b = self.directory[idx]
            if len(b.items) < self.bucket_size or key in b.items:
                b.items[key] = value
                break
            else:
                if b.depth == self.global_depth:
                    self.double_directory()
                self.split_bucket(idx)

    def search(self, key):
        idx = self.hash(key)
        b = self.directory[idx]
        return b.items.get(key, None)

    def delete(self, key):
        idx = self.hash(key)
        b = self.directory[idx]
        if key in b.items:
            del b.items[key]

    def display(self):
        print("\nDirectory:")
        for i, b in enumerate(self.directory):
            print(f"Idx {i:02b} → Depth:{b.depth} Items:{b.items}")


h = ExtendibleHashTable()
h.insert(1, "A")
h.insert(2, "B")
h.insert(3, "C")
h.insert(4, "D")
h.display()

print("Search 3:", h.search(3))
h.delete(3)
print("After delete:")
h.display()
