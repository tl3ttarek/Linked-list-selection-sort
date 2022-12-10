from unordered_list import UnorderedList
from random import randrange
from time import time

def random_linked_list(n):
  """ Generate random linked list that has the length of n """
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

def generate_normal_list(n):
  """ Generate random normal list that has the length of n """
  alist = []
  for i in range(n):
    alist += [randrange(0, 101)]
  return alist

def normal_list_selection_sort(alist):
  """ Operate selection sort on a normal list """
  for i in range(len(alist)-1):
    min_value = alist[i]
    min_index = i

    for j in range(i, len(alist)):
      if alist[j] < min_value:
        min_value = alist[j]
        min_index = j

    alist[min_index], alist[i] = alist[i], alist[min_index]

if __name__ == "__main__":

  # Generate random linked list
  linked_list = random_linked_list(100)

  print("List before sorting:")
  linked_list.printList()
  print()
  begin_time = time()
  
  # Sorting operation
  linked_list_selection_sort(linked_list)
  end_time = time()

  print("List after sorting:")
  linked_list.printList()
  print()

  # Calculating time of the operation
  print(f"Total time of linked list selection sort: {end_time - begin_time:.9f} sec")

  # Doing the same operation on normal list
  normal_list = generate_normal_list(100)
  begin_time = time()
  normal_list_selection_sort(normal_list)
  end_time = time()

  print(f"Total time of normal list selection sort: {end_time - begin_time:.9f} sec")
  