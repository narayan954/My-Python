class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.head is None:
            return 'Empty list'
        else:
            current = self.head
            string = ''
            while current is not None:
                string += str(current.data) + ' '
                current = current.next
            return string

    def __repr__(self):
        return str(self)

    def get_length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_after(self, data, node):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif node is self.tail:
            self.insert_back(data)
        else:
            new_node.next = node.next
            node.next.prev = new_node
            new_node.prev = node
            node.next = new_node
        self.size += 1

    def insert_before(self, data, node):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif node is self.head:
            self.insert_front(data)
        else:
            new_node.prev = node.prev
            node.prev.next = new_node
            new_node.next = node
            node.prev = new_node
        self.size += 1

    def delete_front(self):
        if self.head is None:
            return
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def delete_back(self):
        if self.head is None:
            return
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def delete_node(self, node):
        if self.head is None:
            return
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.delete_front()
        elif node is self.tail:
            self.delete_back()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def reverse(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            next_node = current.next
            while next_node is not None:
                if current.data > next_node.data:
                    temp = current.data
                    current.data = next_node.data
                    next_node.data = temp
                next_node = next_node.next
            current = current.next

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_list_reverse(self):
        if self.tail is None:
            print("List is empty")
            return
        current = self.tail
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()

    def print_list_reverse_recursive(self, node):
        if node is None:
            return
        self.print_list_reverse_recursive(node.prev)
        print(node.data, end=" ")

    def print_list_recursive(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.print_list_recursive(node.next)

    def print_list_recursive_reverse(self, node):
        if node is None:
            return
        self.print_list_recursive_reverse(node.prev)
        print(node.data, end=" ")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_front(1)
    dll.insert_front(2)
    dll.insert_front(3)
    dll.insert_back(4)
    dll.insert_back(5)
    dll.insert_back(6)
    dll.print_list()
    dll.print_list_reverse()
    dll.print_list_reverse_recursive(dll.tail)
    dll.print_list_recursive(dll.head)
    dll.print_list_recursive_reverse(dll.head)
    dll.delete_front()
    dll.delete_back()
    dll.delete_node(dll.search(2))
    dll.print_list()
    dll.print_list_reverse()
    dll.print_list_reverse_recursive(dll.tail)
    dll.print_list_recursive(dll.head)
    dll.print_list_recursive_reverse(dll.head)
    dll.reverse()
    dll.print_list()
    dll.print_list_reverse()
    
