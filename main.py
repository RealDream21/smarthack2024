from global_variables import WEBSITE, API_KEY
import api_connection

#this is the code for the a game to start (it has 42 rounds)
# create try except block to handle exceptions
def game(API_KEY):
    try:
        SESSION_ID = api_connection.session_start(API_KEY)

        print("Session ID:", SESSION_ID)
        #create the first round and get the demands
        round_response = api_connection.play_round(SESSION_ID, API_KEY, 0, [])
        demands = round_response.demand 
        movements = [] # will be a function here
        #parse to another function that will handle the demands
        #this function will return some movements
        for i in range(1, 42):
            try:
                round_response = api_connection.play_round(SESSION_ID, API_KEY, i, movements=movements)
                demands = round_response.demand
                movements = [] # will be a function here
            except api_connection.SessionError as e:
                print(f"An error occurred during round {i}: {e}")
                break
            except api_connection.requests.RequestException as e:
                print(f"A network error occurred during round {i}: {e}")
                break

        api_connection.session_end(API_KEY)
    except api_connection.SessionError as e:
        print("An error occurred during the game session:", e)
    except api_connection.requests.RequestException as e:
        print("A network error occurred during the game session:", e)

def main():
    try:
        game(API_KEY)
    except api_connection.SessionError as e:
        print("An error occurred while starting the session:", e)
    except api_connection.requests.RequestException as e:
        print("A network error occurred:", e)

if __name__ == "__main__":
    main()