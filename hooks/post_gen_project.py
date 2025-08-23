"""Scripts to run after the project generation."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def remove_if(path: str | Path, cond: bool) -> None:  # noqa: FBT001
    """Remove the file/directory if the condition is met."""
    path = Path(path)
    if cond:
        if path.is_file() or path.is_symlink():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)


def run_git(*args: str) -> None:
    """Run a Git command with the given arguments."""
    subprocess.call(["git", *args])  # noqa: S603, S607


# Remove the .jinja file extension from all template files.

for path, _, files in os.walk("."):
    for name in files:
        if name.endswith(".jinja"):
            old_path = Path(path) / name
            new_path = Path(path) / name[: -len(".jinja")]
            old_path.rename(new_path)

# Remove tool-specific config files based on user selection.

use_vscode = "VS Code" in "{{cookiecutter.editor}}"  # noqa: PLR0133
use_latexindent = "latexindent" in "{{cookiecutter.formatter}}"  # noqa: PLR0133
use_chktex = "ChkTeX" in "{{cookiecutter.linter}}"  # noqa: PLR0133

remove_if(".vscode", not use_vscode)
remove_if(".latexindent.yaml", not use_latexindent)
remove_if(".chktexrc", not use_chktex)

# Initialize a Git repository and add all files.

if shutil.which("git"):
    run_git("init")
    run_git("add", ".")
    if use_vscode:
        run_git("add", "-f", ".vscode/settings.json")
    print("Git repository initialized. Files have been staged for commit.")  # noqa: T201
