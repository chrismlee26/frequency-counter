from LinkedList import LinkedList


class Hashtest_Table:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    # 1️⃣ TODO: Complete the create_arr method.

    # Each element of the hash test_table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates
    # each of its elements with a LinkedList object.

    def create_arr(self, size):
        # First attempt but this makes 8 duplicate buckets
        # return [LinkedList()] * size
        # ~~~~~~~~~~
        # this works with random bucket creation
        array = []
        for i in range(size):
            array.append(LinkedList())
        return array

    # 2️⃣ TODO: Create your own hash function.

    # Hash functions are a function that turns each of these keys into an
    # index value that we can use to decide where in our list each key:value
    # pair should be stored.

    def hash_func(self, key):
        index = hash(key) % self.size
        return index

    # 3️⃣ TODO: Complete the insert method.

    # Should insert a key value pair into the hash test_table, where the key is the word and the value is a counter
    # for the number of times the word appeared. When inserting a new word in the hash test_table, be sure to check
    # if there is a Node with the same key in the test_table already.

    def insert(self, key, value):
        # Hash to find which LL we need to access -- RT index of array
        hash_key_index = self.hash_func(key)
        # print(hash_key_index)
        # Using hash key to access which LL inside the array -- RT LL
        # if the key/word is found,

        if self.arr[hash_key_index].find_and_replace(key) == -1:
            # store the value currently in this position
            # then delete node
            # then create a node with (key, value) + new value stored
            # then append data
            self.arr[hash_key_index].append((key, value))

    # 4️⃣ TODO: Complete the print_key_values method.

    # Traverse through the every Linked List in the test_table and print the key value pairs.

    # For example:
    # a: 1
    # again: 1
    # and: 1
    # blooms: 1
    # erase: 2

    def print_key_values(self):
        for LinkedList in self.arr:
            LinkedList.print_nodes()


# if __name__ == "__main__":
#     test_table = Hashtest_Table(8)
#     test_table.insert("apple", 1)
#     print("")
#     test_table.insert("apple", 1)
#     print("")
#     test_table.insert("banana", 1)
#     print("")
#     test_table.insert("apple", 1)
#     print("")
