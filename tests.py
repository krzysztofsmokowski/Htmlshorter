from shorter import html_paragraphs
import unittest

class ShorterModuleTest(unittest.TestCase):
    def test_html_paragraphs(self):
        soup = 'somethingsomething'
        self.assertEqual(soup, html_paragraphs('https://www.crummy.com/software/BeautifulSoup/bs4/doc/'))

if __name__ == '__main__':
    unittest.main()
