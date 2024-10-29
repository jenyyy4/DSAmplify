def valid_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = {}

    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s2:
        if char in char_count:
            if char_count[char] == 1:
                del char_count[char]
            else:
                char_count[char] -= 1
        else:
            return False

    return len(char_count) == 0

s1 = input()
s2 = input()
print(valid_anagram(s1, s2))
