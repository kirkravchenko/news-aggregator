import poster
import telebot
from telebot import types
import properties

BOT_TOKEN = properties.Sensitive.bot_token.value
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='MARKDOWN')

commands = [
    types.BotCommand(command='remove', description='remove'),
    types.BotCommand(command=properties.URLS.un_ru.name, description=properties.Descriptions.un_ru.value),
    types.BotCommand(command=properties.URLS.un_en.name, description=properties.Descriptions.un_en.value),
    types.BotCommand(command=properties.URLS.politico_defense.name, description=properties.Descriptions.politico_defense.value),
    types.BotCommand(command=properties.URLS.politico_economy.name, description=properties.Descriptions.politico_economy.value),
    types.BotCommand(command=properties.URLS.economist_tech.name, description=properties.Descriptions.economist_tech.value),
    types.BotCommand(command=properties.URLS.economist_china.name, description=properties.Descriptions.economist_china.value),
    types.BotCommand(command=properties.URLS.economist_asia.name, description=properties.Descriptions.economist_asia.value),
    types.BotCommand(command=properties.URLS.economist_africa_middle_east.name, description=properties.Descriptions.economist_africa_middle_east.value),
    types.BotCommand(command=properties.URLS.economist_americas.name, description=properties.Descriptions.economist_americas.value),
    types.BotCommand(command=properties.URLS.economist_us.name, description=properties.Descriptions.economist_us.value),
    types.BotCommand(command=properties.URLS.economist_eu.name, description=properties.Descriptions.economist_eu.value),
    types.BotCommand(command=properties.URLS.economist_uk.name, description=properties.Descriptions.economist_uk.value),
    types.BotCommand(command=properties.URLS.bloomberg_politics.name,description=properties.Descriptions.bloomberg_politics.value),
    types.BotCommand(command=properties.URLS.nyt_tech.name, description=properties.Descriptions.nyt_tech.value),
    types.BotCommand(command=properties.URLS.nyt_world.name, description=properties.Descriptions.nyt_world.value),
    types.BotCommand(command=properties.URLS.nyt_africa.name, description=properties.Descriptions.nyt_africa.value),
    types.BotCommand(command=properties.URLS.nyt_americas.name, description=properties.Descriptions.nyt_americas.value),
    types.BotCommand(command=properties.URLS.nyt_asia_pacific.name, description=properties.Descriptions.nyt_asia_pacific.value),
    types.BotCommand(command=properties.URLS.nyt_europe.name, description=properties.Descriptions.nyt_europe.value),
    types.BotCommand(command=properties.URLS.nyt_mid_east.name, description=properties.Descriptions.nyt_mid_east.value),
    types.BotCommand(command=properties.URLS.nyt_us_politics.name, description=properties.Descriptions.nyt_us_politics.value),
    types.BotCommand(command=properties.URLS.nyt_personal_tech.name, description=properties.Descriptions.nyt_personal_tech.value),
    types.BotCommand(command=properties.URLS.nyt_economy.name, description=properties.Descriptions.nyt_economy.value),
    types.BotCommand(command=properties.URLS.nyt_your_money.name, description=properties.Descriptions.nyt_your_money.value),
    types.BotCommand(command=properties.URLS.nyt_small_business.name, description=properties.Descriptions.nyt_small_business.value),
    types.BotCommand(command=properties.URLS.nyt_science.name, description=properties.Descriptions.nyt_science.value),
    types.BotCommand(command=properties.URLS.nyt_movies.name, description=properties.Descriptions.nyt_movies.value)
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
        message_ids.extend(poster.post_it(bot, post, message))


print("bot is running")
bot.infinity_polling()
