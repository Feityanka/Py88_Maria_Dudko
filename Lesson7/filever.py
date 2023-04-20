# Stroke1 = input()
# Stroke2 = input()
# Stroke3 = input()
# Stroke4 = input()
#
# with open("NewFile.txt", "w") as f:
#     f.write(Stroke1)
#     f.write("\n")
#     f.write(Stroke2)
#
# f = open('NewFile.txt', 'a')
# f.write("\n")
# f.write(Stroke3)
# f.write("\n")
# f.write(Stroke4)
# f.close()

dict = {
    123456: ("Mary", "35", "33-22-11"),
    234567: ("Lera", "18", "22-14-23"),
    345678: ("Misha", "32", "42-76-34"),
    456789: ("Vova", "15", "86-92-24"),
    567890: ("Nikita", "22", "71-37-93")
}

import json

with open("data_file.json", "w") as write_file:
    json.dump(dict, write_file, indent=4)

import csv

with open("data_file.json", "r") as f_json:
    data = json.load(f_json)
with open("some.csv", 'w') as f_csv:
    writer = csv.writer(f_csv, delimiter=",")
    headers = ['             ']+[f'person {i}' for i in range(1,len(data)+1)]
    writer.writerow(headers)
    _id = ['id           ']
    names = ['name         ']
    ages = ['age          ']
    phone = ['Phone Number ']
    for k, (username, age, numeros) in data.items():
        _id.append(k)
        names.append(username)
        ages.append(age)
        phone.append(numeros)
    headers2 = [_id, names, ages]
    writer.writerows(headers2)
    writer.writerow(phone)
