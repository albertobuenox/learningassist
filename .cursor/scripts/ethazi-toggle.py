#!/usr/bin/env python3
"""Set alwaysApply on .cursor/rules/ethazi-*.mdc. Usage: ethazi-toggle.py on|off"""

import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or sys.argv[1] not in ("on", "off"):
    sys.exit("usage: ethazi-toggle.py on|off")

value = "true" if sys.argv[1] == "on" else "false"
rules = sorted(Path(__file__).resolve().parents[1].joinpath("rules").glob("ethazi-*.mdc"))
if not rules:
    sys.exit("no ethazi rules found")

pattern = re.compile(r"(?m)^alwaysApply:\s*(true|false)\s*$")
for path in rules:
    text = path.read_text()
    if not text.startswith("---"):
        sys.exit(f"{path.name}: missing frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        sys.exit(f"{path.name}: unclosed frontmatter")
    front, rest = text[:end], text[end:]
    if not pattern.search(front):
        sys.exit(f"{path.name}: no alwaysApply in frontmatter")
    new_front, count = pattern.subn(f"alwaysApply: {value}", front, count=1)
    if count != 1:
        sys.exit(f"{path.name}: expected one alwaysApply")
    path.write_text(new_front + rest)
    print(f"{path.name}: alwaysApply: {value}")
