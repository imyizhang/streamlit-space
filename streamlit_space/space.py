# -*- coding: utf-8 -*-
"""Spacing component for Streamlit"""

from typing import Any, Optional

import streamlit as st


def space(container: Optional[Any] = None, lines: int = 1) -> None:
    """Add blank lines to Streamlit app.

    Args:
        container (any, optional): The Streamlit container. Defaults to `None`.
        lines (int, optional): The number of blank lines to be added. Defaults
    to `1`.
    """
    if container is None:
        container = st
    for _ in range(lines):
        container.write('')
