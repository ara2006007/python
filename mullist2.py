x = [
    ["Student Name", "Maths", "Science", "English", "ICT"],
    ["Ara", 87, 98, 78, 90],
    ["Ava", 77, 58, 48, 80],
    ["Aca", 85, 48, 98, 45],
    ["Mra", 87, 98, 78, 90],
    ["Ari", 82, 58, 74, 70]
]

subjects_count = len(x[0]) - 1  # number of subjects

y = [["Student Name", "Total", "Average"]]

for i in range(1, len(x)):  # skip header
    total = sum(x[i][1:])   # sum marks only
    avg = total / subjects_count
    y.append([x[i][0], total, avg])

print(y)