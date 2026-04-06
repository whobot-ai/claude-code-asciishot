<h1 align="center">claude-code-asciishot</h1>

<p align="center">
  <strong>ASCII Art → Beautiful Themed PNG</strong><br>
  A Claude Code Skill that draws ASCII diagrams and renders them as stunning themed images.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Diagram_Types-28-ff6900?style=flat-square" />
  <img src="https://img.shields.io/badge/Themes-13-0071e3?style=flat-square" />
  <img src="https://img.shields.io/badge/CJK-Perfect_Alignment-10a37f?style=flat-square" />
  <img src="https://img.shields.io/badge/Font-Bundled-bd93f9?style=flat-square" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" />
</p>

<p align="center">
  English · <a href="./README.md">中文</a>
</p>

---

## What is asciishot?

**Write ASCII text → get a beautiful PNG image.** That's it.

Just tell Claude Code "draw an architecture diagram" — the Skill draws it with Unicode box-drawing characters, then renders it to a themed PNG with the bundled monospace font. Box-drawing characters glow in the theme's accent color while text stays in the foreground color.

**No drawing software. No font setup. No Mermaid syntax.**

---

## Gallery

### Architecture

| Cloud Architecture (Xiaomi) | Cloud Architecture (Apple) |
|:--:|:--:|
| ![](examples/cloud_architecture_ascii_xiaomi.png) | ![](examples/cloud_architecture_ascii_apple.png) |

| Microservices | RAG Pipeline |
|:--:|:--:|
| ![](examples/microservices_xiaomi.png) | ![](examples/rag_pipeline_xiaomi.png) |

### Flowcharts

| CI/CD Pipeline | E-commerce Business Flow |
|:--:|:--:|
| ![](examples/cicd_pipeline_xiaomi.png) | ![](examples/business_flow_xiaomi.png) |

| Order State Machine | OAuth 2.0 Auth Flow |
|:--:|:--:|
| ![](examples/state_machine_xiaomi.png) | ![](examples/auth_flow_xiaomi.png) |

### Analysis

| Fishbone Diagram | SWOT Analysis |
|:--:|:--:|
| ![](examples/fishbone_xiaomi.png) | ![](examples/swot_xiaomi.png) |

| Decision Tree | Mind Map |
|:--:|:--:|
| ![](examples/decision_tree_xiaomi.png) | ![](examples/mind_map_xiaomi.png) |

### Data Visualization

| Gantt Chart | Dashboard |
|:--:|:--:|
| ![](examples/gantt_chart_xiaomi.png) | ![](examples/dashboard_xiaomi.png) |

| KPI Data Table | Bar Chart |
|:--:|:--:|
| ![](examples/data_table_xiaomi.png) | ![](examples/bar_chart_xiaomi.png) |

### Technical

| ER Diagram | UML Class Diagram |
|:--:|:--:|
| ![](examples/er_diagram_xiaomi.png) | ![](examples/uml_class_xiaomi.png) |

| Memory Layout | TCP/IP Stack |
|:--:|:--:|
| ![](examples/memory_layout_xiaomi.png) | ![](examples/tcp_stack_xiaomi.png) |

### More

| Git Workflow | Kanban Board |
|:--:|:--:|
| ![](examples/git_workflow_xiaomi.png) | ![](examples/kanban_xiaomi.png) |

| Multi-Agent System | Network Topology |
|:--:|:--:|
| ![](examples/multi_agent_xiaomi.png) | ![](examples/network_topology_xiaomi.png) |

---

## Installation

### Prerequisites

- [Claude Code](https://claude.ai/claude-code) installed
- Python 3.11+
- `pillow` package

### Step 1: Install the Skill

```bash
git clone https://github.com/whobot-ai/claude-code-asciishot.git \
  ~/.claude/skills/claude-code-asciishot
```

### Step 2: Install Python dependency

```bash
pip install pillow
```

> The font is bundled in the project. **No manual font installation needed.**

### Step 3: Verify

```bash
ls ~/.claude/skills/claude-code-asciishot/SKILL.md && echo "✅ Skill installed"
python3 -c "from PIL import Image; print('✅ Pillow ready')"
```

### Start using

In Claude Code, just say:

```
draw a microservices architecture diagram
```
```
create a fishbone diagram for analyzing delivery delays
```

The skill triggers automatically.

---

## 13 Themes

| Theme | Style | Accent |
|-------|-------|--------|
| **xiaomi** (default) | Xiaomi Orange | `#ff6900` 🟠 |
| **apple** | Apple Minimal | `#86868b` ⚪ |
| **dark** | Tokyo Night | `#565f89` 🔵 |
| **cloud** | AWS Console | `#ff9900` 🟠 |
| **gpt** | OpenAI | `#10a37f` 🟢 |
| **onedark** | One Dark Pro | `#61afef` 🔵 |
| **dracula** | Dracula | `#bd93f9` 🟣 |
| **monokai** | Monokai Pro | `#ffd866` 🟡 |
| **nord** | Nord Arctic | `#88c0d0` 🔵 |
| **github-dark** | GitHub Dark | `#58a6ff` 🔵 |
| **github-light** | GitHub Light | `#0969da` 🔵 |
| **catppuccin** | Catppuccin Mocha | `#cba6f7` 🟣 |
| **solarized** | Solarized Dark | `#268bd2` 🔵 |

## 28 Diagram Types

| Category | Types |
|----------|-------|
| **Architecture** | Cloud, Microservices, Multi-Agent, K8s, Network, Monitor, RAG, LLM |
| **Workflow** | CI/CD, Business Flow, State Machine, OAuth, Git, Data Pipeline |
| **Analysis** | Fishbone, SWOT, Decision Tree, Comparison Matrix, Mind Map, User Journey |
| **Data** | Gantt, Data Table, Bar Chart, Dashboard, Kanban, Timeline |
| **Technical** | ER, UML, Binary Tree, Memory Layout, File Tree, Math, TCP/IP, CPU Pipeline, Packet Structure, Radar, API Design, Org Chart |

All templates in [`assets/examples/`](./assets/examples/).

---

## How It Works

1. You ask Claude Code to draw a diagram
2. Claude draws it using Unicode box-drawing characters (`┌─┐│└┘╔═╗▸▼`)
3. Saves to a `.txt` file
4. Renders to PNG with the bundled [Maple Mono NF CN](https://github.com/subframe7536/maple-font) font + chosen theme
5. Box-drawing characters → **accent color**, text → **foreground color**

---

## License

MIT · Font under SIL Open Font License.

---

<p align="center">
  <sub>Made by <a href="https://github.com/jiangshu">@jiangshu</a></sub>
</p>
