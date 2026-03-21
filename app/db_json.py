import json

shipment_dict = {}

file_path = "app/data/data.json"


def load_shipments():
    with open(file_path) as json_file:
        data = json.load(json_file)

        for value in data:
            shipment_dict[value["id"]] = value


def save_shipments():
    with open(file_path, "w") as json_file:
        json.dump(list(shipment_dict.values()), json_file)
