string1 = str(input().strip())
string2 = str(input().strip())
string1_lower = string1.lower()
string2_lower = string2.lower()

if string1_lower < string2_lower:
    print(-1)
elif string1_lower > string2_lower:
    print(1)
else:
    print(0)
