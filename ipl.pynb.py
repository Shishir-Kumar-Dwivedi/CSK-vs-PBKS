# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:26:25 2024

@author: darks
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.espncricinfo.com/cricketers/ashutosh-sharma-1131978/matches"
r= requests.get(url)
print(r)
soup = BeautifulSoup(r.text,"lxml")
#table= soup.find(table class="ds-w-full ds-table ds-table-md ds-table-stripped ds-table-no-wrap ds-table-auto ")
#print(table)
pip install selenium
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()  # Or specify the path to your WebDriver executable

# Open a webpage
driver.get("https://www.espncricinfo.com/cricketers/ashutosh-sharma-1131978/matches")
# Find the table element by its XPath (you can use other locators like ID or class)
table = driver.find_element_by_xpath("//table[@class='ds-w-full ds-table ds-table-md ds-table-stripped ds-table-no-wrap ds-table-auto ']")

# Find all table rows within the table
rows = table.find_elements_by_tag_name("tr")

# Loop through each row
for row in rows:
    # Find all table cells within the row
    cells = row.find_elements_by_tag_name("td")
    
    # Extract data from each cell and print it
    for cell in cells:
        print(cell.text)
# Close the browser
#driver.quit()
