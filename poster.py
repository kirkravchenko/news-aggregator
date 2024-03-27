import feedparser
import ssl
from datetime import datetime

import properties

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def form_post(url):
    post = []
    feed = feedparser.parse(url)
    for entry in feed.entries:
        default_format = '%a, %d %b %Y %H:%M:%S +%f'
        try:
            published_date = (datetime.strptime(entry.published, default_format)
                              .date())
            today = datetime.today().date()
            is_within_interval = ((today - published_date).days <
                                  properties.DateIntervals.week.value)
        except ValueError:
            is_within_interval = True
        if is_within_interval:
            news_item = entry.title + "\n" + entry.link
            post.append(news_item)
    return post


def post_it(bot, post, message):
    text = '\n\n'.join(item for item in post)
    if len(text) > 4095:
        replies_ids = []
        for x in range(0, len(text), 4095):
            replies_ids.append(bot.reply_to(message, text=text[x:x + 4095]).id)
        return replies_ids
    else:
        reply = bot.reply_to(message, '\n\n'.join(post))
        return [reply.id]
