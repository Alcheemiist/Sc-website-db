import os

# Directory containing the text files
directory = "./data-origin/"

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
"Advertise Here",
"Employment:",
"Easy Apply",
"Explore Future Tense careers",
"Show More",
"Explore Future Tense careers",
]

# Function to process a single file
def process_file(file_path, output_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove tabulation
    lines = [line.lstrip('\t') for line in lines]

    # Remove duplicates and filter out lines with keywords
    unique_lines = set()
    processed_lines = []
    for line in lines:
        line.lstrip('\t')
        line = line.lstrip('\n- ')

        if line.strip() and line not in unique_lines and not any(keyword in line for keyword in keywords):
            unique_lines.add(line)
            processed_lines.append(line)

    # Write the processed lines back to the file
    with open(output_path, 'w') as file:
        file.writelines(processed_lines)

# Process each file in the directory
for filename in os.listdir(directory):
    print(f'Processing {filename}...')
    if filename.endswith('.txt'):
        process_file(os.path.join(directory, filename), os.path.join('./data-transform/', filename))
