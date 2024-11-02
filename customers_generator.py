import csv
import uuid
import random

# luam id urile clientilor:

def get_customers_ids():
    ids = []
    filename = "data/customers.csv"
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            ids.append(row['id'])
    return ids

def customer_generator(filename):
    num_rows = 200
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        
        writer = csv.writer(file, delimiter=';')
        # Write header
        writer.writerow(["id", "name","max_input","over_input_penalty","late_delivery_penalty","early_delivery_penalty","node_type"])
        
        # Generate each row with random data
        ids = get_customers_ids()
        max_input_range = (50, 1000)
        over_input_penalty_range = (0, 5)
        late_delivery_penalty_range = (0, 0.9)
        early_delivery_penalty_range = (0, 1.2)
        
        
        for i in range(num_rows):
            id = ids[i]
            name = f'customer {i + 1}'
            max_input = random.randint(*max_input_range)
            over_input_penalty = round(random.uniform(*over_input_penalty_range), 2)
            late_delivery_penalty = round(random.uniform(*late_delivery_penalty_range), 2)
            early_delivery_penalty = round(random.uniform(*early_delivery_penalty_range), 2)
            node_type = "CUSTOMER"
            
            # Write the row to the file
            writer.writerow([id, name, max_input, over_input_penalty, late_delivery_penalty, early_delivery_penalty, node_type])

# filename = "train_customers.csv"
# customer_generator(filename)