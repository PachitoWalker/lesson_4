# import requests

# url = "https://swapi.dev/api/starships/"
# response = requests.get(url).json()

# all_starships = response.get("results")
# for starship in all_starships:
#     print(starship)
# speeds = []
# count = 0
# for starship in all_starships:
#     speed = starship.get("max_atmosphering_speed")
#     if count < 5  and speed != "n/a" and speed.isdigit():
#         speeds.append(int(speed))
#         count += 1
# print(speeds)
# print(max(speeds))



import requests
import bs4
import datetime

today = datetime.datetime.today()
today = today.strftime("%d/%m/%Y") #указываю, что today должно указваться в порядке день/месяц/год
payload = {"date_req": today}

def get_curs(id):
    return xml.find("valute", {"id":id}).value.text   # найти valuete c id  = id


url = "http://www.cbr.ru/scripts/XML_daily.asp?"

response = requests.get(url, params=payload)   # params - параметры - то, что я буду добавлять к url
if response.status_code ==200:   # если код страницы = 200 (никаких ошибок нет) то...
    response = response.content
    xml = bs4.BeautifulSoup(response, "html.parser")
    all = xml.find_all("valute")
    #print(all)
    #print(xml.find("valute").value)   # find отличается от find all тем, что он возвращает только 1 значение (сейчас внутри valute - valute id = "R01010")     xml, найди внутри valute тег value и верни его значение
    print(get_curs("R01235"), "рублей за 1 доллар")
    print(get_curs("R01239"), "рублей за 1 евро")
    print(get_curs("R01375"), "рублей за 1 юань")
    print(get_curs("R01150"), "рублей за 10000 Вьетнамстких донгов")
    print(get_curs("R01010"), "рублей за 1 Австрийский доллар")



