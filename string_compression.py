"""Implement a method to perform basic string compression using the 
counts of repeated characters. For example, the string "aabcccccaaa" 
would become "a2b1c5a3".  If the "compressed" string would not become
smaller than the original string, your method should return the original
string.""" 

def compress(strng):
    """Compresses a string using letters."""

    if not strng:
        return strng

    base_length = len(strng)

    compressed = strng[0]
    count = 1
    compressed_length = 1

    for char in strng[1:]:

        if char != compressed[-1]:
            compressed += str(count) + char
            compressed_length += len(str(count) + char)
            count = 1

        else:
            count += 1
        
        if compressed_length >= base_length:
            return strng

    compressed += str(count)
    if len(compressed) >= base_length:
        return strng

    return compressed