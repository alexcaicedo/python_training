records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

scores_list = []
for student in records:
    for val in student:
        pass