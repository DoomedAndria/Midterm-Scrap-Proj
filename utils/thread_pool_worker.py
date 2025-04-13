from concurrent.futures import ThreadPoolExecutor
import threading
from models.Product import Product



def worker_for_product_details(lst: list[Product],thread_count=5):
    def l(x):
        x.get_details()
        print(threading.current_thread().name)

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        list(executor.map(l, lst))
