# reflect/ — LLM journal & skills

The *non-code* half of the repo: a running reflection on how I actually use
LLMs, plus reusable **skills** (prompt / agent workflows) I author.

It exists so that on days I don't write code, I can still make a meaningful
daily commit — a reflection note or a skill.

## Layout

```
reflect/
├── README.md              # this file (journal index lives below)
├── journal/               # dated reflection notes (markdown)
│   └── YYYY-MM-DD_slug.md
└── skills/                # reusable LLM/agent skills (SKILL.md format)
    ├── README.md
    └── _template/         # clone this to start a new skill
        └── SKILL.md
```

## Add a reflection note

```bash
python3 new_note.py "Why I prefer WorkBuddy for writing"
```

This drops `reflect/journal/YYYY-MM-DD_slug.md` and appends a row to the
journal index table below.

## Journal index

| Date | Note | Path |
|------|------|------|
| 2026-09-29 | Why I keep several LLMs around | [reflect/journal/2026-09-29_why_i_use_multiple_llms](reflect/journal/2026-09-29_why_i_use_multiple_llms) |
