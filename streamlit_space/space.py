# -*- coding: utf-8 -*-
"""Space component for Streamlit."""

from typing import Any, Optional
import streamlit as st


def space(container: Optional[Any] = None, lines: int = 1) -> None:
    """Add blank lines to Streamlit app.

    Args:
        container: Streamlit container
        lines: number of blank lines to be added
    """
    if container is None:
        container = st
    for _ in range(lines):
        container.write('')
