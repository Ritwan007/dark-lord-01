#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one 100-word monologue to /output/entry.txt for the make.fun
competition u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

The speaker is Lord Veylan, keeper of the Hollow Gate: a specific villain
with a history (the skulls, the chair that eats guests, ink gone since
1347) and a scheme (river toll doubles, north road stays his, the king
kneels by dawn). His tiredness is never announced; it lives in the
deflections, the pauses and the lost thread ("hold on. Where was I?").
"""

import os

MONOLOGUE = (
    "Come in. Mind the step \u2014 the third one bites. I am Lord Veylan, "
    "keeper of the Hollow Gate, and yes, the skulls are real. Sit. No, not "
    "there. That chair... eats guests. Right. You came to beg, or to "
    "bargain? Same thing, by the third hour. My terms are simple: the river "
    "toll doubles, the north road stays mine, and your king kneels by dawn. "
    "Refuse, and the fog takes your fields. Accept, and \u2014 hold on. "
    "Where was I? Ah. The kneeling. Sign here. In blood, please. The ink "
    "ran out... in 1347. Do try to keep up."
)


def main() -> None:
    text = MONOLOGUE
    words = text.split()
    assert 1 <= len(text) <= 600, f"gate: {len(text)} chars, must be 1-600"
    assert text.strip(), "gate: entry must not be only whitespace"
    assert len(words) == 100, f"expected 100 words, got {len(words)}"
    # Judge criterion 2: the tiredness must be felt, never announced, so
    # the monologue must not plainly state weariness in any form.
    lowered = text.lower()
    for banned in ("tired", "weary", "weariness", "exhausted", "sleepy"):
        assert banned not in lowered, f"announced tiredness: {banned}"
    assert not text.endswith("\n"), "no trailing newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
