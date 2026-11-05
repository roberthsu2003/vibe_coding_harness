# 03　斜線指令

> ★ 入門　｜　[← 02 基本操作](02-basics.md)　｜　[章節首頁](README.md)　｜　下一站：[04 環境配置 →](04-config.md)

**這一站你會學到**：什麼是斜線指令、新手必學的 8 個指令、每個內建指令的小範例，以及怎麼做出自己的斜線指令。

![斜線指令地圖](assets/slash-map.svg)

---

## 1. 怎麼使用斜線指令？

斜線指令（Slash Command）是 OpenCode 輸入框裡的快捷功能，以 `/` 開頭。

1. 在輸入框打 `/`，會跳出指令選單。
2. 繼續打字可以篩選，例如打 `/un` 會看到 `/undo`。
3. 按 `Enter` 執行。

有些指令可以接一句話，例如：

```text
/btw 剛才提到的 uv 是什麼？
```

> [!TIP]
> **按了 `Enter`，指令還留在輸入框？** 這是在等你補上內容。補完或直接再按一次 `Enter` 就會送出。

> [!NOTE]
> 選單會隨情況變化。`/undo`、`/compact`、`/copy`、`/export`、`/fork`、`/rename`、`/timeline`、`/terminal` 要**對話開始後**才會出現，`/redo` 則要先 `/undo` 過。剛啟動時找不到它們是正常的。

---

## 2. 新手必學 8 個指令

