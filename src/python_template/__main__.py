"""Entry point for python-template CLI."""

from __future__ import annotations

import sys

from python_template.version import __version__


def main() -> None:
    """Run the python-template CLI."""
    import argparse

    parser = argparse.ArgumentParser(
        prog="python-template",
        description="Python 3 template CLI",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="hello",
        help="Command to run (default: hello)",
    )

    args = parser.parse_args()

    if args.command == "hello":
        print(f"Hello from python-template {__version__}!")
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
