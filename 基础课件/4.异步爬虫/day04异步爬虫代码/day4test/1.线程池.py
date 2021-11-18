import requests
from multiprocessing.dummy import Pool
import time

urls = {
    'http://127.0.0.1:5000/kaba',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom',
}


def get_requests(url):
    page_text = requests.get(url).text
    return len(page_text)


if __name__ == "__main__":
    pool = Pool(3)
    start = time.time()
    result_list = pool.map(get_requests, urls)
    print(result_list)
    print('total', time.time() - start)
