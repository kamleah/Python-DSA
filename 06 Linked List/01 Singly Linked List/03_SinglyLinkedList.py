# Implementation of Singly Linked List


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Iterator for the linked list
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert a node at the specified location in the linked list
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            # If the list is empty, set head and tail to the new node
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                # Insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                # Insert at the end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                # Insert at a specific location
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traverse the linked list and print its values
    def traverseList(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search for a node with a given value in the linked list
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The node does not exist in this SLL"

    # Delete a node at a specified location
    def deleteNode(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete the entire linked list
    def deleteEntireSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head = None
            self.tail = None


# Create an instance of the singly linked list
singlyLinkedList = SLinkedList()

# Insert elements at various locations
singlyLinkedList.insertSLL(44, 6)  # Location 6
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(3, 1)  # Location 1
singlyLinkedList.insertSLL(4, 1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(5, 3)  # Location 3
print([node.value for node in singlyLinkedList])

# Display the linked list contents
print("Linked List:")
singlyLinkedList.traverseList()

# Search for a value in the linked list
print("\nSearch value:")
print(singlyLinkedList.searchSLL(4))

# Delete a node at a specific location
print("\nDelete node:")
singlyLinkedList.deleteNode(2)  # Delete at Location 2
singlyLinkedList.traverseList()

# Delete the entire linked list
print("\nDelete entire linked list:")
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
