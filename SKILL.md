---
name: shopee-store-detail-template
version: 1.1.0
description: Convert one generic Shopee Philippines product detail into one or more store-specific listing descriptions using the canonical 28-store template library (3pf01-3pf11, sp01-sp17). Use when the user asks to replace, convert, apply, cross-list, or batch-generate product details for named store IDs. Preserve product facts and each store's exact formatting; do not rewrite or optimize product content unless explicitly requested.
agent_created: true
triggers: ["替换到", "店铺模板", "详情模板", "交叉上架", "批量替换", "3pf01", "sp01", "Shopee详情"]
---

# Shopee Store Detail Template

## Purpose

Turn one generic product detail into store-specific finished descriptions for Shopee Philippines cross-listing. The product information is the source of truth; the selected store file is the formatting and store-copy source of truth.

## Hard rules

1. Never change product facts, claims, quantities, materials, sizes, package contents, feature wording, or item order unless the user explicitly asks for content editing.
2. Never invent a store ID. Supported IDs are exactly `3pf01`–`3pf11` and `sp01`–`sp17`.
3. For every requested store, read only its canonical file at `references/stores/<store_id>.md` before producing output.
4. Preserve the store template's opening block, closing block, emoji, punctuation, capitalization, leading spaces, slot titles, and documented blank-line behavior exactly.
5. Discard the input's generic opening hook and generic Note block when the selected store rule says to replace them.
6. Package Included handling, Features presence/absence, special Specification formatting, and slot order are controlled by the selected store file. Store-specific rules override global defaults.
7. Do not translate to Tagalog. Final listing content is English unless the source product content itself contains another language and the user asks for translation.
8. Do not merge output for different stores. One output file per store. Communicate the store ID in the **file name** and in the chat reply — never inside the copyable body (see rule 10).
9. **Output format is plain text (`.txt`), never Markdown.** The user works on Windows and pastes straight into the Shopee backend; `.md` files carry backticks, tables, and code fences that get in the way of a clean Ctrl+A → Ctrl+C. Do not write `.md`, `.docx`, or HTML deliverables for this skill.
10. **The `.txt` file contains the finished product-description body and nothing else.** No store-ID label, no source/date header, no table, no code fence, no self-check list, no notes. The file must be copy-ready on open: line 1 is the store's opening block, the last line is the store's closing block. Put every warning, ambiguity, or self-check result in the chat reply instead.

11. **Generic-detail item formatting is fixed** (read `references/product-input-example.md` before writing, do not improvise):
    Product Description items are `N.Name: value` / `N.Weight: value` — number, **no space** after the dot, label then a straight-ASCII `: `. Package Included is the last numbered item, written `1PCS * Item`.
    Feature items are **one line each**: `【ALL-CAPS LABEL】：sentence` — the `【】` are full-width and the colon after `】` is full-width `：`. Never put the label on its own line.
12. **Non-canonical input variants (seen 2026-10-16, ❄️🛡️-style raw paste)** — normalize to the rule-11 fixed format; never improvise a third style:
    - Product Description items arriving **unnumbered** (e.g. `Color:White`, `Material：Polypropylene`): number them sequentially in source order as `N.Label: value` — number, no space after the dot, straight-ASCII `: ` with exactly one space after the colon. Values stay verbatim.
    - **Mixed/full-width colons** in the input (`Material：Polypropylene` vs `Color:White`) normalize to ASCII `: `; the label text and value are not rewritten.
    - Feature items arriving as **`-`-prefixed plain sentences** (no `【LABEL】`): strip the `-` bullet marker, keep one sentence per line verbatim. **Never invent `【ALL-CAPS LABEL】` headers** that the source does not contain — that would add content, violating rule 1.
    - `Packing List: X × 1` style package lines pass through verbatim into the store's Package slot (do not rewrite to `1PCS * X` unless the source already uses that form).
    - Tell the user in the chat reply which normalizations were applied; product facts themselves must remain untouched.

## Workflow

1. Parse requested store IDs from the user's message. Normalize case only; do not guess malformed IDs.
2. Parse the generic product detail into:
   - generic opening hook
   - Product Description / specification items
   - Package Included item, if present
   - Feature items
   - generic Note block
3. Read `references/stores/<store_id>.md` for each requested store.
4. Apply that store's exact replacement rules and skeleton.
5. Self-check each result before returning it.
6. Return only the finished store outputs plus concise warnings for unsupported/missing input fields.
7. **Save the deliverable and copy it to the user's Desktop before replying.** Write the finished copy into the workspace as a `.txt` file, then immediately `cp` it to `D:\桌面\Desktop\`. This user's real Desktop is the Lenovo Super Desktop redirect at `D:\桌面\Desktop`, NOT the C: drive Desktop. Do this unprompted — the user has had to ask twice (2026-09-04, 2026-09-10). Then call present_files and state the desktop path in the reply.
   - File name: `<store_id> <店铺名>_详情.txt` (e.g. `sp16 Lvy's HIKE Store_详情.txt`). For a batch, one file per store — never a single combined file.
   - Encoding **UTF-8 with BOM** (`utf-8-sig`), line endings **CRLF**. BOM keeps Chinese Windows Notepad from guessing the encoding wrong and garbling the emoji.
   - Writing the `.txt` must preserve leading spaces, trailing spaces, and full-width punctuation exactly. Do not let any editor or script strip them — verify with a line-by-line `repr()` dump before copying to the Desktop.

## Self-check gate

For every store, verify:

- opening and closing blocks match the canonical store file;
- store slot titles and formatting are exact;
- product facts remain unchanged;
- Package Included is either separated or retained exactly as that store requires;
- Features are included/omitted exactly as that store requires;
- original generic Note lines do not leak into stores that replace them;
- special `【Label：Value` formatting is used where required;
- no requested store is missing and no unrequested store is added;
- the deliverable is a `.txt` (not `.md`), one file per store, and contains the body only — line 1 is the opening block, last line is the closing block;
- leading/trailing spaces and emoji survived the write (confirm with a per-line `repr()` dump).

If any check fails, fix it before answering.

## Batch requests

For requests such as “替换到 sp06、sp07、3pf01”, process each store independently from the same source product detail. Never use one generated store output as the source for the next store.

## Input ambiguity

If a field cannot be safely separated (for example Package Included is absent or Product Description structure is malformed), preserve the user's original product text as much as possible and state the specific ambiguity. Do not fabricate missing product data.

## References

- Supported store list: `references/store-index.md`
- One store at a time: `references/stores/<store_id>.md`
- Input example: `references/product-input-example.md`
- Golden output examples: `references/golden-examples-sp06-sp17.md`
- Original usage rules: `references/source-usage-guide.md`
