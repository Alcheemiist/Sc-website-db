import os

# Directory containing the text files
directory = "./gulfjob-data/"

# Keywords to filter out
keywords = ["Posted on", "Send Me Jobs Like This", "APPLY NOW", "DISCLAIMER", "Email to Friend", "Add to Favourite Jobs  Report Abuse"]  # Add your keywords here

# Function to process a single file
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove duplicates and filter out lines with keywords
    unique_lines = set()
    processed_lines = []
    for line in lines:
        line = line.replace('\t', '')  # Remove tabulation
        if line.strip() and line not in unique_lines and not any(keyword in line for keyword in keywords):
            processed_lines.append(line)
            unique_lines.add(line)

    # Write the processed lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(processed_lines)

# Process each file in the directory
for filename in os.listdir(directory):
    print(f'Processing {filename}...')
    if filename.endswith('.txt'):
        process_file(os.path.join(directory, filename))
