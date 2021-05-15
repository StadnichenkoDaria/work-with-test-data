from csv import DictReader
from json import loads, dumps

result = []

with open("../data/users.json", "r") as json_file:
    with open("../data/books.csv", "r") as csv_file:
        with open("../data/result.json", "w") as write_file:
            people = loads(json_file.read())
            library = DictReader(csv_file)

            for person in people:
                result.append({'name': person.get('name'), 'gender': person.get('gender'),
                               'address': person.get('address')})

            for i, book in enumerate(library):
                if i < len(result):
                    result[i].update({"books": book})
            write_file.write(dumps(result, indent=4))
