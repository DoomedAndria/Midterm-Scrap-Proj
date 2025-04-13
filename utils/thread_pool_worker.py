from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from models.Product import Product


from concurrent.futures import ThreadPoolExecutor, as_completed

def worker_for_product_details(lst: list[Product], thread_count=20):
    total = len(lst)
    completed = 0

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = [executor.submit(x.get_details) for x in lst]

        for future in as_completed(futures):
            completed += 1
            print(f'\rGetting details for results ... Progress: {completed}/{total} ({completed/total*100:.2f}%)', end='')



def worker_for_page_scraping(fn, pages, products, thread_count=8):
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = [executor.submit(fn, i) for i in range(1, pages + 1)]
        for future in as_completed(futures):
            products += future.result()

    return products
