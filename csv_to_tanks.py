import csv
import os

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
                node_type=row['node_type']
            )
            storage_tanks.append(tank)
    return storage_tanks

