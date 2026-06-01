from __future__ import annotations
from typing import Iterable

from gradio.themes.base import Base
from gradio.themes.utils import (
colors,
fonts,
sizes
)

class MetafisikTheme(Base):

    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.cyan,
        secondary_hue: colors.Color | str = colors.blue,
        neutral_hue: colors.Color | str = colors.slate,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_xxl,
        text_size: sizes.Size | str = sizes.text_lg,
        font=(
            fonts.GoogleFont("Quicksand"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono=(
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):

        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )

        self.set(

            body_background_fill=
            "linear-gradient(180deg,#020617,#0f172a,#111827)",

            body_background_fill_dark=
            "linear-gradient(180deg,#020617,#0f172a,#111827)",

            button_primary_background_fill=
            "linear-gradient(90deg,#00c6ff,#0072ff)",

            button_primary_background_fill_hover=
            "linear-gradient(90deg,#22d3ee,#3b82f6)",

            button_primary_background_fill_dark=
            "linear-gradient(90deg,#00c6ff,#0072ff)",

            button_primary_text_color="white",

            block_title_text_weight="700",

            block_border_width="1px",

            block_shadow="0 0 25px rgba(0,198,255,.15)",

            button_large_padding="28px",

            slider_color="#38bdf8",

            slider_color_dark="#38bdf8"
        )
