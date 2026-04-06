"""Render ASCII art text to themed PNG images."""

from __future__ import annotations

import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from themes import Theme

_BOX_DRAWING = re.compile(
    r"[\u2500-\u257F\u2580-\u259F\u2190-\u21FF\u25A0-\u25FF\u2550-\u256C╔╗╚╝║═→]"
)

_FONT_DIRS = [
    Path(__file__).resolve().parent.parent / "assets" / "fonts",
    Path.home() / ".local/share/fonts/MapleMono",
    Path.home() / ".local/share/fonts",
    Path("/usr/share/fonts/truetype"),
]


def _find_font(weight: str = "Regular", font_dir: str | None = None) -> str | None:
    dirs = ([Path(font_dir)] if font_dir else []) + _FONT_DIRS
    for d in dirs:
        for name in [f"MapleMono-NF-CN-{weight}.ttf", "MapleMono-NF-CN-Regular.ttf"]:
            p = d / name
            if p.exists():
                return str(p)
    return None


def render_to_png(
    text: str,
    output: str,
    theme: Theme,
    font_size: int = 28,
    line_height: int | None = None,
    padding: int = 48,
    scale: float = 1.0,
    font_dir: str | None = None,
) -> Path:
    """Render ASCII art text to a themed PNG image."""
    lh = line_height or int(font_size * 1.38)

    font_path = _find_font(theme.font_weight, font_dir) or _find_font("Regular", font_dir)
    if not font_path:
        raise FileNotFoundError("Maple Mono NF CN not found. Check assets/fonts/")
    font = ImageFont.truetype(font_path, font_size)

    lines = text.rstrip("\n").split("\n")
    max_w = max((font.getlength(line) for line in lines), default=0)

    img_w = int(max_w + padding * 2)
    img_h = int(len(lines) * lh + padding * 2)
    img = Image.new("RGB", (img_w, img_h), theme.bg)
    draw = ImageDraw.Draw(img)

    use_accent = theme.accent and theme.accent != theme.fg

    for i, line in enumerate(lines):
        y = padding + i * lh
        if not line:
            continue
        if use_accent:
            x = float(padding)
            for ch in line:
                color = theme.accent if _BOX_DRAWING.match(ch) else theme.fg
                draw.text((x, y), ch, font=font, fill=color)
                x += font.getlength(ch)
        else:
            draw.text((padding, y), line, font=font, fill=theme.fg)

    if scale != 1.0:
        img = img.resize((int(img_w * scale), int(img_h * scale)), Image.LANCZOS)

    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(out), "PNG")
    return out
