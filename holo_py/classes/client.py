import asyncio
import json
import re

import aiohttp

from holo_py.types import HoloResponse


class HoloClient:
    _base_url = "http://discord-holo-api.ml/api/"
    _loop = None

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop

    @classmethod
    async def get_emote(cls, tag: str) -> HoloResponse:
        """
        Get's an emotion from API - http://discord-holo-api.ml/api/

        :param tag: string name of emotion tag to search, like "kiss"
        :return: HoloResponse
        :raise ValueError: if no tag was specified
        """

        tag = re.sub(r"[^ -~]+", r"", tag)

        if not tag or len(tag) < 3:
            raise ValueError("tag length must be more or equal 3" if tag else "you must specify a tag")

        async with aiohttp.ClientSession(loop=cls._loop) as session:
            resp = await session.get(cls._base_url + tag)

            try:
                data = await resp.json()

            except aiohttp.client_exceptions.ContentTypeError as err:
                data = json.loads(await resp.read())

            return HoloResponse(data)
