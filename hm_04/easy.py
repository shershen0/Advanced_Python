import random
import os
import timeit
from threading import Thread
from multiprocessing import Process


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def run():
    n = random.randint(100000, 120000)
    cycles = 10

    start = timeit.default_timer()
    for i in range(cycles):
        fibonacci(n)

    stop = timeit.default_timer()
    sync_time = stop - start

    thread = []
    start = timeit.default_timer()
    for i in range(cycles):
        thread.append(Thread(target=fibonacci, args=(n,)))
    for i in range(cycles):
        thread[i].start()
    for i in range(cycles):
        thread[i].join()
    stop = timeit.default_timer()
    thread_time = stop - start

    process = []
    start = timeit.default_timer()
    for i in range(cycles):
        process.append(Process(target=fibonacci, args=(n,)))
    for i in range(cycles):
        process[i].start()
    for i in range(cycles):
        process[i].join()
    stop = timeit.default_timer()
    mprocc_time = stop - start

    if not os.path.exists("artifacts/"):
        os.makedirs("artifacts/")

    f = open("./artifacts/easy.txt", 'w')
    f.write("N equals = " + str(n) + "\n")
    f.write("Cycles count = " + str(cycles) + "\n\n")

    f.write("Synchronous calculation\n")
    f.write("Time --- " + str(sync_time) + "\n\n\n")

    f.write("Threading calculation\n")
    f.write("Time --- " + str(thread_time) + "\n\n\n")

    f.write("Multiprocessing calculation\n")
    f.write("Time --- " + str(mprocc_time) + "\n\n")

    f.write("//--------------------\n\n")
    f.close()


if __name__ == '__main__':
    run()

