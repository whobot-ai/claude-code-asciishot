<h1 align="center">claude-code-asciishot</h1>

<p align="center">
  <strong>ASCII 图表 → 精美主题 PNG 图片</strong><br>
  一个 Claude Code Skill —— 画 ASCII 图表，一键渲染为高颜值主题图片
</p>

<p align="center">
  <img src="https://img.shields.io/badge/图表类型-28种-ff6900?style=flat-square" />
  <img src="https://img.shields.io/badge/配色主题-13种-0071e3?style=flat-square" />
  <img src="https://img.shields.io/badge/中英文-完美对齐-10a37f?style=flat-square" />
  <img src="https://img.shields.io/badge/字体-内置免安装-bd93f9?style=flat-square" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" />
</p>

<p align="center">
  <a href="./README_EN.md">English</a> · 中文
</p>

---

## 什么是 asciishot？

一句话：**写 ASCII 文本 → 得到一张好看的 PNG 图**。

在 Claude Code 中说一句"画一个架构图"，Skill 自动触发：用 Unicode 制表符画出图表，再用内置等宽字体渲染为带主题色的 PNG 图片。制表符/箭头自动着色为主题强调色，文字保持前景色，一眼分清结构与内容。

**不需要安装任何画图软件、不需要配置字体、不需要学 Mermaid 语法。**

---

## 效果展示

### 架构图

| 云计算平台架构 (小米风格) | 云计算平台架构 (苹果风格) |
|:--:|:--:|
| ![](examples/cloud_architecture_ascii_xiaomi.png) | ![](examples/cloud_architecture_ascii_apple.png) |

| 微服务全景图 | RAG 检索增强生成架构 |
|:--:|:--:|
| ![](examples/microservices_xiaomi.png) | ![](examples/rag_pipeline_xiaomi.png) |

### 流程图

| CI/CD 持续交付流水线 | 电商下单业务流程 (泳道图) |
|:--:|:--:|
| ![](examples/cicd_pipeline_xiaomi.png) | ![](examples/business_flow_xiaomi.png) |

| 订单状态机 | OAuth 2.0 授权码流程 |
|:--:|:--:|
| ![](examples/state_machine_xiaomi.png) | ![](examples/auth_flow_xiaomi.png) |

### 分析图

| 鱼骨图 (根因分析) | SWOT 战略分析 |
|:--:|:--:|
| ![](examples/fishbone_xiaomi.png) | ![](examples/swot_xiaomi.png) |

| 技术选型决策树 | AI PM 知识体系思维导图 |
|:--:|:--:|
| ![](examples/decision_tree_xiaomi.png) | ![](examples/mind_map_xiaomi.png) |

### 数据可视化

| 甘特图 (项目排期) | 运维监控仪表盘 |
|:--:|:--:|
| ![](examples/gantt_chart_xiaomi.png) | ![](examples/dashboard_xiaomi.png) |

| KPI 数据表 (含进度条) | 编程语言排行柱状图 |
|:--:|:--:|
| ![](examples/data_table_xiaomi.png) | ![](examples/bar_chart_xiaomi.png) |

### 技术图表

| ER 实体关系图 | UML 类图 |
|:--:|:--:|
| ![](examples/er_diagram_xiaomi.png) | ![](examples/uml_class_xiaomi.png) |

| 进程内存布局 | TCP/IP 协议栈 + 三次握手 |
|:--:|:--:|
| ![](examples/memory_layout_xiaomi.png) | ![](examples/tcp_stack_xiaomi.png) |

### 更多

| Git 分支管理策略 | Sprint 看板 |
|:--:|:--:|
| ![](examples/git_workflow_xiaomi.png) | ![](examples/kanban_xiaomi.png) |

| 多 Agent 协作系统 | 企业网络拓扑 |
|:--:|:--:|
| ![](examples/multi_agent_xiaomi.png) | ![](examples/network_topology_xiaomi.png) |

| LLM Transformer 架构 | 反向传播数学公式推导 |
|:--:|:--:|
| ![](examples/llm_arch_xiaomi.png) | ![](examples/math_formula_xiaomi.png) |

---

## 安装

### 前置条件

