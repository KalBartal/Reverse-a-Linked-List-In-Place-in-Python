from node import Node


def reverseLinkedList(head):
    # Initialize variables
    current = head  # points to the first node
    previous = None  # initial set to None
    next = None  # initial set to None

    # Iterate through list and make changes
    while current != None:
        # Save the pointer of the current node
        next = current.next

        # Point the pointer of the current node to previous node
        current.next = previous

        # Update variables
        previous = current
        current = next

    # List is reversed

    return previous


# Initialize a Node
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Connect LinkedListNodes
head.next = node2
node2.next = node3
node3.next = node4

# reverse the LinkedList
node = reverseLinkedList(head)

# Verify the LinkedList is in the right order
assert (node.data == 4)
next_node = node.next
assert (next_node.data == 3)
next_node = next_node.next
assert (next_node.data == 2)
next_node = next_node.next
assert (next_node.data == 1)
