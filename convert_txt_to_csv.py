import csv
from os import listdir

def parse_job_data(text):
    """
    Parse the job data from the given text block.
    """
    job_data = {}
    lines = text.strip().split('\n')
    job_data['Title'] = lines[0]


    for line in lines[1:]:
        try:
            key, value = line.split(':', 1)
            job_data[key.strip()] = value.strip()
        except ValueError:
            continue


    return job_data

# File paths
output_file_path = 'output_r.csv'

# Headers for CSV file
headers = ['Title', 'Job Offer Link','COMPANY', "LOCATION", "JOB DESCRIPTION / ROLE","REQUIREMENTS", "ABOUT THE COMPANY", 'Other jobs you might be interested in', "Salary"]

# Directory path
dir_path = './data-filtered'

# Open the output file and write the header
with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

# Read the text file and parse each job
for filename in listdir(dir_path):
    input_file_path = f'{dir_path}/{filename}'
    with open(input_file_path, 'r') as file:
        text = file.read()
        job_blocks = text.split('\n\n')  # Assuming each job is separated by two newlines

        # Append to the output file
        with open(output_file_path, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            # for job_block in job_blocks:
            job_data = parse_job_data(text)
            writer.writerow(job_data)

print("Data conversion complete. Check the output.csv file.")
