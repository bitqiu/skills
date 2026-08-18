# Design Skills Workspace

这个仓库用于维护能够生成 `DESIGN.md` 与可视化预览的 Codex skills，以及相关的资料抓取和输出校验工具。

## 导航

```text
.
├── readme.md
├── design-spec-generator/
│   ├── SKILL.md
│   ├── evals/
│   │   └── evals.json
│   ├── references/
│   │   ├── design-contract.md
│   │   └── product-archetypes.md
│   └── scripts/
│       └── validate_output.py
└── scripts/
    └── download_previews.py
```

### Design Spec Generator

[design-spec-generator/SKILL.md](design-spec-generator/SKILL.md) 将项目源码、功能截图、网站 URL 或需求描述整理成可直接指导界面实现的设计规范。

默认输出：

```text
DESIGN/
├── DESIGN.md
├── preview.html
└── preview-dark.html
```

用户指定其他目录名时，skill 会使用用户提供的名称。支持后端管理、移动端 App、门户网站、落地页、AIGC 产品和大屏等产品形态。

相关资料：

- [输出格式规范](design-spec-generator/references/design-contract.md)
- [产品形态指南](design-spec-generator/references/product-archetypes.md)
- [测试场景](design-spec-generator/evals/evals.json)
- [输出校验脚本](design-spec-generator/scripts/validate_output.py)

校验生成结果：

```bash
python3 design-spec-generator/scripts/validate_output.py DESIGN
```

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
