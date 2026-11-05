# 09　權限設定

> ★★★ 深入　｜　[← 08 Subagent 子代理](08-subagents.md)　｜　[章節首頁](README.md)　｜　下一站：[10 指令模式與 Herdr →](10-cli-run.md)

**這一站你會學到**：用 `opencode.json` 控制 AI 哪些事可以直接做、哪些要先問你、哪些完全禁止。

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

在子代理的 `.md` 檔開頭加上 `permissions`（見 [08 子代理](08-subagents.md)）：

```markdown
---
description: 審查改動，只讀不改
mode: subagent
permissions:
  - action: edit
    resource: "*"
    effect: deny
---
```

代理的規則會接在全域規則**後面**，所以優先權比較高。

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
| `.opencode/agents/*.md` | 專案內 | 自訂代理（見 [08](08-subagents.md)） |
| `~/.config/opencode/cli.json` | 全域 | 介面主題、快捷鍵（見 [04](04-config.md#調整介面clijson)） |

---

## ✅ 自我檢查

- [ ] 在練習專案建立 `opencode.json`，讓 `edit` 變成 `ask`
- [ ] 請 AI 修改檔案時，看到它先問你
- [ ] 用 `opencode debug config` 確認設定

> 下一站：[10 指令模式與 Herdr →](10-cli-run.md)
