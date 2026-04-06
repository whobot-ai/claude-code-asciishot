"""Built-in color themes for asciishot."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    name: str
    label: str
    bg: str
    fg: str
    accent: str
    font_weight: str = "Regular"


THEMES: dict[str, Theme] = {}


def _r(t: Theme):
    THEMES[t.name] = t


_r(Theme("xiaomi", "Xiaomi — 小米橙活力", "#ffffff", "#1a1a1a", "#ff6900", "Medium"))
_r(Theme("apple", "Apple — 纯白极简", "#ffffff", "#1d1d1f", "#86868b", "Medium"))
_r(Theme("dark", "Dark — 深邃暗夜", "#1a1b26", "#c0caf5", "#565f89"))
_r(Theme("cloud", "Cloud — 云计算控制台", "#232f3e", "#ffffff", "#ff9900"))
_r(Theme("gpt", "GPT — OpenAI 风格", "#212121", "#ececec", "#10a37f"))
_r(Theme("onedark", "One Dark — VS Code 经典", "#282c34", "#abb2bf", "#61afef"))
_r(Theme("dracula", "Dracula — 吸血鬼紫", "#282a36", "#f8f8f2", "#bd93f9"))
_r(Theme("monokai", "Monokai — Sublime 经典", "#2d2a2e", "#fcfcfa", "#ffd866"))
_r(Theme("nord", "Nord — 北极冰蓝", "#2e3440", "#d8dee9", "#88c0d0"))
_r(Theme("github-dark", "GitHub Dark — 开发者暗夜", "#0d1117", "#e6edf3", "#58a6ff"))
_r(Theme("github-light", "GitHub Light — 开发者日间", "#ffffff", "#1f2328", "#0969da", "Medium"))
_r(Theme("catppuccin", "Catppuccin — 柔和奶茶", "#1e1e2e", "#cdd6f4", "#cba6f7"))
_r(Theme("solarized", "Solarized — 经典护眼", "#002b36", "#839496", "#268bd2"))
