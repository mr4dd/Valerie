import feedparser
import json


class News:
    def __init__(self, feed):
        self.feed = feed 

    def extract_headlines(self):
        return [f.title for f in feedparser.parse(self.feed).entries]

    def extract_text(self):
        return [f.description for f in feedparser.parse(self.feed).entries]

    def extract_all(self):
        titles = extract_headlines(self.feed)
        descriptions = extract_text(self.feed)

        len_items = len(titles)
        i = 0

        items = []

        while i < len_items:
            items[i] = {'headline': {titles[i]}, 'article': {descriptions[i]}}

        return json.dumps(items)


