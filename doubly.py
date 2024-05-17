class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
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
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
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
            self.head.prev = None
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
            self.tail = removed_node.prev
            self.tail.next = None
            removed_node.prev = None
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

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

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
        new_head.prev = current
        self.reverse_recursive_helper(temp, current)

    def reverse_recursive(self):
        self.reverse_recursive_helper(self.head, None)
        self.head.prev, self.tail.next = None, None
        self.head, self.tail = self.tail, self.head

    def reverse_non_recursive(self):
        current, prev_node = self.head, None
        while current:
            temp = current.next
            current.next = prev_node
            current.prev, prev_node = prev_node, current
            current = temp
        self.head, self.tail = self.tail, self.head

    def make_double(self, singly_linked_list):
        current = singly_linked_list.head
        while current:
            new_node = Node(current.data)
            new_node.prev = self.tail
            if self.head is None:
                self.head = new_node
            else:
                self.tail.next = new_node
            self.tail = new_node
            current = current.next

    def shift(self,k):
        if k == 0 : 
            return
    
        if k < 0:
            k = -k
        else:
            k = self.size - k

        current = self.head  
    
        count = 1
        while count < k and current != None : 
            current = current.next
            count += 1
    
        if current == None : 
            return
    
        NthNode = current  
    
        while current.next != None : 
            current = current.next
    
        current.next = self.head  

        self.head.prev = current  
    
        self.head = NthNode.next
        self.head.prev = None

        NthNode.next = None

