cookiecutter-latex-makefile
===========================

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for
[LaTeX](https://www.latex-project.org/) documents
with a [Makefile](https://github.com/tueda/makefile4latex).

This template requires Cookiecutter 2.1.0 or later.

Usage
-----

```bash
cookiecutter gh:tueda/cookiecutter-latex-makefile
cd <directory_name>
make
```

Configuration Notes
-------------------

The default `.chktexrc` in this template ignores the following warnings:
- All warnings found in the preamble (`-H0`).
- Warning 1: Command terminated with space for `\itshape` (`Silent` section).
    * [TeX - LaTeX Stack Exchange: Why does ChkTeX complain when there is a space after \itshape but not when \bfseries is used?](https://tex.stackexchange.com/q/627808)

  Other commands are also listed in the `Silent` section.
- Warning 3: You should enclose the previous parenthesis with '{}' (`-n3`).
    * [TeX - LaTeX Stack Exchange: Why should I "enclose the previous parenthesis with '{}'"?](https://tex.stackexchange.com/a/529940)
- Warning 8: Wrong length of dash may have been used (`-n8`).
    * Jens T. Berger Thielemann, [ChkTEX v1.7.6 (PDF)](http://mirrors.ctan.org/systems/doc/chktex/ChkTeX.pdf), p.15.
      > This is more or less correct, according to my references. One
      > complication is that most often a hyphen (single dash) is
      > desired between letters, but occasionally an n-dash (double
      > dash) is required. This is the case for theorems named after
      > two people e.g. Jordan–Hölder."
- Warning 24: Delete this space to maintain correct pagereferences (`-n24`).
    * [TeX - LaTeX Stack Exchange: When is leading/opening whitespace of a line
      in a tex file important?](https://tex.stackexchange.com/a/264115)
- Warning 38: You should not use punctuation in front of/after quotes (`-n38`).
    * [Debian Bug report logs - #224939: chktex: punctuation in front of quotes](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=224939)
    * [[texhax] chktex: false positives](https://tug.org/pipermail/texhax/2003-December/001423.html)
