import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        empty_string = ""
        self.assertFalse(check_pwd(empty_string))
    def test2(self):
        lowercase = "PASSWORD"
        self.assertFalse(check_pwd(lowercase))
    def test3(self):
        uppercase = "password"
        self.assertFalse(check_pwd(uppercase))
if __name__ == '__main__':
    unittest.main(verbosity=2)
