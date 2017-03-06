import unittest
from usage_meters.utils import InsensitiveDict


class TestInsensitiveDict(unittest.TestCase):

    def test_all_lower(self):
        class Fake(object):
            prop1 = 'test'

        test_dict = InsensitiveDict(Fake())
        self.assertEquals(test_dict.get('prop1'), 'test')

    def test_all_upper(self):
        class Fake(object):
            PROP1 = 'TEST'
        test_dict = InsensitiveDict(Fake())
        self.assertEquals(test_dict.get('prop1'), 'TEST')


    def test_mixed(self):
        class Fake(object):
            PrOp1 = 'TeSt'
        test_dict = InsensitiveDict(Fake())
        self.assertEquals(test_dict.get('prop1'), 'TeSt')
        
        
