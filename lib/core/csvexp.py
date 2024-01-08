import csv
from datetime import datetime

def parse_time(time_str):
    return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

def extract_station_info(csv_file):
    with open(csv_file, 'r') as file:
        # Read the CSV file
        reader = csv.reader(file)
        lines = list(reader)

    # Extract BSSID information
    bssid_info = lines[1]
    bssid = bssid_info[0]

    # Extract station information
    station_lines = lines[3:]
    
    # Create a dictionary to store station details
    station_details = {
        'BSSID': bssid,
        'Stations': []
    }

    for station_line in station_lines:
        station_mac = station_line[0]
        first_seen = parse_time(f"{station_line[1]} {station_line[2]}")
        last_seen = parse_time(f"{station_line[3]} {station_line[4]}")
        power = int(station_line[5])

        # Append station details to the dictionary
        station_details['Stations'].append({
            'Station MAC': station_mac,
            'First time seen': first_seen,
            'Last time seen': last_seen,
            'Power': power
        })

    return station_details

# Specify the path to your CSV file
csv_file_path = "/Users/alimirmohammad/Macextractor/filecaps/eightcap-01.csv"

# Extract and print the station details
result = extract_station_info(csv_file_path)
print("BSSID\tFirst time seen\tLast time seen\tPower")
print(f"{result['BSSID']}\t{result['Stations'][0]['First time seen']}\t{result['Stations'][0]['Last time seen']}\t{result['Stations'][0]['Power']}")
