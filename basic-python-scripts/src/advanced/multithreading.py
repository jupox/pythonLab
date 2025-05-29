import threading
import time

def worker(thread_id):
    print(f'Thread {thread_id} starting')
    time.sleep(2)
    print(f'Thread {thread_id} finished')

def main():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()