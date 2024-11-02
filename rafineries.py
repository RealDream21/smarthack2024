import pandas as pd
from typing import List
import os
from global_variables import WEBSITE, API_KEY
import requests

class SessionError(Exception):
    """Custom exception for session-related errors."""
    pass


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

        #add current stock attribute  
        self.current_stock = int(initial_stock)

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

def get_refinery_by_name(refineries: List[Refinery], name: str) -> Refinery:
    for refinery in refineries:
        if refinery.name == name:
            return refinery
    return None

# this function calls the api and gets the current stock for each refinery


def change_all_refinery_stock(refineries, SESSION_ID):
    url = "http://localhost:8080/api/v1/play/getNodesByType"

    headers= {
        "accept": "*/*",
        "API-KEY": "7bcd6334-bc2e-4cbf-b9d4-61cb9e868869",
        "SESSION-ID": SESSION_ID,
        "NODE_TYPE": "REFINERY"
    }

    response = requests.post(url, headers=headers, data='')

    if response.status_code != 200:
        raise SessionError(f"Failed to start session: {response.status_code} - {response.text}")
    
    data = response.json()

    for node in data.get('nodeStatusDtos', []):
        name = node.get("name")
        stock = node.get("stock")

        refinery = get_refinery_by_name(refineries, name)

        refinery.current_stock = stock





    
