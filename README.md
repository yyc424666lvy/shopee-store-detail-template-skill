# Shopee Store Detail Template Skill

A WorkBuddy Skill for Shopee Philippines cross-listing. Give WorkBuddy one generic product detail plus one or more store IDs; it applies the corresponding canonical store template while preserving product facts.

## Supported stores

- Cross-border: `3pf01`–`3pf11`
- Local: `sp01`–`sp17`
- Total: 28 canonical store templates

## What it does

- Replaces generic opening/closing copy with the target store's exact copy
- Applies each store's exact Specification / Features / Package structure
- Handles stores with no Package slot or no Features slot
- Handles special `【Label：Value` Specification formatting
- Supports one-store and batch cross-listing requests
- Preserves product facts and feature wording by default

## Install on Windows / WorkBuddy

### Option A — clone then install

```powershell
git clone https://github.com/yyc424666lvy/shopee-store-detail-template-skill.git
cd shopee-store-detail-template-skill
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

### Option B — manual install

Copy the whole repository folder to:

```text
%USERPROFILE%\.workbuddy\skills\shopee-store-detail-template
```

Then restart WorkBuddy or reload Skills and check with `/skills`.

## Usage examples

```text
把下面这份产品详情替换到 sp06
```

```text
这份详情交叉上架到 sp07、sp09、3pf01
```

```text
用 3pf05 的店铺模板替换这份详情，产品内容不要改
```

## Update

If you installed from a cloned repository:

```powershell
git pull
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

## Uninstall

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\uninstall.ps1
```

## Repository structure

```text
shopee-store-detail-template-skill/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── LICENSE
├── install.ps1
├── uninstall.ps1
├── references/
│   ├── store-index.md
│   ├── source-usage-guide.md
│   ├── product-input-example.md
│   ├── golden-examples-sp06-sp17.md
│   └── stores/
│       ├── 3pf01.md ... 3pf11.md
│       └── sp01.md ... sp17.md
├── scripts/
│   └── doctor.py
└── tests/
    └── test_skill.py
```

## Maintenance rule

Store files are canonical. When a store template changes, edit only that store's file and update tests/examples if needed. Do not silently rewrite product content rules.

## Source cleanup applied in v1.0.0

The supplied master template contained `sp03` twice. This package keeps the first `sp03` occurrence as the canonical definition. The duplicate did not introduce a distinct business rule.

## License

MIT for the Skill code and packaging. Store-specific business copy/templates remain your own operational content.

