import csv
import uuid
import random

# luam id urile clientilor:

def extract_ids_from_csv():
    ids = []
    filename = "data/customers.csv"
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            ids.append(row['id'])
    return ids


def get_random_customer_id():
    customer_ids = extract_ids_from_csv()
    customer_range = (0, 199)
    return(customer_ids[random.randint(*customer_range)])


def get_post_days():
    post_days = []
    filename = "data/demands.csv"
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            post_days.append(int(row['post_day']))     
    return post_days


def generate_quantities():
    size = 1542
    # Define ranges and their weights
    weights = [0.7, 0.2, 0.09, 0.01]  
    ranges = [(100, 900), (901, 3000), (3001, 6000), (6001, 9000)]
    
    # Generate random numbers
    results = []
    for _ in range(size):
        selected_range = random.choices(ranges, weights=weights)[0]
        results.append(random.randint(*selected_range))
    
    return results



def generate_random_csv(filename, num_rows):
    # Define the number of rows you want to generate

    quantities = generate_quantities()
    start_delivery_day_range = (3, 12)
    end_delivery_day_offset = (3, 12)  # Offset from start_delivery_day for end_delivery_day
    post_days = get_post_days()

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # Write header
        writer.writerow(["id", "customer_id", "quantity", "post_day", "start_delivery_day", "end_delivery_day"])
        
        # Generate each row with random data
        for i in range(num_rows):
            row_id = str(uuid.uuid4())
            customer_id = get_random_customer_id()
            quantity = quantities[i]
            post_day_val = post_days[i]
            
            start_delivery_day = post_day_val + random.randint(*start_delivery_day_range)
            end_delivery_day = min(start_delivery_day + random.randint(*end_delivery_day_offset), 42)
            
            # Write the row to the file
            writer.writerow([row_id, customer_id, quantity, post_day_val, start_delivery_day, end_delivery_day])


# filename = "train_1.csv"
# num_rows = 1542
# generate_random_csv(filename, num_rows)

