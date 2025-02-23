class Node:
    def __init__(self, data):
        self.data = data  # Stores the data
        self.next = None  # Points to the next node (initially None)

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None  # Initializes an empty list

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, create the first node
            self.head = new_node
            self.head.next = self.head  # Point to itself to form a circular list
            return
        temp = self.head
        while temp.next != self.head:  # Traverse till the last node
            temp = temp.next
        temp.next = new_node  # Link last node to new node
        new_node.next = self.head  # Link new node to head

    def insert_at_front(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty, insert as the first node
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next != self.head:  # Find the last node
            temp = temp.next
        temp.next = new_node  # Update last node's next to new node
        new_node.next = self.head  # New node points to old head
        self.head = new_node  # Update head to new node

    def insert_at_npos(self, pos, data):
        new_node = Node(data)
        if pos == 1:  # If inserting at the first position
            self.insert_at_front(data)
            return
        temp = self.head
        for i in range(1, pos - 1):  # Traverse to the (pos-1)th node
            if temp.next == self.head:  # If position is out of bounds
                print("Invalid position")
                return
            temp = temp.next
        new_node.next = temp.next  # Link new node to the next node
        temp.next = new_node  # Link previous node to new node

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break  # Stop when we reach the head again
        print("(Back to Head)")

    def delete_at_npos(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 1:  # If deleting the first node
            self.delete_first()
            return
        temp = self.head
        for i in range(1, pos - 1):
            if temp.next == self.head:  # If position is out of bounds
                print("Invalid position")
                return
            temp = temp.next
        temp.next = temp.next.next  # Skip the node at position 'pos'

    def delete_first(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp.next != self.head:  # Find last node
            temp = temp.next
        if self.head.next == self.head:  # If only one node exists
            self.head = None
            return
        temp.next = self.head.next  # Last node points to second node
        self.head = self.head.next  # Update head

    def delete_last(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        if temp.next == self.head:  # If only one node exists
            self.head = None
            return
        while temp.next.next != self.head:  # Find second last node
            temp = temp.next
        temp.next = self.head  # Update next of second last node

    def update(self, position, value):
        temp = self.head
        for i in range(1, position):
            if temp.next == self.head:  # If position is out of bounds
                print("Invalid position")
                return
            temp = temp.next
        temp.data = value  # Update node data

sll = CircularSinglyLinkedList()

while True:
    print("\nChoose an operation:")
    print("1. Insert at End")
    print("2. Insert at Front")
    print("3. Insert at N Position")
    print("4. Delete First Node")
    print("5. Delete Last Node")
    print("6. Delete at N Position")
    print("7. Update a Node")
    print("8. Display List")
    print("9. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data = int(input("Enter value to insert at end: "))
        sll.insert_at_end(data)
    elif choice == 2:
        data = int(input("Enter value to insert at front: "))
        sll.insert_at_front(data)
    elif choice == 3:
        pos = int(input("Enter position to insert: "))
        data = int(input("Enter value: "))
        sll.insert_at_npos(pos, data)
    elif choice == 4:
        sll.delete_first()
    elif choice == 5:
        sll.delete_last()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        sll.delete_at_npos(pos)
    elif choice == 7:
        pos = int(input("Enter position to update: "))
        value = int(input("Enter new value: "))
        sll.update(pos, value)
    elif choice == 8:
        sll.display()
    elif choice == 9:
        break
    else:
        print("Invalid choice, please try again.")
