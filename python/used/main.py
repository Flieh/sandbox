import json

data = {
        "user": {
            "name": "William Jones",
            "age": 94,
            "rank": "Captain"
            }
        }

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_str = json.dumps(data)
print(json_str)
