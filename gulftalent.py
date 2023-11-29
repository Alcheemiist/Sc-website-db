import requests
from bs4 import BeautifulSoup
import os
import re

def is_valid_filename(filename):
    return not bool(re.search(r'[\\/*?:"<>|]', filename))

# List of slugs
# with open('sitemap.json', 'r') as f:
#     slugs = f.readlines()
# panel panel-default

slugs = [
"https://www.gulftalent.com/uae/jobs/supply-chain-operation-manager-396699",
"https://www.gulftalent.com/uae/jobs/supply-chain-operation-manager-396699",
"https://www.gulftalent.com/uae/jobs/netsuite-admin-396698",
"https://www.gulftalent.com/uae/jobs/rental-sales-manager-396691",
"https://www.gulftalent.com/uae/jobs/arabic-speaking-sales-executive-for-international-jewellery-brand-396689",
"https://www.gulftalent.com/uae/jobs/digital-project-manager-6-months-contract-396688",
"https://www.gulftalent.com/uae/jobs/it-executive-396686",
"https://www.gulftalent.com/uae/jobs/paralegal-arabic-speaking-396685",
"https://www.gulftalent.com/uae/jobs/executive-assistant-french-speaking-396684",
"https://www.gulftalent.com/uae/jobs/inventory-management-specialist-automobile-396683",
"https://www.gulftalent.com/uae/jobs/business-development-manager-396681",
"https://www.gulftalent.com/uae/jobs/regional-sales-manager-396680",
"https://www.gulftalent.com/uae/jobs/lead-design-mechanical-engineer-396679",
"https://www.gulftalent.com/uae/jobs/social-media-intern-396678",
"https://www.gulftalent.com/uae/jobs/campus-hire-manager-for-an-international-consulting-firm-396676",
"https://www.gulftalent.com/uae/jobs/talent-analytics-senior-specialist-for-an-international-consulting-firm-396675",
"https://www.gulftalent.com/uae/jobs/restaurant-dj-396674",
"https://www.gulftalent.com/uae/jobs/career-dev-staffing-manager-for-an-international-consulting-firm-396672",
"https://www.gulftalent.com/uae/jobs/performance-data-analyst-396670",
"https://www.gulftalent.com/uae/jobs/it-support-396669",
"https://www.gulftalent.com/uae/jobs/family-driver-396668",
"https://www.gulftalent.com/uae/jobs/project-coordinator-396667",
"https://www.gulftalent.com/uae/jobs/junior-product-manager-mobility-products-396665",
"https://www.gulftalent.com/uae/jobs/social-media-marketing-executive-396647",
"https://www.gulftalent.com/uae/jobs/junior-architect-396646",
"https://www.gulftalent.com/uae/jobs/public-relations-executive-396644",
"https://www.gulftalent.com/uae/jobs/planning-engineer-396636",
"https://www.gulftalent.com/uae/jobs/short-video-operations-specialist-396530",
"https://www.gulftalent.com/uae/jobs/government-regulatory-affairs-professional-394993",
"https://www.gulftalent.com/uae/jobs/store-manager-391255",
"https://www.gulftalent.com/uae/jobs/medical-director-388129",
"https://www.gulftalent.com/uae/jobs/salesforce-support-engineer-386881",
"https://www.gulftalent.com/uae/jobs/head-of-pr-government-affairs-385212",
"https://www.gulftalent.com/uae/jobs/sales-manager-385170",
"https://www.gulftalent.com/uae/jobs/real-estate-consultant-384251",
"https://www.gulftalent.com/uae/jobs/sales-and-leasing-consultant-mandarin-speaking-383414",
"https://www.gulftalent.com/uae/jobs/back-end-developer-senior-379339",
"https://www.gulftalent.com/uae/jobs/front-end-developer-377590",
"https://www.gulftalent.com/uae/jobs/residential-real-estate-agent-365572",
"https://www.gulftalent.com/uae/jobs/sales-and-leasing-consultant-360566",
"https://www.gulftalent.com/uae/jobs/assistant-fraud-risk-manager-396587",
"https://www.gulftalent.com/uae/jobs/assistant-manager-bcm-and-orm-396586",
"https://www.gulftalent.com/uae/jobs/financial-controller-396527",
"https://www.gulftalent.com/uae/jobs/human-resource-manager-396526",
"https://www.gulftalent.com/uae/jobs/business-operations-specialist-396523",
"https://www.gulftalent.com/uae/jobs/accounting-manager-396521",
"https://www.gulftalent.com/uae/jobs/strategy-consultant-tech-ai-396520",
"https://www.gulftalent.com/uae/jobs/recruitment-and-sourcing-officer-396519",
"https://www.gulftalent.com/uae/jobs/hr-executive-396518",
"https://www.gulftalent.com/uae/jobs/f-b-supervisor-396517",
"https://www.gulftalent.com/uae/jobs/product-specialist-musical-instruments-396516",
"https://www.gulftalent.com/uae/jobs/graphic-designer-396515"]

i = 0
for slug in slugs:
    i += 1
    slug = slug.strip("[]").replace('"', '').replace(',', '')
    file  = slug.split('/')[-1].strip()
    print(file)
    print(i)
    # os.makedirs(file, exist_ok=True)

    url = slug
    with open(f'./data/{file}.txt', 'w', encoding='utf-8') as outfile:
        outfile.write('Job Offer Link: ' + slug + '\n')
    # Fetch the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements with class 'job-box'
    for element in soup.find_all(class_='header'):
        # Extract the text
        text = element.get_text()
        print("read = ", text.__len__())
        # Write the text to a file
        with open(f'./data/{file}.txt', 'a', encoding='utf-8') as outfile:
            outfile.write(text + '\n')

    for element in soup.find_all(class_='content'):
        # Extract the text
        text = element.get_text()
        print("read = ", text.__len__())
        # Write the text to a file
        with open(f'./data/{file}.txt', 'a', encoding='utf-8') as outfile:
            outfile.write(text + '\n')