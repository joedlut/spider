import time
from multiprocessing.dummy import Pool
def get_page(str):
    print("正在下载",str)
    time.sleep(2)
    print("下载结束",str)


if __name__ == '__main__':
    name_list = ['a','b','c','d']
    start_time = time.time()
    pool = Pool(4)
    pool.map(get_page, name_list)
    end_time = time.time()
    cost_time = end_time - start_time
    print(cost_time)