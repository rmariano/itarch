from datetime import datetime
from pathlib import Path

_TEMPLATE = """+++
title = "{title}"
slug = "{slug}"
date = {date}
[taxonomies]
tags = {tags} 
+++
"""
import re

def remove_non_alphanumeric(input_string):
    return re.sub(r'[^a-zA-Z0-9\-]', '', input_string)


def _slug(title: str) -> str:
    slug = title.lower().replace(" ", "-")
    return remove_non_alphanumeric(slug)


def _today() -> str:
    local_timezone = datetime.now().astimezone().tzinfo
    return datetime.now(local_timezone).isoformat()


def _format_tags(tags: list[str]) -> str:
    formatted_tags = [f"'{tag}'" for tag in tags]
    return f"[{', '.join(formatted_tags)}]"


def new_post() -> None:
    title = input("Title: ")
    slug = _slug(title)
    date = _today()
    tags = input("Tags: ").split()
    new_file = Path("content") / f"{slug}.md"
    with open(new_file, "w") as f:
        f.write(_TEMPLATE.format(title=title, slug=slug, date=date, tags=_format_tags(tags)))
    print(f"New post created at {new_file.name}")


if __name__ == "__main__":
    new_post()
