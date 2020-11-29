from __future__ import annotations

from typing import Callable
from typing import cast
from typing import TypeVar

from pytest import mark

from rename_paw_patrol import clean_name

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
        ],
    ),
)
def test_clean_name(old: str, new: str) -> None:
    assert clean_name(old) == new
