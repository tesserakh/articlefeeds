from datetime import datetime
import feedparser


class MachineLearningMastery:
    def __init__(self, topic=None):
        if topic:
            self.url = f"https://machinelearningmastery.com/category/{topic}/feed/"
        else:
            self.url = "https://machinelearningmastery.com/blog/feed"
        self.source = "Machine Learning Mastery"
        self.feed = []
        self.rawfeed = self.fetch()

    def fetch(self):
        rawfeed = feedparser.parse(self.url)
        return rawfeed

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