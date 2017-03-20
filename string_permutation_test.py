"""Given two strings, write a method to decide if one is a permutation of the other."""

import unittest
from string_permutation import are_permutations

class PermutationMatchingTests(unittest.TestCase):

    def test_empty(self):
        boolean = are_permutations("", "")
        self.assertEqual(boolean, True)

    def test_a(self):
        boolean = are_permutations("a", "A")
        self.assertEqual(boolean, False)

    def test_ab(self):
        boolean = are_permutations("ab", "ab")
        self.assertEqual(boolean, True)

    def test_abba(self):
        boolean = are_permutations("ab", "ba")
        self.assertEqual(boolean, True)

    def test_elizabeth(self):
        boolean = are_permutations("elizabeth", "zithabeel")
        self.assertEqual(boolean, True)

    def test_multiplicity(self):
        boolean = are_permutations("elizabeth", "elizabth")
        self.assertEqual(boolean, False)

    def test_spaces(self):
        boolean = are_permutations("able was I er", "re I saw elba")
        self.assertEqual(boolean, True)

    def test_spaces2(self):
        boolean = are_permutations("able was I ere", "I saw elereba")
        self.assertEqual(boolean, False)

if __name__ == '__main__':
    unittest.main()