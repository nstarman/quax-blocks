"""Test the package itself."""

import importlib.metadata

import quax_blocks as pkg


def test_version() -> None:
    assert importlib.metadata.version("quax_blocks") == pkg.__version__
