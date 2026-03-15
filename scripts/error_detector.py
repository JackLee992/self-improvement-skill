from __future__ import annotations

import os


ERROR_PATTERNS = (
    "error:",
    "failed",
    "command not found",
    "no such file",
    "permission denied",
    "fatal:",
    "exception",
    "traceback",
    "syntaxerror",
    "typeerror",
    "exit code",
    "non-zero",
)


def main() -> None:
    output = os.environ.get("CLAUDE_TOOL_OUTPUT", "")
    lowered = output.lower()
    if any(pattern in lowered for pattern in ERROR_PATTERNS):
        print(
            "<error-detected>\n"
            "A non-trivial tool error was detected. If the fix required investigation,\n"
            "log it to .learnings/ERRORS.md using the self-improvement format.\n"
            "</error-detected>"
        )


if __name__ == "__main__":
    main()
