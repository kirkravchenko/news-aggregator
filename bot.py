import poster
import telebot
from telebot import types
import properties
import sensitive

BOT_TOKEN = sensitive.Bot.token.value
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

commands = [
    types.BotCommand(command='remove', description='remove'),
    types.BotCommand(command=properties.URLS.censor_news.name,
                     description=properties.Descriptions.censor_news.value),
    types.BotCommand(command=properties.URLS.unian.name,
                     description=properties.Descriptions.unian.value),
    types.BotCommand(command=properties.URLS.habr_articles.name,
                     description=properties.Descriptions.habr_articles.value),
    types.BotCommand(command=properties.URLS.habr_news.name,
                     description=properties.Descriptions.habr_news.value),
    types.BotCommand(command=properties.URLS.rbk_news.name,
                     description=properties.Descriptions.rbk_news.value),
    types.BotCommand(command=properties.URLS.ria_news.name,
                     description=properties.Descriptions.ria_news.value),
    types.BotCommand(command=properties.URLS.bbc_news.name,
                     description=properties.Descriptions.bbc_news.value),
    types.BotCommand(command=properties.URLS.independent_news.name,
                     description=properties.Descriptions.independent_news.value),
    types.BotCommand(command=properties.URLS.guardian_europe.name,
                     description=properties.Descriptions.guardian_europe.value),
    types.BotCommand(command=properties.URLS.bild.name,
                     description=properties.Descriptions.bild.value),
    types.BotCommand(command=properties.URLS.dw.name,
                     description=properties.Descriptions.dw.value),
    types.BotCommand(command=properties.URLS.sme.name,
                     description=properties.Descriptions.sme.value),
    types.BotCommand(command=properties.URLS.aktuality.name,
                     description=properties.Descriptions.aktuality.value),
    types.BotCommand(command=properties.URLS.un_ru.name,
                     description=properties.Descriptions.un_ru.value),
    types.BotCommand(command=properties.URLS.guardian_us.name,
                     description=properties.Descriptions.guardian_us.value),
    types.BotCommand(command=properties.URLS.guardian_middle_east.name,
                     description=properties.Descriptions.guardian_middle_east.value),
    types.BotCommand(command=properties.URLS.guardian_world.name,
                     description=properties.Descriptions.guardian_world.value),
    types.BotCommand(command=properties.URLS.guardian_asia.name,
                     description=properties.Descriptions.guardian_asia.value),
    types.BotCommand(command=properties.URLS.guardian_americas.name,
                     description=properties.Descriptions.guardian_americas.value),
    types.BotCommand(command=properties.URLS.guardian_africa.name,
                     description=properties.Descriptions.guardian_africa.value),
    types.BotCommand(command=properties.URLS.guardian_global_dev.name,
                     description=properties.Descriptions.guardian_global_dev.value),
    types.BotCommand(command=properties.URLS.politico_defense.name,
                     description=properties.Descriptions.politico_defense.value),
    types.BotCommand(command=properties.URLS.politico_economy.name,
                     description=properties.Descriptions.politico_economy.value),
    types.BotCommand(command=properties.URLS.economist_tech.name,
                     description=properties.Descriptions.economist_tech.value),
    types.BotCommand(command=properties.URLS.economist_china.name,
                     description=properties.Descriptions.economist_china.value),
    types.BotCommand(command=properties.URLS.economist_asia.name,
                     description=properties.Descriptions.economist_asia.value),
    types.BotCommand(command=properties.URLS.economist_africa_middle_east.name,
                     description=properties.Descriptions.economist_africa_middle_east.value),
    types.BotCommand(command=properties.URLS.economist_americas.name,
                     description=properties.Descriptions.economist_americas.value),
    types.BotCommand(command=properties.URLS.economist_us.name,
                     description=properties.Descriptions.economist_us.value),
    types.BotCommand(command=properties.URLS.economist_eu.name,
                     description=properties.Descriptions.economist_eu.value),
    types.BotCommand(command=properties.URLS.economist_uk.name,
                     description=properties.Descriptions.economist_uk.value),
    types.BotCommand(command=properties.URLS.bloomberg_politics.name,
                     description=properties.Descriptions.bloomberg_politics.value),
    types.BotCommand(command=properties.URLS.nyt_tech.name,
                     description=properties.Descriptions.nyt_tech.value),
    types.BotCommand(command=properties.URLS.nyt_world.name,
                     description=properties.Descriptions.nyt_world.value),
    types.BotCommand(command=properties.URLS.nyt_africa.name,
                     description=properties.Descriptions.nyt_africa.value),
    types.BotCommand(command=properties.URLS.nyt_americas.name,
                     description=properties.Descriptions.nyt_americas.value),
    types.BotCommand(command=properties.URLS.nyt_asia_pacific.name,
                     description=properties.Descriptions.nyt_asia_pacific.value),
    types.BotCommand(command=properties.URLS.nyt_europe.name,
                     description=properties.Descriptions.nyt_europe.value),
    types.BotCommand(command=properties.URLS.nyt_mid_east.name,
                     description=properties.Descriptions.nyt_mid_east.value),
    types.BotCommand(command=properties.URLS.nyt_us_politics.name,
                     description=properties.Descriptions.nyt_us_politics.value),
    types.BotCommand(command=properties.URLS.nyt_personal_tech.name,
                     description=properties.Descriptions.nyt_personal_tech.value),
    types.BotCommand(command=properties.URLS.nyt_economy.name,
                     description=properties.Descriptions.nyt_economy.value),
    types.BotCommand(command=properties.URLS.nyt_your_money.name,
                     description=properties.Descriptions.nyt_your_money.value),
    types.BotCommand(command=properties.URLS.nyt_small_business.name,
                     description=properties.Descriptions.nyt_small_business.value),
    types.BotCommand(command=properties.URLS.nyt_science.name,
                     description=properties.Descriptions.nyt_science.value),
    types.BotCommand(command=properties.URLS.nyt_movies.name,
                     description=properties.Descriptions.nyt_movies.value),
    types.BotCommand(command=properties.URLS.wsj_tech.name,
                     description=properties.Descriptions.wsj_tech.value),
    types.BotCommand(command=properties.URLS.wsj_news.name,
                     description=properties.Descriptions.wsj_news.value)
]
bot.set_my_commands(commands)

message_ids = []


@bot.message_handler()
def command_help(message):
    message_ids.append(message.id)
    bot.set_chat_menu_button(
        message.chat.id, types.MenuButtonCommands('commands')
    )
    if message.text[1:] == "remove":
        bot.delete_messages(message.chat.id, message_ids)
        message_ids.clear()
    elif message.text[1:] != "start":
        url = properties.URLS[message.text[1:]].value
        post = poster.form_post(url)
        messages_ids_output = poster.post_it(bot, post, message)
        message_ids.extend(messages_ids_output)


print("bot is running")
bot.infinity_polling()
