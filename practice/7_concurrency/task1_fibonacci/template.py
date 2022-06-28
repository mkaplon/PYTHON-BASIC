import os
from random import randint
import concurrent.futures
import threading
import time


OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def write_to_file(n: int):
    with open(OUTPUT_DIR + "/" + str(n) + ".txt", "w") as file:
        file.write(str(fib(n)))


def func1(array: list):
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as ex:
        ex.map(write_to_file, array)


def return_value_from_file(filename):
    with open(OUTPUT_DIR+"/"+filename) as file:
        return filename[:-4]+", "+file.read()+"\n"


def func2(result_file: str):
    all_files = os.listdir("output")
    with concurrent.futures.ThreadPoolExecutor(max_workers=14) as ex:
        output = ex.map(return_value_from_file, all_files)
    with open(result_file, "w") as result:
        for obs in output:
            result.writelines(obs)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    lock = threading.Lock()
    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
