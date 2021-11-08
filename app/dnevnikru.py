import logging
from datetime import datetime, timedelta
from typing import Dict

from dateutil import parser
from pydnevnikruapi.aiodnevnik import dnevnik

from app.config import config

logger = logging.getLogger(__name__)


class Timetable:
    def __init__(self, lessons: Dict[str, str], date: datetime):
        self.lessons = lessons
        self.date = date


class Hometask:
    def __init__(self, subject: str, task: str, date: datetime):
        self.subject = subject
        self.task = task
        self.date = date


class DnevnikRu:
    def __init__(self, login: str, password: str, edu_group: int):
        self.login = login
        self.password = password
        self.edu_group = edu_group
        self.client = dnevnik.AsyncDiaryAPI(login=login, password=password)

    async def _get_timetable(self, start_time: datetime, end_time: datetime) -> Timetable:
        lessons = await self.client.get_group_lessons_info(
            group_id=self.edu_group, start_time=str(start_time), end_time=str(end_time)
        )
        lessons = {item["number"]: item["subject"]["name"] for item in lessons}
        return Timetable(lessons, start_time)

    async def get_timetable_today(self) -> Timetable:
        time = datetime.today()
        return await self._get_timetable(start_time=time, end_time=time)

    async def get_timetable_tomorrow(self) -> Timetable:
        time = datetime.today() + timedelta(days=1)
        return await self._get_timetable(start_time=time, end_time=time)

    async def get_hometasks(self):
        start_time = datetime.today()
        end_date = start_time + timedelta(weeks=3)

        response = await self.client.get_school_homework(
            config.DnevnikRu.SCHOOL_ID, start_time=str(start_time), end_time=str(end_date)
        )
        works = response["works"]
        subjects = response["subjects"]
        lessons = response["lessons"]

        kv_subjects = {}
        kv_lessons = {}

        for subject in subjects:
            kv_subjects.update({subject["id"]: subject["name"]})

        for lesson in lessons:
            kv_lessons.update({lesson["id"]: lesson["date"]})

        home_tasks = []

        for work in works:
            home_tasks.append(
                Hometask(
                    subject=kv_subjects[work["subjectId"]],
                    task=work["text"],
                    date=parser.parse(kv_lessons[work["lesson"]]),
                )
            )

        return home_tasks


dnevnikru = DnevnikRu(
    login=config.DnevnikRu.LOGIN,
    password=config.DnevnikRu.PASSWORD,
    edu_group=config.DnevnikRu.EDU_GROUP,
)
