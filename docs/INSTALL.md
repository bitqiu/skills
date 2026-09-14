# 安装教程

## 环境要求

- Git
- POSIX Shell（macOS、Linux 或 WSL）
- Python 3（用于仓库校验和锁文件更新）

## 从本地仓库安装

在仓库根目录执行：

```sh
./scripts/install.sh
```

默认安装到 `$HOME/.codex/skills/product-engineering`。可通过环境变量指定目录：

```sh
SKILLS_HOME="$HOME/.codex/skills/product-engineering" ./scripts/install.sh
```

脚本会复制 flat namespace 下的全部 Skill，并在安装前运行 `validate-skills.sh`。如需覆盖已有目录：

```sh
FORCE=1 ./scripts/install.sh
```

## 手动安装

将 `skills/` 下的每个 Skill 目录复制到 Agent 平台的 Skills 目录，保持目录名与 `SKILL.md` 中的 `name` 一致。不要复制 `.skill-drafts/`、`registry/` 或 `workflows/` 到运行时目录。

## 更新公开仓库 Skill

```sh
./scripts/sync-upstream.sh
```

脚本会拉取 Matt Pocock/skills 和 obra/superpowers 的最新提交，并更新 `UPSTREAM.lock.json`。同步后重新安装即可：

```sh
FORCE=1 ./scripts/install.sh
```

## 验证安装

```sh
./scripts/validate-skills.sh
./scripts/list-skills.sh
```

看到 `PASS` 且能列出 Skill 路径，即表示仓库内容有效。
