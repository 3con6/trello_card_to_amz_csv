import b_func
from data import discord_token
import aiohttp
import time

async def upload_discord(binary,name):
    discord_header = {
        'Authorization': discord_token,
    }
    new = aiohttp.FormData()
    new.add_field('file',  binary,filename=f'{name}.jpg',content_type='image/jpeg')
    url = "https://discord.com/api/v9/channels/1029685295593033730/messages"
    status,_,_,res =  await b_func.async_request_all(url, 'POST', 'FILE', new,headers=discord_header)
    while status not in range(200,203) :
        time.sleep(1)
        status,_,_,res =  await b_func.async_request_all(url, 'POST', 'FILE', payload=new, proxy=None, auth_info=None, headers=discord_header)
        
    return res['attachments'][0]['url']