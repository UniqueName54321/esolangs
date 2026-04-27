# C-4

Python interpreter for **C-4**, a self-destructive joke language where every program is valid and running one deletes both the program and the interpreter.

## Usage

```sh
python3 interpreter.py program.c4
```

Running the interpreter attempts to delete:

- the program file passed on the command line
- `interpreter.py` itself

If the program is read from standard input, only the interpreter is deleted:

```sh
python3 interpreter.py - < program.c4
```

## Example

Any file is a valid C-4 program, including an empty file.

```text
anything can go here
```

## Notes

On Unix-like systems, a running Python script can usually unlink its own file. On other platforms or restricted filesystems, self-deletion may fail; the interpreter reports failures to standard error and exits with a non-zero status.
