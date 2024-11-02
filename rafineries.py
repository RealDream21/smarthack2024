import pandas as pd
from typing import List
import os

class Refinery:
    def __init__(self, id, name, capacity, max_output, production, overflow_penalty, underflow_penalty, 
                 over_output_penalty, production_cost, production_co2, initial_stock, node_type):
        self.id = id
        self.name = name
        self.capacity = int(capacity)
        self.max_output = int(max_output)
        self.production = int(production)
        self.overflow_penalty = float(overflow_penalty)
        self.underflow_penalty = float(underflow_penalty)
        self.over_output_penalty = float(over_output_penalty)
        self.production_cost = float(production_cost)
        self.production_co2 = float(production_co2)
        self.initial_stock = int(initial_stock)
        self.node_type = node_type

    def __repr__(self):
        return (
            f"<Refinery(id={self.id}, name={self.name}, capacity={self.capacity}, max_output={self.max_output}, "
            f"production={self.production}, overflow_penalty={self.overflow_penalty}, underflow_penalty={self.underflow_penalty}, "
            f"over_output_penalty={self.over_output_penalty}, production_cost={self.production_cost}, "
            f"production_co2={self.production_co2}, initial_stock={self.initial_stock}, node_type={self.node_type})>"
        )

def read_refineries_from_csv(filepath = None):

    filepath = os.getcwd()
    filepath = os.path.join(filepath, 'data')
    filepath = os.path.join(filepath,'refineries.csv')

    df = pd.read_csv(filepath, delimiter=';')
    
    refineries = [
        Refinery(
            id=row['id'],
            name=row['name'],
            capacity=row['capacity'],
            max_output=row['max_output'],
            production=row['production'],
            overflow_penalty=row['overflow_penalty'],
            underflow_penalty=row['underflow_penalty'],
            over_output_penalty=row['over_output_penalty'],
            production_cost=row['production_cost'],
            production_co2=row['production_co2'],
            initial_stock=row['initial_stock'],
            node_type=row['node_type']
        )
        for _, row in df.iterrows()
    ]
    
    return refineries

