import queue
import time
from threading import Thread

from src.util.csv_writer import CsvWriter
from src.util.js_executor import JsExecutor
from src.util.js_preparator import JsPreparator


class Main:

    financial_year = None
    financial_year_plan = None
    state_name = None

    csv_writer = CsvWriter()

    allowed_to_stop = False
    panch_queue = queue.Queue()
    num_workers = 5
    workers = []

    @staticmethod
    def start_workers():
        for _ in range(Main.num_workers):
            worker = Thread(target=Main.process_queue)
            Main.workers.append(worker)
            worker.start()

    @staticmethod
    def stop_workers():
        Main.allowed_to_stop = True
        for worker in Main.workers:
            worker.join()

    @staticmethod
    def process_queue():
        browser = JsExecutor.get_browser_on_page()
        while True:
            try:
                input = Main.panch_queue.get(block=False)
            except queue.Empty:
                if Main.allowed_to_stop:
                    break
                else:
                    time.sleep(10)
                    continue
            try:
                panchs_tuple = input['tuple']
                panch_request = input['request']
                state_code = input['state-code']
                district_name = input['district-name']
                block_panch_name = input['block-panch-name']
                district_code = input['district-code']
                block_panch_code = input['block-panch-code']

                panch_name = panchs_tuple[0]
                panch_code = panchs_tuple[1]
                plan_id = panchs_tuple[4]
                script = JsPreparator.get_list_of_panchayat_report(Main.financial_year, Main.financial_year_plan, Main.state_name, district_code, block_panch_code)
                script += panch_request
                try:
                    browser.execute_script(script)
                except:
                    time.sleep(1)
                    browser = JsExecutor.get_browser_on_page()
                    browser.execute_script(script)
                all_rows = JsExecutor.parse_response_for_list_of_panchs_2(browser=browser)
                for row in all_rows:
                    Main.csv_writer.line_queue.put(f'{Main.financial_year}, {Main.state_name}, {state_code}, {district_name}, {district_code}, {block_panch_name}, {block_panch_code}, {panch_name}, {panch_code}, {plan_id}, {", ".join(row)}')
                    # print(f'{Main.financial_year}, {Main.state_name}, {state_code}, {district_name}, {district_code}, {block_panch_name}, {block_panch_code}, {panch_name}, {panch_code}, {plan_id} {", ".join(row)}')
            except Exception as ex:
                print(f'Orchestrator failed for {input}: {str(ex)}')

    @staticmethod
    def run(villages=None):
        print(f'Starting State {Main.state_name} for {Main.financial_year_plan}')
        Main.csv_writer.start_worker(f'results_{Main.state_name}_{Main.financial_year}.csv')
        Main.start_workers()

        try:
            script = JsPreparator.prepare_state(Main.financial_year, Main.financial_year_plan, Main.state_name)
            script += JsPreparator.get_list_of_districts(Main.financial_year, Main.state_name)
            browser = JsExecutor.execute(script)
            state_code = JsPreparator.get_state_code(Main.state_name)
            district_block_panch_tuples = JsExecutor.parse_response_for_list_of_districts(browser, Main.financial_year, state_code)
        except Exception as ex:
            raise Exception(f'Failed to get list of districts for {Main.state_name} {Main.financial_year}: {str(ex)}')

        for idx, district_block_panch_tuple in enumerate(district_block_panch_tuples):
            try:
                district_name = district_block_panch_tuple[0]
                block_panch_name = district_block_panch_tuple[1]
                district_code = district_block_panch_tuple[2]
                block_panch_code = district_block_panch_tuple[3]
                print(f'Starting {idx} {block_panch_name} in district {district_name} in state {Main.state_name} for {Main.financial_year_plan}')
                script = JsPreparator.prepare_state(Main.financial_year, Main.financial_year_plan, Main.state_name)
                script += JsPreparator.get_list_of_panchayats(Main.financial_year, Main.state_name, district_code, block_panch_code)
                browser = JsExecutor.execute(script)
                panchs_tuples = JsExecutor.parse_response_for_list_of_panchs(browser=browser)
                for panchs_tuple in panchs_tuples:
                    panch_name = panchs_tuple[0]
                    panch_code = panchs_tuple[1]
                    plan_id = panchs_tuple[4]
                    unique_id = f'{panch_name.strip()}-{panch_code.strip()}-{plan_id.strip()}'
                    if villages is not None and villages.get(unique_id):
                        continue
                    print(f'Adding {unique_id} to the queue')
                    panch_request = panchs_tuple[3]
                    Main.panch_queue.put({
                        'tuple': panchs_tuple,
                        'request': panch_request,
                        'state-code': state_code,
                        'district-name': district_name,
                        'block-panch-name': block_panch_name,
                        'district-code': district_code,
                        'block-panch-code': block_panch_code
                    })
            except Exception as ex:
                print(f'Failed to analyze {idx} {district_block_panch_tuple[0]} {district_block_panch_tuple[1]} : {str(ex)}')

        Main.stop_workers()
        Main.csv_writer.stop_worker()
