class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

""" To solve this problem I created a set to store unique values from the input linked lists
    The overall tiem complexity is O(N^2) due to the use of sorted list function and the space complexity is O(n).
"""
def union(llist_1, llist_2):
    # We create a set 
    s_union = set()

    if llist_1.head is not None:
        curr_node = llist_1.head

        while curr_node:
            s_union.add(curr_node.value)
            curr_node = curr_node.next

    if llist_2.head is not None:
        curr_node = llist_2.head

        while curr_node:
                s_union.add(curr_node.value)
                curr_node = curr_node.next
    
    # Check if union set is empty
    if not s_union:
        return "union set is empty"
    # Create a linked list
    l_union = LinkedList()
    
    # Create a sorted list from the union set
    # The time complexity is O(n^2)
    for item in sorted(list(s_union)):
        l_union.append(item)

    return l_union

def intersection(llist_1, llist_2):   
    # Create first set
    f_set = set()

    if llist_1.head is not None:
        curr_node = llist_1.head
        while curr_node:
            f_set.add(curr_node.value)
            curr_node = curr_node.next
    # Create the second set
    s_set = set() 
    if llist_2.head is not None:
        curr_node = llist_2.head
        while curr_node:
            s_set.add(curr_node.value)
            curr_node = curr_node.next

    # Create the intersection set
    i_set = set()     
    # set the actual intersection values
    i_set = f_set.intersection(s_set)

    # If intersection is empty
    if not i_set:
        return "The intersection set is empty"
    
    # Create a LinkedList
    i_list = LinkedList()


    for item in sorted(list(i_set)):
        # Added values to the intersection
        i_list.append(item)
    
    return i_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = []
element_2 = [1,7,8,9,11,1, 44, 14, 82, 16]

for item in element_1:
    linked_list_5.append(item)

for item in element_2:
    linked_list_6.append(item)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
print (intersection(linked_list_5,linked_list_6))