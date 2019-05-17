import sys
import discord
import requests

from collections import defaultdict
from bs4 import BeautifulSoup

client = discord.Client()

r = requests.get("https://qiita.com/takeharu/items/bb154a4bc198fb102ff3")
soup = BeautifulSoup(r.content, "html.parser")

# デイリーいいねランキングの中身を全量取得
div = soup.find('div', id="item-bb154a4bc198fb102ff3")
title = div.find_all('h1')
links = div.find_all('h4')
print(title[1].text)
print(links[0].text)
print(links[0].text, links[0].find_all('a')[1].attrs['href'])
print(links[1].text)
print(links[2].text)
print(links[3].text)
print(links[4].text)


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('*************')
    print('* bot Start *')
    print('*************')

    # divの中身を上手い事分割して取得と出力くりかえせればいけそう
    data = div.find("span", id="デイリーいいねランキング")

    # チャンネルのオブジェクトを取得
    channel = client.get_channel()

    big = "__**" + title[1].text + "**__"
    # タイトルを出力
    await channel.send(big)

    for i in range(10):
        outputText = links[i].text
        outputUrl = links[i].find_all('a')[1].attrs['href']

        # 内容を出力
        await channel.send(outputText)
        await channel.send(outputUrl)

    sys.exit()

# @client.event
# async def on_message(message):
#     # 「おはよう」で始まるか調べる
#     if message.content.startswith("おはよう"):
#         # 送り主がBotだった場合反応したくないので
#         if client.user != message.author:
#             # メッセージを書きます
#             m = "おはようございます" + message.author.name + "さん！"
#             # メッセージが送られてきたチャンネルへメッセージを送ります
#             # 何故か失敗する
#             # await message.channel.send(message.channel, m)
#             await message.channel.send(m)
#     elif message.content.startswith("こんばんわ"):
#         # await message.channel.send(soup.find("h1",class_="it-Header_title").text)
#
#         await message.channel.send(big)
#         test = "```"
#
#         for i in range(10):
#             # await message.channel.send(links[i].text)
#             # await message.channel.send(links[i].find_all('a')[1].attrs['href'])
#
#             outputText = links[i].text
#             outputUrl = links[i].find_all('a')[1].attrs['href']
#
#             # 内容を出力
#             await message.channel.send(outputText)
#             await message.channel.send(outputUrl)
#         # output += test
#         # await message.channel.send(output)

# bot実行
client.run("")