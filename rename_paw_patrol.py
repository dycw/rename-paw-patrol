#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path
from re import IGNORECASE
from re import search
from string import capwords
from typing import Iterator


__version__ = "0.0.1"


def yield_files() -> Iterator[Path]:
    for p in Path("/data/derek/Paw Patrol/").glob("**/*"):
        if p.is_file() and not search("Torrent", p.name):
            yield p


PATTERN_RENAME = re.compile(
    r"(?:Paw\.Patrol)?\.?s(\d{2})e(\d{2})\.([\w\.\'-]+?)(?:\.?\d+p(?:\.NICK)?\.WEB\-DL\.AAC\.?2\.0\.[Hx]\.?264(?:\-RTN)?)\.?(mp4|mkv)",  # noqa: E501
    flags=IGNORECASE,
)


def clean_name(name: str) -> str:
    if (match := PATTERN_RENAME.search(name)) is not None:
        season, ep_no, ep_name, ext = match.groups()
        ep_name = capwords(ep_name.replace(".", " "))
        return f"S{season}E{ep_no} - {ep_name}.{ext}"
    else:
        raise ValueError(f"Could not match the following:\n    {name}")


PATTERN_CLEAN = re.compile(r"S\d{2}E\d{2} - [\s\w\'\-]+\.[mp4|mkv]")


def process_file(path: Path) -> None:
    old_name = path.name
    if PATTERN_CLEAN.search(old_name):
        return
    else:
        print(f"Needs processing:\n    {old_name}")
        new_name = clean_name(old_name)
        while True:
            ans = input(  # noqa: S322
                f"Rename as follows? (y/n)\n    {new_name}\n>>> ",
            )
            if ans == "y":
                new_path = path.parent.joinpath(new_name)
                path.rename(new_path)
                return
            elif ans == "n":
                break


if __name__ == "__main__":
    for p in yield_files():
        process_file(p)
