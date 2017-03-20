"""Given two strings, write a method to decide if one is a permutation of the other."""

# def are_permutations(strng1, strng2):

#     chars1 = list(strng1)
#     chars2 = list(strng2)

#     if len(chars1) != len(chars2):
#         return False

#     while chars1:
#         char = chars1.pop()
#         try:
#             chars2.remove(char)
#         except ValueError:
#             return False

#     return True

def are_permutations(strng1, strng2):
    """Checks if two strings are permutations. Linear runtime."""

    counter1 = {}
    counter2 = {}

    for char in strng1:
        counter1[char] = counter1.get(char, 0) + 1

    for char in strng2:
        counter2[char] = counter2.get(char, 0) + 1

    return counter1 == counter2

