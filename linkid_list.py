"""
2. Create LinkedList Class with methods:
 a) get(i) 
 b) put(i, val)
 c) delete(i)
 d) indexOf(el) - first element = el
 e) size()
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

    def get_value(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return 'lenght: [ ' + str(count) + ' ]'

    def indexOf(self, value):
        node = self.head
        node_id = 1

        while node:
            if node.has_value(value):
                return '[ ' + node_id + ' ]'
            node = node.next
            node_id += 1
        return False

    def get(self, index):
        node = self.head
        node_index = 1

        while node:
            if node_index == index:
                return '[ ' + node.get_value() + ' ]'
            node = node.next
            node_index += 1
        return False

    def search(self, key):
        link = self.head
        if link != None:
            while link.next != None:
                if (link.data == key):
                    return link
                link = link.next
            if (link.data == key):
                return link
        return None

    def remove(self, key):
        tmp = key.prev
        key.prev.next = key.next
        key.prev = tmp

    def __str__(self):
        line_answer = ''
        link = self.head
        if link != None:
            while link.next != None:
                line_answer += '[ ' + str(link.data) + ' ]'
                link = link.next
            line_answer += '[ ' + link.data + ' ]'
        return line_answer


l = LinkedList()

l.add('1')
l.add('2')
l.add('3')
l.add('4')
l.add('5')
l.add('6')
l.add('7')
l.add('1')


print(l)
l.remove(l.search('7'))
print(l)
print(l.list_length())
print(l.get(4))
print(l.get(3))
