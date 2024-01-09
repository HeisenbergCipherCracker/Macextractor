def extract_the_mac(file_path="/Users/alimirmohammad/Macextractor/filecaps/extracted.txt"):
    unique_macs = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                mac = line.strip()
                unique_macs.add(mac)  # Use a set to ensure uniqueness
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return list(unique_macs)

# Example usage:
unique_macs_list = extract_the_mac()

# Now you can iterate through the unique MAC addresses using a for loop:
# for mac in unique_macs_list:
#     new = [line for line in unique_macs_list]
