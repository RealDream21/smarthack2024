import csv
import random

def extract_ids_from_csv():
    ids = []
    filename = "data/refineries.csv"
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            ids.append(row['id'])
    return ids

# Function to generate a random float with two decimal places between given min and max
def random_float(min_val, max_val):
    return round(random.uniform(min_val, max_val), 2)

# Function to generate a random integer between given min and max
def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

# Function to generate quantities with specific ranges and weights
def generate_quantities(size):
    weights = [0.15, 0.35, 0.35, 0.15]
    ranges = [(100, 1000), (1001, 10000), (10001, 100000), (100001, 300000)]
    
    results = []
    for _ in range(size):
        selected_range = random.choices(ranges, weights=weights)[0]
        results.append(random.randint(*selected_range))
    
    return results

def generate_refinery_data(filename):
    ids = extract_ids_from_csv()
    num_rows = len(ids)
    quantities = generate_quantities(num_rows)  # Pass the integer num_rows to generate_quantities

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # Write header
        writer.writerow([
            "id", "name", "capacity", "max_output", "production",
            "overflow_penalty", "underflow_penalty", "over_output_penalty",
            "production_cost", "production_co2", "initial_stock", "node_type"
        ])
        
        for i in range(num_rows):
            refinery_id = ids[i]
            name = f"refinery {i}"
            
            # Capacity with more likelihood between 1000 and 10000
            capacity = quantities[i]
            
            # max_output strictly less than capacity
            max_output = random_int(1, capacity - 1)
            
            # production less than max_output
            production = random_int(1, max_output)
            
            # Penalties, costs, and CO2 are floats between 2.0 and 6.0
            overflow_penalty = random_float(2.0, 6.0)
            underflow_penalty = random_float(2.0, 6.0)
            over_output_penalty = random_float(2.0, 6.0)
            production_cost = random_float(2.0, 6.0)
            production_co2 = random_float(2.0, 6.0)
            
            # initial_stock must be less than capacity, ensuring initial_stock + production < capacity
            max_initial_stock = capacity - production - 1
            initial_stock = random_int(0, max_initial_stock)
            
            node_type = "REFINERY"

            # Write the row to the CSV
            writer.writerow([
                refinery_id, name, capacity, max_output, production,
                overflow_penalty, underflow_penalty, over_output_penalty,
                production_cost, production_co2, initial_stock, node_type
            ])
    
    print(f"CSV file '{filename}' generated successfully.")

# Example of how to call the function from another script
# generate_refinery_data("output/refinery_data.csv")

generate_refinery_data("test_refineries.csv")