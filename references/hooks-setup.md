# Codex Hook Setup

Use hooks only if you want lightweight reminders to log learnings. The skill works without hooks.

## Recommended

For most projects, add a short reminder to `AGENTS.md` instead of enabling hooks:

```markdown
## Self-Improvement

After non-obvious failures, user corrections, or repeated workflow friction, log the result to `.learnings/`.
Promote stable patterns into this file when they become durable project rules.
```

## Optional Codex Hook

Create `.codex/settings.json` and run a small Python reminder after each prompt:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python ./.codex/skills/self-improvement/scripts/activator.py"
          }
        ]
      }
    ]
  }
}
```

If your environment exposes tool output to hooks, you can also use the error detector:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python ./.codex/skills/self-improvement/scripts/error_detector.py"
          }
        ]
      }
    ]
  }
}
```

## Verification

1. Start a new Codex session.
2. Trigger a prompt.
3. Confirm the reminder output appears.
4. Run a failing command and confirm the error reminder appears if your environment passes tool output through the hook environment.

## Notes

- The Python scripts are cross-platform and avoid shell-specific setup on Windows.
- If relative paths are inconvenient, use absolute paths to the installed skill directory.
- If you do not want hook overhead, skip hooks entirely and rely on the `AGENTS.md` reminder.
