students = [
        {"name": "Арсений", "score": 67, "attempts": 1},
        {"name": "Егор", "score": 42, "attempts": 5},
        {"name": "Данил", "score": 78, "attempts": 4},
        {"name": "Захар", "score": 80, "attempts": 2},
]

names1 = []
for i in students:
    if i["score"] >= 60 and i["attempts"] <= 3:
        names1.append(i["name"])
print(names1)

names2 = [i["name"] for i in students if i["score"] >= 60 and i["attempts"] <= 3]
print(names2)
print(names1 == names2)
