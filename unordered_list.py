from node import Node

class UnorderedList:
  """ Unordered linked list class with some useful methods that helps you in the process """

  def __init__(self):
    """ Constructs a linked list and make the head refer to nothing """
    self.head = None
    self.length = 0

  def isEmpty(self):
    """ Checks if the linked list is empty """
    return self.head is None

  def getHead(self):
    return self.head

  def add(self, newItem):
    """ Adds new item to your list """
    temp = Node(newItem)
    temp.setNext(self.head)
    self.head = temp
    self.length += 1;
    
  def getLength(self):
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
      if current.getData() == item:
        return True
      current = current.getNext()
    return False

  def remove(self, item):
    """ Removes a specific item that does exist in the list """
    previous = None
    current = self.head
    
    while current is not None:
      if current.getData() == item:
        break
      else:
        previous = current
        current = current.getNext()

    if previous is None:
      self.head = current.getNext()
      self.length -= 1
    else:
      try:
        previous.setNext(current.getNext())
        self.length -= 1
      except:
        print("The element you want to remove is not found.")

  def printList(self):
    """ Prints the content of the list """
    current = self.head
    while current is not None:
      print('(', current.getData(), ') ', end="=> ", sep="")
      current = current.getNext()
    print("None")

if __name__ == "__main__":
  alist = UnorderedList()
  alist.add(1)
  alist.add(2)
  alist.add(3)
  alist.add(4)
  alist.add(5)
  alist.remove(6)
  alist.printList()
  