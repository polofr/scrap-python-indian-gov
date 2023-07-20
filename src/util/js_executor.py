import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lxml import etree
from retry import retry


class JsExecutor:

    installer = None

    @staticmethod
    def get_browser_on_page():
        url = 'https://egramswaraj.gov.in/approveActionPlan.do'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--silent')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-gpu')
        if JsExecutor.installer is None:
            JsExecutor.installer = ChromeDriverManager().install()
        browser = webdriver.Chrome(service=ChromeService(JsExecutor.installer), options=chrome_options)
        browser.get(url=url)
        return browser

    @staticmethod
    @retry(tries=2, delay=60)
    def execute(script):
        browser = JsExecutor.get_browser_on_page()
        browser.execute_script(script)
        return browser

    @staticmethod
    def parse_response_for_list_of_districts(browser, financial_year, state_code):
        result = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.ID, 'statewise-report')))
        str_res = result.get_attribute('innerHTML')
        district_block_panch_tuples_simple = re.findall(rf"onclick=\"javascript:getgpreport\('{state_code}',3,'{financial_year}','([0-9]+)','([0-9]+)',0\);\"", str_res)
        district_block_panch_tuples = re.findall(rf"<td class=\"text-center\">([0-9_A-Za-z- ()\[\]./]+)</td>[ \t\n]*<td class=\"text-center\">([0-9_A-Za-z- ()\[\]./]+)</td>[ \t\n]*<td class=\"text-center\"><a href=\"#\" class=\"level-link\" onclick=\"javascript:getgpreport\('{state_code}',3,'{financial_year}','([0-9]+)','([0-9]+)',0\);\"", str_res)
        if len(district_block_panch_tuples_simple) != len(district_block_panch_tuples):
            raise Exception(f'imperfect parsing in parse_response_for_list_of_districts: {len(district_block_panch_tuples_simple)} vs {len(district_block_panch_tuples)}')
        return district_block_panch_tuples

    @staticmethod
    def parse_response_for_list_of_panchs(browser):
        result = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.ID, 'statewise-report')))
        str_res = result.get_attribute('innerHTML')
        panch_tuples = re.findall(rf"<td class=\"text-center\">([0-9_A-Za-z- ()\[\]./]+)</td>[ \t\n]*<td class=\"text-center\">([0-9]+)</td>[ \t\n]*<td class=\"text-center\">[0-9]+\((Main|Supplementary) Plan\)[ \t\n]*</td>[ \t\n]*<td class=\"text-center\"><a href=\"#\" class=\"level-link\" onclick=\"javascript:(getplanView\('([0-9]+)','([0-9]+)',([0-9]+),([0-9]+),'([0-9_A-Za-z- ()\[\]./]+)','([0-9_A-Za-z- ()\[\]./]+)','([0-9_A-Za-z- ()\[\]./]+)','([0-9]+)'\);)\"", str_res)
        return panch_tuples

    @staticmethod
    def parse_response_for_list_of_panchs_2(browser):
        result = WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '//body')))
        str_res = result.get_attribute('innerHTML')
        str_res = str_res.replace('\t', '')
        str_res = str_res.replace('\n', '')
        str_res_bis = re.search(r'SECTION 2 : Sectoral View(.*)SECTION 3 : Scheme View', str_res, flags=re.DOTALL)
        if str_res_bis is None:
            raise Exception(f'Unable to find section 2')
        between_section_str = str_res_bis.group(0)
        str_res_ter = re.search(r'<tbody>.*</tbody>', between_section_str, flags=re.DOTALL)
        if str_res_ter is None:
            raise Exception(f'Unable to find tbody in section 2')
        table_str = str_res_ter.group(0)
        table_str = table_str.replace('<tbody>', '<table>')
        table_str = table_str.replace('</tbody>', '</table>')
        table_str = table_str.replace('\t', '')
        table_str = table_str.replace('\n', '')
        table = etree.HTML(table_str).find('body/table')
        rows = iter(table)
        all_rows = []
        for row in rows:
            values = [col.text for col in row]
            all_rows.append(values[1:])
        if len(all_rows) == 0 or (all_rows[-1][0] is not None and all_rows[-1][0] != 'Total'):
            raise Exception(f'Unable to read table: {len(all_rows)} or {all_rows[-1][0]}')
        all_rows[-1][0] = 'Total'
        return all_rows
