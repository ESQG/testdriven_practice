"""Implement a method to perform basic string compression using the 
counts of repeated characters. For example, the string "aabcccccaaa" 
would become "a2b1c5a3".  If the "compressed" string would not become
smaller than the original string, your method should return the original
string.""" 

import unittest
from string_compression import compress

class CompressionTests(unittest.TestCase):

    def test_example(self):
        example = compress("aabcccccaaa")
        self.assertEqual(example, "a2b1c5a3")

    def test_short(self):
        self.assertEqual(compress("a"), "a")

    def test_equal_length(self):
        sample = "aabbccaabbcc"
        self.assertEqual(compress(sample), sample)

    def test_empty(self):
        self.assertEqual(compress(""), "")

    def test_longer_then_shorter(self):
        sample = "abcaaaaaa"
        self.assertEqual(compress(sample), "a1b1a6")

    def test_repeated_bigram(self):
        sample = "ababababab"
        self.assertEqual(compress(sample), sample)


if __name__ == '__main__':
    unittest.main()