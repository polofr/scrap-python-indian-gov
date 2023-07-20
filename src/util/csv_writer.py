import csv
import queue
import time
from threading import Thread


# TODO this could be better
# https://stackoverflow.com/questions/11983938/python-appending-to-same-file-from-multiple-threads
# use logging module whcih is thread safe instead of print
# try ThreadPoolExecutor ?
# threading.Lock() instead of queue??
class CsvWriter:

    allowed_to_stop = False
    line_queue = queue.Queue()
    worker = None

    def start_worker(self, file_path):
        self.worker = Thread(target=self.process_queue, args=[file_path])
        self.worker.start()

    def stop_worker(self):
        self.allowed_to_stop = True
        self.worker.join()

    def process_queue(self, file_path):
        with open(file_path, "a", newline="") as csv_file:
            while True:
                try:
                    next_line = self.line_queue.get(block=False)
                except queue.Empty:
                    if self.allowed_to_stop:
                        break
                    else:
                        time.sleep(10)
                        continue
                try:
                    csv_file.write(f"{next_line}\n")
                except Exception as ex:
                    print(f"Writer failed for {next_line}: {str(ex)}")

    @staticmethod
    def write(file_path, lines):
        with open(file_path, "w", newline="", encoding="utf8") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            for line_array in lines:
                writer.writerow(line_array)
