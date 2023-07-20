from src.util.js_executor import JsExecutor
from src.util.orchestrator import Main
from src.util.js_preparator import JsPreparator


def test_problematic_list():
    Main.financial_year = '2019'
    Main.financial_year_plan = '2019-2020'
    Main.state_name = 'CHHATTISGARH'
    district_code = '272737'
    block_panch_code = '4067'
    script = JsPreparator.prepare_state(Main.financial_year, Main.financial_year_plan, Main.state_name)
    script += JsPreparator.get_list_of_panchayats(Main.financial_year, Main.state_name, district_code,
                                                  block_panch_code)
    browser = JsExecutor.get_browser()
    browser = JsExecutor.execute(browser, script)
    panchs_tuples = JsExecutor.parse_response_for_list_of_panchs(browser=browser)
    print(panchs_tuples)

def test_empty_village():
    panch_request = "getplanView('2220408','28420',5,4,'BHIWANI','DADRI-I','SANKROAD','3');"
    Main.financial_year = '2018'
    Main.financial_year_plan = '2018-2019'
    Main.state_name = 'HARYANA'
    district_code = '59'
    block_panch_code = '1040'
    script = JsPreparator.get_list_of_panchayat_report(Main.financial_year, Main.financial_year_plan,
                                                       Main.state_name, district_code, block_panch_code)
    script += panch_request
    browser = JsExecutor.get_browser()
    browser = JsExecutor.execute(browser, script)
    all_rows = JsExecutor.parse_response_for_list_of_panchs_2(browser=browser)
    for row in all_rows:
        print(row)

def test_csv():
    Main.financial_year = '2019'
    Main.financial_year_plan = '2019-2020'
    Main.state_name = 'UTTAR PRADESH'
    district_code = '178'
    block_panch_code = '2205'
    panch_request = "getplanView('2431296','265924',5,4,'VARANASI','SEVAPURI','MANIYARIPUR','3');"
    script = JsPreparator.get_list_of_panchayat_report(Main.financial_year, Main.financial_year_plan,
                                                       Main.state_name, district_code, block_panch_code)
    script += panch_request
    browser = JsExecutor.get_browser()
    JsExecutor.execute(browser, script)
    all_rows = JsExecutor.parse_response_for_list_of_panchs_2(browser=browser)
    print(all_rows)

