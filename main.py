from unordered_list import UnorderedList
from random import randrange
from time import time

def random_list(n):
  """ Generate random list that have the length of n """
  alist = UnorderedList()
  for i in range(n):
    alist.add(randrange(0, 101))
  return alist

def linked_list_selection_sort(alist):
  """ Operate selection sort on a linked list """
  length = alist.getLength()
  pointer = alist.getHead()

  for i in range(length-1):
    mn = pointer
    cursor = pointer.getNext()
    while cursor is not None:
      if cursor.getData() < mn.getData():
        mn = cursor
      cursor = cursor.getNext()

    # Swaping the elements
    temp = mn.getData()
    mn.setData(pointer.getData())
    pointer.setData(temp)
  
    pointer = pointer.getNext()

if __name__ == "__main__":

  # Generate random linked list
  mylist = random_list(1000)

  print("List before sorting:")
  mylist.printList()
  begin_time = time()
  print()

  # Sorting operation
  linked_list_selection_sort(mylist)
  end_time = time()

  print("List after sorting:")
  mylist.printList()
  print()

  print(f"Total time of the operation: {end_time - begin_time:.9f} sec")