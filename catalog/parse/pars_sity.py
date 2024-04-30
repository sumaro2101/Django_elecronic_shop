from bs4 import BeautifulSoup
import requests
import lorem_text.lorem as lorem
import json

url = 'https://www.citilink.ru/product/smartfon-huawei-nova-12ii-ctr-l81-256gb-8gb-zelenyi-3g-4g-6-8-1080x238-2015329/'

class ParseSite:
    
    __url = None
    all_sites = []
    
    def __init__(self, url, tag, class_=None) -> None:
        self.url = url if type(url) == list else [url]
        self.tag = tag
        self.class_ = class_

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
        
    
    def get_request(self):
        list_response = []
        for elem in self.url:
            request = requests.get(elem)
            self.status_code = request.status_code
            print(self.status_code)
            list_response.append(request.text)
        return list_response
        
        
    def get_parse(self):
        for item in self.get_request():
            self.soup = BeautifulSoup(item, 'html.parser')
            self.all_sites.append(self.soup.find_all(self.tag, class_=self.class_))
         
        
    def parse_items(self):
        self.get_parse()
        to_save = []
        for item_parse in self.all_sites:
            
            try:
                price = int(''.join([item.find('span', class_='e1ap1az10 e119ip7e0 e106ikdt0 app-catalog-fep1ps e1gjr6xo0').text for item in item_parse]).replace(" ", ""))
            except:
                price = int(''.join([item.find('span', class_='e1j9birj0 e106ikdt0 app-catalog-8hy98m e1gjr6xo0').text for item in item_parse]).replace(" ", ""))
                
            try:
                discount = float(''.join([item.find('span', class_='e1ys5m360 e106ikdt0 app-catalog-em023l e1gjr6xo0').text for item in item_parse]).replace('-', '').strip().replace('%', ''))
            except:
                discount = 0.0
                
            filtred_site = {
                "model": "catalog.product",
            "fields": {
                "name": ' '.join(''.join([item.find('h1', class_='e1ubbx7u0 eml1k9j0 app-catalog-lc5se5 e1gjr6xo0').text for item in item_parse]).split(',')[0].split(' ')[1:]),
                "descriptions": lorem.words(50),
                "image_item": "",
                "company": ''.join([item.find('span', class_='app-catalog-nhng7j e1l49rf80').text for item in item_parse]).title(),
                "category": 'Компьютеры',
                "price": price,
                "discount": discount,
                "quantity": 0,
                "discontinued": 0,
                "created_at": "2024-04-23T17:57:05.539Z",
                "created_up": "2024-04-23T17:57:05.539Z",
                "release": "2024-04-23T00:00:00Z"
            }
            }
            to_save.append(filtred_site)
        return to_save
    
    def save_to_json(self):
        with open('parse_result.json', 'w', encoding='utf-8') as file:
            json.dump(self.parse_items(), file, ensure_ascii=False, indent=2)
            print('Готово')
    
    
