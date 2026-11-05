# 05　Skill 配置

> ★★ 進階　｜　[← 04 環境配置](04-config.md)　｜　[章節首頁](README.md)　｜　下一站：[06 AGENTS.md 專案規則 →](06-agents-md.md)

**這一站你會學到**：Skill 是什麼、放在哪裡、`SKILL.md` 怎麼寫，以及如何建立、使用和管理自己的 Skill。

![Skill 的運作方式](assets/skill-flow.svg)

---

## 1. Skill 是什麼？

**Skill 就像交給 AI 的一份工作手冊。** 你把某件事的做法寫下來，之後 AI 遇到這件事就會翻開手冊照做，你不用每次重新交代。

它和另外兩個功能很像，差別在這裡：

| | `AGENTS.md`（規則） | 斜線指令 | Skill（工作手冊） |
| :--- | :--- | :--- | :--- |
| **何時作用** | 每次對話都載入 | 你輸入 `/指令` 時 | AI 判斷需要時，或你用 `@` 指定時 |
| **適合內容** | 永遠要遵守的規矩 | 常打的一段話 | 特定工作的步驟 |
| **例子** | 一律用繁體中文回覆 | `/hello 小明` | 怎麼寫週報、怎麼部署網站 |

> [!TIP]
> 同一件事交代 AI 超過兩次，就值得做成 Skill。

---

## 2. Skill 放在哪裡？

每個 Skill 是一個資料夾，裡面一定要有 `SKILL.md`。

| 範圍 | 位置 | 誰能用 |
| :--- | :--- | :--- |
| **專案** | `.opencode/skills/<skill 名稱>/SKILL.md` | 這個專案，可用 Git 分享給同學 |
| **全域** | `~/.config/opencode/skills/<skill 名稱>/SKILL.md` | 你電腦上的所有專案 |

OpenCode 也會讀取其他工具的 Skill 資料夾，所以裝過就能共用：

| 來源 | 專案 | 全域 |
| :--- | :--- | :--- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| 通用格式 | `.agents/skills/` | `~/.agents/skills/` |

> [!NOTE]
> `.opencode`、`.claude` 前面都有一個點，所以 Finder 預設看不到（按 `Cmd+Shift+.` 可以顯示）。

---

## 3. 方法一：一句話請 AI 建立（推薦）

不用自己寫檔案，用中文說明你要什麼：

```text
請幫我在這個專案建立一個 OpenCode skill，名稱叫 weekly-report，放在 .opencode/skills/ 底下，用途是把我這週做的事整理成繁體中文週報，分成「完成事項」「遇到問題」「下週計畫」三段。
```

AI 會建立 `.opencode/skills/weekly-report/SKILL.md`。打開看一下，不滿意就繼續用中文要求修改。

接著就能試用了。在輸入框打 `@week`，從選單選右邊標示 **skill** 的項目：

```text
@weekly-report 這週完成了登入頁面，但部署時遇到權限錯誤，下週要做購物車
```

送出後畫面會顯示 `skill  weekly-report`，代表 AI 已經讀了這份手冊。

> [!NOTE]
> 如果選單裡沒有出現，輸入 `/reload` 重新載入，再用 `/skills` 確認。

---

## 4. 方法二：自己寫 `SKILL.md`

### 最小範例

建立 `.opencode/skills/commit-message/SKILL.md`：

```markdown
---
name: commit-message
description: 撰寫 Git commit 訊息時使用，產生繁體中文、格式一致的訊息
---

請依照以下步驟撰寫 commit 訊息：

1. 執行 git diff --staged，看這次改了什麼。
2. 第一行用「類型: 摘要」的格式，類型只能是 feat、fix、docs。
3. 摘要使用繁體中文，不超過 50 個字。
4. 把訊息給我看，等我同意才能 commit。
```

分成兩個部分：

- **`---` 中間**：Skill 的基本資料。
- **`---` 下面**：AI 實際要照做的內容。

### 欄位說明

| 欄位 | 用途 | 寫法建議 |
| :--- | :--- | :--- |
| `name` | 顯示的名稱 | 和資料夾名稱相同 |
| `description` | **最重要**。AI 靠它判斷要不要用這個 Skill | 寫清楚「什麼時候用」和「會做什麼」 |
| `disable-model-invocation` | 設成 `true` 時，AI 不會自動使用，只有你用 `@` 才會觸發 | 用在有風險的工作，例如部署 |

> [!IMPORTANT]
> **沒有寫 `description`，AI 就不會知道有這個 Skill。** 只有你自己用 `@` 能叫到它。

