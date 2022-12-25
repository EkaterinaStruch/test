import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as csvfile:
        data = []
        json_data = []
        rows = csvfile.read()[:-1].split('\n')
        for row in rows:
            data.append(row.split(','))
        for i in range(1, len(rows)):
            json_data.append(dict(zip(data[0], data[i])))

    return json_data
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
