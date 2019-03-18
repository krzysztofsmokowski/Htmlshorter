from bs4 import BeautifulSoup
import requests

def html_paragraphs(url):
    requested_page = requests.get('{}'.format(url))
    soup = BeautifulSoup(requested_page.text, 'html.parser')
    paragraphs = ''
    for paragraph_element in soup.find_all('p'):
        paragraphs += paragraph_element.text
    return paragraphs

