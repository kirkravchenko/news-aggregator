import poster
import telebot
from telebot import types
import properties

BOT_TOKEN = properties.Sensitive.bot_token.value
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='MARKDOWN')

commands = [
    types.BotCommand(command=properties.URLS.un_ru.name, description=properties.Descriptions.un_ru.value),
    types.BotCommand(command=properties.URLS.un_en.name, description=properties.Descriptions.un_en.value),
    types.BotCommand(command=properties.URLS.politico_defense.name, description=properties.Descriptions.politico_defense.value),
    types.BotCommand(command='remove', description='remove')
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
        print(message_ids)
        bot.delete_messages(message.chat.id, message_ids)
        message_ids.clear()
    elif message.text[1:] != "start":
        url = properties.URLS[message.text[1:]].value
        post = poster.form_post(url)
        message_ids.extend(poster.post_it(bot, post, message))
    print(str(message_ids))

print("bot is running")
bot.infinity_polling()
