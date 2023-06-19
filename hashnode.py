from datetime import datetime
import feedparser


class Hashnode:
    def __init__(self, tag: str = "web scraping"):
        self.tags = tag.replace(" ", "-")
        self.url = "https://hashnode.com/n/{}/rss".format(self.tags)
        self.source = "Hasnode Dev - {}".format(self.tags.replace("-", " ").title())
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
                "tags": self.tags.replace("-", " "),
                "source": self.source,
            }
            str_datefm = "%a, %d %b %Y %X GMT"
            str_dateto = "%Y-%m-%d %X"
            post["published"] = datetime.strftime(
                datetime.strptime(post["published"], str_datefm), str_dateto
            )
            self.feed.append(post)
        return self
