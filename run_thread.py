import urllib3
from threading import Thread
import threading

urllib3.disable_warnings()

class TestThread(Thread):
    def __init__(self, file_name, url):
        Thread.__init__(self, name=file_name)
        self.file_name = file_name
        self.url = url

    # the run method will automatically be run in a new thread everytime
    def run(self):
        time.sleep(1)

        curr_thread = threading.currentThread()
        print(f"State of thread { curr_thread.name } in run: { repr(curr_thread) }. Is the Thread alive? { curr_thread.isAlive() }")

        print(f"Downloading the contents of { self.url } into { self.file_name } from { threading.currentThread().name }")
        http = urllib3.PoolManager()

        response = http.request(method="GET", url=self.url)
        with open(self.file_name, "wb") as f:
            f.write(response.data)

        print(f"Download of { self.url } done")


if __name__ == "__main__":
    test_dict = {
        "Google": "http://www.google.com",
        # "Python": "http://www.python.org",
        "Bing": "http://www.bing.com",
        # "Yahoo": "http://www.yahoo.com"
    }
    for key in test_dict:
        test = TestThread(key, test_dict[key])
        test.start()



"""
Doing it the function way


def run_in_a_thread():
    print("Name of the current thread is {}".format(threading.current_thread().name))

if __name__ == "__main__":

    for i in range(2):
        new_thread = Thread(target=run_in_a_thread)
        new_thread.start()


"""