| 指令 | 一句話說明 | 什麼時候用 |
| :--- | :--- | :--- |
| [`/connect`](#connect連接模型供應商) | 連接模型供應商 | 第一次使用、登入失效時 |
| [`/models`](#models切換模型) | 切換模型 | 模型太慢或無法使用時 |
| [`/init`](#init產生專案規則) | 產生專案規則 | 進到新專案時 |
| [`/undo`](#undo復原上一步) | 復原上一步 | AI 改壞東西時 |
| [`/diff`](#diff看-ai-改了什麼) | 看 AI 改了什麼 | AI 改完檔案後 |
| [`/compact`](#compact壓縮對話) | 壓縮對話 | 對話太長、AI 開始忘東忘西時 |
| [`/new`](#new開新對話) | 開新對話 | 換一個新任務時 |
| [`/exit`](#exit離開-opencode) | 離開 OpenCode | 下課時 |

> [!TIP]
> 不用背！忘記指令時打 `/` 看選單，或按 `Ctrl+P` 開指令面板。

---

## 3. A 區：連線與模型

### `/connect`：連接模型供應商

```text
/connect
```

**結果**：列出所有供應商，已連接的前面有 ✓。選一個後依畫面登入或貼上 API Key。

### `/models`：切換模型

```text
/models
```

**結果**：開啟模型清單，免費模型右邊標示 `Free`。直接打字可以搜尋，例如打 `free`。按 `Ctrl+F` 可以加入最愛。快捷鍵：`Ctrl+X` → `M`。

### `/variants`：調整思考強度

```text
/variants
```

**結果**：選擇 `low`、`medium`、`high` 等強度（要看模型支不支援）。越高通常想得越久。別名：`/thinking`、`/effort`。按 `Ctrl+T` 可以直接切換下一個。

### `/agents`：切換代理

```text
/agents
```

**結果**：選擇主代理，例如 `build`（會動手改）或 `plan`（只規劃）。按 `Shift+Tab` 可以直接輪流切換。

### `/skills`：查看可用的 Skill

```text
/skills
```

**結果**：列出這個專案能用的所有 Skill 和說明。Skill 是什麼，見 [05 Skill 配置](05-skills.md)。

### `/mcps`：查看 MCP 伺服器

```text
/mcps
```

**結果**：列出 MCP 伺服器和連線狀態。連線失敗的會標示 `Failed`，按 `Space` 可以重試。MCP 是什麼，見 [04 環境配置](04-config.md#5-mcp讓-ai-使用外部工具)。

---

## 4. B 區：專案規則與檢查

### `/init`：產生專案規則

```text
/init 請用繁體中文撰寫，並記錄這個專案用 uv 管理套件
```

**結果**：AI 閱讀專案後，建立或更新 `AGENTS.md`。後面那句話可以省略，有寫的話 AI 會照著做。完整說明見 [06 AGENTS.md 專案規則](06-agents-md.md)。

### `/diff`：看 AI 改了什麼

```text
/diff
```

**結果**：開啟差異檢視器，綠色 `+` 是新增的行，紅色 `-` 是刪除的行。按 `Esc` 或 `q` 關閉。

### `/review`：請 AI 審查程式

```text
/review
```

**結果**：AI 檢查目前還沒 commit 的改動，指出問題和修改建議。也可以指定審查對象：

```text
/review main
```

後面可以接 commit 編號、分支名稱，或 PR 編號。

---

## 5. C 區：復原與對話管理

### `/undo`：復原上一步

請 AI 建立一個小檔案，然後輸入：

```text
/undo
```

**結果**：撤銷你上一則訊息和 AI 之後做的事，畫面顯示 `1 message reverted`，剛才的訊息會回到輸入框讓你修改。可以連續執行好幾次。快捷鍵：`Ctrl+X` → `U`。

### `/redo`：把復原做回來

```text
/redo
```

**結果**：恢復剛才 `/undo` 掉的內容。如果 `/undo` 之後已經送出新訊息，就不能再 `/redo` 了。快捷鍵：`Ctrl+X` → `R`。

### `/compact`：壓縮對話

```text
/compact
```

**結果**：把前面的對話整理成摘要，騰出空間，還能繼續做同一件事。快捷鍵：`Ctrl+X` → `C`。

### `/new`：開新對話

```text
/new
```

**結果**：開一段全新的對話，AI 不記得剛才聊過什麼。舊對話沒有消失，可以用 `/sessions` 找回。快捷鍵：`Ctrl+X` → `N`。

### `/clear`：清空畫面，回到首頁

```text
/clear
```

**結果**：回到 OpenCode 的首頁，下一則訊息會是新的對話，目前選的模型和代理不變。效果和 `/new` 很接近，用哪個都可以。

### `/sessions`：找回舊對話

```text
/sessions
```

**結果**：列出這個專案的舊對話，選一個就能繼續。在清單裡按 `Ctrl+R` 改名、`Ctrl+D` 刪除、`Ctrl+A` 看所有專案。別名：`/resume`、`/continue`。快捷鍵：`Ctrl+X` → `L`。

### `/rename`：幫對話改名

```text
/rename 登入功能
```

**結果**：把目前的對話改名，之後在 `/sessions` 比較好找。

### `/timeline`：跳到之前的訊息

```text
/timeline
```

**結果**：列出這段對話裡你送出的訊息和時間，選一則就跳過去。快捷鍵：`Ctrl+X` → `G`。

### `/fork`：從這裡分岔

```text
/fork
```

**結果**：選擇整段對話或某一則訊息，複製出一段新對話。想試另一種做法、又不想弄亂原本的對話時很好用。

### `/copy`：複製 AI 最後的回答

```text
/copy
```

**結果**：把 AI 最後一則回答複製到剪貼簿，畫面顯示 `Message copied to clipboard!`。

### `/export`：匯出對話

```text
/export
```

**結果**：選擇 Markdown 或 JSON 格式，以及要不要包含思考過程和工具紀錄，然後複製或匯出。適合用來交作業或留筆記。快捷鍵：`Ctrl+X` → `X`。

---

## 6. D 區：輸入輔助

### `/btw`：問個題外話

```text
/btw AGENTS.md 是什麼？
```

**結果**：回答會顯示在彈出視窗，**不會加進對話**，也不影響 AI 手上的工作。正適合隨口問問。

### `/editor`：用編輯器寫長訊息

```text
/editor
```

**結果**：開啟你的文字編輯器。寫完存檔、關閉後，內容會回到輸入框，再按 `Enter` 送出。要先設定 `EDITOR`，見 [04 環境配置](04-config.md#4-環境變數)。快捷鍵：`Ctrl+X` → `E`。

### `/terminal`：開一個終端機

```text
/terminal
```

**結果**：在 OpenCode 裡開一個終端機窗格，可以直接打 shell 指令。

> [!NOTE]
> 開啟後，鍵盤輸入會進到終端機。如果指令打下去出現 `no such file or directory`，就是你正在終端機裡。

---

## 7. E 區：切換位置

### `/open`：切換專案

```text
/open
```

**結果**：列出最近的對話和專案，選一個就切換過去。別名：`/project`、`/projects`。

### `/cd`：切換工作資料夾

```text
/cd src
```

**結果**：邊打邊出現符合的資料夾，選好後切換過去。

### `/worktrees`：管理 Git Worktree

```text
/worktrees
```

**結果**：列出這個專案的 worktree。按 `Ctrl+A` 新增、`Ctrl+D` 刪除。Worktree 是什麼，見 [Branch 與 Worktree](../worktree/README.md)。

### `/pair`：用手機或瀏覽器連線

```text
/pair
```

**結果**：顯示連結和 QR Code，讓瀏覽器或手機連到這個 OpenCode。別名：`/web`。

> [!WARNING]
> 這個連結等於進入你電腦的通行證，不要分享給別人，也不要截圖貼到群組。

---

## 8. F 區：查狀態與設定

### `/help`：看怎麼找指令

```text
/help
```

**結果**：提醒你按 `Ctrl+P` 查看所有指令。實際要找指令時，直接打 `/` 或按 `Ctrl+P` 更快。

### `/status`：看目前狀態

```text
/status
```

**結果**：顯示 MCP 伺服器等連線狀態。覺得哪裡怪怪的時候，先來這裡看。快捷鍵：`Ctrl+X` → `S`。

### `/stats`：看使用統計

```text
/stats
```

**結果**：顯示 token 用量圖表、活躍天數和對話次數。

### `/debug`：看除錯資訊

```text
/debug
```

**結果**：顯示版本、作業系統、終端機和目前的模型。向老師或同學求助時，把這些資訊一起附上。

### `/themes`：換介面主題

```text
/themes
```

**結果**：列出所有主題，選一個就能換上。快捷鍵：`Ctrl+X` → `T`。

### `/settings`：開啟設定

```text
/settings
```

**結果**：開啟設定畫面，用 `←`、`→` 調整主題、側邊欄、思考過程顯示等選項。

### `/plugins`：查看外掛

```text
/plugins
```

**結果**：列出已安裝的外掛。

### `/reload`：重新載入設定

```text
/reload
```

**結果**：重新讀取設定檔，不用關掉 OpenCode。改了設定卻沒生效時先試這個。

### `/highlights`：看新版亮點

```text
/highlights
```

**結果**：再次顯示這個版本的更新重點。

### `/update`：更新 OpenCode

```text
/update
```

**結果**：檢查並安裝新版本。畫面上出現 `/update to install v…` 時就是有新版了。

### `/exit`：離開 OpenCode

```text
/exit
```

**結果**：離開 OpenCode。對話會保留，下次用 `/sessions` 就能接著做。別名：`/quit`、`/q`，也可以按 `Ctrl+C`。

---

## 9. 做一個自己的斜線指令

同一段話老是要重打？把它做成斜線指令。

### 方法一：一句話請 AI 建立（推薦）

```text
請幫我建立一個 OpenCode 自訂斜線指令 /explain，放在 .opencode/commands/，功能是用國中生聽得懂的繁體中文解釋我指定的檔案。
```

AI 會建立 `.opencode/commands/explain.md`。之後這樣用：

```text
/explain src/app.py
```

### 方法二：自己建立檔案

每個 `.md` 檔就是一個指令，**檔名就是指令名稱**。

| 範圍 | 位置 |
| :--- | :--- |
| 這個專案 | `.opencode/commands/` |
| 所有專案 | `~/.config/opencode/commands/` |

**範例：`.opencode/commands/hello.md`**

```markdown
---
description: 用一句話跟某人打招呼
---
請用一句繁體中文跟 $ARGUMENTS 打招呼。
```

存檔後不用重新啟動。打 `/hello 小明`，AI 實際收到的是：

```text
請用一句繁體中文跟 小明 打招呼。
```

### 指令裡可以放什麼？

| 寫法 | 意思 | 範例 |
| :--- | :--- | :--- |
| `$ARGUMENTS` | 指令後面的全部文字 | `/hello 小明` → `小明` |
| `$1`、`$2` | 第 1、第 2 段文字。最後一個會拿走剩下的全部 | `/pos 甲 乙 丙` → `$1` 是 `甲`，`$2` 是 `乙 丙` |
| `` !`指令` `` | 先執行 shell 指令，把結果放進內容 | `` !`git status` `` |

如果內容裡沒有 `$ARGUMENTS`，你多打的文字會自動接在最後面。

**範例：整理今天的工作（`.opencode/commands/today.md`）**

```markdown
---
description: 根據 Git 紀錄整理今天做了什麼
---
這是最近的 commit：
!`git log --oneline -10`

請用繁體中文條列今天完成的事情。
```

> [!WARNING]
> `` !`指令` `` 會**直接執行，不會先問你**。只用自己看得懂的指令，也不要把別人給的內容放進去。

### 常用設定欄位

開頭 `---` 中間的欄位都可以省略：

| 欄位 | 用途 | 範例 |
| :--- | :--- | :--- |
| `description` | 顯示在選單上的說明 | `description: 打招呼` |
| `agent` | 指定由哪個代理執行 | `agent: plan` |
| `model` | 指定模型 | `model: opencode/nemotron-3.5-lightning-free` |
| `subagent` | `true` 時交給子代理在背景做，不佔用主對話 | `subagent: true` |

> [!NOTE]
> 指令檔裡的 `@檔名` **不會**自動展開。要附檔案時，在打指令時從輸入框用 `@` 選。如果自訂指令和內建指令同名，會蓋掉內建指令。

---

## ✅ 動手練習

1. 打 `/` 看選單，再打 `/mo` 看篩選的效果。
2. 用 `/models` 搜尋 `free`，選一個免費模型。
3. 請 AI 建立一個小檔案，用 `/diff` 看改動，再用 `/undo` 復原。
4. 用 `/btw` 問一個問題，確認回答沒有加進對話。
5. 建立 `/hello` 指令，用 `/hello 小明` 試試看。

> 下一站：[04 環境配置 →](04-config.md)
