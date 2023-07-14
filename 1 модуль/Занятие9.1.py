# посмотри библиотеку Scrapy
import requests
import bs4
import random

def get_interesting_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content   # из всего response мне нужен только response.content ==> response = response.content
    html = bs4.BeautifulSoup(response, 'lxml')   # получает информацию о том, что мы получили с сайта и на что его разложить
    fact = random.choice(html.find_all(class_ = 'p-2 clearfix'))   # найти все в html с class_ = p-2 clearfix, выбрать один случайный результат
    print(fact.text)
    print(fact.a.attrs['href'])

def get_event():
    response = requests.get('https://kudago.com/msk/festival/')
    response = response.content
    html = bs4.BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='post-title'))
    print(fest.text)
    print(fest.a.attrs['href'])

def get_concert():
    response = requests.get('https://kudago.com/msk/concerts')
    response = response.content
    html = bs4.BeautifulSoup(response, 'lxml')
    concert = random.choice(html.find_all(class_='post-title'))
    print(concert.text)
    print(concert.a.attrs['href'])


def get_bash():
    response =requests.get('http://bashorg.org/casual')
    response = response.content
    html = bs4.BeautifulSoup(response, 'html.parser')
    quote_base = html.find(class_ = 'q')
    vote = quote_base.find(class_ = 'vote')
    quote = vote.find_next_sibling()   # найти следующий блок за блоком vote

    print(vote.get_text())
    print(quote.get_text(separator='\n'))
get_concert()
get_event()
get_interesting_fact()