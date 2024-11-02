import requests

WEBSITE = "http://localhost:8080"

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
        raise SessionError(f"Failed to execute round: {response.status_code} - {response.text}")

    # Return the parsed JSON response

    # TODO - Implement the logic to handle the response
    # CREATE a function that gets the response and create an object.
    return response.json()


try:
    API_KEY = "7bcd6334-bc2e-4cbf-b9d4-61cb9e868869"
    SESSION_ID = session_start(API_KEY)
    print("Session ID:", SESSION_ID)

    play_round(SESSION_ID, API_KEY, 0, [])

    session_end(API_KEY)
except SessionError as e:
    print("An error occurred while starting the session:", e)
except requests.RequestException as e:
    print("A network error occurred:", e)