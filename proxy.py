import urllib.request, socket
import asyncio
from proxybroker import Broker
import queue

working_proxies = queue.Queue(maxsize=1_000)

socket.setdefaulttimeout(5)


def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({"http": pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        urllib.request.install_opener(opener)
        urllib.request.urlopen(
            "http://login.aliexpress.com"
        )  # change the url address here
    except Exception:
        return 1
    return 0


async def filter_and_save(proxies):
    while True:
        proxy_wrapper = await proxies.get()
        if proxy_wrapper is None:
            break
        else:
            proxy = str(proxy_wrapper.host) + ":" + str(proxy_wrapper.port)
            if not is_bad_proxy(proxy):
                working_proxies.put(proxy)
                size = working_proxies.qsize()
                print(f"added proxy: {proxy}, for now {size}")


def fill_proxies_queue(limit):
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    judge = ["http://httpbin.org/get", "http://login.aliexpress.com"]
    tasks = asyncio.gather(
        broker.find(
            types=["HTTP", "HTTPS"], limit=limit, countries=["US"], judges=judge
        ),
        filter_and_save(proxies),
    )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)


def get_proxy():
    proxy = working_proxies.get()
    return proxy
