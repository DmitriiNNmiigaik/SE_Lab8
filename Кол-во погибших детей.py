import csv
deceased_children_by_embarkation = {'C': 0, 'Q': 0, 'S': 0}

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if row[6] != '':
            age = float(row[6])
            survived_status = int(row[1])
            embarked = row[11]

            if survived_status == 0 and (age and float(age) < 18):
                deceased_children_by_embarkation[embarked] += 1

for embarkation, count in deceased_children_by_embarkation.items():
    print(f"Пункт посадки {embarkation}: {count} погибших детей (возраст ниже 18 лет)")

