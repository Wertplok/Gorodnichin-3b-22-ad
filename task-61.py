coords = [(1, 2), (3, 4), (-1, 5), (6, -3)]

coords.sort(key=lambda x: (x[0]**2 + x[1]**2)**0.5)
print(coords)
