lst1 = []
for i in range(100):
    if i % 2 == 0:
        lst1.append(i*i)

lst2 = [i*i for i in range(100) if i % 2 == 0]

print(lst1)
print(lst2)
print(lst1 == lst2)
