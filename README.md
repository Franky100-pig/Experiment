# Experiment

> A daily-commit lab: small runnable code experiments **and** a reflection
> journal + skills about how I use LLMs.

Two halves, one habit. Every day I make at least one meaningful commit: either
a code experiment, a reflection note, or a skill. The goal is a real GitHub
streak plus a searchable personal knowledge base — not heroic projects.

## 1. Code experiments

```bash
python3 new_exp.py "Bouncing ball with pygame"
```

Creates `experiments/YYYY-MM-DD_slug/` with a runnable `main.py` + `README.md`,
and appends to [INDEX.md](INDEX.md).

## 2. Reflection notes & skills

```bash
python3 new_note.py "Why I prefer WorkBuddy for writing"
```

Creates `reflect/journal/YYYY-MM-DD_slug.md` and appends to the journal index
in [reflect/README.md](reflect/README.md). Author reusable LLM / agent skills
under [reflect/skills/](reflect/skills/) (start from its `_template/`).

## Layout

```
Experiment/
├── new_exp.py           # scaffold a code experiment
├── new_note.py          # scaffold a reflection note
├── INDEX.md             # table of code experiments
├── experiments/
│   └── YYYY-MM-DD_slug/{main.py, README.md}
└── reflect/
    ├── README.md        # journal index
    ├── journal/         # dated reflection notes
    └── skills/          # reusable LLM/agent skills (SKILL.md)
```

## Rules I keep (loose)

- One commit per day minimum; more if inspired.
- Code experiments: zero/few deps so they run anywhere (CI runs them).
- Reflection notes / skills: plain markdown, no build needed.
- Every `experiments/*/main.py` should run with `python3 main.py`.

## Index

- Code experiments: [INDEX.md](INDEX.md)
- Reflection journal: [reflect/README.md](reflect/README.md)
