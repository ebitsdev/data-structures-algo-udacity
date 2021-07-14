# LRU Cache solution explanation

I am using doubly linked lists as the most appropriate approach to solving this problem LRU cache. With doubly linked lists, we can efficiently move nodes.
The solution consist of 4 methods:

- addNodeToHead as the name says, with this method I add node to the doubly linked list
- removeNode method is used to remove the node from the doubly linked list if full.
- get method helps to iterate over the list by comparing the values based on the key. If a value is found, the method returns it otherwise it returns -1
- set method allows to implement the LRU cache by replace the least recently used node with the inserted node.

The time complexity for above methods is O(1).
The space complexity for this solution is O(n).