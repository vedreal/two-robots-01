"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line: a robot that rehearsed the ride 4,000 times in simulation
and still has nothing to say. Machine logic (simulation, rehearsal)
showing through the politeness; the awkwardness is the whole joke.
"""

import os

ENTRY = "I rehearsed this ride 4,000 times in simulation. I still have nothing to say to you."


def output_path():
    """Return the path of entry.txt for this run."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    """Write the entry line to entry.txt, creating the folder if needed."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
