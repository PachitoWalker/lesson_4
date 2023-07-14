import bs4
import random
import requests

def get_interesting_fact():
    response = requests.get('https://i-fakt.ru/')   # с помощью requests.get я могу получать информацию с какого-либо внешнего источника (например сайта, адрес который я положил в '')
    response = response.content   # из всего response (смотри в отладчики в Locals) мне нужно получить только content
    html = bs4.BeautifulSoup(response, 'lxml')   # BeautifulSoup получает на вход нашш запрос и информацию от том, из чего он состоит, мы говорим ему что это будет lxml
    fact = random.choice(html.find_all(class_='p-2 clearfix'))   # я говорю html: найди внутри себя все, в чем class = "p-2 clearfix", и выбери случайный (random.choice)
    return(fact.text)   # напечатать случайный факт(я выбрал его прошлой строкой), только его текст
    print(fact.a.attrs['href'])   # напечатать ссылку на тот факт


def get_event():   # тоже самое, что и прошлая функция
    response = requests.get('https://kudago.com/msk/festival/') 
    response = response.content 
    html =bs4.BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='post-title'))
    print(fest.text)
    print(fest.a.attrs['href'])


def get_concert(): # тоже самое, что и прошлые 2 функции
    response = requests.get('https://kudago.com/msk/concerts/')
    response = response.content
    html = bs4.BeautifulSoup(response, 'lxml')
    concert = random.choice(html.find_all(class_='post-title'))
    print(concert.text)
    print(concert.a.attrs['href'])
user_wish = ''

def get_bash():
    response = requests.get('http://bashorg.org/casual')
    response = response.content
    html = bs4.BeautifulSoup(response, 'html.parser')
    quote_base = html.find(class_='q')   # html, найди внутри себя блок с class = 'q'
    vote = quote_base.find(class_='vote')   # quote_base, найди внутри себя блок с class ='vote'
    quote = vote.find_next_sibling()   # vote, возьми следующий блок после себя

    print(vote.get_text())
    print(quote.get_text(separator='\n'))   # separator указывает, что вставлять между значениями (например, в print('asdf', 'jkl;') по умолчанию был бы пробел, а если добавить separator='\n', то они перенесутся на другую строку) 

get_interesting_fact()
get_bash()