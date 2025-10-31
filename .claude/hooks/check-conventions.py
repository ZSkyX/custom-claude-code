#!/usr/bin/env python3
"""
PreToolUse hook to enforce project conventions.
Checks for:
- Documentation files being created without /write-documentation command
- Print statements instead of loggers
- Files created in wrong directories
"""

import json
import sys

def main():
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)
        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})

        # Check for documentation file creation
        if tool_name == "Write":
            file_path = tool_input.get("file_path", "")
            content = tool_input.get("content", "")

            # Block README or .md documentation creation
            if file_path.endswith("README.md") or (file_path.endswith(".md") and "/docs/" in file_path):
                output = {
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Documentation files should only be created using /write-documentation command"
                }
                print(json.dumps(output))
                sys.exit(0)

            # Warn about print statements
            if "print(" in content and not "# print is ok" in content:
                output = {
                    "permissionDecision": "allow",
                    "userMessage": "⚠️  Consider using loggers instead of print statements (per project conventions)"
                }
                print(json.dumps(output))
                sys.exit(0)

        # Allow by default
        sys.exit(0)

    except Exception as e:
        # Don't block on errors
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
