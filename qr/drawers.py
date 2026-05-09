"""Convenience factories for qrcode module drawers (see qrcode.image.styles.moduledrawers.pil)."""

from __future__ import annotations

from qrcode.image.styles.moduledrawers.pil import VerticalBarsDrawer


def vertical_bars_drawer(horizontal_shrink: float = 0.8) -> VerticalBarsDrawer:
    """
    Rounded vertical bars: contiguous dark modules merge into tall pills.
    ``horizontal_shrink`` in (0, 1] narrows each bar (more gap between columns).
    """
    return VerticalBarsDrawer(horizontal_shrink=horizontal_shrink)
