from shorter import html_paragraphs
import unittest
from mock import MagicMock

class ShorterModuleTest(unittest.TestCase):
    def test_html_paragraphs(self):
        soup = MagicMock(return_value=[
            "paragraph1"
            "paragraph2"
            ])
        function_test = html_paragraphs('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
        self.assertEqual(soup, function_test)

if __name__ == '__main__':
    unittest.main()
