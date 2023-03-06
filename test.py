import unittest

from hashmap import HashMap
from node import Node, ChainingNode, LinkedList, LPNode
from chaining_hashmap import ChainingHashMap
from linear_probing_hashmap import LinearProbingHashMap
from dictionary import Dictionary
from exceptions import KeyError


class CustomTestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def assertIsType(self, obj, cls):
        if type(obj) != cls:
            raise self.failureException(f"{obj} is not of Type {cls}")


# * HashMap


class TestHashMap(CustomTestCase):
    def test_get_bucket_size(self):
        hm = HashMap()
        self.assertIs(hm.get_bucket_size(), hm._HashMap__bucket_size)

    def test_create(self):

        self.assertRaises(ValueError, HashMap, bucket_size=-1)
        hm = HashMap()
        self.assertEqual(hm.get_bucket_size(), 2)
        self.assertListEqual(hm.buckets, [None, None])

        hm = HashMap(bucket_size=4)
        self.assertEqual(hm.get_bucket_size(), 4)
        self.assertListEqual(hm.buckets, [None, None, None, None])

        hm = HashMap(2)
        self.assertEqual(hm.get_bucket_size(), 2)
        self.assertListEqual(hm.buckets, [None, None])


# * Chaining HashMap


class TestNode(CustomTestCase):
    def test_create(self):
        node = Node(1, 2)
        self.assertEqual(node.key, 1)
        self.assertEqual(node.value, 2)


class TestLinkedList(CustomTestCase):
    def create_sll(self):
        sll = LinkedList()
        sll.insert(1, 1)
        sll.insert(2, 2)
        sll.insert(3, 3)
        sll.insert(4, 4)
        sll.insert(5, 5)
        sll.insert(6, 6)
        return sll

    def test_create(self):
        temp_ll = LinkedList(1, 1)
        self.assertIsType(temp_ll.head, ChainingNode)
        temp_ll.insert(2, 2)
        temp_ll.insert(3, 3)

        result = temp_ll.return_display()
        self.assertEqual(result, "(1, 1) -> (2, 2) -> (3, 3)")

        another_ll = LinkedList()
        self.assertIsNone(another_ll.head)
        another_ll.insert(1, 1)
        another_ll.insert(2, 2)
        another_ll.insert(3, 3)
        another_ll.insert(4, 4)
        result = another_ll.return_display()
        self.assertEqual(result, "(1, 1) -> (2, 2) -> (3, 3) -> (4, 4)")
        another_ll.insert(3, 123)
        result = another_ll.return_display()
        self.assertEqual(result, "(1, 1) -> (2, 2) -> (3, 123) -> (4, 4)")

    def test_get(self):
        sll = self.create_sll()
        self.assertEqual(sll.get(1), 1)
        self.assertEqual(sll.get(2), 2)
        self.assertEqual(sll.get(2, 123), 2)
        self.assertEqual(sll.get(6), 6)
        self.assertEqual(sll.get(123, 222), 222)
        self.assertIsNone(sll.get(123))

    def test_delete(self):
        sll = self.create_sll()

        sll.delete(1)
        result = sll.return_display()
        self.assertEqual(result, "(2, 2) -> (3, 3) -> (4, 4) -> (5, 5) -> (6, 6)")

        sll.delete(6)
        result = sll.return_display()
        self.assertEqual(result, "(2, 2) -> (3, 3) -> (4, 4) -> (5, 5)")

        sll.delete(3)
        result = sll.return_display()
        self.assertEqual(result, "(2, 2) -> (4, 4) -> (5, 5)")

        self.assertRaises(KeyError, sll.delete, key=9)

        sll.delete(2)
        sll.delete(4)
        sll.delete(5)
        result = sll.return_display()
        self.assertEqual(result, "")

        self.assertRaises(KeyError, sll.delete, key=9)


# TODO Add test cases
class TestChainingHashMap(CustomTestCase):
    pass


