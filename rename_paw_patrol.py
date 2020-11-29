#!/usr/bin/env python3
from __future__ import annotations


__version__ = "0.0.1"

from pathlib import Path
from re import search
from string import capwords
from typing import Iterator


def yield_files() -> Iterator[Path]:
    for p in Path("/data/derek/Paw Patrol/").glob("**/*"):
        if p.is_file() and not search("Torrent", p.name):
            yield p


def clean_name(name: str) -> str:
    if (
        match := search(
            r"(?:paw\.patrols)?"
            r"\.?"
            r"s(\d{2})e(\d{2})"
            r"\.?"
            r"([\w\.\'-]+)"
            r"(?:[\d+p|.\d+p.web-dl.aac.2.0.h.?264])?"
            r"\.?"
            r"(mp4|mkv)",
            name,
        )
    ) is not None:
        season, ep_no, ep_name, ext = match.groups()
        ep_name = capwords(ep_name.replace(".", " "))
        return f"S{season}E{ep_no} - {ep_name}.{ext}"
    else:
        raise ValueError(f"Could not match the following:\n    {name}")


def process_file(path: Path) -> None:
    old_name = path.name
    if search(r"S\d{2}E\d{2} - [\s\w\'\-]+\.[mp4|mkv]", old_name):
        return
    else:
        print(f"Needs processing:\n    {old_name}")
        new_name = clean_name(old_name)
        while True:
            ans = input(  # noqa: S322
                f"Rename as follows?\n    {new_name}\n'y', 'n'",
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
