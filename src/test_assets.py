import unittest
import assets


class TestAssets(unittest.TestCase):

    def test_get_the_tray_icon(self):
        self.assertTrue(assets.get_tray_icon())


if __name__ == '__main__':
    unittest.main()
