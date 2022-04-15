import json


def read_json(json_file):
    json_decoded = json.load(json_file)
    return json_decoded


def add_dict(dict1, dict2):
    dict1.update(dict2)
    return dict1


def save_json(jsonDict, name):
    jsonData = json.dumps(jsonDict, sort_keys=True, indent=4)
    jsonFile = open(name, "w")
    jsonFile.write(jsonData)
    jsonFile.close()
