from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from models.Product import Product



def worker_for_product_details(lst: list[Product],thread_count=5):
    def l(x):
        x.get_details()
        print(threading.current_thread().name)

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        list(executor.map(l, lst))



def worker_for_page_scraping(fn,pages,products,thread_count=8):
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = [executor.submit(fn, i) for i in range(1, pages + 1)]
        for future in as_completed(futures):
            products += future.result()

    return products
