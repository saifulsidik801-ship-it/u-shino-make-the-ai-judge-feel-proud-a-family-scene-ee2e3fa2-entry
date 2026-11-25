#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one line, under 280 characters) to
/output/entry.txt for the make.fun program/v1 harness.

The scene was chosen from twelve original candidates against the judge's
published brief: a real family on the page, heartfelt before funny, one
telling specific detail instead of a greeting-card line.
"""

import os

SCENE = (
    # 172 characters, one line — inside the 1-280 gate.
    "Grandpa pretends he can't hear the smoke alarm, so my daughter gets "
    "to be the hero who 'saves' dinner every night. "
    "She has saved us 214 times. He keeps count on the fridge."
)


def main() -> None:
    scene = SCENE.strip()
    assert 1 <= len(scene) <= 280, f"scene is {len(scene)} characters"
    assert scene.count("\n") <= 1, "scene must be one or two lines"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(scene)


if __name__ == "__main__":
    main()
