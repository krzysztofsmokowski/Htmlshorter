from bs4 import BeautifulSoup
import requests

def html_paragraphs(url):
    requested_page = requests.get('{}'.format(url))
    soup = BeautifulSoup(requested_page.text, 'html.parser')
    for paragraph_element in soup.find_all('p'):
        print(paragraph_element.text)

def main():
    html_paragraphs('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')


if __name__ == '__main__':
    main()
