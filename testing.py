import unittest
from functions import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for get_formatted_name function"""

    def test_first_last_name(self):
        """Test for Janis Joplin"""

        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Test for Wolfgang Amadeus Mozart"""

        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
