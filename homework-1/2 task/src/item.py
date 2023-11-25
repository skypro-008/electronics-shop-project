# В src/channel.py

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


# class Item:
#     def __init__(self, id, name, price):
#         self._id = id
#         self._name = name
#         self._price = price
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 10:
#             self._name = value[:10]
#         else:
#             self._name = value
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         items = []
#         with open('src/items.csv', 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 item = cls(row['id'], row['name'], row['price'])
#                 items.append(item)
#         return items
#
#     @staticmethod
#     def string_to_number(string):
#         return int(string)