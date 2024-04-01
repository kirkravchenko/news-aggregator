import feedparser
import ssl
from datetime import datetime
import properties
import telebot

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def get_datetime(item):
    try:
        pub_date = datetime.strptime(item.published,
                                     '%a, %d %b %Y %H:%M:%S +%f').date()
    except ValueError:
        pub_date = datetime.strptime(item.published,
                                     '%a, %d %b %Y %H:%M:%S GMT').date()
    return pub_date


def within_interval(item, interval):
    today = datetime.today().date()
    pub_date = get_datetime(item)
    is_within = (today - pub_date).days < interval
    return is_within


def form_post(url):
    post = []
    feed = feedparser.parse(url)
    feed_filtered = [item for item in feed.entries if
                     within_interval(item,
                                     properties.DateIntervals.today.value)]
    feed_sorted = sorted(feed_filtered, key=lambda t: t.published, reverse=True)
    for item in feed_sorted:
        date_formatted = telebot.formatting.hitalic(
            item.published.split(" +")[0])
        news_item = (date_formatted + "\n" +
                     telebot.formatting.hlink(item.title, item.link))
        post.append(news_item)
    return post


def post_it(bot, post, message):
    max_items = 15
    sub_posts = [post[i:i + max_items] for i in range(0, len(post), max_items)]
    replies_ids = []
    for sub_post in sub_posts:
        text = '\n\n'.join(sub_post)
        reply_id = bot.reply_to(message, text).id
        replies_ids.append(reply_id)
    return replies_ids


# DEPRECATED
def form_post_old(url):
    post = []
    feed = feedparser.parse(url)
    for entry in feed.entries:
        default_format = '%a, %d %b %Y %H:%M:%S +%f'
        try:
            published_date = (datetime.strptime(entry.published, default_format)
                              .date())
            today = datetime.today().date()
            is_within_interval = ((today - published_date).days <
                                  properties.DateIntervals.today.value)
        except ValueError:
            is_within_interval = True
        if is_within_interval:
            pub_date = telebot.formatting.hitalic(
                entry.published.split(" +")[0])
            news_item = f"{entry.title}\n {entry.link}\n{pub_date}"
            post.append(news_item)
    return post
