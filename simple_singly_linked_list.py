# 1: Start with a Single Node
# 2: Join nodes to get a Linked List
# 3: Add required methods to the LinkedList class

# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# A Linked List class with single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion method for the Linked List
    def insert(self, data):
        newNode = Node(data)

        # If a Node exists
        if(self.head):
            current = self.head
            # While not pointing to Null
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # Print method for the Linked List
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


# creating a single node
# first = Node(3)
# print(first.data)

# Singly Linked List
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()