import csv
import random

def extract_ids_from_csv():
    """Extracts tank IDs from the 'data/tanks.csv' file."""
    ids = []
    filename = "data/tanks.csv"
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

def generate_tanks_data(csv_path):
    """
    Generates tank data based on IDs from 'data/tanks.csv' and writes it to a specified CSV path.
    
    Parameters:
    - csv_path: The path where the generated CSV file will be saved.
    """
    ids = extract_ids_from_csv()
    num_rows = len(ids)  # Use the number of rows equal to the number of extracted IDs
    
    # List to hold the data
    data = []

    for i in range(num_rows):
        tank_id = ids[i]
        name = f"tank {i}"
        capacity = random_int(10**4, 10**6)
        max_input = random_int(10**3, 10**4)
        max_output = random_int(max_input + 1, max_input + 10**3)  # Ensure max_output > max_input
        overflow_penalty = random_float(1.0, 6.0)
        underflow_penalty = random_float(1.0, 6.0)
        over_input_penalty = random_float(1.0, 6.0)
        over_output_penalty = random_float(1.0, 6.0)
        initial_stock = random_int(10**4, 10**6)
        node_type = "STORAGE_TANK"
        
        data.append([
            tank_id, name, capacity, max_input, max_output,
            overflow_penalty, underflow_penalty, over_input_penalty,
            over_output_penalty, initial_stock, node_type
        ])

    # Write data to CSV with semicolon as delimiter
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # Write header
        writer.writerow([
            "id", "name", "capacity", "max_input", "max_output",
            "overflow_penalty", "underflow_penalty", "over_input_penalty",
            "over_output_penalty", "initial_stock", "node_type"
        ])
        # Write data rows
        writer.writerows(data)

    print(f"CSV file '{csv_path}' generated successfully.")

generate_tanks_data("generated_tanks.csv")