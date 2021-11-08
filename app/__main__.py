import logging

from vkwave.bots import SimpleLongPollBot
from vkwave.bots.core.dispatching import filters

from app.config import config
from app.routers import chat

logging.basicConfig(level=logging.INFO)

bot = SimpleLongPollBot(config.Bot.TOKEN, config.Bot.GROUP_ID)
bot.router.registrar.add_default_filter(filters.EventTypeFilter("message_new"))

bot.dispatcher.add_router(chat.router)

try:
    bot.run_forever()

except KeyboardInterrupt:
    exit()
