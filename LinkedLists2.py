class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current_node = self.head
        length_num = 0
        while current_node.next is not None:
            current_node = current_node.next
            length_num += 1
        return length_num

    def show(self):
        content = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            content.append(current_node.data)
        print(content)

    def get(self, index_):
        if index_ >= self.length():
            print("Index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index_:
                return current_node.data
            current_index += 1

    def remove(self, index_):
        if index_ >= self.length():
            print("Index out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index_:
                last_node.next = current_node.next
                return
            current_index += 1

    def include(self, data1, index_):
        list_length = self.length()
        if index_ >= list_length:
            print("Index out of range")
            return None
        current_index = 0
        current_node = self.head
        new_node = Node(data=data1)
        while current_index < list_length:
            new_next_node = current_node.next.next
            current_node = current_node.next
            if current_index == index_:
                current_node.next = new_node
                new_node.next = new_next_node
                current_index = current_index + 1
            current_index = current_index + 1
        return

    def include_tc(self, data1, index_):
        current_index = 1
        current_node = self.head
        new_node = Node(data=data1)
        new_next_node = current_node.next.next
        current_node = current_node.next
        if current_index == index_:
            current_node.next = new_node
            new_node.next = new_next_node
        return

mylist0 = LinkedList()
mylist0.append(1)
mylist0.append('a')
mylist0.append(2)
mylist0.append('b')
mylist0.include_tc("aaa", 1)

import time
time_list = []
for i in range(1, 21):
    begin = time.time()
    mylist0.include_tc("aaa", 1)
    time.sleep(1)
    end = time.time()
    total = end - begin
    time_list.append(total)

print(time_list)









