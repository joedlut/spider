import asyncio
import time
impo

async def download_job(url):
    print(url + ' 正在下载')
    #time.sleep(2)
    await asyncio.sleep(2)
    print(url + '下载完毕')

if __name__ == '__main__':
    start = time.time()
    stasks = []
    urls = [
        'www.baidu.com',
        'www.sougou.com',
        'www.douban.com'
    ]
    for url in urls:
        c = download_job(url)
        task = asyncio.ensure_future(c)
        stasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(stasks))
    print(time.time()-start)