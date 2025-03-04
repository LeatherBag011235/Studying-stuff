import threading
import multiprocessing
import time

def compute():
    total = 0
    for i in range(10**7):
        total += i

threads = []
start = time.time()
for _ in range(8):
    thread = threading.Thread(target=compute)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Multithreading Time: {time.time() - start:.5f} sec")


if __name__ == "__main__":
    processes = []
    start = time.time()
    for _ in range(8):
        process = multiprocessing.Process(target=compute)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Multiprocessing Time: {time.time() - start:.5f} sec")