from __future__ import annotations

from typing import Callable
from typing import cast
from typing import TypeVar

from pytest import mark

from rename_paw_patrol import clean_name
from rename_paw_patrol import PATTERN_CLEAN

T = TypeVar("T")


@cast(
    Callable[[T], T],
    mark.parametrize(
        "old, new",
        [
            (
                "Paw.Patrol.S04E01.Pups.Save.A.Blimp.1080p.WEB-DL.AAC2.0.H.264.mkv",
                "S04E01 - Pups Save A Blimp.mkv",
            ),
            (
                "Paw.Patrol.S04E13.Pups.Save.The.Carnival.1080p.WEB-DL.AAC.2.0.H264.mkv",  # noqa: E501
                "S04E13 - Pups Save The Carnival.mkv",
            ),
            (
                "PAW.Patrol.S04E32.Sea.Patrol.Pirate.Pups.to.the.Rescue.1080p.NICK.WEB-DL.AAC2.0.x264-RTN.mkv",  # noqa: E501
                "S04E32 - Sea Patrol Pirate Pups To The Rescue.mkv",
            ),
        ],
    ),
)
def test_clean_name(old: str, new: str) -> None:
    assert clean_name(old) == new
    assert PATTERN_CLEAN.search(new)
