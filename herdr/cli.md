# Herdr CLI 操作

查核日期：**2026-10-13**。本頁採官方 CLI 與 automation 文件；旗標以實際安裝版為準。本文的 POSIX shell 範例適用 macOS / Linux。

## 先查詢，再控制

這些操作範例應在 **Herdr 管理的 shell 窗格**執行。先確認環境：

```bash
test "${HERDR_ENV:-}" = 1
```

若 exit code 不是 0，先開啟 Herdr 並切到其中的 shell。環境欄位可查看：

```bash
printf '%s\n' "$HERDR_WORKSPACE_ID" "$HERDR_TAB_ID" "$HERDR_PANE_ID"
```

Herdr 會注入呼叫端脈絡，`--current` 用來指定發出命令的窗格。實際 ID 由 Herdr 回傳，不要假設一定是 `w1:p1`。[官方 CLI reference：Environment variables / Panes](https://herdr.dev/docs/cli-reference/)

先用 `herdr --help` 或命令群組查詢支援功能：

```bash
herdr pane
herdr agent
herdr workspace
```

不要用 `herdr workspace create` 之類的建立命令來試探說明；即使未給參數，也可能真的建立資源。

## 查閱目前版面

```bash
herdr workspace list
herdr tab list --workspace "$HERDR_WORKSPACE_ID"
herdr pane current --current
herdr pane list --workspace "$HERDR_WORKSPACE_ID"
herdr agent list
```

管理命令多數輸出 JSON；`pane read` 與 `agent read` 則輸出終端文字。[官方 CLI reference](https://herdr.dev/docs/cli-reference/)

## 建立另一個 shell 窗格

以下範例需要 `jq` 解析 JSON；請先確認 `command -v jq` 有結果。從目前 shell 往右分割，保留 cwd 與原來焦點：

```bash
split_result=$(herdr pane split --current --direction right --cwd "$PWD" --no-focus)
new_pane_id=$(printf '%s\n' "$split_result" | jq -er '.result.pane.pane_id')
```

確認兩行均成功，再送入普通 shell 指令並讀取畫面：

```bash
herdr pane run "$new_pane_id" "git status --short"
herdr pane read "$new_pane_id" --source recent-unwrapped --lines 80
```

`pane run` 會提交文字與 Enter；執行前須確認目標仍是可接受命令的 shell。若目標跑著編輯器或其他程序，輸入會送到該程序。窄窗格可改用 `--direction down`。[官方 Panes 指令](https://herdr.dev/docs/cli-reference/)

## 在另一個窗格啟動 OpenCode

沿用上面仍停在 shell 提示的 `$new_pane_id`：

```bash
herdr agent start doc-reviewer --kind opencode --pane "$new_pane_id"
herdr agent prompt doc-reviewer "請閱讀 README.md，只回報文字與連結問題，不修改檔案。" --wait --timeout 120000
herdr agent read doc-reviewer --source recent-unwrapped --lines 120
```

先完成 OpenCode 登入並設定 [整合](opencode-integration.md)。`agent start` 不會建立窗格；名稱須在執行中的 agents 之間唯一。`--timeout` 單位為毫秒。[官方 Agent automation](https://herdr.dev/docs/agent-automation/)

`--wait` 預設等到 `idle`、`done` 或 `blocked`，因此回傳後必須核對狀態與輸出。它追蹤生命週期，不追蹤特定一則提示；若 agent 本來就在工作，目前那輪完成也可能滿足等待。

遇到 `blocked`、timeout 或 `agent_prompt_stalled`，先用 `herdr agent get doc-reviewer` 與 `agent read` 查看狀況。超時不表示提示沒有送出，直接重送可能造成重複任務。[官方等待語意](https://herdr.dev/docs/agent-automation/)

Agent 名稱只是目前窗格內 agent 的別名；也能使用該 agent 所在的 pane ID。Agent 結束或被替換後別名會清除。[官方 Agents reference](https://herdr.dev/docs/cli-reference/)

## 進階功能入口

| 需求 | 官方文件 |
| --- | --- |
| 建立其他專案工作區或分頁 | [CLI：Workspaces / Tabs](https://herdr.dev/docs/cli-reference/) |
| 以獨立 Git checkout 分工 | [CLI：Worktrees](https://herdr.dev/docs/cli-reference/) |
| 遠端工作機與 SSH | [Connecting machines](https://herdr.dev/docs/connecting-machines/) |
| 自訂 agent 狀態整合 | [Integrations](https://herdr.dev/docs/integrations/) |

若多個 agent 同時修改程式，先分配不同檔案範圍，或使用不同 Git worktree；新增窗格本身不會隔離檔案修改。
