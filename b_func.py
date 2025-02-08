
import time
import asyncio
import aiohttp


# Limit
class rate_limit_conf:
    def __init__(self, number, second):
        self.updated_at = time.monotonic()
        self.NUMBER = number
        self.SECOND = second
        self.TOKEN = 0


async def rate_limit(g):
    def add_token():
        if time.monotonic() - g.updated_at > (g.SECOND / g.NUMBER):
            g.TOKEN = 1

    while g.TOKEN < 1:
        add_token()
        await asyncio.sleep(0.01)
    g.updated_at = time.monotonic()
    g.TOKEN = 0

trello_limit = rate_limit_conf(8, 1)
discord_limit = rate_limit_conf(1, 2)

async def async_request_all(url, method, type, payload=None, proxy=None, auth_info=None, headers=None):
    if 'trello' in str(url):
        await rate_limit(trello_limit)
    elif 'discord' in str(url):
        await rate_limit(discord_limit)    
    auth = aiohttp.BasicAuth(
        auth_info['login'], auth_info['password']) if auth_info != None else None
    http_proxy = "http://" + proxy if proxy != None else None
    if headers == None:
        headers = {}
    timeout = aiohttp.ClientTimeout(total=60)

    try:
        async with aiohttp.ClientSession(timeout=timeout, auth=auth) as session:
            await rate_limit(trello_limit)
            if method == "GET":
                async with session.get(url, headers=headers) as response:
                    if type == "JSON":
                        html = await response.json()
                    elif type == "FILE":
                        html = await response.read()
                    else:
                        html = await response.text()
                    return response.status, response.headers, response.request_info, html

            elif method == "POST":
                if type == "JSON":
                    async with session.post(url, headers=headers, json=payload) as response:
                        html = await response.json()
                        return response.status, response.headers, response.request_info, html
                elif type == "FILE":
                    async with session.post(url, headers=headers, data=payload) as response:
                        html = await response.json()
                        return response.status, response.headers, response.request_info, html
                else:
                    async with session.post(url, headers=headers, data=payload) as response:
                        html = await response.text()
                        return response.status, response.headers, response.request_info, html

            elif method == "PUT":
                async with session.put(url, headers=headers, json=payload) as response:
                    if type == "JSON":
                        html = await response.json()
                    else:
                        html = await response.text()
                    return response.status, response.headers, response.request_info, html

            elif method == "DELETE":
                async with session.delete(url, headers=headers) as response:
                    if type == "JSON":
                        html = await response.json()
                    else:
                        html = await response.text()
                    return response.status, response.headers, response.request_info, html

    # except aiohttp.ClientResponseError as ex:
    #     status = ex.status
    #     return status, '', '', ''
    # except aiohttp.ClientConnectionError:
    #     status = 'ErrConn'
    #     return status, '', '', ''
    except Exception as e:
        return e, '', '', ''