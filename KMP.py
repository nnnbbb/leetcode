

def prefix_table(pattern):
    prefix = [None] * len(pattern)
    prefix[0] = 0
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            prefix[i] = length
            i += 1
        else:
            if length > 0:
                length = prefix[length-1]
            else:
                prefix[i] = length
                i += 1
    return prefix


def move_prefix_table(prefix):
    t = prefix[0:-1]
    return [-1] + t


def kmp_search(text, pattern):
    prefix = prefix_table(pattern)
    prefix = move_prefix_table(prefix)
    # text[i]  len(text)    m
    # text[j]  len(pattern) n
    m = len(text)
    n = len(pattern)
    i = j = 0
    while i < m:
        if j == n - 1 and text[i] == pattern[j]:
            print("Found", i - j)
            index = i - j
            j = prefix[j]
            return index
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = prefix[j]
            if j == -1:
                i += 1
                j += 1
    return -1


pattern = "AB"
text = "ABABABCABAABABABAB"
# prefix = prefix_table(pattern)
# prefix = move_prefix_table(prefix)
# print('prefix ->', prefix)
r = kmp_search(text, pattern)
print(r)
