# Creation of Singly Linked List


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        # Insert a new node with given value at the specified location
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

    def traverseSLL(self):
        # Traverse and print the elements of the linked list
        if self.head is None:
            print("This singly linked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value, end=" -> ")
                node = node.next

    def searchSLL(self, nodeValue):
        # Search for a value in the linked list
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in the list"

    def deleteNode(self, location):
        # Delete a node at a given location
        if self.head is None:
            print("The SSL does not exist")
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

    def deleteEntireSLL(self):
        # Delete the entire linked list
        if self.head is None:
            print("The SSL does not exist")
        else:
            self.head = None
            self.tail = None


# Create an instance of the singly linked list
singlyLinkedList = SLinkedList()

# Insert elements
singlyLinkedList.insertSLL(1, 0)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(1, 3)
singlyLinkedList.insertSLL(4, 3)

# Display linked list contents
print("Linked List:")
singlyLinkedList.traverseSLL()

# Print values using list comprehension
print("\nList comprehension:")
print([node.value for node in singlyLinkedList])

# Search for a value
print("\nSearch value:")
print(singlyLinkedList.searchSLL(4))

# Delete a node
print("\nDelete node:")
singlyLinkedList.deleteNode(3)
singlyLinkedList.traverseSLL()

# Delete entire linked list
print("\nDelete entire linked list:")
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
