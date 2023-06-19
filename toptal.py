from datetime import datetime
import feedparser


class Toptal:
    def __init__(self):
        self.url = "https://www.toptal.com/developers/blog.rss"
        self.source = "Toptal Blog"
        self.feed = []
        self.fetch()

    def fetch(self):
        self.rawfeed = feedparser.parse(self.url)

    def parse(self):
        entries = self.rawfeed.get("entries")
        for entry in entries:
            post = {
                "title": entry.get("title"),
                "author": entry.get("author").split(",")[0],
                "link": entry.get("link"),
                "published": entry.get("published"),
                "tags": [entry.get("link").split("/")[-2].replace("-", " ")],
                "source": self.source,
            }
            str_datefm = "%a, %d %b %Y %X %z"
            str_dateto = "%Y-%m-%d %X"
            post["published"] = datetime.strftime(
                datetime.strptime(post["published"], str_datefm), str_dateto
            )
            self.feed.append(post)
        return self
