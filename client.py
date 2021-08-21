import asyncio
import aiohttp
import json
import re


class HoloResponse:
    def __init__(self, data: dict):
        self.url: str = data.get("url", None)


class HoloClient:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop
        self._base_url = "http://discord-holo-api.ml/api/"

    async def get_emote(self, tag: str) -> HoloResponse:
        """
        Get's an emotion from API - http://discord-holo-api.ml/api/

        :param tag: string name of emotion tag to search, like "kiss"
        :return: HoloResponse
        :raise ValueError: if no tag was specified
        """

        tag = re.sub(r"[^ -~]+", r"", tag)

        if not tag or len(tag) < 3:
            raise ValueError("tag length must be more or equal 3" if tag else "you must specify a tag")

        async with aiohttp.ClientSession(loop=self._loop) as session:
            resp = await session.get(self._base_url + tag)

            try:
                data = await resp.json()

            except aiohttp.client_exceptions.ContentTypeError as err:
                data = json.loads(await resp.read())

            return HoloResponse(data)
