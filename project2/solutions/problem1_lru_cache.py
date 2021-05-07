class DoublyLinkedList:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None
# LRU Cache Class
class LRUCache: 
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = DoublyLinkedList(0, 0)
        self.tail = DoublyLinkedList(0, 0)
        self.head.next = self.tail # at the start the head and tail are the same
        self.tail.prev = self.head # at the start the head and tail are the same
        self.count = 0

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addNodeToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
    # Below methods have O(1) time complexity.
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            result = node.value
            self.removeNode(node)
            self.addNodeToHead(node)
            return result
        return -1
    
    def set(self, key, value):
        if self.capacity <= 0:
            return print("The cache capacity is 0 or negative")
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.removeNode(node)
            self.addNodeToHead(node)
        else:
            node = DoublyLinkedList(key, value)
            self.map[key] = node
            if self.count < self.capacity:
                self.count += 1
                self.addNodeToHead(node)
            else:
                del self.map[self.tail.prev.key]
                self.removeNode(self.tail.prev)
                self.addNodeToHead(node)
    
if __name__ == '__main__':
    # Test case 1
    our_cache = LRUCache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(our_cache.get(3))      # returns -1 because 3 is not present in the cache

    # Test Case 2
    our_cache = LRUCache(2)

    our_cache.set(2, 3)
    our_cache.set(5, 1)
    print(our_cache.get(3))
    print(our_cache.get(5)) 

    # Test case 3
    our_cache = LRUCache(-1)
    our_cache.set(1, 2)
    our_cache.set(1, 1)
    print(our_cache.get(1))

    # Test case 3 with 0 capacity
    our_cache = LRUCache(0)
    our_cache.set(5,1)
    our_cache.set(3, 2)
    print(our_cache.get(1))


