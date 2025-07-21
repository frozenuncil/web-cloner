import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin







url = 'your-url'
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')

with open('cloned_page.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

os.makedirs('assets', exist_ok=True)

for link in soup.find_all('link', href=True):
    href = link['href']
    if 'css' in href:
        file_url = urljoin(url, href)
        filename = href.split('/')[-1]
        css_data = requests.get(file_url).text
        with open(f'assets/{filename}', 'w', encoding='utf-8') as f:
            f.write(css_data)

# Dont use this to scam people!
# I assume no liability for things that are done with it!
