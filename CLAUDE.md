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

#### For Python Projects
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

#### For JavaScript/TypeScript Projects

**Backend Services** (Node.js/Express/Hono) - Organize by domain:

```
src/
├── server/           # Server-side code (handlers, middleware, utils)
├── mcp/              # MCP server implementation
├── tests/            # Test files and mocks
│   └── mocks/        # Mock data for testing
└── types/            # Shared TypeScript types (optional)
```

**Frontend Applications** (Next.js/React) - Organize by component category:

```
web/
├── app/              # Next.js app directory (routes + API routes)
│   ├── api/          # API route handlers
│   ├── [route]/      # Page routes
│   ├── layout.tsx    # Root layout
│   └── page.tsx      # Home page
├── components/       # All React components organized by category
│   ├── layout/       # Layout components (header, footer, nav)
│   ├── pages/        # Page-specific components
│   ├── providers/    # Context providers and app-level wrappers
│   ├── shared/       # Reusable components across pages
│   └── ui/           # Base UI components (buttons, inputs, cards)
├── hooks/            # Custom React hooks
├── lib/              # Utilities, types, and helper functions
│   ├── types.ts      # TypeScript type definitions
│   └── utils.ts      # Utility functions
├── public/           # Static assets (images, fonts, icons)
└── supabase/         # Database migrations and config (if using Supabase)
```

**Best Practices:**
- Organize components by category (`layout/`, `pages/`, `shared/`, `ui/`) rather than by feature
- Keep page-specific components in `components/pages/` for easy navigation
- Use `components/shared/` for components used across multiple pages
- Place base UI components (shadcn/ui, etc.) in `components/ui/`
- Import files directly (avoid barrel files for better tree-shaking)
- Keep backend and frontend code separated (`src/` vs `web/`)

### Coding Conventions

#### General (All Projects)
1. **No emojis** - Unless explicitly requested by the user
2. **Shell script location** - Place shell scripts in `scripts/` folder
3. **Documentation** - Only create documentation when `/write-documentation` command is triggered

#### For Python Projects
1. **Use loggers** - Prefer logging over `print()` statements
2. **Shell scripts** - Write simple scripts with clear variable-based arguments
   ```bash
   ARG1="xx"
   ARG2="yy"
   uv run python main.py --arg1 "$ARG1" --arg2 "$ARG2"
   ```

#### For JavaScript/TypeScript Projects
1. **Use loggers** - Prefer logging over `console.log()` statements
2. **Shell scripts** - Write simple scripts with clear variable-based arguments
   ```bash
   ARG1="xx"
   ARG2="yy"
   npm run script -- --arg1 "$ARG1" --arg2 "$ARG2"
   ```

## Code Execution

### For Python Projects
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

### For JavaScript/TypeScript Projects
1. **Always use `npm`** for package management
2. **Install dependencies** before running code:
   ```bash
   npm install
   ```
3. **Install packages** using:
   ```bash
   npm install <package>
   # or for dev dependencies
   npm install --save-dev <package>
   ```
4. **Run scripts** defined in package.json:
   ```bash
   npm run <script-name>
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
