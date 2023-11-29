import os

# Directory containing the text files
directory = "./data/"

# Keywords to filter out
keywords = [
"Jobs",
"Salaries",
"Resources",
"Free CV Review",
"CV Writing Service",
"Labour Laws",
"Public Holidays",
"For Employers",
"Login",
"Register",
"Posted"
"Easy Apply",
"New Job Search",
"View Similar Jobs",
"{{ flashMessage.message }}",
"Expand all",
"×",
"Explore our CV database",
"Post a job now",
"Find Top Talent",
"Explore Michael Page careers",
"Receive relevant jobs by email",
"Advertise Here"
]

# Function to process a single file
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove duplicates and filter out lines with keywords
    unique_lines = set()
    processed_lines = []
    for line in lines:
        if line.strip() and line not in unique_lines and not any(keyword in line for keyword in keywords):
            processed_lines.append(line)
            unique_lines.add(line.replace('\t', '') )

    # Write the processed lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(processed_lines)

# Process each file in the directory
for filename in os.listdir(directory):
    print(f'Processing {filename}...')
    if filename.endswith('.txt'):
        process_file(os.path.join(directory, filename))
