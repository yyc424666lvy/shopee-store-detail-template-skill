---
name: shopee-store-detail-template
version: 1.0.0
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
8. Do not merge output for different stores. Label each finished result with its store ID outside the copyable product-description body.

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

## Self-check gate

For every store, verify:

- opening and closing blocks match the canonical store file;
- store slot titles and formatting are exact;
- product facts remain unchanged;
- Package Included is either separated or retained exactly as that store requires;
- Features are included/omitted exactly as that store requires;
- original generic Note lines do not leak into stores that replace them;
- special `【Label：Value` formatting is used where required;
- no requested store is missing and no unrequested store is added.

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
