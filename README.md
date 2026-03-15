# Self Improvement Skill for Codex

Codex-first adaptation of the upstream `self-improving-agent` skill.

This version is tuned for Codex workflows:

- logs durable learnings to `.learnings/`
- promotes stable patterns to `AGENTS.md`
- uses cross-platform Python hook helpers
- keeps upstream OpenClaw material only as optional legacy reference

## Install

Use your skill installer against this repo:

```powershell
python "$env:USERPROFILE\\.codex\\skills\\.system\\skill-installer\\scripts\\install-skill-from-github.py" `
  --repo JackLee992/self-improvement-skill `
  --path . `
  --name self-improvement
```

## Included

- `SKILL.md` - Codex workflow and logging format
- `agents/openai.yaml` - Codex UI metadata
- `references/examples.md` - entry examples
- `references/hooks-setup.md` - optional Codex hook setup
- `scripts/activator.py` - prompt reminder hook
- `scripts/error_detector.py` - tool error reminder hook

## Workflow

1. Create `.learnings/` in the repo.
2. Log non-trivial errors, corrections, and missing capabilities.
3. Promote recurring project rules into `AGENTS.md`.
4. Extract a dedicated skill when a pattern becomes cross-project and durable.
