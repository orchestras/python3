"""Tests for the __main__ entry point."""

from __future__ import annotations

import subprocess
import sys

import pytest


def test_main_hello(capsys: pytest.CaptureFixture[str]) -> None:
    """Running with 'hello' command prints greeting."""
    from python_template.__main__ import main

    original = sys.argv
    sys.argv = ["python-template", "hello"]
    try:
        main()
    finally:
        sys.argv = original

    captured = capsys.readouterr()
    assert "Hello from python-template" in captured.out


def test_main_version_flag() -> None:
    """--version flag should exit with version string."""
    result = subprocess.run(
        [sys.executable, "-m", "python_template", "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "python-template" in result.stdout or "python-template" in result.stderr


def test_main_unknown_command() -> None:
    """Unknown command should exit with non-zero code."""
    result = subprocess.run(
        [sys.executable, "-m", "python_template", "unknown-command"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
