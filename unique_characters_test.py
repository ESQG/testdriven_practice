"""Implement an algorithm to determine if a string has all unique characters.
(What if you cannot use additional data structures?)"""

import unittest
from unique_characters import characters_are_unique, characters_are_unique2

true_samples = ["", " 5\t", "a", "A", "aA", "Elizabeth", "Special.", "snowflake"]
false_samples = ["!.!", "apple", " 5 ", "Special snowflake"]

class StringUniquenessTests(unittest.TestCase):
    """When strings are input, each test should return True or False accordingly."""
        
    def test_1_true(self):
        """All testcases that should return True, on the first function."""
        for sample in true_samples:
            test_count += 1
            boolean = characters_are_unique(sample)
            self.assertEqual(boolean, True)

    def test_1_false(self):
        """All testcases that should return False, on the second function."""
        for sample in false_samples:
            boolean = characters_are_unique(sample)
            self.assertEqual(boolean, False)

    def test_2_true(self):
        for sample in true_samples:
            test_count += 1
            boolean = characters_are_unique2(sample)
            self.assertEqual(boolean, True)

    def test_2_false(self):
        for sample in false_samples:
            boolean = characters_are_unique2(sample)
            self.assertEqual(boolean, False)

if __name__ == '__main__':
    unittest.main()