- [Claude Code](https://claude.ai/claude-code) 已安装
- Python 3.11+
- `pillow` 库（图片渲染依赖）

### 第一步：安装 Skill

```bash
git clone https://github.com/whobot-ai/claude-code-asciishot.git \
  ~/.claude/skills/claude-code-asciishot
```

### 第二步：安装 Python 依赖

```bash
pip install pillow
```

> 字体已内置在项目中，**无需手动安装任何字体**。

### 第三步：验证

```bash
# 检查 Skill 文件
ls ~/.claude/skills/claude-code-asciishot/SKILL.md && echo "✅ Skill 已安装"

# 检查 Pillow
python3 -c "from PIL import Image; print('✅ Pillow 已就绪')"
```

### 开始使用

在 Claude Code 中直接说：

```
画一个微服务架构图
```
```
draw a CI/CD pipeline diagram
```
```
帮我画一个鱼骨图，分析一下项目延期的原因
```

Skill 自动触发，画出 ASCII 图并渲染为 PNG。

---

## 13 种主题

| 主题 | 风格 | 强调色 | 背景 |
|------|------|--------|------|
| **xiaomi** (默认) | 小米橙 · 活力 | `#ff6900` 🟠 | 白底 |
| **apple** | 苹果 · 极简 | `#86868b` ⚪ | 白底 |
| **dark** | Tokyo Night · 暗夜 | `#565f89` 🔵 | 深蓝 |
| **cloud** | AWS 控制台 | `#ff9900` 🟠 | 深蓝 |
| **gpt** | OpenAI 风格 | `#10a37f` 🟢 | 深灰 |
| **onedark** | One Dark Pro | `#61afef` 🔵 | 深灰 |
| **dracula** | Dracula 暗紫 | `#bd93f9` 🟣 | 暗紫 |
| **monokai** | Monokai Pro | `#ffd866` 🟡 | 暖灰 |
| **nord** | Nord 北极冰蓝 | `#88c0d0` 🔵 | 极地蓝 |
| **github-dark** | GitHub Dark | `#58a6ff` 🔵 | 纯黑 |
| **github-light** | GitHub Light | `#0969da` 🔵 | 白底 |
| **catppuccin** | Catppuccin · 奶茶 | `#cba6f7` 🟣 | 深紫 |
| **solarized** | Solarized · 护眼 | `#268bd2` 🔵 | 深青 |

---

## 支持的 28 种图表

| 分类 | 图表类型 |
|------|----------|
| **架构设计** | 云计算架构、微服务架构、多 Agent 系统、K8s 部署、网络拓扑、监控告警、RAG 架构、LLM Transformer 架构 |
| **流程工作流** | CI/CD 流水线、电商业务流程 (泳道)、订单状态机、OAuth 授权流程、Git 分支策略、数据处理流水线 |
| **分析决策** | 鱼骨图、SWOT 分析、技术选型决策树、方案对比矩阵、思维导图、用户旅程图 |
| **数据可视化** | 甘特图、KPI 数据表、柱状图、运维仪表盘、看板、AI 时间线 |
| **技术底层** | ER 实体关系图、UML 类图、二叉搜索树/链表/栈、进程内存布局、项目目录树、数学公式推导、TCP/IP 协议栈、CPU 五级流水线、HTTP/2 包结构、能力雷达图、RESTful API 规范、公司组织架构 |

所有模板文件在 [`assets/examples/`](./assets/examples/) 目录。

---

## 工作原理

```
你说一句话 → Claude 画 ASCII 图 → 保存 .txt → 渲染为 PNG
                │                    │              │
                ▼                    ▼              ▼
           用 Unicode 制表符     纯文本文件     Maple Mono 字体
           ┌─┐│└┘╔═╗▸▼         对齐精确        + 主题配色渲染
```

核心特性：
- **制表符着色**：`┌─┐│└┘╔═╗▸▼` 等 Unicode 制表符自动渲染为主题强调色
- **CJK 完美对齐**：中文字符严格等于 2 倍 ASCII 宽度，不再错位
- **箭头不歪**：使用 `▸` (U+25B8) 而非 `→` (U+2192)，与横线 `─` 同基线
- **内置字体**：[Maple Mono NF CN](https://github.com/subframe7536/maple-font)，SIL OFL 许可证

---

## 项目结构

```
claude-code-asciishot/
├── SKILL.md                         # Skill 定义（触发条件 + 渲染方法）
├── scripts/
│   ├── render.py                    # 渲染引擎 (Pillow)
│   └── themes.py                    # 13 种主题定义
├── assets/
│   ├── fonts/                       # 内置 Maple Mono NF CN 字体
│   │   ├── MapleMono-NF-CN-Regular.ttf
│   │   └── MapleMono-NF-CN-Medium.ttf
│   └── examples/                    # 28 种 ASCII 图表模板
├── examples/                        # 渲染效果图 (56 张 PNG)
├── dist/
│   └── claude-code-asciishot.skill  # 打包好的 Skill 文件
└── README.md
```

---

## License

MIT

字体 [Maple Mono NF CN](https://github.com/subframe7536/maple-font) 采用 SIL Open Font License。

---

<p align="center">
  <sub>Made by <a href="https://github.com/jiangshu">@jiangshu</a></sub>
</p>
