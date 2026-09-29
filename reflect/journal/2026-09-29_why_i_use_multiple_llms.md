# Why I keep several LLMs around

Date: 2026-09-29

A running note on how I actually split work across the models I pay attention
to. Not a benchmark — just what's been true in practice.

## The split (so far)

- **ChatGPT** — knots research, literature, and "explain this concept"
  warm-ups. Feels conversational; good for open-ended exploration.
- **Claude** — Python / Colab coding and longer multi-file reasoning. Holds
  context well on fiddly debugging.
- **Gemini** — quick lookups and a fast second opinion.
- **WorkBuddy** — writing + fact-check, and the agentic stuff (file ops,
  running commands, shipping to GitHub). This is the one that *does* things,
  not just chats.

## What I've noticed

- I almost always start fuzzy and ask "can you change X?" before committing to
  a direction. Models that push back or ask a clarifying question save me time.
- For learning (LA, knots) I want step-by-step + Q&A, not a wall of answer.
- I trust a model more when it **verifies** (runs the code, checks the file)
  instead of just asserting. That's why the agentic workflow won me over.
- Tone matters: casual, concise, opinionated beats corporate and verbose.

## Open questions

- When does bouncing between models actually help vs. just add overhead?
- Is there a task I'm handing to the "wrong" model out of habit?
