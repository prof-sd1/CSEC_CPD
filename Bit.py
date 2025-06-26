n = int(input())  # Number of statements
x = 0  # Initial value of x

for _ in range(n):
    statement = input()
    if "++" in statement:
        x += 1
    else:
        x -= 1

print(x)