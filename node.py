class Node:
    """ Node Class: used to represent data structures like linked list, tree, ... etc """

    def __init__(self, initData):
        """ Construct node with value and set next to none """
        self.data = initData
        self.next = None

    def getData(self):
        """ Returns the value of the node """
        return self.data

    def getNext(self):
        """ Returns the pointer that refer to the next node """
        return self.next

    def setData(self, newData):
        """ Changes the value of the node data """
        self.data = newData

    def setNext(self, newNext):
        """ Changes what the node refrence for """
        self.next = newNext
