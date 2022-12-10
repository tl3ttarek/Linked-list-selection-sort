class Node:
    """ Node Class: used to represent data structures like linked list, tree, ... etc """

    def __init__(self, init_data):
        """ Construct node with value and set next to none """
        self.data = init_data
        self.next = None

    def get_data(self):
        """ Returns the value of the node """
        return self.data

    def get_next(self):
        """ Returns the pointer that refer to the next node """
        return self.next

    def set_data(self, new_data):
        """ Changes the value of the node data """
        self.data = new_data

    def set_next(self, new_next):
        """ Changes what the node reference for """
        self.next = new_next
