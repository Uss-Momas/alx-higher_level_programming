#!/usr/bin/python3
"""test_base Module"""


import unitttest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test class to test the Base class"""
    def setUp(self):
        pass
    
    def test_id(self):
        """test the id attribute"""
        base = Base()
        self.assertEqual(base.id, None)

if __name__ == '__main__':
    unittest.main()
