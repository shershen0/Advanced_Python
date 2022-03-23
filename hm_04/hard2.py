import os
import time
from multiprocessing import Process, Pipe
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime


def A(f, s):
    while True:
        time.sleep(5)
        e = f.recv()
        s.send(e)
        e.lower()


def B(f, s):
    while True:
        s.send(f.recv())


def run():
    rootA, Aroot = Pipe()
    AB, BA = Pipe()
    Broot, rootB = Pipe()

    proc1 = Process(target=A, args=(Aroot, AB), daemon=True).start()
    proc2 = Process(target=B, args=(BA, rootB), daemon=True).start()

    if not os.path.exists("artifacts/"):
        os.makedirs("artifacts/")

    with open("artifacts/hard.txt", "a") as f:
        f.write("\n\n-----Pipe\n")
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            text = input(">")
            f.write(str(current_time) + "  " + text + "\n")
            rootA.send(text)
            text2 = Broot.recv()
            print(text2)
            f.write(str(current_time) + "  " + text2 + "\n")



if __name__ == '__main__':
    run()
