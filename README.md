# Article Feeds

Get articles from tech-blog's RSS feeds. The module is using feedparser as dependency.

Blog list:

- AWS blog (argument: topic)
- Comparitech
- DataHen
- Dev Community
- DZone (argument: category)
- Hashnode (argument: tag)
- Medium (argument: publication, tag)
- Toptal Blog
- Uber Development Blog

List: (spreadsheet)[https://docs.google.com/spreadsheets/d/1gM8kfnr-uu2-Li5S4ts5cFgx0APqJSJRCW3i5VWjFmk/view]

## Installation

Clone or download repository and save to working directory:

```bash
git clone https://github.com/tesserakh/articlefeeds.git
```

## Usage

AWS blog and Hashnode can use topic or tag as an input:


```python
import articlefeeds
import json

aws_topics = ["storage", "database"]
for topic in aws_topics:
    naming = topic.lower().replace(" ", "-")
    feed = articlefeeds.Aws(topic=topic).parse()
    filename = articlefeeds.create_filename(topic, prefix="aws")
    filepath = articlefeeds.create_storage_path(filename, path="data")
    with open(filepath, "w") as fout:
        json.dump(feed.feed, fout)
```

Medium can use a publication name, a tag, or both (a tag under certain publication) as argument:

```python
import articlefeeds
import json

medium_pubs = [
    {"publication": "airbnb-engineering", "tag": None},
    {"publication": "Lyft Engineering", "tag": "Data"},
    {"publication": "medium engineering"},
    {"publication": None, "tag": "web scraping"},
    {"tag": "python"},
]
for pub in medium_pubs:
    feed = articlefeeds.Medium(**pub).parse()
    filename = articlefeeds.create_filename(pub, prefix="medium")
    filepath = articlefeeds.create_storage_path(filename, path="data")
    with open(filepath, "w") as fout:
        json.dump(feed.feed, fout)
```

Others are need to manually filter using given tags:

```python
import articlefeeds
import json

def fetch(tags, feeds):
    food = []
    for tag in tags:
        for i, feed in enumerate(feeds):
            avail_tags = feed.get("tags")
            if avail_tags is not None:
                avail_tags = [tag.lower() for tag in avail_tags]
                if tag.lower() in avail_tags:
                    food.append(feed)
                    del feeds[i]
    return food

toptal_tags = [
    "artificial-intelligence",
    "big-data",
    "data-science",
    "api-development",
    "database",
    "json",
    "r",
    "python",
]
toptal_feeds = articlefeeds.Toptal().parse()
toptal_filter = fetch(toptal_tags, toptal_feeds.feed)

toptal_filepath = articlefeeds.create_storage_path("toptal.json", path="data")
with open(toptal_filepath, "w") as fout:
    json.dump(toptal_filter, fout)
```

Sample result using tag "python" for Medium blog:

```json
[
    {
        "title": "Let’s Practice Python in AWS",
        "author": "Cristin Jenkins",
        "link": "https://medium.com/@cristinj/lets-practice-python-in-aws-ca27379d786c",
        "published": "2023-06-19 14:10:37",
        "tags":
        [
            "aws",
            "linux",
            "github",
            "cloud9",
            "python"
        ],
        "source": "Python on Medium"
    },
    ...
]
```

Published is in UTC/GMT.