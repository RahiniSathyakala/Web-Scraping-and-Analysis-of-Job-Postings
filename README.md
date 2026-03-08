# Web Scraping and Job Market Analysis

## Project Overview
This project focuses on collecting job listing data from a website using web scraping techniques and analyzing the demand for different technical skills in the job market. Web scraping allows us to automatically extract useful information from webpages, which can then be analyzed using data science tools.

The objective of this project is to gather job listing information such as job titles, company names, and locations, and then analyze the most frequently requested skills in job postings.

---

## Objectives
- Extract job listings from a webpage using web scraping
- Collect job title, company name, and location information
- Store the scraped data in a structured dataset
- Perform basic data analysis on job titles
- Identify the most demanded technical skills
- Visualize skill demand using charts

---

## Dataset
The data for this project was collected directly from a webpage containing sample job listings.

Each job listing includes the following information:
- Job Title
- Company Name
- Location

After scraping the webpage, the extracted data was organized into a structured dataset using a Pandas DataFrame.

---

## Tools and Technologies
The following technologies were used in this project:

- Python
- Requests (for sending HTTP requests)
- BeautifulSoup (for parsing HTML)
- Pandas (for data manipulation)
- Matplotlib (for visualization)

---

## Project Workflow

### 1. Sending Request to the Webpage
The webpage containing job listings was accessed using the Python **requests** library.

Example:

import requests

response = requests.get("website_url")

This retrieves the HTML content of the webpage.

---

### 2. Parsing the HTML
The HTML content of the webpage was parsed using **BeautifulSoup** to extract useful elements.

BeautifulSoup helps navigate the structure of HTML documents and find specific tags that contain job information.

---

### 3. Extracting Job Information
The following information was extracted from each job listing:

- Job Title
- Company Name
- Job Location

These values were collected and stored in lists before converting them into a dataset.

---

### 4. Creating a Structured Dataset
The scraped information was converted into a Pandas DataFrame for easier analysis.

Example structure of the dataset:

| Job Title | Company | Location |
|----------|---------|----------|
| Senior Python Developer | Payne, Roberts and Davis | Stewartbury, AA |
| Energy Engineer | Vasquez-Davidson | Christopherville, AA |

The dataset was also saved as a CSV file for future use.

---

### 5. Skill Analysis
To analyze job market demand, job titles were scanned for commonly required skills such as:

- Python
- SQL
- Machine Learning
- Data
- Artificial Intelligence (AI)

The frequency of each skill was counted to determine how often it appears in job listings.

---

### 6. Data Visualization
A bar chart was created to visualize the demand for different skills.

The visualization helps quickly identify which skills are most frequently mentioned in job postings.

Example visualization:

- Python appears most frequently
- Data-related roles appear regularly
- AI and machine learning roles are emerging

---

## Key Insights
The analysis revealed several insights about job market trends:

- Python is one of the most frequently requested skills in job postings.
- Data-related roles are common across multiple companies.
- Artificial intelligence and machine learning skills are growing in demand.
- Technical roles are distributed across different industries and companies.

---

## Challenges Faced
Some challenges encountered during this project included:

- Understanding the structure of the webpage HTML
- Extracting the correct tags for job information
- Handling text formatting and cleaning extracted data

These challenges were resolved by carefully inspecting the HTML structure and refining the scraping logic.

---

## Conclusion
This project demonstrates how web scraping can be used to collect real-world job market data and analyze industry trends. By combining web scraping with data analysis tools, valuable insights can be extracted from publicly available information.

Such analysis can help students and professionals understand which technical skills are currently in high demand in the job market.

---

## Skills Demonstrated
- Web Scraping
- HTML Parsing
- Data Extraction
- Data Cleaning
- Data Analysis
- Data Visualization
- Python Programming

---

## Output
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/7dc0296c-7ee1-4001-a775-210ffbb054ee" />
<img width="957" height="1020" alt="Image" src="https://github.com/user-attachments/assets/ba6434c7-d340-452b-b440-ada26618c142" />

---
