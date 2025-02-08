from data import trello_token,trello_key
from b_func import async_request_all
import aiohttp

auth = f"key={trello_key}&token={trello_token}"




# Trello async ----------------
async def get_trello_list(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists?{auth}"
    status, _, _, html = await async_request_all(url, "GET", "JSON", proxy=None, auth_info=None)
    print(html)
    return html


async def get_trello_cards(list_id, fields):
    url = f"https://api.trello.com/1/lists/{list_id}/cards?fields={fields}&{auth}"
    status, _, _, html = await async_request_all(url, "GET", "JSON", None, None, None)
    return html


async def create_card_on_list(list_id,name):
    # await rate_limit(trello_limit)
    url = f"https://api.trello.com/1/cards?idList={list_id}&name={name}&keepFromSource=all&{auth}"
    status, _, _, html = await async_request_all(url, "POST", "JSON", None, None, None)
    return html


async def create_attachment_on_card(card_id,name,binary):
    new = aiohttp.FormData()
    new.add_field('file',  binary,filename=name,content_type='application/vnd.ms-excel.sheet.macroEnabled.12')
    url = f"https://api.trello.com/1/cards/{card_id}/attachments?{auth}"
    status, _, _, html = await async_request_all(url, "POST", "FILE", new, None, None)
    return html


async def get_attachments_in_card(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}/attachments?field=url&{auth}"
    status, _, _, html = await async_request_all(url, "GET", "JSON", None, None, None)
    return html

async def move_cart_to_list(card_id,list_id):
    # await rate_limit(trello_limit)
    url = f"https://api.trello.com/1/cards/{card_id}?idList={list_id}&{auth}"
    status, _, _, html = await async_request_all(url, "PUT", "JSON", None, None, None)
    print(status)
    return html

async def comment_to_cart(card_id,message):
    # await rate_limit(trello_limit)
    url = f"https://api.trello.com/1/cards/{card_id}/actions/comments?text={message}&{auth}"
    status, _, _, html = await async_request_all(url, "POST", "JSON", None, None, None)
    return html

async def download_trello_attachments(url):
    headers = {
        'Authorization': f'OAuth oauth_consumer_key="{trello_key}", oauth_token="{trello_token}"'
    }
    print(url)
    status, _, _, html = await async_request_all(url, "GET", "FILE", headers = headers)
    return html

async def get_trello_card_label_async(card_id):
    # await rate_limit(trello_limit)
    url = f"https://api.trello.com/1/cards/{card_id}/labels?{auth}"
    status, _, _, html = await async_request_all(url, "GET", "JSON", proxy=None, auth_info=None)
    return html




