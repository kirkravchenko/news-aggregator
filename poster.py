import feedparser
import ssl

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def form_post(url):
    post = []
    feed = feedparser.parse(url)
    for entry in feed.entries:
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
