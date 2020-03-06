from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):

        return hash(key) % len(self.buckets)

    def keys(self):

        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):

        values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                values.append(value)
        return values

    def items(self):

        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        return self.count

    def contains(self, key):

        try:
            self.get(key)
        except KeyError:
            return False
        else:
            return True

    def get(self, key):

        item, bucketLinkedList = self.get_item(key)
        if item:
            return item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):

        item, bucketLinkedList = self.get_item(key)
        if item:
            bucketLinkedList.replace(item, (key, value))
        else:
            bucketLinkedList.append((key, value))
            self.count += 1

    def delete(self, key):

        item, bucketLinkedList = self.get_item(key)
        if item:
            bucketLinkedList.delete(item)
            self.count -= 1
        else:
            raise KeyError('Key not found: {}'.format(key))

    def get_item(self, key):
        bucketLinkedList = self.buckets[self._bucket_index(key)]
        item = bucketLinkedList.find(lambda node: node[0] == key)
        return item, bucketLinkedList


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
