from shorter import html_paragraphs
import unittest
from mock import MagicMock

class ShorterModuleTest(unittest.TestCase):
    def test_html_paragraphs(self):
        html_paragraphs = MagicMock(return_value=["paragraph1 paragraph2"])
        self.assertEqual("paragraph1 paragraph2", html_paragraphs)

if __name__ == '__main__':
    unittest.main()
