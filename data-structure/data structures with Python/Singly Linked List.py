"""

Linked List

"""
import unittest


# Node Class
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


# LinkedList Class
class SList:
    def __init__(self, item):
        self.head = Node(item)

    def insert(self, item):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(item)

    def delete(self, item):
        if self.head.data == item:  # 첫 번째 노드를 삭제할 경우 수행되는 조건문
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == item:
                    current.next = current.next.next    # 다음 노드의 값이 삭제하려는 값일 경우, 현재 노드의 포인터를 다다음 노드로 넘김
                    return
                else:
                    current = current.next

    def print_list(self):
        current = self.head
        while current.next is not None:
            print('{} ->'.format(current.data), end='')
            current = current.next
        print(current.data)


# Test Class
class SinglyLinkedListTest(unittest.TestCase):
    def test(self):
        ll = SList(3)
        ll.insert(4)
        ll.insert(5)
        ll.print_list()
        ll.delete(4)
        ll.print_list()
        ll.insert(7)
        ll.print_list()
        ll.delete(5)
        ll.print_list()
