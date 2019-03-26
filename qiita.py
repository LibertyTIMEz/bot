import discord
import requests
from collections import defaultdict
from bs4 import BeautifulSoup

client = discord.Client()

r = requests.get("https://qiita.com/takeharu/items/bb154a4bc198fb102ff3")

soup = BeautifulSoup(r.content, "html.parser")

# デイリーいいねランキングの中身を全量取得
div = soup.find("div",id="item-bb154a4bc198fb102ff3")

# divの中身を上手い事分割して取得と出力くりかえせればいけそう


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            #何故か失敗する
            #await message.channel.send(message.channel, m)
            await message.channel.send(m)
    elif message.content.startswith("こんばんわ"):
        await message.channel.send(soup.find("h1",class_="it-Header_title").text)

client.run("NTYwMDgzNDk4ODAzNjU4NzUz.D3ux-Q.3adPcSPykHSbbf8quXlLXFvXQlE")