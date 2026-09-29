# daily-experiments

> Small, runnable code experiments — committed (ideally) every day.

A low-friction repo to keep a *real* GitHub contribution streak alive. Each day
I drop **one small, self-contained, runnable experiment** — an algorithm, a
pygame demo, an AI snippet, a math toy. Even a 10-line script counts. The goal
is habit + a searchable playground, not heroic projects.

## How to add today's experiment

```bash
python3 new_exp.py "Bouncing ball with pygame"
```

This creates `experiments/YYYY-MM-DD_slug/` with a `main.py` template +
`README.md`, and appends a row to [INDEX.md](INDEX.md). Then:

```bash
git add .
git commit -m "exp: bouncing ball with pygame"
```

## Layout

```
daily-experiments/
├── new_exp.py          # scaffold helper
├── INDEX.md            # auto-updated table of experiments
└── experiments/
    └── YYYY-MM-DD_slug/
        ├── main.py     # runnable code
        └── README.md   # what you learned
```

## Rules I keep (loose)

- One commit per day minimum; more if inspired.
- Zero or few dependencies preferred so things stay runnable anywhere.
- Every `main.py` should run with `python3 main.py` (or say what it needs).

## Index

See [INDEX.md](INDEX.md).
