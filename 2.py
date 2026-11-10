names = ["Александр", "Борис", "Владислав", "Георгий"]
marks = [5, 4, 3, 5]

strings = []
for k, v in zip(names, marks):
    strings.append(f"{k}: {v}")
print(strings)
