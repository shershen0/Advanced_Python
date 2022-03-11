import functools
import os
import timeit
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math
from functools import partial

def integrate_dist(f, n_iter, range_dist=''):
    a = range_dist[0]
    b = range_dist[1]
    acc = 0
    step = (b - a) / n_iter
    start = timeit.default_timer()
    for i in range(n_iter):
        acc += f(a + i * step) * step
    stop = timeit.default_timer()

    print("Integrate from {} to {:.16f}, res = {:.16f} in {}".format(a, b, acc, stop - start))
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=1000, runner):
    step_devision = (b - a) / n_jobs

    if isinstance(runner, ProcessPoolExecutor):
        print("ProcessPoolExecutor")
    elif isinstance(runner, ThreadPoolExecutor):
        print("ThreadPoolExecutor\n")
    intF = partial(integrate_dist, f, n_iter)

    dist = []
    for i in range(n_jobs):
        dist.append((a + step_devision * i, a + step_devision * (i + 1)))
    with runner(max_workers=n_jobs) as executor:
        return sum(executor.map(intF, dist))


def run():
    a = 0
    b = math.pi / 2
    n_iter = 10000

    start = timeit.default_timer()
    casualRes = integrate(math.cos, a, b, n_jobs=1, runner=ThreadPoolExecutor, n_iter=n_iter)
    stop = timeit.default_timer()
    casualTime = stop - start

    threadTxt = []
    for n_jobs in range(1, multiprocessing.cpu_count() * 2 + 1):
        start = timeit.default_timer()
        res = integrate(math.cos, a, b, n_jobs=n_jobs, runner=ThreadPoolExecutor, n_iter=n_iter)
        stop = timeit.default_timer()
        threadTxt.append("Thread with n_jobs={} in {:.17f} res = {}\n".format(n_jobs, stop - start, res))

    processTxt = []
    for n_jobs in range(1, multiprocessing.cpu_count() * 2 + 1):
        start = timeit.default_timer()
        res = integrate(math.cos, a, b, n_jobs=n_jobs, runner=ProcessPoolExecutor, n_iter=n_iter)
        stop = timeit.default_timer()
        processTxt.append("Process with n_jobs={} in {:.17f} res = {}\n".format(n_jobs, stop - start, res))

    if not os.path.exists("artifacts/"):
        os.makedirs("artifacts/")

    with open("artifacts/medium.txt", "w") as f:
        f.write("----------Usual calculation\n")
        f.write("Integrate from {} to {} with n_jobs={} in {:.17f} res = {}\n".format(a, b, 1, casualTime, casualRes))

        f.write("\n\n----------ThreadPoolExecutor Integrate from {} to {}\n".format(a, b))
        for log in threadTxt:
            f.write(log)

        f.write("\n\n----------ProcessPoolExecutor Integrate from {} to {}\n".format(a, b))
        for log in processTxt:
            f.write(log)


if __name__ == '__main__':
    run()