# * Linear Probing HashMap


class TestLPNode(CustomTestCase):
    def test_create(self):
        lpn = LPNode(1, 1)
        self.assertIsType(lpn, LPNode)
        self.assertIsInstance(lpn, Node)
        self.assertFalse(lpn.is_deleted)

    def test_delete(self):
        lpn = LPNode(1, 1)
        self.assertFalse(lpn.is_deleted)
        lpn.delete()
        self.assertTrue(lpn.is_deleted)


class TestLinearProbingHashMap(CustomTestCase):
    def create_lphm(self):

        lp_hm = LinearProbingHashMap(4)
        lp_hm.insert(1, 1)
        lp_hm.insert(2, 2)
        lp_hm.insert(5, 3)
        lp_hm.insert(9, 0)
        return lp_hm

    def test_insert(self):
        lp_hm = LinearProbingHashMap(4)

        lp_hm.insert(1, 1)
        lp_hm.insert(2, 2)
        self.assertEqual(lp_hm.return_display(), "[None, (1, 1), (2, 2), None]")

        lp_hm.insert(2, 99)
        self.assertEqual(lp_hm.return_display(), "[None, (1, 1), (2, 99), None]")
        lp_hm.insert(5, 3)
        self.assertEqual(lp_hm.return_display(), "[None, (1, 1), (2, 99), (5, 3)]")
        lp_hm.insert(9, 0)
        self.assertEqual(lp_hm.return_display(), "[(9, 0), (1, 1), (2, 99), (5, 3)]")

        lp_hm.delete(1)
        self.assertTrue(lp_hm.get_bucket(1).is_deleted)
        lp_hm.insert(0, 1)
        self.assertEqual(lp_hm.return_display(), "[(9, 0), (0, 1), (2, 99), (5, 3)]")

    def test_get(self):
        lp_hm = self.create_lphm()
        self.assertEqual(lp_hm.get(1), 1)
        self.assertEqual(lp_hm.get(5), 3)
        self.assertEqual(lp_hm.get(99, -1), -1)
        self.assertIsNone(lp_hm.get(99, None))

        lp_hm = LinearProbingHashMap(4)
        lp_hm.insert(1, 1)
        lp_hm.insert(2, 2)
        lp_hm.insert(0, 0)
        self.assertEqual(lp_hm.get(0), 0)
        self.assertIsNone(lp_hm.get(3))
        lp_hm.delete(1)
        self.assertIsNone(lp_hm.get(1))

    def test_delete(self):
        lp_hm = self.create_lphm()

        self.assertFalse(lp_hm.get_bucket(1).is_deleted)
        lp_hm.delete(1)
        self.assertTrue(lp_hm.get_bucket(1).is_deleted)
        self.assertRaises(KeyError, lp_hm.delete, key=1)
        self.assertRaises(KeyError, lp_hm.delete, key=99)

    def test_resize(self):
        lp_hm = LinearProbingHashMap()
        lp_hm.insert(1, 1)
        lp_hm.insert(7, 1)
        lp_hm.insert(2, 1)
        lp_hm.insert(6, 1)
        lp_hm.insert(4, 1)
        self.assertEqual(
            lp_hm.return_display(),
            "[None, (1, 1), (2, 1), None, (4, 1), None, (6, 1), (7, 1)]",
        )


class TestDictionary(CustomTestCase):
    def test_dict(self):
        d = Dictionary()
        self.assertIsInstance(d, LinearProbingHashMap)

        d[1] = "abc"
        self.assertEqual(d[1], "abc")
        d[1] = "def"
        self.assertEqual(d[1], "def")
        d[2] = "xyz"
        del d[1]
        self.assertEqual(d[2], "xyz")
        # CONFIRM if this is right? It's saying d[1] is None
        self.assertIsNone(d[1])


if __name__ == "__main__":
    unittest.main()
