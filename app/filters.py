from typing import List

from vkwave.bots import BaseEvent
from vkwave.bots.core.dispatching.filters import CommandsFilter as BaseCommandsFilter
from vkwave.bots.core.dispatching.filters import get_text
from vkwave.bots.core.dispatching.filters.base import BaseFilter, FilterResult
from vkwave.types.objects import MessagesMessageActionStatus

from app.config import config
from app.fmt import get_my_mention


class PeerIDsFilter(BaseFilter):
    def __init__(self, peer_ids: List[str]):
        self.peer_ids = peer_ids

    async def check(self, event: BaseEvent) -> FilterResult:
        if self.peer_ids == ["*"]:
            return FilterResult(True)
        if str(event.object.object.message.peer_id) in self.peer_ids:
            return FilterResult(True)

        return FilterResult(False)


class InviteMeFilter(BaseFilter):
    def __init__(self):
        pass

    async def check(self, event: BaseEvent) -> FilterResult:
        action = event.object.object.message.action
        if action:
            if action.type == MessagesMessageActionStatus.CHAT_INVITE_USER:
                if action.member_id == -config.Bot.GROUP_ID:
                    return FilterResult(True)

        return FilterResult(False)


class CommandsFilter(BaseCommandsFilter):
    def __init__(self, *commands: str):
        super(CommandsFilter, self).__init__(
            prefixes=("!", "/", get_my_mention() + " "),
            commands=commands,
            ignore_case=True,
        )


class OnlyMentionMe(BaseFilter):
    async def check(self, event) -> FilterResult:
        text = get_text(event)
        print(text)
        print(get_my_mention())
        if text:
            if text == get_my_mention():
                return FilterResult(True)

        return FilterResult(False)
