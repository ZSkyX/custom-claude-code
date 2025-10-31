# Claude Code Workflow Requirements

This document outlines the conventions and workflow for working with Claude Code on this project.

## Planning Mode

### When Planning
1. **Planning is crucial** - Engineering is scientific, and proper planning is essential before implementation
2. **Ask questions** - When requirements are ambiguous, ask clarifying questions or provide options rather than making assumptions
3. **Planning completion** - Planning phase ends ONLY when the `/finished-planning` command is triggered

### Custom Commands
- `/finished-planning` - Completes planning phase and transitions to implementation mode
- `/write-documentation [type]` - Generates documentation (manual|design|readme|all)

## Code Implementation

### Directory Structure
Organize code into proper folders:
```
project/
├── data/              # Data files and datasets
│   ├── data_subfolder_1/
│   └── data_subfolder_2/
├── src/               # Source code
│   ├── utils/         # Utility functions
│   └── code_group_1/  # Feature groups
│   └── code_group_2/  # Feature groups
├── scripts/           # Shell scripts
├── logs/              # Log files
└── docs/              # Documentation
    ├── manual/        # User documentation
    └── design/        # Technical design docs
```

### Coding Conventions
1. **No emojis** - Unless explicitly requested by the user
2. **Use loggers** - Prefer logging over `print()` statements
3. **Shell scripts** - Write simple scripts with clear variable-based arguments
   ```bash
   ARG1="xx"
   ARG2="yy"
   uv run python main.py --arg1 "$ARG1" --arg2 "$ARG2"
   ```
4. **Shell script location** - Place shell scripts in `scripts/` folder
5. **Documentation** - Only create documentation when `/write-documentation` command is triggered

## Code Execution

### Python Environment
1. **Always use `uv`** for Python package management
2. **Activate environment** before running Python code:
   ```bash
   source .venv/bin/activate
   ```
3. **Install packages** using:
   ```bash
   uv add <package>
   # or
   uv pip install <package>
   ```

## Workflow Enforcement

### Automated Hooks
This project uses PreToolUse hooks to enforce conventions:
- Blocks creation of README.md or docs/*.md without `/write-documentation` command
- Warns when using `print()` instead of loggers

### Configuration
- Custom commands: `.claude/commands/`
- Hooks: `.claude/hooks/`
- Settings: `.claude/settings.json`

## Summary
These conventions ensure consistent code quality, proper organization, and efficient workflow when working with Claude Code on this project.
