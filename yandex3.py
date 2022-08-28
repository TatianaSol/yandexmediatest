# Написать чат-бота, который будет публиковать последнюю новость с vc.ru
import telebot
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# you can find bot at http://t.me/solo2143bot
token = open('token.txt').read()
bot = telebot.TeleBot(token)

ua = UserAgent()
news = {
    'link': '',
    'text': ''
}


def get_news_page(url) -> None:
    response = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    news_block = BeautifulSoup(response.text, 'lxml').find('div', class_='news_item')
    news['link'] = news_block.find('a', class_='news_item__title').get('href').strip()
    news['text'] = news_block.find('a', class_='news_item__title').text.strip()


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text != "":
        bot.send_message(message.chat.id, f"Последняя новость на vc.ru:\n{news['text']}\n{news['link']}")


if __name__ == '__main__':
    get_news_page(url='https://vc.ru/')
    bot.polling(none_stop=True)
