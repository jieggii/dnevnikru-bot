from datetime import datetime
from typing import List

from app.config import config
from app.dnevnikru import Hometask, Timetable


def get_pretty_date(date: datetime) -> str:
    return date.strftime("%d.%m")


def get_pretty_timetable(timetable: Timetable) -> str:
    response = f"Расписание на {get_pretty_date(timetable.date)}:\n"
    for lesson in timetable.lessons:
        response += f"{lesson}. {timetable.lessons[lesson]}\n"
    return response


def get_pretty_hometasks(hometasks: List[Hometask]) -> str:
    response = "Список домашних заданий:\n"
    for i, task in enumerate(hometasks):
        response += f"{i+1}. {task.subject} (на {get_pretty_date(task.date)}): {task.task}\n\n"
    return response


def get_my_mention() -> str:
    return f"[club{config.Bot.GROUP_ID}|@{config.Bot.DOMAIN}]"
