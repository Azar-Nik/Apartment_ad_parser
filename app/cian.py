import requests
from datetime import datetime


def get_json():
    headers = {
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_CIAN_GK=6185b240-da51-404e-bdc1-7f4c5741e93b; _gcl_au=1.1.892344793.1719501793; tmr_lvid=6a980df07e3befa2d3e7257f8acdc206; tmr_lvidTS=1719501793029; uxfb_usertype=searcher; uxs_uid=2b6dc6f0-3499-11ef-90e8-f1b334d3c454; _ym_uid=1719501794372331611; _ym_d=1719501794; afUserId=cc0765e0-616d-47e8-9e35-2e68319dac3a-p; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D; _ga=GA1.1.1811209600.1719501793; _ym_isad=1; AF_SYNC=1723214410127; session_region_id=1; session_main_town_region_id=1; uxfb_card_satisfaction=%5B265389823%5D; cf_clearance=DKoWr.58PRkBLqQFLraw0JaJK_ZHQ1rx3w0Z0NcBDEM-1723227769-1.0.1.1-D0DAsPqarhRxfQ2DEB2CCou5OG3l9m_8X8O1L_z9JA0phm.49cD3Bb9n5kgFFT2Mtvww0XPEZ6_qnxeCoIFGDw; sopr_session=eb953edbe2bf49b4; _ym_visorc=b; __cf_bm=gx4S_KcsPQp55F.br4j3WzFxuOQO1H1EMMn19sL7JEY-1723228242-1.0.1.1-AV6TdvvUNmcckJ6iayIj2XaDvz2Oys_BDVGs78D4DczvHi0wwqs9yQD8Me_vhpb9IW1qCnlCvCdiPYc2sUQVPg; _ga_3369S417EL=GS1.1.1723227768.4.1.1723228780.32.0.0',
        'origin': 'https://www.cian.ru',
        'priority': 'u=1, i',
        'referer': 'https://www.cian.ru/',
        'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
    }
    
    json_data = {
        'jsonQuery': {
            '_type': 'flatrent',
            'sort': {
                'type': 'term',
                'value': 'creation_date_desc',
            },
            'engine_version': {
                'type': 'term',
                'value': 2,
            },
            'region': {
                'type': 'terms',
                'value': [
                    1,
                ],
            },
            'price': {
                'type': 'range',
                'value': {
                    'lte': 50000,
                },
            },
            'currency': {
                'type': 'term',
                'value': 2,
            },
            'bbox': {
                'type': 'term',
                'value': [
                    [
                        36.3260936597,
                        55.2377198848,
                    ],
                    [
                        38.6854076246,
                        56.1076675167,
                    ],
                ],
            },
            'for_day': {
                'type': 'term',
                'value': '!1',
            },
            'room': {
                'type': 'terms',
                'value': [
                    1,
                    2,
                ],
            },
            'only_foot': {
                'type': 'term',
                'value': '2',
            },
            'foot_min': {
                'type': 'range',
                'value': {
                    'lte': 15,
                },
            },
        },
    }
    
    response = requests.post(
        'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
        headers=headers,
        json=json_data,
    )
    
    data = response.json()
    return data


def get_offer(item):
    offer = {}
    offer['offer_id'] = item['id']
    offer['url'] = item["fullUrl"]
    timestamp = datetime.fromtimestamp(item["addedTimestamp"])
    timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H:%M')
    offer['offer_date'] = timestamp
    return offer


def get_offers(data):
    results = []
    for item in data["data"]["offersSerialized"]:
        offer = get_offer(item)
        results.append(offer)
    return results


def main():
    data = get_json()
    return get_offers(data)


if __name__ == "__main__":
    main()