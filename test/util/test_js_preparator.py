import unittest

from src.util.js_preparator import JsPreparator


class TestJsPreparator(unittest.TestCase):

    def test_prepare_state(self):
        res = JsPreparator.prepare_state(financial_year='2020', financial_year_plan='2020-2021',state_name='MAHARASHTRA')
        print(res)


if __name__ == '__main__':
    unittest.main()
