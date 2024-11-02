import requests
from global_variables import WEBSITE, API_KEY

class Demand:
    def __init__(self, customer_id, amount, post_day, start_day, end_day):
        self.customer_id = customer_id
        self.amount = amount
        self.post_day = post_day
        self.start_day = start_day
        self.end_day = end_day

    def __repr__(self):
        return f"Demand(customer_id={self.customer_id}, amount={self.amount}, post_day={self.post_day}, start_day={self.start_day}, end_day={self.end_day})"

class Kpis:
    def __init__(self, day, cost, co2):
        self.day = day
        self.cost = cost
        self.co2 = co2

    def __repr__(self):
        return f"Kpis(day={self.day}, cost={self.cost}, co2={self.co2})"

class RoundResponse:
    def __init__(self, round, demand, penalties, delta_kpis, total_kpis):
        self.round = round
        self.demand = demand
        self.penalties = penalties  # list of penalty dictionaries or further subclassed if structure known
        self.delta_kpis = delta_kpis
        self.total_kpis = total_kpis

    def __repr__(self):
        return (f"RoundResponse(round={self.round}, demand={self.demand}, penalties={self.penalties}, "
                f"delta_kpis={self.delta_kpis}, total_kpis={self.total_kpis})")

    @classmethod
    def from_json(cls, data):
        # Parse demand list
        demand = [Demand(d['customerId'], d['amount'], d['postDay'], d['startDay'], d['endDay']) for d in data.get('demand', [])]

        # Parse delta and total KPIs
        delta_kpis = Kpis(**data['deltaKpis'])
        total_kpis = Kpis(**data['totalKpis'])

        return cls(
            round=data['round'],
            demand=demand,
            penalties=data.get('penalties', []),
            delta_kpis=delta_kpis,
            total_kpis=total_kpis
        )
    
class SessionError(Exception):
    """Custom exception for session-related errors."""
    pass

def session_start(API_KEY):
    url =  WEBSITE + "/api/v1/session/start"
    
    headers = {
    "accept": "*/*",
    "API-KEY": API_KEY
    }

    response = requests.post(url, headers=headers, data='')

    if response.status_code != 200:
        raise SessionError(f"Failed to start session: {response.status_code} - {response.text}")

    # Return the session ID
    return response.text.strip()

def session_end(API_KEY):
    url = WEBSITE + "/api/v1/session/end"
    headers = {
        "accept": "*/*",
        "API-KEY": API_KEY
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data='')

    # Raise an error if the request was not successful
    if response.status_code != 200:
        raise SessionError(f"Failed to end session: {response.status_code} - {response.text}")

    # Return the result, typically confirmation or an empty response
    return response.json()

def play_round(SESSION_ID, API_KEY, day, movements):
    url = WEBSITE + "/api/v1/play/round"
    headers = {
        "accept": "*/*",
        "API-KEY": API_KEY,
        "SESSION-ID": SESSION_ID,
        "Content-Type": "application/json"
    }

    # Define the JSON payload
    payload = {
        "day": day,
        "movements": movements
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    # Raise an error if the request was not successful
    if response.status_code != 200:
        session_end(API_KEY) # End the session if an error occurred
        raise SessionError(f"Failed to execute round: {response.status_code} - {response.text}")

    # Return the RoundResponse object
    return RoundResponse.from_json(response.json())

