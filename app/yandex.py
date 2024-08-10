import requests
from datetime import datetime
from time import sleep
from realry import check_database


def get_json():
    headers = {
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'client-view-type': 'desktop',
        # 'cookie': 'yandexuid=4402866201702325368; is_gdpr=0; is_gdpr_b=CI7bbxD33gEoAg==; yashr=8760536521702325392; _ym_uid=1702325393554738843; my=YwA=; gdpr=0; gpb=gpauto.53_507934%3A34_395809%3A140%3A1%3A1704831410; sessionid2=3:1717269291.5.0.1706297036859:MGHUsA:4.1.2:1|1079277211.-1.2.3:1706297036|6:10191679.525749.fakesign0000000000000000000; _yasc=Yf83NoV9Zp442NiY02pB51GmBT5tBNuomJYTU3PtFrlFitnqAwx4HpkwpOt3SlcHFtX0QA==; i=efN9c/QBWz+pW5mpEhF7SOr6IkRtGFay4qDs/KRrVzRkn7JrpLLDQl+q68kvhjE/rHkZdiWl0yNPU2A2P5dsmVG3dw4=; yandex_csyr=1723211214; isa=SMSSD0b1IxOL/J6Pu1aYE6yLW3CdYk+99kEOpvsPUG6Kc52dKrGV22enbLOJolSSs8eLpFz8EAPPNK+pM+A9ty9Hx6Y=; sae=0:EAA36A15-15BA-4379-A37A-C658567C2F22:p:24.6.4.580:w:d:RU:20231211; bh=ElAiQ2hyb21pdW0iO3Y9IjEyNCIsICJZYUJyb3dzZXIiO3Y9IjI0LjYiLCAiTm90LUEuQnJhbmQiO3Y9Ijk5IiwgIllvd3NlciI7dj0iMi41IhoFIng4NiIiDCIyNC4xLjUuODAzIioCPzAyAiIiOgkiV2luZG93cyJCCCIxNS4wLjAiSgQiNjQiUmciQ2hyb21pdW0iO3Y9IjEyNC4wLjYzNjcuMjQzIiwgIllhQnJvd3NlciI7dj0iMjQuNi40LjU4MCIsICJOb3QtQS5CcmFuZCI7dj0iOTkuMC4wLjAiLCAiWW93c2VyIjt2PSIyLjUiWgI/MGCd3dy1Bmoh3Mrh/wiS2KGxA5/P4eoD+/rw5w3r//32D/uRh9YH84EC; sso_status=sso.passport.yandex.ru:synchronized; Session_id=3:1723293953.5.0.1706297036859:MGHUsA:4.1.2:1|1079277211.-1.2.3:1706297036|192720156.16544199.2.2:16544199.3:1722841235|6:10193635.788523.fJrb4aRm1od-A35zrpWW7oEsVO0; sessar=1.1192.CiACO6lkaYpuleOBZsZzlEjbrd5-mni-lSwuyTd3nZIe8w.0izwxBZJMzA7SItRRW0RPEzofqG5sehzNPXvUgtO1RY; yandex_login=romazarkin; yp=1723364565.uc.ru#1723364565.duc.ru#1754377236.cld.2378379-1#2038652753.pcs.1#2038653953.udn.cDrQoNC%2B0LzQsNC9INCQLg%3D%3D#1725207550.hdrc.1#1745239434.stltp.serp_bk-map_1_1713703434#1733037298.szm.1:3440x1440:1700x1295#2038201235.multib.1#2038652603.2fa.1; ys=newsca.native_cache#svt.1#def_bro.1#ead.2FECB7CF#udn.cDrQoNC%2B0LzQsNC9INCQLg%3D%3D#c_chck.3650328573; L=WAlgfkRZAg8HRWNGdEtcRlZkBXcBcGRjJxUnBhVWJywwJg==.1723293953.15839.334754.3a5bf9101cbaac0bcb03163f845fd183; mda2_beacon=1723293953641; suid=0f177766f21b09df3f778ee031f5c9ca.f8327f61899463e3d67a69ebdc93f2a3; _csrf_token=3b595f8b5f6d18d5d5e8ab27871dcecccea1e210cd6c30ed; from=search; exp_uid=a7e81fdc-90e8-4fce-a93c-95e76e6de1db; show_egrn_reports_link=NO_1079277211; font_loaded=YSv1; _ym_d=1723294398; _ym_isad=1; KIykI=1; prev_uaas_data=%7B%22uaasExpNames%22%3A%5B%22REALTYFRONT-16113_bring_tenant_banner%22%2C%22REALTYFRONT-16792_show_arenda_chat_button%22%2C%22REALTYFRONT-17599_new_owner_target%22%2C%22REALTYFRONT-19425_redesign_site_plans_modals%22%2C%22REALTYFRONT-18481_verticals_3d_tour%22%2C%22REALTYFRONT-18486_hide_candidates_questionnaire%22%2C%22REALTYFRONT-20711_quick_request_for_an_impression%22%2C%22REALTYFRONT-21701_owner_get_consultation_target%22%2C%22REALTYBACK-13472_newbuilding_rate_change%22%2C%22REALTYFRONT-18560_realty_hidden_flat_number%22%2C%22REALTYFRONT-22002_show_podbor_pdf_for_mobile_number_banners%22%2C%22REALTYBACK-9999_disable_paid_only%22%2C%22REALTYFRONT-21257_new_podbor_landing%22%2C%22REALTYFRONT-21695_show_new_landing_owner%22%2C%22REALTYFRONT-22452_new_podbor_entrypoints%22%2C%22REALTYFRONT-18660_additional_cta_on_paid_site_card%22%2C%22REALTYFRONT-23113_podbor_site_and_offer_cards_mortgage_calc_up%22%2C%22REALTYFRONT-22354_redesign_samolet_gallery%22%2C%22REALTYFRONT-20932_without_newbuilding_carousel%22%2C%22REALTYFRONT-22274_arenda_trade_in_banner%22%2C%22REALTYFRONT-23562_show_offer_draft_agents_promo%22%2C%22REALTYFRONT-23433_podbor_monthly_payment_quiz_popup%22%2C%22REALTYBACK-14986_dj_relevance_log_bid_for_newbuildings_ranking%22%2C%22REALTYFRONT-21278_hidden_price_desc%22%2C%22REALTYFRONT-21282_guaranteed_payments_banner%22%2C%22REALTYFRONT-17115_referral_with_stories%22%2C%22REALTYFRONT-22025_arenda_map_pin%22%2C%22realty_aa_experiment%22%2C%22arenda-aa-exp%22%5D%2C%22uaasUid%22%3A%224402866201702325368%22%7D; prev_uaas_expcrypted=So3OEHAmmVTVYp4yofYI6PsgVmt01m8s-htcoFF2Pae2by5jvwLzy77RyhwBz-GVjn7fP0nYAophj4_F5SYXOAc4-Exxt1tO40cq8_5if1DrvlCeX1XEYZ1Koti212bu4uA6gdJ_Tyl5aXkXBsy3cuQuiNYk4oKc3MR89BddFuhFf0TzLqTsWq9uEOyLjzSSoDC1ywRaHY9cZ3ktUEqMcr6Cm7Ed9lM5SYfsTKbexo748HfIYib8Np15bpM4Z0afrUDHUK8Y8h6ugC0vdjHrLCmZgBxJfZbtOvfGSVtklAqria-xUC34kNA8UkJPbBXiPU5m6w6746rp_4LNXh6Fh8x7dJjx5jM9h7aPuU1sDlU%2C; rgid=587795; geo_id=213; region_id=1; from_lifetime=1723295082372; _yasc=NW9p/ZiwPhNxhctouj2C44/yXMfGtDq7DCJ9tMnVGM4ZdYjG10DezLx8tZPFscAR',
        'priority': 'u=1, i',
        'referer': 'https://realty.ya.ru/moskva/snyat/kvartira/1,2-komnatnie/?priceMax=50000&metroTransport=ON_FOOT&timeToMetro=15&sort=DATE_DESC',
        'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.243", "YaBrowser";v="24.6.4.580", "Not-A.Brand";v="99.0.0.0", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
        'x-client-version': '756.1.1',
        'x-metrika-client-id': '1702325393554738843',
        'x-page-request-id': '928294ee82e7dcb30e1a33903fc2572c',
        'x-requested-with': 'XMLHttpRequest',
        'x-retpath-y': 'https://realty.ya.ru/moskva/snyat/kvartira/1,2-komnatnie/?priceMax=50000&metroTransport=ON_FOOT&timeToMetro=15&sort=DATE_DESC',
    }

    params = {
        'priceMax': '50000',
        'metroTransport': 'ON_FOOT',
        'timeToMetro': '15',
        'rgid': '587795',
        'type': 'RENT',
        'category': 'APARTMENT',
        'roomsTotal': [
            '1',
            '2',
        ],
        '_pageType': 'search',
        '_providers': [
            'ads',
            'breadcrumbs',
            'filters',
            'filtersParams',
            'forms',
            'init-ya-arenda-slider-snippets',
            'mapsPromo',
            'mf-footer',
            'newbuildingPromo',
            'offers-stats',
            'queryId',
            'react-search-data',
            'refinements',
            'related-newbuildings',
            'reviews',
            'samolet-related-newbuildings',
            'search',
            'searchHistoryParams',
            'searchParams',
            'searchPresets',
            'seo',
            'seo-data-offers-count',
            'seo-texts',
            'showSurveyBanner',
            'ya-arenda-rent-pladge-snippets',
        ],
        'crc': 'ub4622286027c705b14e7e2dc6363a566',
    }

    response = requests.get('https://realty.ya.ru/gate/react-page/get/', params=params, headers=headers)
    data = response.json()
    return data


def get_offer(item):
    offer = {}
    offer["offer_id"] = item["offerId"]
    offer['price'] = item["price"]["value"]
    offer['title'] = ''
    offer['url'] = item["shareUrl"]
    offer_date = datetime.strptime(item["creationDate"], "%Y-%m-%dT%H:%M:%SZ")
    offer_date = datetime.strftime(offer_date, '%d.%m.%Y в %H:%M')
    offer['offer_date'] = offer_date
    
    return offer


def get_offers(data):
    for item in data["response"]["search"]["offers"]["entities"]:
        offer = get_offer(item)
        check_database(offer)


def main():
    data = get_json()
    get_offers(data)


if __name__ == '__main__':
    while True:
        main()
        sleep(60)