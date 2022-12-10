from node import Node


class UnorderedList:
    """ Unordered linked list class with some useful methods that helps you in the process """

    def __init__(self):
        """ Constructs a linked list and make the head refer to nothing """
        self.head = None
        self.length = 0

    def is_empty(self):
        """ Checks if the linked list is empty """
        return self.head is None

    def get_head(self):
        return self.head

    def add(self, new_item):
        """ Adds new item to your list """
        temp = Node(new_item)
        temp.set_next(self.head)
        self.head = temp
        self.length += 1

    def get_length(self):
        """ Returns the length of your list """
        # count = 0
        # current = self.head
        # while current != None:
        #   count += 1
        #   current = current.getNext()
        # return count
        return self.length

    def search(self, item):
        """ Search for a specific item in the list """
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        """ Removes a specific item that does exist in the list """
        previous = None
        current = self.head

        while current is not None:
            if current.get_data() == item:
                break
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
            self.length -= 1
        else:
            try:
                previous.set_next(current.get_next())
                self.length -= 1
            except:
                print("The element you want to remove is not found.")

    def print_list(self):
        """ Prints the content of the list """
        current = self.head
        while current is not None:
            print('(', current.get_data(), ') ', end="=> ", sep="")
            current = current.get_next()
        print("None")


if __name__ == "__main__":
    alist = UnorderedList()
    alist.add(1)
    alist.add(2)
    alist.add(3)
    alist.add(4)
    alist.add(5)
    alist.remove(6)
    alist.print_list()