urls = ['https://www.citilink.ru/product/smartfon-honor-90-lite-5g-8-256gb-polunochnyi-chernyi-1982551/',
        'https://www.citilink.ru/product/smartfon-honor-x9a-5g-8-256gb-izumrudnyi-zelenyi-1969115/',
        'https://www.citilink.ru/product/smartfon-honor-x7a-4-128gb-sinii-okean-1911904/',
        'https://www.citilink.ru/product/smartfon-honor-x8a-6-128gb-nebesno-goluboi-1911907/',
        'https://www.citilink.ru/product/smartfon-honor-x7b-8-128gb-chernyi-1998157/',
        'https://www.citilink.ru/product/smartfon-honor-70-8-128gb-5109ajac-chernyi-1864246/',
        'https://www.citilink.ru/product/smartfon-honor-90-lite-5g-8-256gb-polunochnyi-chernyi-1982551/',
        'https://www.citilink.ru/product/smartfon-honor-x6a-4-128gb-polunochnyi-chernyi-1977230/',
        'https://www.citilink.ru/product/smartfon-honor-x6a-6-128gb-nebesno-serebristyi-1977234/',
        'https://www.citilink.ru/product/smartfon-honor-x5-plus-4-64gb-polunochnyi-chernyi-1977228/',
        'https://www.citilink.ru/product/smartfon-huawei-nova-y72-8-128gb-mga-lx3-chernyi-2002840/',
        'https://www.citilink.ru/product/smartfon-huawei-nova-12ii-ctr-l81-128gb-8gb-zelenyi-3g-4g-6-8-1080x238-2015336/',
        'https://www.citilink.ru/product/smartfon-huawei-nova-y61-4-128gb-eve-lx9n-sinii-2011648/',
        'https://www.citilink.ru/product/smartfon-huawei-nova-11i-8-128gb-mao-lx9n-myatnyi-zelenyi-1936633/',
        'https://www.citilink.ru/product/smartfon-huawei-nova-y91-8-128gb-stg-lx1-lunnoe-serebro-1936630/',
        'https://www.citilink.ru/product/smartfon-huawei-nova-10-8-128gb-chernyi-1892208/',
        'https://www.citilink.ru/product/smartfon-huawei-p60-8-256gb-lna-lx9-zelenyi-1970381/',
        'https://www.citilink.ru/product/smartfon-infinix-note-30-8-256gb-x6833b-chernyi-1927929/',
        'https://www.citilink.ru/product/smartfon-infinix-note-30-pro-8-256gb-x678b-chernyi-1927932/',
        'https://www.citilink.ru/product/smartfon-infinix-note-30-8-128gb-x6833b-chernyi-1926549/',
        'https://www.citilink.ru/product/smartfon-infinix-hot-40i-8-128gb-x6528b-chernyi-1993924/',
        'https://www.citilink.ru/product/smartfon-infinix-hot-40-8-256gb-x6836-chernyi-1993928/',
        'https://www.citilink.ru/product/smartfon-infinix-note-30i-8-256gb-x6716-chernyi-1926453/',
        'https://www.citilink.ru/product/smartfon-infinix-note-30i-8-128gb-x6716-chernyi-1931566/',
        'https://www.citilink.ru/product/smartfon-infinix-smart-8-3-64gb-x6525-chernyi-1993225/',
        'https://www.citilink.ru/product/smartfon-infinix-smart-8-4-128gb-x6525-chernyi-1993221/',
        'https://www.citilink.ru/product/smartfon-infinix-smart-8-plus-4-128gb-x6526-belyi-1998563/',
        'https://www.citilink.ru/product/smartfon-infinix-zero-30-8-256gb-x6731b-zolotoi-1993926/',
        'https://www.citilink.ru/product/smartfon-infinix-note-12-vip-nfc-8-256gb-x672-seryi-1744225/',
        'https://www.citilink.ru/product/smartfon-infinix-smart-7-hd-2-64gb-x6516-chernyi-1914531/',
        'https://www.citilink.ru/product/smartfon-infinix-hot-20s-8-128gb-x6827-belyi-1896279/',
        ]

# a = (ParseSite(urls, 'html'))
# a.save_to_json()
to_save = []
for url in urls:
    b = BeautifulSoup(requests.get(url).text, 'html.parser')
    parse = b.find('script', type="application/ld+json")
    try:
        discount = float(''.join(b.find('span', class_='e1ys5m360 e106ikdt0 app-catalog-em023l e1gjr6xo0').text.split(' ')[-1]).replace('%', ''))
    except:
        discount = 0.0
    load = json.loads(parse.text)
    filtred_site = {
                    "model": "catalog.product",
                "fields": {
                    "name": ' '.join(load['name'].split(',')[0].split(' ')[1:]),
                    "descriptions": load['description'].text if load['description'] is not None else lorem.words(50),
                    "image_item": "",
                    "company": load['brand'].title(),
                    "category": 'Компьютеры',
                    "price": int(load['offers']['price']),
                    "discount": discount,
                    "quantity": 0,
                    "discontinued": 0,
                    "created_at": "2024-04-23T17:57:05.539Z",
                    "created_up": "2024-04-23T17:57:05.539Z",
                    "release": "2024-04-23T00:00:00Z"
                }
                }
    to_save.append(filtred_site)
    print(url.split('//')[1].split('/')[2])
    
with open('parse_result.json', 'w', encoding='utf-8') as file:
            json.dump(to_save, file, ensure_ascii=False, indent=2)
            print('Готово')
