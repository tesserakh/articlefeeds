from datetime import datetime
import feedparser


class Medium:
    def __init__(self, tag: str = None, publication: str = None, **kwargs):
        source_text = "{} on Medium"
        if publication is not None:
            publication = publication.replace("-", " ").title()
            self.source = source_text.format(publication)
            publication = publication.lower().replace(" ", "-")
            if tag is not None:
                tag = tag.lower().replace(" ", "-")
                self.url = "https://medium.com/feed/{}/tagged/{}".format(
                    publication, tag
                )
            else:
                self.url = "https://medium.com/feed/{}".format(publication)
        else:
            tag = tag.replace("-", " ").title()
            self.source = source_text.format(tag)
            tag = tag.lower().replace(" ", "-")
            self.url = "https://medium.com/feed/tag/{}".format(tag)
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
                "link": entry.get("link").split("?")[0],
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
