"""

Linked List

"""
import unittest


# Node Class
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


# LinkedList Class
class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        # 첫 노드가 없을 시
        if self.size == 0:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def delete(self, data):
        current = self.head

        while current is not None:
            # 삭제하려는 노드를 찾았을 때
            if current.data == data:
                # 첫 번째 노드가 아닐 경우
                if current.prev is not None:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    # 삭제하려는 노드가 마지막 노드일 경우 tail 재 선언
                    if current.next is None:
                        current.prev = self.tail
                # 첫 번째 노드일 경우
                else:
                    self.head = current.next
                    current.next.prev = None
            current = current.next

        self.size -= 1

    def print_list(self):
        current = self.head
        while current.next is not None:
            print('{} -> '.format(current.data), end='')
            current = current.next
        print(current.data)


# Test Class
class DoublyLinkedListTest(unittest.TestCase):
    def test(self):
        ll = DList()
        ll.insert(4)
        ll.print_list()
        ll.insert(5)
        ll.print_list()
        ll.insert(4)
        ll.print_list()
        ll.delete(5)
        ll.print_list()
        ll.insert(5)
        ll.print_list()



