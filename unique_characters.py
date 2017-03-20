"""Implement an algorithm to determine if a string has all unique characters.
(What if you cannot use additional data structures?)"""

def characters_are_unique(strng):
    """Checks if the characters in a string are unique."""

    return len(set(strng)) == len(strng)


def characters_are_unique2(strng):
    """Fail-fast implementation to see if characters in a string are unique."""

    seen = set([])

    for char in strng:
        if char in seen:
            return False

        seen.add(char)

    return True

def characters_are_unique3(strng):
    """Implemented without any other data structures.
    Quadratic runtime (in length of strng), but constant runspace."""

    for char in strng:
        if strng.count(char) > 1:
            return False
    return True

