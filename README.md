SIZE = 10
hash_table = [None] * SIZE

def hash_func(key):
    return key % SIZE

def insert():
    key = int(input("Enter key to insert: "))
    index = hash_func(key)

    while hash_table[index] is not None:
        index = (index + 1) % SIZE  
    hash_table[index] = key
    print("Key inserted at index", index)

def search():
    key = int(input("Enter key to search: "))
    index = hash_func(key)
    start = index

    while hash_table[index] is not None:
        if hash_table[index] == key:
            print("Key found at index", index)
            return
        index = (index + 1) % SIZE
        if index == start:
            break
    print("Key not found!")

def delete():
    key = int(input("Enter key to delete: "))
    index = hash_func(key)
    start = index

    while hash_table[index] is not None:
        if hash_table[index] == key:
            hash_table[index] = None
            print("Key deleted from index", index)
            return
        index = (index + 1) % SIZE
        if index == start:
            break
    print("Key not found!")

def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])
    print()

while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        insert()
    elif ch == 2:
        search()
    elif ch == 3:
        delete()
    elif ch == 4:
        display()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

