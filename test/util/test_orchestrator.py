import unittest

from src.util.js_executor import JsExecutor
from src.util.orchestrator import Main
from src.util.js_preparator import JsPreparator


class TestOrchestrator(unittest.TestCase):

    def test_csv(self):
        Main.financial_year = '2019'
        Main.financial_year_plan = '2019-2020'
        Main.state_name = 'UTTAR PRADESH'
        district_code = '178'
        block_panch_code = '2205'
        panch_request = "getplanView('2431296','265924',5,4,'VARANASI','SEVAPURI','MANIYARIPUR','3');"
        script = JsPreparator.get_list_of_panchayat_report(Main.financial_year, Main.financial_year_plan,
                                                           Main.state_name, district_code, block_panch_code)
        script += panch_request
        browser = JsExecutor.get_browser_on_page()
        browser.execute_script(script)
        all_rows = JsExecutor.parse_response_for_list_of_panchs_2(browser=browser)
        print(all_rows)


if __name__ == '__main__':
    unittest.main()
