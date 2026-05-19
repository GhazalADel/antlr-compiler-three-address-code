# ANTLR Compiler — Principles of Compiler Design Final Project
**Amirkabir University of Technology | Spring 2024**

## Overview
A compiler for a custom C-like language, built with ANTLR4 (Python target). The compiler parses source code, builds a parse tree, performs semantic analysis, and generates three-address code that compiles and runs as C.

## Pipeline
```
Source (.txt) → Lexer → Parser → Parse Tree → Listener (Semantic Analysis + Code Gen) → Three-Address C Code
```

## Language Features
- Types: `int`, `double`, `boolean`, `void`
- Functions with by-value parameters
- Control flow: `decide` (if/else), `loop` (while)
- Operators with full precedence (unary, arithmetic, relational, logical)
- `++` / `--`, string literals, comments (`//` and `/* */`)

## Code Generation
Three-address code is emitted into a C `main()` using a simulated memory array `m[]` as RAM, with `top` (stack pointer) and `bottom` (frame pointer) for activation record management.

## Files
| File | Description |
|------|-------------|
| `MyGrammer.g4` | ANTLR4 grammar |
| `main.py` | Entry point |
| `src/MyGrammer{Lexer,Parser,Listener}.py` | ANTLR-generated + custom listener |
| `main.c` | C runtime template for generated code |

## Usage
```bash
pip install antlr4-python3-runtime

# Generate parse tree (GUI)
antlr4-parse MyGrammer.g4 program -tree test.txt -gui

# Run compiler
python main.py  # outputs three-address C code
```
