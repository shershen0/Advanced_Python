import os
import time
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime

def A(f , s):
    while True:
        while not f.empty():
            time.sleep(5)
            e = f.get()
            s.put(e)
            e.lower()



def B(f, s):
    while True:
       s.put(f.get())


def run():
    rootA = Queue()
    AB = Queue()
    Broot = Queue()
    proc1 = Process(target=A, args=(rootA, AB), daemon=True).start()
    proc2 = Process(target=B, args=(AB, Broot), daemon=True).start()

    if not os.path.exists("artifacts/"):
        os.makedirs("artifacts/")

    with open("artifacts/hard.txt", "a") as f:
        f.write("-----Queue\n")
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            text = input(">")
            f.write(str(current_time) + "  " + text + "\n")
            rootA.put(text)
            text2 = Broot.get()
            print(text2)
            f.write(str(current_time) + "  " + text2 + "\n")

    proc1.join()
    proc2.join()



if __name__ == '__main__':
    run()