class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        return 'LinkedList({!r})'.format(self.items())

    def items(self):

        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        return self.head is None

    def length(self):
        return self.count

    def append(self, item):

        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.tail
            current_node.next = new_node
            self.tail = current_node.next

        self.count += 1

    def prepend(self, item):

        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1

    def find(self, quality):
        current_node = self.head
        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next
        return None

    def delete(self, item):

        list_len_1 = self.length()
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == item:
                self.count -= 1
                if previous_node is not None:
                    previous_node.next = current_node.next
                    if self.tail.data == item:
                        self.tail = previous_node

                else:
                    if current_node.next is None:
                        self.tail = None
                        self.head = None
                        break
                    else:
                        self.head = current_node.next
                        current_node = self.head

            previous_node = current_node
            current_node = current_node.next

        list_len_2 = self.length()
        if list_len_1 == list_len_2:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
