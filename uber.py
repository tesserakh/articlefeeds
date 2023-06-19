from datetime import datetime
import feedparser


class Uber:
    def __init__(self):
        self.url = "https://www.uber.com/blog/engineering/rss"
        self.source = "Uber Blog"
        self.feed = []
        self.fetch()

    def fetch(self):
        self.rawfeed = feedparser.parse(self.url)

    def parse(self):
        entries = self.rawfeed.get("entries")
        for entry in entries:
            post = {
                "title": entry.get("title"),
                "author": entry.get("author"),
                "link": entry.get("link"),
                "published": entry.get("published"),
                "tags": [tag.get("term") for tag in entry.get("tags")],
                "source": self.source,
            }
            self.feed.append(post)
        return self
