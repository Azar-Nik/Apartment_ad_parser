# Без прокси не работает, сразу банят.
# JSON файл через мобильную версию
# Нужно настроить get_offer и get_offers

import requests
from datetime import datetime
from time import sleep
#import json
from realry import check_database


def get_json():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9',
        # 'cookie': 'srv_id=Zl1n-hk8Qoj3p55-.mM7lUpNqq4txm4tRiD3APx08fnOM-_a_QMzJofRRkBUO1N1UDoUx_O4eo_duNNR-ObNM.VbBAT9HQCWqWUR-9YqM1wTqdPEnexmU2x81TdebF30Q=.web; u=32axl6uo.1d2auy8.3a0nmyrdcqa0; _ga=GA1.1.1483569910.1704635226; tmr_lvid=58e09cd11f73d2ec71eec8f0cf271da5; tmr_lvidTS=1704635225665; _ym_uid=170463522665014885; uxs_uid=3e9df190-ad63-11ee-9763-2988ad3c1fd5; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; _ym_d=1723229034; _gcl_au=1.1.259996322.1723229034; f=5.3fbe2ea70238d638b32428cf8e3c6b5047e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a7b0d53c7afc06d0b2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b90a983f6e93802b5f68e2978c700f15b6bf11f980bc2bc377f2c082410b22639b4e0d8a280d6b65f00df103df0c26013aba0ac8037e2b74f9268a7bf63aa148d22ebf3cb6fd35a0ac8b1472fe2f9ba6b97b0d53c7afc06d0b71e7cb57bbcb8e0f03c77801b122405c03c77801b122405c2da10fb74cac1eab2ebf3cb6fd35a0ac20f3d16ad0b1c546b892c6c84ad16848a9b4102d42ade879dcb5a55b9498f642baf80da35caa52287658d123ba269e0378d0f770042e14e14334186bb7daf4af17c7721dca45217bf072be90bbe19ad40138a903faa4fd02e2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fa267a6ba384b6d357b6c9122eda0b0e572da10fb74cac1eab3fdb0d9d9f6f145bd1ce76042dff8395312f8fecc8ca5e543486a07687daa291; ft="tMN6nPBo2xeErqzTIazd+Q0V9D7Gvx5cP3BeJC1RxsK/wrnijsnJv6qNOwbR+iqW5Sn1PzfghZSOTKOlum0jv/XIGih849vxGoBZYCSYxpqe4vGq1rBhb5bGKZwQRUHzelBG4E6xnZ3U+5mFvHVxi2zvf2hA8dNkZ444PpVlT192c0Yi+4Qwh/0mk3PEdPVv"; buyer_location_id=637640; luri=moskva; buyer_laas_location=637640; _ym_isad=1; _mlocation=637640; _mlocation_mode=laas; domain_sid=f3MGd-9znNBuZeAgV-PPV%3A1723303770834; redirectMav=1; _inlines_order=categoryNodes.locationGroup.params[504].params[550].price; sx=H4sIAAAAAAAC%2F1TSXXLqMAyG4b34mgv%2FSbK6G1m2E1oIBIJLciZ7P9MLOnQDz2heff%2BMbbbE4loQphRckkgeuPoSSy7Zkvn4Z7r5MLreiKe%2BDfIs7YvK8RtlGG2chgIyBXMw1Xw48iE4iBD2g%2FFOvJRUPFlsAjFLdpy1YlDrbLEv%2BYh%2BxjSts8h26mP8FArU%2B1qunN3zXWZPZPeDQUTUQtgYGTAiV8o1cCGwqlT4JU86tPbAJyyn%2BeLqfRScrv263R7wldbyLrvgeT8YoiIxc4uFRbhhFNKUICtLCk5%2F5W052vnbXi%2Fn3B9%2BXGjs95B8%2FprOR3gs7zWIbNwPJjkvTb3HKjUSMdTsY7C%2BEicWK79yHnS%2BHdP3NmsY5sv0GIpv5a4xlryl95sBAPaDYd%2BiBWUfWH3klDMmrpRUmhUbykumfOcVKq8Wlyc9U9aBVyya8iV5P%2F%2F5IMSfGqyhWUqhQSNWUYylqtMKxIFa%2BN0GbPFe%2BsVucLH0dVvPM7h%2Bxs%2BI%2FtQs%2Fu0cfrYhnpmgpqCYONsM2WL0mqDF5FoOL3n59FO%2FbfW03Pq9jzXg5nrYjssYH0rur0y87%2F8DAAD%2F%2F5RvJ3jRAgAA; v=1723312820; _ga_M29JC28873=GS1.1.1723315027.12.1.1723315028.59.0.0; tmr_detect=0%7C1723315030555',
        'priority': 'u=1, i',
        'referer': 'https://m.avito.ru/items/search?locationId=637640&footWalkingMetro=15&categoryId=24&params[201]=1060&params[504]=5256&params[550][]=5703&params[550][]=5704&priceMax=50000&sort=date&presentationType=serp',
        'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-mobile-site': '1',
    }

    params = {
        'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
        'parameters[locationId]': '637640',
        'parameters[footWalkingMetro]': '15',
        'parameters[categoryId]': '24',
        'parameters[params][201]': '1060',
        'parameters[params][504]': '5256',
        'parameters[params][550][0]': '5703',
        'parameters[params][550][1]': '5704',
        'parameters[priceMax]': '50000',
        'parameters[sort]': 'date',
        'parameters[presentationType]': 'serp',
        'parameters[inlinesOrder][0]': 'categoryNodes',
        'parameters[inlinesOrder][1]': 'locationGroup',
        'parameters[inlinesOrder][2]': 'params[504]',
        'parameters[inlinesOrder][3]': 'params[550]',
        'parameters[inlinesOrder][4]': 'price',
    }

    response = requests.get('https://m.avito.ru/api/5/items/search/header', params=params, headers=headers)
    
    data = response.json()
    #with open('data.json', 'w', encoding='utf-8') as f:
    #    f.write(json.dumps(data, ensure_ascii=False, indent=4))
    return data


def get_offer(item):
    offer = {}
    offer['offer_id'] = item['id']
    offer['price'] = item["price"]
    offer['title'] = ''
    offer['url'] = 'https://www.avito.ru' + item["uri_mweb"]
    timestamp = datetime.fromtimestamp(item["time"])
    timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H:%M')
    offer['offer_date'] = timestamp
    return offer


def get_offers(data):
    for item in data["result"]["items"]:
        if 'item' in item['type']:
            offer = get_offer(item['value'])
            check_database(offer)


def main():
    data = get_json()
    get_offers(data)


if __name__ == "__main__":
    while True:
        main()
        sleep(60)