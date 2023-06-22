from datetime import datetime
import feedparser


class Dzone:
    def __init__(self, category):
        self.url = "https://feeds.dzone.com/{}".format(category)
        self.source = "DZone - {}".format(category.title())
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
            str_datefm = "%a, %d %b %Y %X GMT"
            str_dateto = "%Y-%m-%d %X"
            post["published"] = datetime.strftime(
                datetime.strptime(post["published"], str_datefm), str_dateto
            )
            self.feed.append(post)
        return self