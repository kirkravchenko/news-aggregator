import feedparser
import ssl
from datetime import datetime
import properties

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def form_post(url):
    post = []
    feed = feedparser.parse(url)
    published_date = datetime.today()
    for entry in feed.entries:
        default_format = '%a, %d %b %Y %H:%M:%S +%f'
        try:
            published_date = (datetime.strptime(entry.published, default_format)
                              .date())
            today = datetime.today().date()
            is_within_interval = ((today - published_date).days <
                                  properties.DateIntervals.day.value)
        except ValueError:
            is_within_interval = True
        if is_within_interval:
            date = published_date.strftime("%H:%M %B %d, %Y")
            news_item = f"{entry.title}\n {entry.link}\n{date}"
            post.append(news_item)
    return post


def post_it(bot, post, message):
    sub_posts = [post[i:i+15] for i in range(0, len(post), 15)]
    replies_ids = []
    for sub_post in sub_posts:
        text = '\n\n'.join(sub_post)
        reply_id = bot.reply_to(message, text).id
        replies_ids.append(reply_id)
    return replies_ids
