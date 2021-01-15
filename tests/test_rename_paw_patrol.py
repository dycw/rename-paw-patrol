from typing import Callable
from typing import cast
from typing import TypeVar

from pytest import mark

from main import clean_name
from main import PATTERN_CLEAN


T = TypeVar("T")


@cast(
    Callable[[T], T],
    mark.parametrize(
        "old, new",
        [
            (
                "PAW.Patrol.S01E23.Pups.and.the.Ghost.Pirate.720p.WEBRip.x264.AAC.mp4",
                "Paw Patrol S01E23 Pups And The Ghost Pirate.mp4",
            ),
            (
                "Paw.patrol.S03E12.pups.save.the.paw.patroller.eng.1080p.mkv",
                "Paw Patrol S03E12 Pups Save The Paw Patroller.mkv",
            ),
            (
                "PAW.Patrol.S03E25.Tracker.Joins.the.Pups!.1080p.WEBRip.x264.mkv",
                "Paw Patrol S03E25 Tracker Joins The Pups!.mkv",
            ),
            (
                "Paw.Patrol.S04E01.Pups.Save.A.Blimp.1080p.WEB-DL.AAC2.0.H.264.mkv",
                "Paw Patrol S04E01 Pups Save A Blimp.mkv",
            ),
            (
                "Paw.Patrol.S04E13.Pups.Save.The.Carnival.1080p.WEB-DL.AAC.2.0.H264.mkv",  # noqa: E501
                "Paw Patrol S04E13 Pups Save The Carnival.mkv",
            ),
            (
                "PAW.Patrol.S04E16.Mission.PAW.Pups.Save.The.Royal.Throne.1080p.NICK.WEBRip.AAC2.0.x264-RTN.mkv",  # noqa: E501
                "Paw Patrol S04E16 Mission Paw Pups Save The Royal Throne.mkv",
            ),
            (
                "PAW.Patrol.S04E32.Sea.Patrol.Pirate.Pups.to.the.Rescue.1080p.NICK.WEB-DL.AAC2.0.x264-RTN.mkv",  # noqa: E501
                "Paw Patrol S04E32 Sea Patrol Pirate Pups To The Rescue.mkv",
            ),
            (
                "PAW.Patrol.S04E37.Pups.Save.the.Runaway.Turtles.1080p.mkv",
                "Paw Patrol S04E37 Pups Save The Runaway Turtles.mkv",
            ),
        ],
    ),
)
def test_clean_name(old: str, new: str) -> None:
    assert clean_name(old) == new
    assert PATTERN_CLEAN.search(new)
