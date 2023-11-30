import re
import os

directory = './data-origin'  # Directory path
files = os.listdir(directory)  # Get a list of all files in the directory

# Provided text (truncated for the example)
for file in files:
    with open(os.path.join(directory, file), 'r') as f:
        text = f.read()
    # Dictionary to hold structured data
    structured_data = {}

    # Extracting sections using regular expressions and string methods

    # Job Offer Link
    link_pattern = r"Job Offer Link: (https?://\S+)"
    structured_data['Job Offer Link'] = re.search(link_pattern, text).group(1).strip()

    # Job Title (assuming it follows 'Register')
    title_pattern = r"Register\s*\n*\s*(.*?)\s*\n"
    structured_data['Job Title'] = re.search(title_pattern, text, re.DOTALL).group(1).strip()

    # Company Name
    company_pattern = r"\n\s*(.*?)\s*\nUAE"
    structured_data['Company'] = re.search(company_pattern, text, re.DOTALL).group(1).strip()

    # Job Description (simplified for example)
    description_start = text.find("JOB DESCRIPTION / ROLE") + len("JOB DESCRIPTION / ROLE")
    description_end = text.find("REQUIREMENTS")
    job_description = text[description_start:description_end].strip()
    structured_data['Job Description'] = re.sub(r'\s+', ' ', job_description)

    # Requirements (simplified for example)
    requirements_start = description_end + len("REQUIREMENTS")
    requirements_end = text.find("ABOUT THE COMPANY")
    requirements = text[requirements_start:requirements_end].strip()
    structured_data['Requirements'] = re.sub(r'\s+', ' ', requirements)

    # Company Info (simplified for example)
    company_info = text[requirements_end + len("ABOUT THE COMPANY"):].strip()
    structured_data['About The Company'] = re.sub(r'\s+', ' ', company_info)

    # Printing structured data
    for key, value in structured_data.items():
        with open(os.path.join('./data-structured', file), 'a') as f:
            f.write(f"{key}: {value}\n")