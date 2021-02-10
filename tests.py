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
    def test4(self):
        digits = "password1"
        self.assertTrue(check_pwd(digits))
    def test5(self):
        symbols = "password!"
        self.assertTrue(check_pwd(symbols))
if __name__ == '__main__':
    unittest.main(verbosity=2)
