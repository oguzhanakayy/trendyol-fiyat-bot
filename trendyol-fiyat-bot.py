import requests
from bs4 import BeautifulSoup
from telegram import Bot


async def main():
    url = "TRENDYOL LINK"
    TOKEN = "YOUR TOKEN"
    CHAT_ID = "YOUR CHAT-ID"

    sayfa = requests.get(url)
    html_sayfa = BeautifulSoup(sayfa.content, "html.parser")

    isim = html_sayfa.find("h1", class_="pr-new-br").getText()

    fiyat = html_sayfa.find("span", class_="prc-dsc").getText()

    # TELEGRAM KISMI
    tele_mesaj = isim + "\n" + fiyat 

    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=tele_mesaj)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
