#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
expected=[f"3pf{i:02d}" for i in range(1,12)]+[f"sp{i:02d}" for i in range(1,18)]
errors=[]
if not (ROOT/"SKILL.md").exists(): errors.append("SKILL.md missing")
store_files=list((ROOT/"references"/"stores").glob("*.md"))
actual=[p.stem for p in store_files]
for sid in expected:
    p=ROOT/"references"/"stores"/f"{sid}.md"
    if not p.exists(): errors.append(f"missing {sid}")
    elif not re.search(rf"^###\s+{re.escape(sid)}\b", p.read_text(encoding="utf-8"), re.M): errors.append(f"bad heading {sid}")
extra=[sid for sid in actual if sid not in expected]
if extra: errors.append("unexpected store files: "+", ".join(extra))
if len(actual) != len(set(actual)): errors.append("duplicate store IDs")
print(f"store_count={len(actual)}")
print(f"unique_store_count={len(set(actual))}")
print("status=PASS" if not errors else "status=FAIL")
for e in errors: print("error="+e)
sys.exit(1 if errors else 0)
