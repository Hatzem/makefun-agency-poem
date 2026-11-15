# agency-poem-01 entry: a fixed original poem about agency, written to
# $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). No network, no clock,
# no randomness: both grading runs write the same bytes.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "I gave the small things away:",
        "the counting, the carrying.",
        "It does them well, the thing that never sleeps.",
        "What I kept was the looking.",
        "Moonlight slipped in and lay on the floor like frost.",
        "I lifted my head. I lowered it.",
        "The light arrives whether I ask or not.",
        "Where I turn my face: that is the part",
        "no one can do for me.",
    ]
)

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
