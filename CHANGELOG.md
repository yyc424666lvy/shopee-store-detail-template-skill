# Changelog

## 1.1.0 - 2026-10-30

- **Output format hardened.** Deliverables are plain `.txt` (UTF-8 with BOM, CRLF line endings), never Markdown. One file per store, body only: line 1 is the store's opening block, the last line is its closing block. Warnings and self-check results go in the chat reply, not the file.
- **Formatted-input contract added (rule 11).** Product Description items are `N.Label: value` (no space after the dot); Feature items are one line each as `【ALL-CAPS LABEL】：sentence`.
- **Non-canonical input normalization added (rule 12).** Unnumbered items get sequential numbers, mixed full-width/half-width colons normalize to ASCII `: `, `-`-prefixed Feature sentences keep their wording without inventing labels, and `Packing List: X × 1` passes through verbatim.
- **Desktop delivery step added to the workflow.** The finished `.txt` is written to the workspace, verified with a per-line `repr()` dump so leading/trailing spaces and emoji survive, then copied to the user's real Desktop.
- **3pf09 clarified.** The `[零宽字符行]` markers exist only in the originally supplied template; finished output uses ordinary blank lines and writes no U+FEFF.
- **Scope narrowed to the format stage only.** This package converts an existing generic product detail into store-specific copy. It does not fetch, scrape, or log in to any external product source; anything upstream of the generic detail is out of scope.

## 1.0.0 - 2026-08-26

- Initial WorkBuddy Skill package.
- Added 28 canonical store templates: 3pf01-sp17.
- Added batch cross-listing workflow and exact-format self-check rules.
- Added source/golden examples and Windows installer/uninstaller.
- De-duplicated repeated sp03 source definition by retaining the first canonical occurrence.
