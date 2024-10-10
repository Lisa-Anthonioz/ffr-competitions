from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json
import time

url = 'https://competitions.ffr.fr/clubs/aix-universite-rugby/competitions/provence-alpes-cote-dazur-regionale-1-championnat-territorial/calendrier.html'

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(0.5)
html = driver.page_source
driver.quit()

page = BeautifulSoup(html, 'html.parser')
table = page.find_all('div', attrs={'class': 'general-container-wrapper'})

matches = []

for row in table:
    match = {}
    match['team'] = row.find('span', attrs={'class': 'nom-club'}).text
    matches.append(match)

json_filename = 'docs/result.json'
if os.path.exists(json_filename):
  os.remove(json_filename)

with open(json_filename, 'a') as json_file:
  json.dump(matches, json_file)