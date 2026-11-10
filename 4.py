words = ["fox", "cat", "dog", "cat", "eagle", "fox"]

d1 = {}
for i in words:
    d1[i] = len(i)
print("d1:", d1)

d2 = {i: len(i) for i in words}
print("d2:", d2)

print(f"d1 == d2: {d1 == d2}")