### 取名規則

名稱由**資料夾名稱**決定，建議只用小寫英文、數字和連字號：

| 名稱 | 可以嗎 |
| :--- | :--- |
| `weekly-report` | ✅ |
| `git-release-2` | ✅ |
| `Weekly_Report` | ❌ 不要用大寫和底線 |
| `週報` | ❌ 不要用中文，換到其他工具可能無法使用 |

### `description` 怎麼寫？

| 寫法 | 評語 |
| :--- | :--- |
| `週報` | ❌ 太短，AI 不知道什麼時候該用 |
| `幫忙處理文件` | ❌ 太模糊，什麼文件都可能符合 |
| `當使用者要整理本週工作或寫週報時使用，產生三段式的繁體中文週報` | ✅ 時機和成果都很清楚 |

---

## 5. 怎麼使用 Skill？

| 方式 | 怎麼做 | 範例 |
| :--- | :--- | :--- |
| **讓 AI 自己判斷** | 直接說需求，符合 `description` 就會自動使用 | `幫我把這週做的事寫成週報` |
| **用 `@` 指定** | 打 `@`，選標示 **skill** 的項目 | `@weekly-report 這週做了登入頁面` |
| **用中文指定** | 在句子裡說要用哪個 Skill | `請使用 weekly-report 這個 skill 整理週報` |

> [!NOTE]
> OpenCode 的 Skill 不是斜線指令，`/weekly-report` 不會觸發它（除非你另外做了同名的自訂指令）。

---

## 6. 附上腳本和範本

Skill 資料夾裡可以放其他檔案，AI 只有在 `SKILL.md` 叫它看的時候才會讀：

```text
weekly-report/
├── SKILL.md            ← 必要：主要的工作說明
├── references/         ← 參考資料
│   └── 範例週報.md
└── scripts/            ← 可以執行的腳本
    └── count_commits.sh
```

要在 `SKILL.md` 裡寫清楚什麼時候用：

```markdown
格式請參考 references/範例週報.md。
先執行 scripts/count_commits.sh 取得本週的 commit 數量。
```

> [!WARNING]
> Skill 裡的腳本會在你的電腦上執行。從網路下載別人的 Skill 前，先把內容看過一遍。

---

## 7. 管理 Skill

### 查看

```text
/skills
```

列出所有可用的 Skill。全域安裝的也會列出來，所以可能比你想的多。

### 修改

用中文請 AI 改，改完再試一次：

```text
請修改 weekly-report 這個 skill，在週報最後多加一段「需要協助的事情」。
```

### 刪除

直接刪除那個 Skill 的資料夾：

```text
請刪除這個專案的 weekly-report skill，刪除前先讓我確認要刪哪個資料夾。
```

### 限制 AI 使用哪些 Skill（進階）

在 `opencode.json` 用權限規則控制，規則的寫法見 [09 權限設定](09-permissions.md)：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    // 所有 skill 都要先問我
    { "action": "skill", "resource": "*", "effect": "ask" },
    // 這個可以直接用
    { "action": "skill", "resource": "commit-message", "effect": "allow" },
    // internal- 開頭的完全禁止
    { "action": "skill", "resource": "internal-*", "effect": "deny" }
  ]
}
```

---

## 8. Skill 沒有作用？

| 現象 | 先檢查 |
| :--- | :--- |
| `/skills` 看不到 | 檔名是不是全大寫的 `SKILL.md`？資料夾放對位置了嗎？再輸入 `/reload` 試試 |
| 看得到，但 AI 不會自動用 | `description` 寫得夠清楚嗎？有沒有設定 `disable-model-invocation`？ |
| 用 `@` 找不到 | 選單裡要選標示 **skill** 的項目，不要選到同名的檔案 |
| AI 拒絕使用 | 權限是不是設成 `deny` 了？ |
| 內容不是你剛寫的版本 | 其他位置有沒有同名的 Skill？`.opencode/skills/` 會蓋過 `.claude/skills/` |

---

## ✅ 動手練習

1. 輸入 `/skills`，看看現在有哪些 Skill。
2. 用一句話請 AI 建立 `weekly-report`。
3. 打開 `SKILL.md`，找到 `name`、`description` 和內文。
4. 用 `@weekly-report` 試用，確認畫面顯示 `skill  weekly-report`。
5. 不用 `@`，改說「幫我寫這週的週報」，看 AI 會不會自動使用。
6. 請 AI 幫週報多加一段，再試一次。

> 下一站：[06 AGENTS.md 專案規則 →](06-agents-md.md)
