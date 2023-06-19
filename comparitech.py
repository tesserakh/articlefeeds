from datetime import datetime
import feedparser


class Comparitech:
    def __init__(self, tag: str = "information-security"):
        tag = tag.replace(" ", "-")
        self.url = "https://www.comparitech.com/blog/{}/feed/".format(tag)
        self.source = "Comparitech Blog"
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
            str_datefm = "%a, %d %b %Y %X %z"
            str_dateto = "%Y-%m-%d %X"
            post["published"] = datetime.strftime(
                datetime.strptime(post["published"], str_datefm), str_dateto
            )
            self.feed.append(post)
        return self
