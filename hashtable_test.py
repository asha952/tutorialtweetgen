import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


from hashtable import HashTable
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):

    def test_init(self):
        ht = HashTable(4)
        assert len(ht.buckets) == 4
        assert ht.length() == 0

    def test_keys(self):
        ht = HashTable()
        assert ht.keys() == []
        ht.set('I', 1)
        assert ht.keys() == ['I']
        ht.set('V', 5)
        self.assertCountEqual(ht.keys(), ['I', 'V'])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(ht.keys(), ['I', 'V', 'X'])  # Ignore item order

    def test_values(self):
        ht = HashTable()
        assert ht.values() == []
        ht.set('I', 1)
        assert ht.values() == [1]
        ht.set('V', 5)
        self.assertCountEqual(ht.values(), [1, 5])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(ht.values(), [1, 5, 10])  # Ignore item order

    def test_items(self):
        ht = HashTable()
        assert ht.items() == []
        ht.set('I', 1)
        assert ht.items() == [('I', 1)]
        ht.set('V', 5)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5)])
        ht.set('X', 10)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5), ('X', 10)])

    def test_length(self):
        ht = HashTable()
        assert ht.length() == 0
        ht.set('I', 1)
        assert ht.length() == 1
        ht.set('V', 5)
        assert ht.length() == 2
        ht.set('X', 10)
        assert ht.length() == 3

    def test_contains(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.contains('I') is True
        assert ht.contains('V') is True
        assert ht.contains('X') is True
        assert ht.contains('A') is False

    def test_set_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3
        with self.assertRaises(KeyError):
            ht.get('A')

    def test_set_twice_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 4)
        ht.set('X', 9)
        assert ht.length() == 3
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3

    def test_delete(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.length() == 3
        ht.delete('I')
        ht.delete('X')
        assert ht.length() == 1
        with self.assertRaises(KeyError):
            ht.delete('X')
        with self.assertRaises(KeyError):
            ht.delete('A')


if __name__ == '__main__':
    unittest.main()
