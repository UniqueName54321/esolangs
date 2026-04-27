#!/usr/bin/env python3
"""Interpreter for A very BASIC esolang (AVBE)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PRINT_RE = re.compile(r'^PRINT OUT THE CURRENT STRING (?P<value>"(?:[^"\\]|\\.)*"|input)$')
GOTO_RE = re.compile(r"^GOTO (?P<line>[1-9][0-9]*)$")
PLAY_RE = re.compile(r"^PLAY NOTE (?P<note>[A-Ga-g]) (?P<volume>-?[0-9]+) (?P<pitch>-?[0-9]+)$")


class AVBEError(Exception):
    """Raised when an AVBE program cannot be executed."""


def decode_quoted_string(value: str) -> str:
    result = []
    index = 1
    while index < len(value) - 1:
        char = value[index]
        if char == "\\":
            index += 1
            if index >= len(value) - 1:
                raise AVBEError("unterminated escape sequence")
            escapes = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "\\": "\\"}
            result.append(escapes.get(value[index], value[index]))
        else:
            result.append(char)
        index += 1
    return "".join(result)


def run(source: str) -> None:
    lines = source.splitlines()
    input_value = ""
    started = False
    pc = 0

    while pc < len(lines):
        raw_line = lines[pc]
        line = raw_line.strip()
        line_number = pc + 1

        if not line:
            pc += 1
            continue

        if not started:
            if line == "START PROGRAM":
                started = True
            pc += 1
            continue

        if line == "START PROGRAM":
            pc += 1
            continue

        if line == "EXIT":
            return

        if line == "ASK USER FOR INPUT":
            try:
                input_value = input()
            except EOFError:
                input_value = ""
            pc += 1
            continue

        print_match = PRINT_RE.match(line)
        if print_match:
            value = print_match.group("value")
            if value == "input":
                print(input_value)
            else:
                print(decode_quoted_string(value))
            pc += 1
            continue

        goto_match = GOTO_RE.match(line)
        if goto_match:
            destination = int(goto_match.group("line"))
            if destination > len(lines):
                raise AVBEError(f"line {line_number}: GOTO destination {destination} is outside the program")
            pc = destination - 1
            continue

        play_match = PLAY_RE.match(line)
        if play_match:
            sys.stderr.write("\a")
            sys.stderr.flush()
            pc += 1
            continue

        raise AVBEError(f"line {line_number}: unknown command: {raw_line}")

    if not started:
        raise AVBEError("program does not contain START PROGRAM")


def read_source(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run an AVBE program.")
    parser.add_argument("program", help="AVBE source file, or '-' for standard input")
    args = parser.parse_args(argv)

    try:
        run(read_source(args.program))
    except OSError as error:
        print(f"avbe: {error}", file=sys.stderr)
        return 1
    except AVBEError as error:
        print(f"avbe: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
