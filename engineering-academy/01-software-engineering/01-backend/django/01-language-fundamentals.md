# 01. Language Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Django is Python, and modern Python code uses type hints, clear classes and good tooling. Solid Python makes every
Django feature easier to understand. Current Django releases need Python 3.12 or later. Back to the
[roadmap](./README.md).

## Modern Python and type hints

Type hints say what each value should be. Python does not enforce them when the code runs, but tools such as mypy
check them, and they make code easier to read and review.

**What to learn:**

- Built-in types, f-strings, comprehensions, and unpacking
- Type hints for parameters, return values and variables, including `X | None` and generics such as `list[str]`
- Running mypy in strict mode, and reading its errors

**Resources:**

- [The Python tutorial](https://docs.python.org/3/tutorial/)
- [Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html), mypy documentation

**Level:** Practitioner · Core

## Classes and data classes

Django is built from classes: models, views, serializers and settings. You read and write them every day.

**What to learn:**

- Classes, inheritance and `super()`, and properties
- Data classes for simple values, and `Enum` for fixed sets of values
- Protocols and abstract base classes, for code that depends on an interface instead of a concrete class

**Resources:** [Classes](https://docs.python.org/3/tutorial/classes.html) and
[dataclasses](https://docs.python.org/3/library/dataclasses.html), Python documentation

**Level:** Practitioner · Core

## Errors and exceptions

Python reports problems by raising exceptions. Handling them in the right place keeps errors clear for users and
useful for developers.

**What to learn:**

- Raising and catching exceptions, `finally`, and context managers with `with`
- Writing your own exception classes for problems in your domain
- Catching only the exceptions you expect, never a bare `except:`

**Resources:** [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html), Python documentation

**Level:** Practitioner · Core

## Packages and environments

Each project needs its own Python version and packages. Modern Python projects describe them in `pyproject.toml`
and lock exact versions.

**What to learn:**

- Virtual environments, and why packages are never installed into the system Python
- `pyproject.toml`, adding packages, and committing a lock file, for example with uv
- Checking packages for known security issues, for example with `pip-audit`

**Resources:**

- [Installing packages](https://packaging.python.org/en/latest/tutorials/installing-packages/), Python Packaging
  User Guide
- [uv documentation](https://docs.astral.sh/uv/)

**Level:** Practitioner · Core

## Code style and linting

A shared code style keeps reviews about behaviour, not formatting. A linter finds likely bugs before review.

**What to learn:**

- PEP 8 (Python Enhancement Proposal 8), the official Python style guide, and formatting code automatically
- Ruff for linting and formatting, and mypy for types, in the editor and before every commit

**Resources:**

- [PEP 8](https://peps.python.org/pep-0008/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations

**Level:** Practitioner · Core

## Async Python

Python can run many waiting tasks at once with `async` and `await`. Django supports async views, but most Django
code is still synchronous.

**What to learn:**

- `async def`, `await` and `asyncio`, and when async helps, such as calling many slow services
- Why calling blocking code inside an async function slows everything down

**Resources:** [Coroutines and tasks](https://docs.python.org/3/library/asyncio-task.html), Python documentation

**Level:** Advanced · Optional

## Project: Write a Slug Library in Python

**Brief:** Before you use Django, write a small Python package that turns an article title into a URL slug, such as
`How to Train Your Dragon` into `how-to-train-your-dragon`, and makes it unique when a slug is already taken. Your
RealWorld API uses the same rules in later stages.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The package has a `pyproject.toml` and a committed lock file, and installs into a virtual environment
- [ ] Every function has type hints, and mypy in strict mode reports no errors
- [ ] Titles with accents, punctuation and repeated spaces give lower-case, hyphen-separated ASCII slugs, and a title
  of only symbols raises a clear exception
- [ ] A taken slug gets a suffix, such as `-2`, through a protocol that a later stage can back with the database
- [ ] pytest tests cover each of these cases
- [ ] Ruff reports no lint or formatting issues
- [ ] The README explains how to install, test and use the package

Next: [02. The Framework](./02-the-framework.md)
