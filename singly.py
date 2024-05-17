class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_front(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_at_front(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            removed_node = self.head
            self.head = None
            self.tail = None
        else:
            removed_node = self.head
            self.head = removed_node.next
            removed_node.next = None
        self.size -= 1
        return removed_node.data

    def delete_at_end(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            removed_node = self.tail
            self.head = None
            self.tail = None
        else:
            removed_node = self.tail
            c = self.head
            while c.next != removed_node:
                c = c.next
            self.tail = c
            self.tail.next = None
        self.size -= 1
        return removed_node.data

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def size(self):
        return self.size

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


    def print_back_helper(self, node):
        if node == None:
            return
        self.print_back_helper(node.next, end=' ')
        print(node.data)

    def print_backward(self):
        self.print_back_helper(self.head)

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def reverse_recursive_helper(self, current, new_head):
        if not current:
            self.head = new_head
            return None
        temp = current.next
        current.next = new_head
        self.reverse_recursive_helper(temp, current)

    def reverse_recursive(self):
        self.reverse_recursive_helper(self.head, None)
        self.head, self.tail = self.tail, self.head

    def reverse_non_recursive(self):
        #gaidi
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head, self.tail = self.tail, self.head

            
