import connections
import csv_to_customers
import csv_to_tanks
import rafineries
import gymnasium as gym
import numpy as np


class Model_Inatorul(gym.Env):
    def __init__(self, rafineries, tanks, customers, connections):
        self.rafineries = rafineries
        self.tanks = tanks
        self.customers = customers
        self.connections = connections
        self.con_out_max = max([x.max_capacity for x in self.connections])
        self.action_space = gym.spaces.Box(low=0.0, high=self.con_out_max, shape=(len(connections),), dtype=np.int32)
        self.connection_set = set([(x.from_id. x.to_id) for x in connections])
        
        for ref in rafineries:
            for tank in tanks:
                connections.append()

        self.observation_space = gym.spaces.Discrete(len(rafineries))(
        )

    def __repr__(self):
        return (f"env(rafineries={self.rafineries}, tanks={self.tanks}, customers={self.customers}, connections={self.conections})")
        







