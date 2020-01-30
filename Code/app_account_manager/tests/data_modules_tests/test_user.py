import unittest
import main_page.data_modules.user as test_user


# TODO: add unit tests, be careful with web info (parameter time is always changes)


class TestUser(unittest.TestCase):

    def test_profile(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
