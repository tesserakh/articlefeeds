from datetime import datetime
import feedparser


class Devto:
    # not all hashtag has feed https://dev.to/tags
    def __init__(self, tag: str = ""):
        self.url = "https://dev.to/feed/{}".format(tag)
        self.source = "Dev Community"
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
                "tags": entry.get("tags"),
                "source": self.source,
            }
            if post["tags"] is not None:
                post["tags"] = [tag.get("term") for tag in post["tags"]]
            str_datefm = "%a, %d %b %Y %X %z"
            str_dateto = "%Y-%m-%d %X"
            post["published"] = datetime.strftime(
                datetime.strptime(post["published"], str_datefm), str_dateto
            )
            self.feed.append(post)
        return self
