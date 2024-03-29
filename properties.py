from enum import Enum


class URLS(Enum):
    un_en = "https://news.un.org/feed/subscribe/en/news/all/rss.xml"
    un_ru = "https://news.un.org/feed/subscribe/ru/news/all/rss.xml"
    politico_defense = "https://rss.politico.com/defense.xml"
    politico_economy = "https://rss.politico.com/economy.xml"
    economist_tech = "https://www.economist.com/science-and-technology/rss.xml"
    economist_china = "https://www.economist.com/china/rss.xml"
    economist_asia = "https://www.economist.com/asia/rss.xml"
    economist_africa_middle_east = "https://www.economist.com/middle-east-and-africa/rss.xml"
    economist_americas = "https://www.economist.com/the-americas/rss.xml"
    economist_us = "https://www.economist.com/united-states/rss.xml"
    economist_eu = "https://www.economist.com/europe/rss.xml"
    economist_uk = "https://www.economist.com/britain/rss.xml"
    bloomberg_politics = "https://feeds.bloomberg.com/politics/news.rss"
    nyt_tech = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
    nyt_world = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    nyt_africa = "https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml"
    nyt_americas = "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml"
    nyt_asia_pacific = "https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml"
    nyt_europe = "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml"
    nyt_mid_east = "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml"
    nyt_us_politics = "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
    nyt_personal_tech = "https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml"
    nyt_economy = "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml"
    nyt_your_money = "https://rss.nytimes.com/services/xml/rss/nyt/YourMoney.xml"
    nyt_small_business = "https://rss.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml"
    nyt_science = "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml"
    nyt_movies = "https://rss.nytimes.com/services/xml/rss/nyt/Movies.xml"
    censor_news = "https://assets.censor.net/rss/censor.net/rss_uk_news.xml"
    censor_events = "https://assets.censor.net/rss/censor.net/rss_uk_events.xml"
    censor_resonance = "https://assets.censor.net/rss/censor.net/rss_uk_resonance.xml"
    rbk_news = "https://rssexport.rbc.ru/rbcnews/news/30/full.rss"
    ria_news = "https://ria.ru/export/rss2/archive/index.xml"
    mid_ru = "https://mid.ru/ru/rss.php"
    unian = "https://rss.unian.net/site/news_rus.rss"
    wsj_tech = "https://feeds.a.dj.com/rss/RSSWSJD.xml"
    wsj_news = "https://feeds.a.dj.com/rss/RSSWorldNews.xml"
    reuters_middle_east = "https://www.reutersagency.com/feed/?best-regions=middle-east&post_type=best"
    reuters_africa = "https://www.reutersagency.com/feed/?best-regions=africa&post_type=best"
    reuters_europe = "https://www.reutersagency.com/feed/?best-regions=europe&post_type=best"
    reuters_north_america = "https://www.reutersagency.com/feed/?best-regions=north-america&post_type=best"
    reuters_south_america = "https://www.reutersagency.com/feed/?best-regions=south-america&post_type=best"
    reuters_asia = "https://www.reutersagency.com/feed/?best-regions=asia&post_type=best"


class Descriptions(Enum):
    un_en = 'UN news EN'
    un_ru = 'UN news RU'
    politico_defense = 'Politico defense'
    politico_economy = 'Politico economy'
    economist_tech = 'The Economist technology & science'
    economist_china = 'The Economist China'
    economist_asia = 'The Economist Asia'
    economist_africa_middle_east = 'The Economist Africa, Middle East'
    economist_americas = 'The Economist The Americas'
    economist_us = 'The Economist The US'
    economist_eu = 'The Economist The EU'
    economist_uk = 'The Economist The UK'
    bloomberg_politics = 'Bloomberg politics'
    nyt_tech = 'NYT Technology'
    nyt_world = 'NYT WOLRD'
    nyt_africa = 'NYT AFRICA'
    nyt_americas = 'NYT AMERICAS'
    nyt_asia_pacific = 'NYT ASIA PACIFIC'
    nyt_europe = 'NYT EU'
    nyt_mid_east = 'NYT MID EAST'
    nyt_us_politics = 'NYT US POLITICS'
    nyt_personal_tech = 'NYT PERSONAL TECH'
    nyt_economy = 'NYT ECONOMY'
    nyt_your_money = 'NYT YOUR MONEY'
    nyt_small_business = 'NYT SMALL BUSINESS'
    nyt_science = 'NYT SCIENCE'
    nyt_movies = 'NYT MOVIES'
    censor_news = 'Цензор.НЕТ новости'
    censor_events = 'Цензор.НЕТ события'
    censor_resonance = 'Цензор.НЕТ резонанс'
    rbk_news = 'РБК Новости'
    ria_news = 'РИА Новости'
    mid_ru = 'МИД РФ'
    unian = 'УНИАН'
    wsj_tech = "WSJ technology"
    wsj_news = "WSJ news"
    reuters_middle_east = "Reuters middle east"
    reuters_africa = "Reuters africa"
    reuters_europe = "Reuters europe"
    reuters_north_america = "Reuters north america"
    reuters_south_america = "Reuters south america"
    reuters_asia = "Reuters asia"


class DateIntervals(Enum):
    day = 2
    week = 7
    month = 31