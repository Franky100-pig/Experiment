# skills/

Reusable LLM / agent **skills** I author — prompt and agent workflows worth
keeping. Each skill lives in its own folder with a `SKILL.md` (YAML frontmatter
+ instructions). The `_template/` folder is a starting point: copy it, rename,
fill in.

The format mirrors the WorkBuddy `SKILL.md` convention, so a skill authored
here can later be dropped into `~/.workbuddy/skills/` if it proves useful.

## Skills index

| Skill | What it does |
|-------|--------------|
| _template | Starter skeleton — clone to begin a new skill |
| [raycaster-playbook](raycaster-playbook/SKILL.md) | Build a pseudo-3D raycast FPS: DDA, fisheye fix, sprites, wall sliding |
| [fps-game-feel](fps-game-feel/SKILL.md) | Tuning checklist for gunplay: latency, feedback, recoil, TTK, sound |
| [moba-design-primer](moba-design-primer/SKILL.md) | MOBA anatomy: economy, hero kits, items, snowball control, balance |
| [moba-lite-prototype](moba-lite-prototype/SKILL.md) | Build a playable mini-MOBA in pygame, step by step |
| [data-driven-tuning](data-driven-tuning/SKILL.md) | Balance without code edits: stats in JSON, hot-reload, match logs |
| [debug-frame-drops](debug-frame-drops/SKILL.md) | Diagnose stutter systematically: frame-time graph, cProfile, budgets |
| [game-mvp-scoping](game-mvp-scoping/SKILL.md) | *(stub — mine to write)* Vertical-slice scoping method |
