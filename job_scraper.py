# Task 6: Web Scraping and Analysis of Job Postings

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Website with sample job listings
url = "https://realpython.github.io/fake-jobs/"

# Request the webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find job cards
jobs = soup.find_all("div", class_="card-content")

job_titles = []
companies = []
locations = []

# Extract data
for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    job_titles.append(title)
    companies.append(company)
    locations.append(location)

# Create DataFrame
df = pd.DataFrame({
    "Job Title": job_titles,
    "Company": companies,
    "Location": locations
})

print("\nFirst 5 Jobs")
print(df.head())

# Save scraped jobs
df.to_csv("job_listings.csv", index=False)

# ---------------------------------
# Skill Analysis
# ---------------------------------

skills = ["Python", "SQL", "Machine Learning", "Data", "AI"]

skill_count = {}

for skill in skills:
    count = df["Job Title"].str.contains(skill, case=False).sum()
    skill_count[skill] = count

skill_df = pd.DataFrame(list(skill_count.items()), columns=["Skill", "Frequency"])

print("\nSkill Frequency")
print(skill_df)

# ---------------------------------
# Visualization
# ---------------------------------

plt.figure(figsize=(8,5))

plt.bar(skill_df["Skill"], skill_df["Frequency"])

plt.title("Most Demanded Skills from Job Listings")
plt.xlabel("Skills")
plt.ylabel("Frequency")

plt.xticks(rotation=30)

plt.tight_layout()

# Save graph
plt.savefig("skill_demand.png")

# Show graph on screen
plt.show()

print("\nGraph saved as 'skill_demand.png'")
print("Task 6 Completed Successfully")