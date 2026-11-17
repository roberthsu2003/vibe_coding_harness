# 08　權限設定

> ★★★ 深入　｜　[← 07 Subagent 子代理](07-subagents.md)　｜　[章節首頁](README.md)　｜　下一站：[09 指令模式與 Herdr →](09-cli-run.md)

**這一站你會學到**：用 `opencode.json` 控制 AI 哪些事可以直接做、哪些要先問你、哪些完全禁止。

---

## 開始前：建立本節練習資料夾

先完成[課堂練習準備](../practice/README.md)的工具確認與教材下載，再在**一般終端機**逐行執行：

```bash
python3 ~/terminal-ai-course/practice/prepare.py ~/terminal-ai-labs/opencode/08
cd ~/terminal-ai-labs/opencode/08
opencode
```

看到目的資料夾已存在時，直接 `cd` 進去接續；要重做則把路徑最後一段改成 `08-retry`。本節的程式、筆記與初始 Git commit 都已準備好。

---

## 1. 為什麼要設權限？

> [!WARNING]
> OpenCode **預設幾乎什麼都直接做**，包含修改檔案和執行指令，只有讀取 `.env` 這類機密檔案時會先問你。想要多一層保護，就要自己設定。

最簡單的方式是用一句話請 AI 設定：

```text
請修改這個專案的 opencode.json：改檔案和執行指令前都要先問我，git status 和 git diff 可以直接執行，rm 完全禁止。
```

## 2. 三種效果

| 值 | 意思 |
| :--- | :--- |
| `allow` | 直接執行，不問 |
| `ask` | 先問你，你同意才執行 |
| `deny` | 禁止 |

AI 問你的時候有三個選擇：

| 選擇 | 意思 |
| :--- | :--- |
| `once` | 只同意這一次 |
| `always` | 同意，以後在這個專案遇到類似的操作都不再問 |
| `reject` | 拒絕 |

## 3. 範例

權限是一條一條的規則，每條規則有三個部分：

- **`action`**：什麼動作，例如 `edit`（改檔案）、`shell`（執行指令）。
- **`resource`**：針對什麼，例如檔案路徑、指令內容，`*` 表示全部。
- **`effect`**：怎麼處理，也就是 `allow`、`ask`、`deny`。

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    // 修改檔案前先問我
    { "action": "edit", "resource": "*", "effect": "ask" },
    { "action": "edit", "resource": "*protected.txt", "effect": "deny" },

    // 執行指令：預設先問
    { "action": "shell", "resource": "*", "effect": "ask" },
    // 安全的指令直接允許
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "git diff *", "effect": "allow" },
    { "action": "shell", "resource": "uv run pytest *", "effect": "allow" },
    // 危險的指令禁止
    { "action": "shell", "resource": "rm *", "effect": "deny" }
  ]
}
```

> [!IMPORTANT]
> 規則的順序很重要：**最後一條符合的規則生效**。所以要把通用的 `"*"` 放在最前面，特別的規則放在後面。

> `git status *` 也包含沒有參數的 `git status`。

### 完整小範例：三種權限各測一次

1. 在本章練習專案，用編輯器將上面的 JSONC 存成 `opencode.jsonc`（若已有 `opencode.json`，則合併到那份檔案，避免同時維護兩份）。
2. 輸入 `/reload`，必要時離開再啟動；使用 Build，且不要加 `--auto`。
3. 一次送出一列：

| 在 OpenCode 輸入框送出 | 預期結果與檢查 |
| :--- | :--- |
| `請實際執行 git status --short。` | 因 allow 規則直接執行 |
| `請在 reading-notes.md 最後加上「今天完成權限練習」。` | 出現 edit 詢問，選 `once`；用 `cat reading-notes.md` 確認新增文字 |
| `請用檔案修改工具把 protected.txt 改成「已修改」；若被拒絕就停止，不要換用 shell。` | 因 deny 規則被拒絕；`cat protected.txt` 應保持原文 |

只選 `once`，方便重做時再次看到詢問。若已有持續授權，改用新的 `08-retry` 練習專案測試。

**收尾**：只刪除本次新增的權限規則，再 `/reload`；若本次才建立設定檔，可將檔案改名為 `opencode.jsonc.bak` 後重載，保留作業紀錄。

## 4. 常用的動作

| `action` | 控制什麼 | `resource` 比對什麼 |
| :--- | :--- | :--- |
| `read` | 讀檔案 | 檔案路徑 |
| `edit` | 新增和修改檔案 | 檔案路徑 |
| `shell` | 執行指令 | 指令內容 |
| `subagent` | 派工給子代理 | 代理名稱 |
| `skill` | 載入 [Skill](05-skills.md) | Skill 名稱 |
| `webfetch` | 讀取網頁 | 網址 |
| `websearch` | 上網搜尋 | 搜尋字詞 |

## 5. 只限制某個代理

在子代理的 `.md` 檔開頭加上 `permissions`（見 [07 子代理](07-subagents.md)）：

```markdown
---
description: 審查改動，只讀不改
mode: subagent
permissions:
  - action: edit
    resource: "*"
    effect: deny
---

請審查指定檔案，只回報問題與行號，不要修改檔案。
```

代理的規則會接在全域規則**後面**，所以優先權比較高。

**實作驗證代理權限**：將上面的完整 Markdown 存成 `.opencode/agents/readonly-lab.md`，先執行 `mkdir -p .opencode/agents` 建立資料夾。輸入 `/reload`，送出 `@readonly-lab 請檢查 calc.py 除以零時會怎樣，只回報，不要修改。`。**驗收**：子代理回報邊界問題，`git diff -- calc.py` 無輸出。練完將檔案移出 `agents/`，重載後 `@readonly-lab` 不再出現。

## 6. 確認設定有生效

```bash
opencode debug config
```

會列出 OpenCode 讀到的每一份設定。設定檔放在哪裡，見 [04 環境配置](04-config.md#2-設定檔放在哪裡)。

> [!WARNING]
> 上面的輸出可能包含 API Key，不要整段貼給別人。

> [!NOTE]
> **`--auto` 參數**會自動同意所有沒有被明確 `deny` 的操作（`opencode --auto`、`opencode run --auto`）。練習時不要用，自動化時也要先設好 `deny` 規則。

---

## 設定檔一覽

| 檔案 | 放哪裡 | 用途 |
| :--- | :--- | :--- |
| `AGENTS.md` | 專案根目錄 | 用中文寫的專案規則（見 [06](06-agents-md.md)） |
| `opencode.json` | 專案根目錄 | 權限、預設模型、MCP（見 [04](04-config.md)） |
| `.opencode/commands/*.md` | 專案內 | 自訂斜線指令（見 [03](03-slash-commands.md)） |
| `.opencode/skills/*/SKILL.md` | 專案內 | 自訂 Skill（見 [05](05-skills.md)） |
| `.opencode/agents/*.md` | 專案內 | 自訂代理（見 [07](07-subagents.md)） |
| `~/.config/opencode/cli.json` | 全域 | 介面主題、快捷鍵（見 [04](04-config.md#調整介面clijson)） |

---

## ✅ 自我檢查

- [ ] 在練習專案建立 `opencode.json`，讓 `edit` 變成 `ask`
- [ ] 請 AI 修改檔案時，看到它先問你
- [ ] 用 `opencode debug config` 確認設定

> 下一站：[09 指令模式與 Herdr →](09-cli-run.md)
