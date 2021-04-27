class Node:

    def __init__(self, data):
        # data is a tuple (key, value)
        self.data = data
        self.next = None

    def update(self):
        '''This is the helper function to update the key # for the hash table
        '''
        # split data into key & value to use in HT
        key, value = self.data
        value += 1
        self.data = (key, value)
