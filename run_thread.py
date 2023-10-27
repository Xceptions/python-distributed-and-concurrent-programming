from threading import Thread
import threading

def run_in_a_thread():
    print("Name of the current thread is {}".format(threading.current_thread().name))

if __name__ == "__main__":

    for i in range(2):
        new_thread = Thread(target=run_in_a_thread)
        new_thread.start()

    # run_in_a_thread() # this is usually called main thread