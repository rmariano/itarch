"""
Migrate single file to Markdown format
"""

import sys
import re
import subprocess
from dateutil.parser import parse as parse_date

from os.path import basename
from os import unlink

_METADATA_FORMAT = re.compile(r"^\.\.\s(?P<label>\w+)\:\s(?P<value>.*)")


def _get_post_metadata(filename: str) -> list[str]:
    content = []
    with open(filename, "r") as f:
        for line in f:
            if line.startswith(".."):
                content.append(line)
            else:
                break
    return content


def _convert_post_metadata(raw_metadata: list[str]) -> str:
    metadata = {}
    for line in raw_metadata:
        if (match := re.match(_METADATA_FORMAT, line)) is not None:
            data_dict = match.groupdict()
            metadata[data_dict["label"]] = data_dict["value"]
        else:
            print(line)

    metadata["tags"] = list(map(str.strip, metadata["tags"].split(",")))
    metadata["date"] = parse_date(metadata["date"]).isoformat()
    extra = []
    for key in ("link", "description"):
        if value := metadata[key]:
            extra.append(f'{key} = "{value}"')

    return f"""+++
title = "{metadata['title']}"
slug = "{metadata['slug']}"
date = {metadata['date']}
tags = {metadata['tags']}
{"\n".join(extra)}
+++
"""


def _convert_post_to_markdown(source_filename: str, target_filename: str) -> None:
    subprocess.check_call(["pandoc", source_filename, "-s", "-o", target_filename])


def _write_final_post_file(metadata: str, temp_filename: str, final_filename: str):
    with open(final_filename, "w+") as f, open(temp_filename, "r") as src:
        f.write(metadata)
        f.write("\n")
        f.write(src.read())


def main():
    filename = sys.argv[1]
    medatata = _convert_post_metadata(_get_post_metadata(filename))
    temp_filename = f"tmp_{basename(filename)}.md"
    _convert_post_to_markdown(filename, temp_filename)
    _write_final_post_file(medatata, temp_filename, filename.replace(".rst", ".md"))
    unlink(temp_filename)


if __name__ == "__main__":
    main()
