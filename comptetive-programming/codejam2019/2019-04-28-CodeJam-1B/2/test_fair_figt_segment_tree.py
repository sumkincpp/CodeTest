import unittest
import random
from fair_fight_segment_tree import MaxSegmentTree


class TestSegmentTree(unittest.TestCase):

    def test_simple(self):
        lst = [1, 2, 3]

        st = MaxSegmentTree(lst)

        for i in range(0, len(lst)):
            self.assertEqual(st.query(i, i-1), None)

        for i in range(0, len(lst)):
            self.assertEqual(st.query(i, i), lst[i])

        for i in range(0, len(lst)-1):
            self.assertEqual(st.query(i, i+1), max(lst[i:i+2]))

        self.assertEqual(st.query(0, len(lst) - 1), max(lst))

    def test_random(self):
        n = 20
        lst = [int(random.random()*n) for i in range(0, n)]

        st = MaxSegmentTree(lst)

        for i in range(0, 100):
            print(lst)
            l = int(random.random()*n)
            r = int(random.random()*n)

            if l > r:
                l, r = r, l

            print(f"l={l} r={r} lst={lst[l:r+1]}")

            self.assertEqual(st.query(l, r), max(lst[l:r+1]))
