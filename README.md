
# Selection Sort on Linked List

Task🚀 : Implement a Selection sort algorithm on Linked List

## *Contents*
- Implement `Node` & `Linked List` Classes
- Create Unordered Linked List 
- Performing `Selection Sort` on `Linked List` & `Normal List`
- Comparing the performance of the algorithm on both Data Structures

## Implementation Node & Linked list classes

## Node Class
| Parameters | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `data` | `attribute` | holds the data stored in each node |
| `next` | `attribute` | points the `next node` in Linked List |
| `__init__` | `function` | creates an instance of class node with `data` |
| `set_data` | `function` | sets new data to `data` attribute |
| `get_data` | `function` | returns `data` stored in node |
| `set_next` | `function` | sets the `next` pointer to another node |
| `get_next` | `function` | returns next node in Linked List |


## Linked List Class
| Parameters | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `head` | `attribute` | points to `first node` in linked list |
| `length` | `attribute` | holds the `size` of linked list |
| `__init__` | `function` | creates an instance of linked list |
| `get_head` | `function` | returns pointer to `first node` |
| `is_empty` | `function` | true if linked list is is_empty |
| `get_length` | `function` | returns value stored in `length` attribute |
| `add` | `function` | inserts `new node` in linked list |
| `search` | `function` | check if a node exists in linked list |
| `remove` | `function` | deletes a node from linked list |
| `print_list` | `function` | printes linked list |



### Generating random elements using `randrange` method
```python
from random import randrange
alist = []
    for i in range(n):
        alist += [randrange(0, 101)]
```
### Testing Performance of two data structure
```python

    # Linked List
    linked_list = random_linked_list(1000)
    begin_time = time()
    linked_list_selection_sort(linked_list)
    linked_list_time = time() - begin_time
    
    # Normal List
    normal_list = generate_normal_list(1000)
    begin_time = time()
    normal_list_selection_sort(normal_list)
    normal_list_time = time() - begin_time
```
<br/>

## TEAM members :
- `Leader` Talaat Tarek  
- Hazem Elakbawy
- Abdulrahman Khattab
- Moataz Eleryan
- Elsayed Abdelmongey
- Mostafa Khalil
- Mahmoud Feshar
- Doha Ali
- Habiba Nezar
- Ahmed Abdallah
- Ayman hussein
- Abdallah Yousry
- Mohamed Mosalam
- Mohamed Elashry
- Mohmoud Elkholy
- Mostafa Elbebany
- Nader Magdy
