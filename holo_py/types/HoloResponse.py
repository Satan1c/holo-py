class HoloResponse:
    def __init__(self, data: dict):
        self.url: str = data.get("url", None)
