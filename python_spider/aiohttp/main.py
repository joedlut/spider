import asyncio
import time 

async def request(url):
    print(url + ' begin')
    print(url + ' end')
    return url
def call_back(task):
    print(task.result())

if __name__ == '__main__':
    c = request('www.baidu.com')
    # 被废弃
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(c)

    loop = asyncio.get_event_loop()
    task = loop.create_task(c)
    task.add_done_callback(call_back)
    #print(task)
    loop.run_until_complete(task)
    #print(task)

    #loop = asyncio.get_event_loop()
    #task = asyncio.ensure_future(c)
    #loop.run_until_complete(task)





