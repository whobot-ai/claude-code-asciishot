---
name: claude-code-asciishot
description: Draw ASCII art diagrams and render them to beautiful themed PNG images with perfect CJK alignment. Trigger when user asks to draw diagrams, create ASCII art, render architecture charts, flowcharts, mind maps, org charts, or convert text art to images. Also trigger on "画图", "架构图", "流程图", "思维导图", "鱼骨图", "甘特图", "ASCII", "asciishot". Supports 28+ diagram types and 13 color themes. Bundled with Maple Mono NF CN font for CJK support.
---

# claude-code-asciishot

Draw ASCII art diagrams → render to beautiful themed PNG images.

## How It Works

1. **Draw**: Create ASCII art using box-drawing characters (`┌─┐│└┘├┤┬┴┼╔═╗║╚╝`)
2. **Save**: Write to a `.txt` file
3. **Render**: Run the render script with a theme

## Render Command

```bash
python3 <<'PYEOF'
from pathlib import Path
import sys, re
sys.path.insert(0, str(Path("~/.claude/skills/claude-code-asciishot/scripts").expanduser()))
from render import render_to_png
from themes import THEMES

render_to_png(
    text=Path("INPUT.txt").read_text(),
    output="OUTPUT.png",
    theme=THEMES["xiaomi"],       # or: apple, dark, cloud, gpt, onedark, dracula, monokai, nord, github-dark, github-light, catppuccin, solarized
    font_dir=str(Path("~/.claude/skills/claude-code-asciishot/assets/fonts").expanduser()),
)
PYEOF
```

## Available Themes (13)

`xiaomi` (default), `apple`, `dark`, `cloud`, `gpt`, `onedark`, `dracula`, `monokai`, `nord`, `github-dark`, `github-light`, `catppuccin`, `solarized`

## Drawing Tips

- Box-drawing chars render in theme **accent color**, text in **foreground color**
- Use `▸` (U+25B8) for arrows — same baseline as `─`. Avoid `→` (U+2192)
- CJK = 2 display columns. Use `wcwidth` for alignment if needed
- Title block: `╔══ 标题 ══╗`, layer border: `┌─ 层名 ──...──┐`

## 28 Example Templates

Ready-to-use templates in `assets/examples/`:

architecture, microservices, multi_agent, deployment_arch, network_topology, system_monitor, rag_pipeline, llm_arch, cicd_pipeline, business_flow, state_machine, auth_flow, git_workflow, data_pipeline, fishbone, swot, decision_tree, comparison_matrix, mind_map, user_journey, gantt_chart, data_table, bar_chart, dashboard, kanban, ai_timeline, er_diagram, uml_class, binary_tree, memory_layout, file_tree, math_formula, tcp_stack, cpu_pipeline, packet_structure, radar_chart, api_design, org_chart

## Resources

### scripts/
- `render.py` — Pillow-based renderer (accent color for box-drawing)
- `themes.py` — 13 theme definitions

### assets/
- `fonts/` — Maple Mono NF CN (Regular + Medium, SIL OFL)
- `examples/` — 28 ASCII diagram templates
