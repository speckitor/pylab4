marks = [5, 2, 3, 4, 5]
for i in range(len(marks)):
    print(f"{i + 1}. {marks[i]}")
print()
for i, m in enumerate(marks, start=1):
    print(f"{i}. {m}")
