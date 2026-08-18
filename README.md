# Skills

这是一个可持续扩展的多 skill 仓库。每个 skill 都独立放在 `skills/<skill-name>/` 下；仓库级辅助工具放在根目录 `scripts/` 下。

目录布局遵循 [Agent Skills 规范](https://agentskills.io/specification) 和 [OpenAI Skills](https://github.com/openai/skills) 的多 skill 仓库组织方式。

## 仓库结构

```text
.
├── README.md
├── skills/
│   └── design-spec-generator/
│       ├── SKILL.md
│       ├── evals/
│       │   └── evals.json
│       ├── references/
│       │   ├── design-contract.md
│       │   └── product-archetypes.md
│       └── scripts/
│           └── validate_output.py
└── scripts/
    └── download_previews.py
```

## Skills 目录

| Skill | 用途 | 入口 |
|---|---|---|
| `design-spec-generator` | 从源码、截图、URL 或需求描述生成设计规范与亮色/暗色预览 | [SKILL.md](skills/design-spec-generator/SKILL.md) |

## 使用与安装

本仓库的 `skills/` 是 skill 源码集合。需要让 Codex 自动发现某个 skill 时，将对应目录复制或链接到以下位置之一：

- 用户级：`$HOME/.agents/skills/<skill-name>/`
- 项目级：`<target-repository>/.agents/skills/<skill-name>/`

例如，在目标仓库中安装当前 skill：

```bash
mkdir -p .agents/skills
cp -R /path/to/this-repository/skills/design-spec-generator \
  .agents/skills/design-spec-generator
```

每个安装目录中都应直接包含 `SKILL.md`，不要把整个多 skill 仓库复制为一个 skill。

### Design Spec Generator

[design-spec-generator](skills/design-spec-generator/SKILL.md) 将项目源码、功能截图、网站 URL 或需求描述整理成可直接指导界面实现的设计规范。

默认输出：

```text
DESIGN/
├── DESIGN.md
├── preview.html
└── preview-dark.html
```

用户指定其他目录名时，skill 会使用用户提供的名称。支持后端管理、移动端 App、门户网站、落地页、AIGC 产品和大屏等产品形态。

相关资料：

- [输出格式规范](skills/design-spec-generator/references/design-contract.md)
- [产品形态指南](skills/design-spec-generator/references/product-archetypes.md)
- [测试场景](skills/design-spec-generator/evals/evals.json)
- [输出校验脚本](skills/design-spec-generator/scripts/validate_output.py)

校验生成结果：

```bash
python3 skills/design-spec-generator/scripts/validate_output.py DESIGN
```

## 共享脚本

### Git 仓库资料抓取

[scripts/download_previews.py](scripts/download_previews.py) 从远程 Git 仓库或本地 Git 工作树收集每套设计的 `DESIGN.md`、`preview.html` 和 `preview-dark.html`。

直接抓取默认的 `VoltAgent/awesome-design-md` 仓库：

```bash
python3 scripts/download_previews.py --output-dir design-md
```

抓取其他远程仓库或分支：

```bash
python3 scripts/download_previews.py https://github.com/example/design-repo.git \
  --ref main \
  --source-dir design-md \
  --output-dir design-md
```

读取本地仓库，只复制仓库中已经存在的文件，不访问预览网站：

```bash
python3 scripts/download_previews.py /path/to/local/repository \
  --repo-only \
  --output-dir design-md
```

只抓取指定设计，可重复使用 `--only`：

```bash
python3 scripts/download_previews.py --only airbnb --only linear.app
```

脚本默认优先读取仓库文件。仓库缺少预览文件时，它会从相邻 README 中提取预览链接；如果 README 只提供设计详情页，则继续解析详情页中的预览 iframe。

## 新增 Skill

新增 skill 时使用独立的 kebab-case 目录名：

```text
skills/<skill-name>/
├── SKILL.md              # 必需：name、description 和工作流说明
├── agents/               # 可选：UI 元数据和工具依赖
├── references/           # 可选：规范、背景资料和示例
├── scripts/              # 可选：仅供该 skill 使用的确定性脚本
├── assets/               # 可选：模板、图标、字体等静态资源
└── evals/                # 可选：测试提示和期望结果
```

约定：

- `SKILL.md` frontmatter 中的 `name` 与目录名保持一致。
- skill 专用资源和脚本放在该 skill 目录内，避免与其他 skill 隐式耦合。
- 只有多个 skill 都会使用的维护工具才放到根级 `scripts/`。
- 在本 README 的 Skills 目录表中登记新 skill。
- 提交前验证 `SKILL.md`、相对链接、脚本参数和至少一个代表性输出。
