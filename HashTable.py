from LinkedList import LinkedList


class Hashtest_Table:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    def create_arr(self, size):
        # Each element of the hash test_table (arr) is a linked list. This method creates an array (list) of a given size and populates each of its elements with a LinkedList object
        array = []
        for _ in range(size):
            array.append(LinkedList())
        return array

    def hash_func(self, key):
        # Hash functions are a function that turns each of these keys into and index value that we can use to decide where in our list each key:value pair should be stored.
        index = hash(key) % self.size
        return index

    def insert(self, key, value):
        # Should insert a key value pair into the hash test_table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash test_table, be sure to check if there is a Node with the same key in the test_table already.
        # Hash to find which LL we need to access -- RT index of array
        hash_key_index = self.hash_func(key)
        # if the key/word is found,
        if self.arr[hash_key_index].find_and_replace(key) == -1:
            self.arr[hash_key_index].append((key, value))

    def print_key_values(self):
        # Traverse through the every Linked List in the test_table and print the key value pairs.
        for LinkedList in self.arr:
            LinkedList.print_nodes()

# Testing Code
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
