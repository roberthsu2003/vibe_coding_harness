# OpenCode V2 設定與自訂命令

查核日期：**2026-10-13**。以下範例供讀者放入自己的專案，未在此 repo 啟用任何 OpenCode 設定。

## 專案指示：AGENTS.md

在專案根目錄建立 `AGENTS.md`，記錄長期適用的規則，例如：

```markdown
# 專案協作規則

- 文件使用繁體中文。
- 描述 CLI 操作時，區分 shell 指令與 TUI 指令。
- 更新工具教學前查閱官方文件，記錄查核日期與來源。
- 修改 Markdown 後檢查相對連結與程式碼區塊。
```

OpenCode V2 會探索適用的 `AGENTS.md`，目前不以 `CLAUDE.md` 作為 fallback。專案指示可提交到 Git，讓團隊共用。[官方 Instructions](https://opencode.ai/v2/docs/instructions/)

## 專案設定：opencode.jsonc

一般專案可在根目錄放 `opencode.jsonc`；全域設定在 `~/.config/opencode/opencode.json(c)`。JSONC 支援註解與尾端逗號，`$schema` 可協助編輯器檢查欄位。[官方 Config](https://opencode.ai/v2/docs/config/)

以下是教學用權限範例：讀檔允許，編輯與 shell 執行先詢問，查閱 Git 狀態與差異可直接執行。

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "read", "resource": "*", "effect": "allow" },
    { "action": "edit", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "git diff *", "effect": "allow" }
  ]
}
```

V2 的規則由前往後處理，**最後符合的規則生效**。`allow` 直接執行、`ask` 詢問、`deny` 拒絕；沒有匹配規則時使用 `ask`。這是工具權限設定，不能取代作業系統層級隔離。[官方 Permissions](https://opencode.ai/v2/docs/permissions/)

## 可重複使用的 slash command

在目標專案新增 `.opencode/commands/doc-review.md`：

```markdown
---
description: 檢查文件的操作步驟與可讀性
---

請檢查 $ARGUMENTS。
使用繁體中文指出：操作步驟是否完整、版本是否清楚、來源是否可追溯。
先回報問題與建議，不修改檔案。
```

在 OpenCode TUI 執行：

```text
/doc-review README.md
```

`$ARGUMENTS` 會代入整段參數；這個命令會提交提示，工具可執行哪些操作仍取決於 agent 權限。全域命令可放在 `~/.config/opencode/commands/`。[官方自訂 Commands](https://opencode.ai/v2/docs/commands/)

## 設定檔各自負責什麼

| 檔案 | 用途 |
| --- | --- |
| `AGENTS.md` | 自然語言的專案協作規則 |
| `opencode.jsonc` | 模型、工具權限、MCP 等設定 |
| `.opencode/commands/*.md` | 常用提示的 slash command |
| `.opencode/agents/*.md` | 自訂 agent profile |
| `.opencode/skills/<名稱>/SKILL.md` | 可載入的工作流程與相關資源 |
| `~/.config/opencode/cli.json` | V2 全域終端介面設定 |

自訂 agent 與 skill 分別參考 [Agents](https://opencode.ai/v2/docs/agents/) 與 [Skills](https://opencode.ai/v2/docs/skills/)；新增設定後可用 `opencode debug config` 核對設定來源。[CLI 除錯命令](https://opencode.ai/v2/docs/cli/commands/)
