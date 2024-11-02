import os
import csv

class Customer:
    def __init__(self, id, name, max_input, over_input_penalty, late_delivery_penalty, early_delivery_penalty, node_type):
        self.id = id
        self.name = name
        self.max_input = float(max_input)
        self.over_input_penalty = float(over_input_penalty)
        self.late_delivery_penalty = float(late_delivery_penalty)
        self.early_delivery_penalty = float(early_delivery_penalty)
        self.node_type = node_type

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, max_input={self.max_input})"


def read_customers_from_csv():
    customers = []
    path = os.getcwd()
    path = os.path.join(path, 'data')
    path = os.path.join(path,'customers.csv')
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            customer = Customer(
                id=row['id'],
                name=row['name'],
                max_input=row['max_input'],
                over_input_penalty=row['over_input_penalty'],
                late_delivery_penalty=row['late_delivery_penalty'],
                early_delivery_penalty=row['early_delivery_penalty'],
                node_type=row['node_type']
            )
            customers.append(customer)
    return customers

