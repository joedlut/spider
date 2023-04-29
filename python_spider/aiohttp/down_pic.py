import aiohttp
import asyncio
import os
from lxml import etree

async def download_picture(url):
    pass

async def get_tree_obj(url,headers):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url,headers=headers) as response:
            page_text = await response.text()
            tree = etree.HTML(page_text)
            return tree

def call_back(task):
    tree = task.result()
    li_list = tree.xpath('/html/body/div[2]/div/div[3]/ul/li')
    for li in li_list:
        tmp_url = li.xpath('./a/@href')[0]
        page_url = "http://pic.netbian.com" + tmp_url
        print(page_url)

    print(len(li_list))
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    urls = ['https://pic.netbian.com/4kdongman/index.html']
    for i in range(2,125):
        url = "https://pic.netbian.com/4kdongman/index_" + str(i) + '.html'
        urls.append(url)
    print(urls)
    pic_dir = 'D://libs'
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)

    tasks = []
    for url in urls:
        c = get_tree_obj(url,headers)
        task = asyncio.ensure_future(c)
        task.add_done_callback(call_back)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))



