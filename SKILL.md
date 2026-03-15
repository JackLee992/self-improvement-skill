---
name: self-improvement
description: Capture reusable learnings, recurring errors, and missing capabilities during Codex work. Use when a task fails unexpectedly, the user corrects an assumption, a tool or API behaves unexpectedly, a better recurring workflow is discovered, or a missing capability should be tracked for later implementation.
metadata:
---

# Self-Improvement

Use this skill to turn one-off mistakes into reusable guidance. Log high-signal findings to `.learnings/`, then promote stable patterns into project memory such as `AGENTS.md`.

## Quick Reference

| Situation | Action |
|-----------|--------|
| Command or tool failed in a non-obvious way | Append to `.learnings/ERRORS.md` |
| User corrected an assumption or fact | Append to `.learnings/LEARNINGS.md` with category `correction` |
| Better workflow or durable pattern discovered | Append to `.learnings/LEARNINGS.md` with category `best_practice` |
| Missing capability or automation gap identified | Append to `.learnings/FEATURE_REQUESTS.md` |
| Learning is stable and broadly reusable | Promote it to `AGENTS.md` or project docs |

## Codex Workflow

1. Create `.learnings/` in the project if it does not exist.
2. Log only information that is likely to help future sessions.
3. Prefer concise entries with a clear trigger, failure mode, and next action.
4. When a pattern becomes stable, promote it out of `.learnings/` into durable guidance.

### What to Promote

- Project workflow rules -> `AGENTS.md`
- Project facts or conventions -> the most relevant repo doc
- Cross-project reusable technique -> consider extracting a new skill

## Setup

Create these files in the working repo:

```text
.learnings/
  LEARNINGS.md
  ERRORS.md
  FEATURE_REQUESTS.md
```

Use the templates in `assets/` if you want starter files. For entry examples, read `references/examples.md`. For optional Codex hook reminders, read `references/hooks-setup.md`.

## Logging Format

### Learning Entry

Append to `.learnings/LEARNINGS.md`:

```markdown
## [LRN-YYYYMMDD-XXX] category

**Logged**: ISO-8601 timestamp
**Priority**: low | medium | high | critical
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
One-line description of what was learned

### Details
What happened, what was wrong, and what is correct

### Suggested Action
Specific fix or workflow change

### Metadata
- Source: conversation | error | user_feedback
- Related Files: path/to/file.ext
- Tags: tag1, tag2
- See Also: LRN-20250110-001
- Pattern-Key: simplify.dead_code | harden.input_validation

---
```

### Error Entry

Append to `.learnings/ERRORS.md`:

```markdown
## [ERR-YYYYMMDD-XXX] skill_or_command_name

**Logged**: ISO-8601 timestamp
**Priority**: high
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
Brief description of what failed

### Error
```
Actual error message or output
```

### Context
- Command or operation attempted
- Input or parameters used
- Relevant environment details

### Suggested Fix
What is most likely to resolve or avoid it next time

### Metadata
- Reproducible: yes | no | unknown
- Related Files: path/to/file.ext
- See Also: ERR-20250110-001

---
```

### Feature Request Entry

Append to `.learnings/FEATURE_REQUESTS.md`:

```markdown
## [FEAT-YYYYMMDD-XXX] capability_name

**Logged**: ISO-8601 timestamp
**Priority**: medium
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Requested Capability
What is missing

### User Context
Why it matters

### Complexity Estimate
simple | medium | complex

### Suggested Implementation
How it could be added

### Metadata
- Frequency: first_time | recurring
- Related Features: existing_feature_name

---
```

## IDs and Status

- ID format: `TYPE-YYYYMMDD-XXX`
- Types: `LRN`, `ERR`, `FEAT`
- Status values: `pending`, `in_progress`, `resolved`, `wont_fix`, `promoted`

When resolving an entry, add:

```markdown
### Resolution
- **Resolved**: 2026-03-15T09:00:00Z
- **Commit/PR**: abc123 or #42
- **Notes**: What changed
```

## Notes

- Keep `.learnings/` high-signal. Do not log trivial typos or obvious one-off mistakes.
- If a pattern is recurring and cross-project, extract a dedicated skill instead of growing `AGENTS.md` indefinitely.
- `references/openclaw-integration.md` is legacy material from the upstream skill and is only relevant if you intentionally want OpenClaw compatibility.
