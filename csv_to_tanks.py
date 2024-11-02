import csv
import os
import requests

class SessionError(Exception):
    """Custom exception for session-related errors."""
    pass

class StorageTank:
    def __init__(self, id, name, capacity, max_input, max_output, overflow_penalty, underflow_penalty, over_input_penalty, over_output_penalty, initial_stock, node_type):
        self.id = id
        self.name = name
        self.capacity = float(capacity)
        self.max_input = float(max_input)
        self.max_output = float(max_output)
        self.overflow_penalty = float(overflow_penalty)
        self.underflow_penalty = float(underflow_penalty)
        self.over_input_penalty = float(over_input_penalty)
        self.over_output_penalty = float(over_output_penalty)
        self.initial_stock = float(initial_stock)
        self.node_type = node_type

        self.current_stock = float(initial_stock)

    def __repr__(self):
        return f"StorageTank(id={self.id}, name={self.name}, capacity={self.capacity}, initial_stock={self.initial_stock})"

# Function to read the CSV and create StorageTank objects
def read_storage_tanks_from_csv():
    path = os.getcwd()
    path = os.path.join(path, 'data')
    path = os.path.join(path,'tanks.csv')
    # print(path)
    storage_tanks = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            tank = StorageTank(
                id=row['id'],
                name=row['name'],
                capacity=row['capacity'],
                max_input=row['max_input'],
                max_output=row['max_output'],
                overflow_penalty=row['overflow_penalty'],
                underflow_penalty=row['underflow_penalty'],
                over_input_penalty=row['over_input_penalty'],
                over_output_penalty=row['over_output_penalty'],
                initial_stock=row['initial_stock'],
                node_type=row['node_type'],
            )
            storage_tanks.append(tank)
    return storage_tanks


def get_tank_by_name(storage_tanks, name):
    for tank in storage_tanks:
        if tank.name == name:
            return tank
    return None

def change_all_tank_stock(storage_tanks, SESSION_ID):
    url = "http://localhost:8080/api/v1/play/getNodesByType"

    headers= {
        "accept": "*/*",
        "API-KEY": "7bcd6334-bc2e-4cbf-b9d4-61cb9e868869",
        "SESSION-ID": SESSION_ID,
        "NODE_TYPE": "STORAGE_TANK"
    }

    response = requests.post(url, headers=headers, data='')

    if response.status_code != 200:
        raise SessionError(f"Failed to start session: {response.status_code} - {response.text}")
    
    data = response.json()

    for node in data.get('nodeStatusDtos', []):
        name = node.get("name")
        stock = node.get("stock")

        tanks = get_tank_by_name(storage_tanks, name)
        tanks.current_stock = stock
