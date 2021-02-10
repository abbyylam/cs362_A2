import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        empty_string = ""
        self.assertFalse(check_pwd(empty_string))

if __name__ == '__main__':
    unittest.main(verbosity=2)
