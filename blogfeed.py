import feedparser
import time
from urllib.parse import urljoin


class BlogFeed:
    """Superclass"""

    def __init__(self, url, name):
        self.url = url
        self.source = name
        self.feed = []

    def fetch(self):
        print("GET", self.url)
        rawfeed = feedparser.parse(self.url)
        return rawfeed

    def parse(self):
        entries = self.rawfeed.get("entries")
        for entry in entries:
            post = {
                "title": entry.get("title"),
                "author": entry.get("author"),
                "link": entry.get("link"),
                "published": entry.get("published_parsed"),
                "tags": entry.get("tags"),
                "source": self.source,
            }
            if post["tags"] is not None:
                post["tags"] = [tag.get("term") for tag in post["tags"]]
            post["published"] = time.strftime("%Y-%m-%d %X", post["published"])
            self.feed.append(post)
        return self


class Aws(BlogFeed):
    def __init__(self, topic: str):
        BlogFeed.__init__(
            self, url=f"https://aws.amazon.com/blogs/{topic}/feed/", name="AWS Blog"
        )
        self.rawfeed = self.fetch()


class Azure(BlogFeed):
    def __init__(self, category=None):
        BlogFeed.__init__(
            self,
            url="https://azure.microsoft.com",
            name="Microsoft Azure",
        )
        if category:
            self.url = urljoin(self.url, f"/en-us/blog/category/{category}/feed/")
        else:
            self.url = urljoin(self.url, "/en-us/blog/feed/")
        self.rawfeed = self.fetch()


class Comparitech(BlogFeed):
    def __init__(self, tag=None):
        if tag:
            tag = tag.replace(" ", "-")
            url = f"https://www.comparitech.com/blog/{tag}/feed/"
        else:
            url = "https://www.comparitech.com/blog/feed/"
        BlogFeed.__init__(self, url=url, name="Comparitech Blog")
        self.rawfeed = self.fetch()


class DataHen(BlogFeed):
    def __init__(self):
        BlogFeed.__init__(
            self,
            url="https://www.datahen.com/blog/rss/",
            name="DataHen Blog",
        )
        self.rawfeed = self.fetch()


class Devto(BlogFeed):
    # not all hashtag has feed https://dev.to/tags
    def __init__(self, tag: str = ""):
        BlogFeed.__init__(
            self,
            url=f"https://dev.to/feed/{tag}",
            name="Dev Community",
        )
        self.rawfeed = self.fetch()


class Dzone(BlogFeed):
    def __init__(self, category=None):
        if category:
            name = f"DZone - {category.title()}"
            url = f"https://feeds.dzone.com/{category}"
        else:
            name = "DZone"
            url = f"https://feeds.dzone.com/home"
        BlogFeed.__init__(self, url=url, name=name)
        self.rawfeed = self.fetch()


class MachineLearningMastery(BlogFeed):
    def __init__(self, category=None):
        BlogFeed.__init__(
            self,
            url="https://machinelearningmastery.com",
            name="Machine Learning Mastery",
        )
        if category:
            self.url = urljoin(self.url, f"/category/{category}/feed/")
        else:
            self.url = urljoin(self.url, "/feed/")
        self.rawfeed = self.fetch()


class Salesforce(BlogFeed):
    def __init__(self):
        BlogFeed.__init__(
            self,
            url="https://engineering.salesforce.com/feed",
            name="Salesforce Engineering",
        )
        self.rawfeed = self.fetch()


class SoftwareEngDaily(BlogFeed):
    def __init__(self, category=None):
        BlogFeed.__init__(
            self,
            url="https://softwareengineeringdaily.com",
            name="Software Engineering Daily",
        )
        if category:
            self.url = urljoin(self.url, f"/category/{category}/feed/")
        else:
            self.url = urljoin(self.url, "/feed/")
        self.rawfeed = self.fetch()


class Uber(BlogFeed):
    def __init__(self):
        BlogFeed.__init__(
            self,
            url="https://www.uber.com/blog/engineering/rss",
            name="Uber Blog",
        )
        self.rawfeed = self.fetch()
