# from multiprocessing import Process
# import time

# num_processes = 1
# processes = []

# number = 10000

# def calculate_factorial(number):
#     factorial = 1

#     for n in range(1, number + 1):
#         factorial *= n

# if __name__ == "__main__":
#     start = time.time()
#     for i in range(num_processes):
#         process_name = f"Process { i }"
#         p = Process(target=calculate_factorial, args=(number,), name=process_name)
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()
#     end = time.time()
#     print(f"With { num_processes } Processes, we took { end - start } seconds to calculate factorial of { number }")

import os
from multiprocessing import Process

print("Number of cpu : ", os.cpu_count())

def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()