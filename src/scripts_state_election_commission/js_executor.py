import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lxml import etree

from src.util.csv_writer import CsvWriter


class JsExecutor:

    installer = None

    @staticmethod
    def get_browser_on_page():
        url = 'http://sec.up.nic.in/ElecLive/WinnerList.aspx'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--silent')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-gpu')
        if JsExecutor.installer is None:
            JsExecutor.installer = ChromeDriverManager().install()
        browser = webdriver.Chrome(JsExecutor.installer, chrome_options=chrome_options)
        browser.get(url=url)
        return browser

    @staticmethod
    def submit_form(browser):
        values = ['50', '53', '11', '54', '19', '24', '66', '29', '45', '21', '30', '28', '64', '32', '31', '22', '41',
                  '6', '69', '58', '62', '7', '70', '39', '33', '72', '35', '65', '43', '42', '16', '40', '27', '25',
                  '18', '15', '8', '57', '68', '59', '55', '5', '38', '51', '10', '73', '67', '2', '23', '26', '4',
                  '12', '63', '36', '74', '13', '44', '47', '49', '34', '71', '56', '3', '17', '61', '14', '52', '1',
                  '60', '48', '75', '37', '46', '20', '9']
        value_for_select_2 = '5'
        select_2 = WebDriverWait(browser, 60).until(
            ec.presence_of_element_located((By.XPATH, "//select[@name='ctl00$ContentPlaceHolder1$ddlpost']")))
        Select(select_2).select_by_value(value_for_select_2)
        for value in values:
            select_1 = WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, "//select[@name='ctl00$ContentPlaceHolder1$ddlDistrict']")))
            Select(select_1).select_by_value(value)
            time.sleep(10)
            table = WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, "//table[@id='ContentPlaceHolder1_winnerdetail']")))
            table_str = table.get_attribute('innerHTML')
            table_str = table_str.replace('<tbody>', '<table>')
            table_str = table_str.replace('</tbody>', '</table>')
            table_str = table_str.replace('\t', '')
            table_str = table_str.replace('\n', '')
            table = etree.HTML(table_str).find('body/table')
            rows = iter(table)
            all_rows = []
            for row in rows:
                row_values = [col.text for col in row]
                all_rows.append(row_values)
            new_file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_state_election_commission/results/{value}.csv'
            CsvWriter.write(new_file_path, all_rows)
            print(f'finish for {value}')
