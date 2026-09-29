import json


def save_cycle(cycle_data):

    try:
        with open("cycle_data.json", "r") as file:
            cycles = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        cycles = []

    cycles.append(cycle_data)

    with open("cycle_data.json", "w") as file:
        json.dump(
            cycles,
            file,
            indent=4)


def get_cycles():

    try:
        with open("cycle_data.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []