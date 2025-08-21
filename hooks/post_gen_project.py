"""Scripts to run after the project generation."""

import os
import shutil
import subprocess


def remove_if(path, cond):
    # type: (str, bool) -> None
    """Remove the file/directory if the condition is met."""
    if cond:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)


def run_git(*args):
    # type: (*str) -> None
    """Run a Git command with the given arguments."""
    subprocess.call(["git", *args])  # noqa: S603, S607


# Remove the .jinja file extension from all template files.

for path, _, files in os.walk("."):
    for name in files:
        if name.endswith(".jinja"):
            os.rename(
                os.path.join(path, name),
                os.path.join(path, name[: -len(".jinja")]),
            )

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
