def correct_word_case(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = len(s) - uppercase_count     
    if uppercase_count > lowercase_count:
        return s.upper()
    else:
        return s.lower()
s = input()
print(correct_word_case(s))
