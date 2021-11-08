import logging

from vkwave.bots import BotEvent, DefaultRouter, SimpleBotEvent
from vkwave.bots.core.dispatching import filters

from app import fmt
from app.config import config
from app.dnevnikru import dnevnikru
from app.filters import CommandsFilter, InviteMeFilter, OnlyMentionMe, PeerIDsFilter

logger = logging.getLogger(__name__)

router = DefaultRouter(
    [
        filters.MessageFromConversationTypeFilter("from_chat"),
        PeerIDsFilter(config.Bot.PEER_IDS),
    ]
)
reg = router.registrar

invite_me_filter = InviteMeFilter()
only_mention_me_filter = OnlyMentionMe()


@reg.with_decorator(invite_me_filter)
async def handle_invite_me(event: BotEvent):
    event = SimpleBotEvent(event)
    await event.answer(
        "Привет-с! Я бот для классной беседы, с моей помощью вы сможете узнать расписание и дз.\n"
        f"Чтобы узнать список команд -- пишите @{config.Bot.DOMAIN}"
    )


@reg.with_decorator(only_mention_me_filter | CommandsFilter("help", "помощь", "команды"))
async def handle_help(event: BotEvent):
    event = SimpleBotEvent(event)
    await event.answer(
        "Список моих команд:\n"
        "/help -- список команд\n"
        "/ht -- список ДЗ\n"
        "/today -- расписание на сегодня\n"
        "/tomorrow -- расписание на завтра\n"
    )


@reg.with_decorator(CommandsFilter("ht", "дз"))
async def handle_ht(event):
    event = SimpleBotEvent(event)
    hometasks = await dnevnikru.get_hometasks()
    response = fmt.get_pretty_hometasks(hometasks)
    await event.answer(response)


@reg.with_decorator(CommandsFilter("today", "сегодня", "td"))
async def handle_today(event):
    event = SimpleBotEvent(event)
    timetable = await dnevnikru.get_timetable_today()
    response = fmt.get_pretty_timetable(timetable)
    await event.answer(response)


@reg.with_decorator(CommandsFilter("tomorrow", "завтра", "tm"))
async def handle_tomorrow(event):
    event = SimpleBotEvent(event)
    timetable = await dnevnikru.get_timetable_tomorrow()
    response = fmt.get_pretty_timetable(timetable)
    await event.answer(response)
