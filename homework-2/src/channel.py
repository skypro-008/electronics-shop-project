
import json
from src.youtube_api import YoutubeAPI

class Channel:
    def __init__(self, id, title, description, link, subscribers, videos, views):
        self.id = id
        self.title = title
        self.description = description
        self.link = link
        self.subscribers = subscribers
        self.videos = videos
        self.views = views

    @classmethod
    def get_service(cls):
        return YoutubeAPI()

    def to_json(self):
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "link": self.link,
            "subscribers": self.subscribers,
            "videos": self.videos,
            "views": self.views
        }
        with open(f"{self.id}.json", "w") as file:
            json.dump(data, file)
