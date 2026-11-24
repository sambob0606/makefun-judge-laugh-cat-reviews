#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human entry.

Writes a single original one-line one-star review (<=200 chars) by a
house cat about its human to /output/entry.txt. Stdlib only; no network,
no reads outside the repo, fully deterministic.
"""

import os

LINE = (
    "One star. She feeds me at 6am sharp, then acts shocked when I "
    "scream at 5:59. I am not early. She is late."
)
# The joke: the cat's complaint is not that breakfast is late, it is that
# the human's clock is wrong. Setup ("feeds me at 6am sharp") fixes the
# human's rule; the scream at 5:59 shows the cat enforcing it a minute
# early; the sting ("I am not early. She is late.") flips the blame, so
# the review reveals more about the cat than the owner — the human is
# measured by cat standards, and by those standards she is the one who
# fails. Deadpan one-star-review shape, specific and recognisable (the
# food bowl, the morning feed), one sentence each, ends on its strongest
# beat ("She is late."), well under 200 chars, no trailing newline.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read what was written and re-check it: the grader runs the
    # program twice and gates the file, so a silent write failure must
    # never pass as a success.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry does not match the line"
    # Deterministic confirmation for the run log; the file itself stays
    # exactly the one line, no trailing newline.
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
