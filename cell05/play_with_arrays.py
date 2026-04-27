a = [2, 8, 9, 48, 8, 22, -12, 2]
b = []

for x in a:
    if x > 5:
        b.append(x + 2)

print(a)
print(set(b))