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
    length = alist.get_length()
    pointer = alist.get_head()

    for i in range(length - 1):
        mn = pointer
        cursor = pointer.get_next()
        while cursor is not None:
            if cursor.get_data() < mn.get_data():
                mn = cursor
            cursor = cursor.get_next()

        # Swapping the elements
        temp = mn.get_data()
        mn.set_data(pointer.get_data())
        pointer.set_data(temp)

        pointer = pointer.get_next()


def generate_normal_list(n):
    """ Generate random normal list that has the length of n """
    alist = []
    for i in range(n):
        alist += [randrange(0, 101)]
    return alist


def normal_list_selection_sort(alist):
    """ Operate selection sort on a normal list """
    for i in range(len(alist) - 1):
        min_value = alist[i]
        min_index = i

        for j in range(i, len(alist)):
            if alist[j] < min_value:
                min_value = alist[j]
                min_index = j

        alist[min_index], alist[i] = alist[i], alist[min_index]


if __name__ == "__main__":
    # Generate random linked list
    linked_list = random_linked_list(1000)
    print("=" * 70)
    print("Linked List before sorting:")
    linked_list.print_list()
    print("=" * 70)
    print("Linked List after sorting:")
    begin_time = time()
    linked_list_selection_sort(linked_list)
    linked_list_time = time() - begin_time
    linked_list.print_list()
    print("=" * 70)
    normal_list = generate_normal_list(1000)
    begin_time = time()
    normal_list_selection_sort(normal_list)
    normal_list_time = time() - begin_time
    print(f"Total time for linked list : {linked_list_time:.9f}")
    print(f"Total time for normal list of (same size) : {normal_list_time:.9f}")
