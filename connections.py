import pandas as pd
import os
class Connection:
    def __init__(self, id, from_id, to_id, distance, lead_time_days, connection_type, max_capacity):
        self.id = id
        self.from_id = from_id
        self.to_id = to_id
        self.distance = int(distance)
        self.lead_time_days = int(lead_time_days)
        self.connection_type = connection_type
        self.max_capacity = int(max_capacity)

    def __repr__(self):
        return (f"Connection(id={self.id}, from_id={self.from_id}, to_id={self.to_id}, "
                f"distance={self.distance}, lead_time_days={self.lead_time_days}, "
                f"connection_type={self.connection_type}, max_capacity={self.max_capacity})")


path = os.getcwd()

# Load CSV data into a pandas DataFrame
df = pd.read_csv('data/connections.csv', delimiter=';')

def create_connections():
    # Convert each row in the DataFrame to a Connection object
    connections = [Connection(row['id'], row['from_id'], row['to_id'], row['distance'],
                            row['lead_time_days'], row['connection_type'], row['max_capacity'])
                for _, row in df.iterrows()]
    return connections

