import json
from pathlib import Path

from .badges import Badges

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


def setup(bot):
    cog = Badges(bot)
    bot.add_cog(cog)
