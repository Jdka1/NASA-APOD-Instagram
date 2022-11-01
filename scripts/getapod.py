import requests
from bs4 import BeautifulSoup
import sys
sys.path.append('/Users/arymehr/Documents/CS Projects/NASA-APOD/')

def get_apod():
    html = requests.get('https://apod.nasa.gov/apod/').content
    soup = BeautifulSoup(html, 'html.parser')

    apod_src = soup.find('img')['src']
    img_url = f'https://apod.nasa.gov/apod/{apod_src}'
    img_data = requests.get(img_url).content

    with open('results/apod.jpg', 'wb') as handler: 
        handler.write(img_data)
    
    info = soup.find_all('center')[1]
    title = info.find('b').text.strip(' ')
    credit = 'Image Credit:' +info.text.split('Image Credit:')[1].replace('\n', '')
    
    with open('results/caption.txt', 'w') as f:
        f.write(title + '\n' + credit)

