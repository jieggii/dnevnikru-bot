from betterconf import Config as BetterConfig
from betterconf import caster, field


class Config(BetterConfig):
    class Bot(BetterConfig):
        _prefix_ = "BOT"
        TOKEN = field()
        GROUP_ID = field(caster=caster.to_int)
        DOMAIN = field()
        PEER_IDS = field(caster=caster.to_list, default=["*"])

    class DnevnikRu(BetterConfig):
        _prefix_ = "DNEVNIKRU"
        LOGIN = field()
        PASSWORD = field()
        SCHOOL_ID = field(caster=caster.to_int)
        EDU_GROUP = field(caster=caster.to_int)


config = Config()
