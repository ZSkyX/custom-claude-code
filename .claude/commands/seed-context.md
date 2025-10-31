---
description: Load files and all their dependencies recursively
argument-hint: @file1 @file2 @file3...
---

Seeding comprehensive project context from: $ARGUMENTS

I will:
1. Read the specified files
2. Parse and identify all imports/dependencies (Python imports, JS/TS imports, etc.)
3. Recursively read all dependency files
4. Build a complete understanding of the module structure
5. Map relationships between components

This provides deep context including all related code. For lightweight context without dependencies, use /load-context instead.

Building dependency tree and reading all related files...
