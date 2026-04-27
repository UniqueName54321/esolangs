# AVBE

Python interpreter for **A very BASIC esolang**.

## Usage

```sh
python3 interpreter.py program.avbe
```

You can also run code from standard input:

```sh
python3 interpreter.py - < program.avbe
```

## Commands

| Command | Description |
| --- | --- |
| `START PROGRAM` | Starts execution. Lines before this command are skipped. |
| `PRINT OUT THE CURRENT STRING "string"` | Prints a quoted string. |
| `PRINT OUT THE CURRENT STRING input` | Prints the latest value read from input. |
| `ASK USER FOR INPUT` | Reads one line from standard input into `input`. |
| `GOTO [line number]` | Jumps to a 1-based source line number. |
| `PLAY NOTE [note letter] [volume] [pitch]` | Emits a terminal bell as a dependency-free audio placeholder. |
| `EXIT` | Ends the program. |

## Examples

```avbe
START PROGRAM
PRINT OUT THE CURRENT STRING "Hello, World!"
EXIT
```

```avbe
START PROGRAM
ASK USER FOR INPUT
PRINT OUT THE CURRENT STRING input
```
