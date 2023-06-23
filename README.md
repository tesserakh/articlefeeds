# Article Feeds

Get articles from tech-blog's RSS feeds. The library is using [feedparser](https://github.com/kurtmckee/feedparser) as dependency.

Blog list:

| Blog                        | Object (class)    | Argument   | Mandatory? |
|-----------------------------|-------------------|------------|:----------:|
| AWS Blog                    | `Aws()`           | `topic`    | Yes        |
| Microsoft Azure Blog        | `Azure()`         | `category` | No         |
| Comparitech                 | `Comparitech()`   | -          | -          |
| DataHen                     | `DataHen()`       | -          | -          |
| Dev Community               | `Devto()`         | -          | -          |
| DZone                       | `Dzone()`         | `category` | No         |
| Hashnode                    | `Hashnode()`      | `tag`      | Yes        |
| Machine Learning Mastery    | `MachineLearningMastery()` | `category` | No |
| Medium                      | `Medium()`        | `publication`, `tag` | Yes (either) |
| Salesforce Engineering Blog | `Salesforce()`    | -          | -          |
| Software Engineering Daily  | `SoftwareEngDaily()` | `category` | No      |
| Toptal Blog                 | `Toptal()`        | -          | -          |
| Uber Development Blog       | `Uber()`          | -          | -          |

Listing on progress ([spreadsheet](https://docs.google.com/spreadsheets/d/1gM8kfnr-uu2-Li5S4ts5cFgx0APqJSJRCW3i5VWjFmk/view))

## Installation

Clone or download repository and save to working directory:

```bash
git clone https://github.com/tesserakh/articlefeeds.git
```

## Usage

Each blog has its own `BlogFeed` object which will pull the XML file from its website. When executed, it will give us raw XML structured by feedparser.

```python
from articlefeeds import Azure

azure = Azure()
print(azure.rawfeed)
```

In order to make it simpler and ready to use, leave only the fields needed, `parse()` method is provided for this work. The result will store in `feed`.

```python
azure.parse()
print(azure.feed)
```

For some blogs, arguments can be used to filter posts according to category or tag. Others even require using tag.

```python
from articlefeeds import Aws

aws = Aws("database").parse()
print(aws.feed)
```

### More Example

AWS blog, Azure blog, Hashnode, DZone, etc. can use category, tag, or topic as an input. See blog list table for detail. Below is sample for AWS blog:


```python
import articlefeeds
import json

aws_topics = ["storage", "database"]
for topic in aws_topics:
    feed = articlefeeds.Aws(topic=topic).parse()
    filename = articlefeeds.create_filename(topic.lower(), prefix="aws")
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

### Result

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