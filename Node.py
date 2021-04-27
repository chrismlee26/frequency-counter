class Node:

    def __init__(self, data):
        # data is a tuple (key, value)
        self.data = data
        self.next = None

    def update(self):
        # split data into key & value
        key, value = self.data
        value += 1
        self.data = (key, value)
