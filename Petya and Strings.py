s1 = input().strip()
s2 = input().strip()

# Convert both strings to lowercase for case-insensitive comparison
s1_lower = s1.lower()
s2_lower = s2.lower()

# Compare lexicographically
if s1_lower < s2_lower:
    print(-1)
elif s1_lower > s2_lower:
    print(1)
else:
    print(0)