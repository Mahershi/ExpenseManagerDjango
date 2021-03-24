import threading
import time


class TestThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(1, 10):
            print(i)
            time.sleep(2)