#!/usr/bin/env python3
"""Interpreter for C-4, the self-destructive esolang."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def delete_file(path: Path) -> OSError | None:
    try:
        path.unlink()
    except FileNotFoundError:
        return None
    except OSError as error:
        return error
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run a C-4 program by deleting it and this interpreter."
    )
    parser.add_argument("program", help="C-4 source file, or '-' for standard input")
    args = parser.parse_args(argv)

    errors: list[str] = []

    if args.program == "-":
        sys.stdin.read()
    else:
        program_path = Path(args.program)
        error = delete_file(program_path)
        if error is not None:
            errors.append(f"could not delete program {program_path}: {error}")

    interpreter_path = Path(__file__)
    error = delete_file(interpreter_path)
    if error is not None:
        errors.append(f"could not delete interpreter {interpreter_path}: {error}")

    for error_message in errors:
        print(f"c-4: {error_message}", file=sys.stderr)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
