dyef min_road_width(n, h, heights):
    width = 0
    for height in heights:
        if height <= h:
            width += 1
        else:
            width +=3
    return width
n, h = map(int, input("Enter number of friends and the height of the fence: " ).split())
heights = list(map(int, input("Enter the height of the i-th person: ").split()))

print(min_road_width(n, h, heights))
