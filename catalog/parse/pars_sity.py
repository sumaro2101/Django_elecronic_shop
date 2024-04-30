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
    
    
urls = ['https://www.citilink.ru/product/noutbuk-igrovoi-msi-titan-18-hx-a14vig-211ru-9s7-182221-211-18-ips-int-2000998/',
        'https://www.citilink.ru/product/noutbuk-msi-creator-16-ai-studio-a1vig-060ru-core-ultra-9-185h-64gb-ss-2001036/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-asus-rog-zephyrus-duo-16-gx650py-nm085w-90nr0bi1-m004x-1942669/',
        'https://www.citilink.ru/product/noutbuk-msi-stealth-16-ai-studio-a1vig-062ru-ul9-185h-32gb-ssd2tb-rtx4-2001141/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-msi-creatorpro-x17-hx-a13vks-267ru-9s7-17q231-267-17-3-1931858/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-asus-rog-strix-scar-18-g834jyr-r6080w-90nr0ip2-m00400-2000013/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-msi-creator-z17-hx-studio-a14vgt-267ru-9s7-17n212-267-2001043/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-samsung-galaxy-book-3-ultra-np960-np960xfh-xa1in-16-20-1988328/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-asus-zenbook-pro-16x-oled-ux7602vi-my073x-90nb10k1-m00-1973232/',
        'https://www.citilink.ru/product/noutbuk-lenovo-thinkpad-x1-carbon-gen-10-21cb0068rt-14-ips-intel-core-2001231/',
        'https://www.citilink.ru/product/noutbuk-dell-xps-15-9530-i7-13700h-16gb-ssd1tb-rtx4060-8gb-15-6-oled-t-2011669/',
        'https://www.citilink.ru/product/noutbuk-dell-xps-13-9320-i7-1360p-32gb-ssd1tb-13-4-oled-touch-fhd-w11p-2011663/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-hp-omen-16-wf0032ci-9e694ea-16-1-ips-intel-core-i7-137-2005335/',
        'https://www.citilink.ru/product/noutbuk-hp-spectre-x360-16-f1028nn-79s16ea-16-transformer-ips-intel-co-1986118/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-asus-rog-flow-gv601vi-nl055w-90nr0g01-m002v0-16-2023-t-2000071/',
        'https://www.citilink.ru/product/noutbuk-msi-pulse-17-ai-c1vgkg-ul9-185h-16gb-ssd1tb-rtx4070-8gb-17-ips-2001128/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-msi-vector-16-hx-a14vgg-283ru-9s7-15m242-283-16-ips-in-2000990/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-msi-raider-ge77hx-12uhs-232ru-9s7-17k514-232-17-3-ips-1833340/',
        'https://www.citilink.ru/product/noutbuk-lenovo-thinkpad-x1-carbon-g10-21ccs9q201-14-2023-ips-intel-cor-1877153/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-msi-summit-e16-ai-studio-a1vetg-017ru-9s7-159621-017-1-2001135/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-msi-prestige-16-ai-studio-b1veg-080ru-9s7-15a211-080-1-2001053/',
        'https://www.citilink.ru/product/noutbuk-samsung-galaxy-book-3-pro-np944-np944xfg-kc1it-14-2023-amoled-1982456/',
        'https://www.citilink.ru/product/noutbuk-apple-macbook-air-a2681-m2-8-core-16gb-ssd512gb-8-core-gpu-13-2016322/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-asus-vivobook-pro-16x-oled-k6604jv-mx112w-90nb1102-m00-1929247/',
        'https://www.citilink.ru/product/noutbuk-lenovo-legion-slim-5-16irh8-i7-13700h-16gb-ssd1tb-rtx4070-8gb-1996061/',
        'https://www.citilink.ru/product/noutbuk-asus-expertbook-b9-b9403cva-km0499x-90nx05w1-m00nj0-14-2023-ol-2000062/',
        'https://www.citilink.ru/product/noutbuk-msi-sword-17-hx-b14vgkg-i9-14900hx-16gb-ssd1tb-rtx4070-8gb-17-2000993/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-asus-tuf-gaming-a15-fa507ui-hq059-90nr0i65-m00330-15-6-2000065/',
        'https://www.citilink.ru/product/noutbuk-lenovo-legion-slim-5-16aph8-ryzen-7-7840hs-16gb-ssd1tb-rtx4070-1995965/',
        'https://www.citilink.ru/product/noutbuk-igrovoi-lenovo-loq-15irh8-82xv00kcrk-15-6-2023-ips-intel-core-2001270/'
            
        ]

a = (ParseSite(urls, 'html'))
a.save_to_json()


# b = BeautifulSoup(requests.get(url).text, 'html.parser')
# parse = b.find('script', type="application/ld+json")

# print(json.loads(parse.text)['description'])
