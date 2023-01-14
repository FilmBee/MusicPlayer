"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", 23467646)
        self.API_HASH: str = os.environ.get("API_HASH", b9a5a0a968c4fddaad8db274b35d67f5)
        self.SESSION: str = os.environ.get("SESSION", AQBz9Dl9qeR4-gNZlzvrFJ48PYZXbjdMGpt_Cw_GSjO7Oh-98cj2SxILrvpjnUCL2WMwO9sSbmCF7iR6aL8ISWcbuimfKtRna3IdiYZUauwrBpzTHGPTG2RSzz2nxTL2v7zWN8tktiB5Xmoa1U9Vh7-vO9T8iuEwDLGvy5sf3NpnW0c23q4_BPyxOSu5WI4l7LN6dUfKXe9o5x-CJ-okD-RWE3ETldHpt96sTAu6JGo-Cshr9Fmor7cR5K7IIDA-y5J_lDVodtbt9P-110W9QjWt0VjuIKZ3zpTcXb4n8LVJoERr3ssuyB80aPt7x9rT_QZ8Rx41YjrFA8PRHAtriDp-AAAAAWAVMpsA)
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", 5846340024:AAGcItiFy0LmHztJnDC22YBer6TgzIonLR0)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
