# OpenCode CLI 操作指南

## 導覽目錄

1. [安裝與確認版本](#1-安裝與確認版本)
2. [設定 Provider 與選擇 Model（必備前置）](#2-設定-provider-與選擇-model必備前置)
3. [在你的專案中建立 AGENTS.md（規範虛擬環境與工具）](#3-在你的專案中建立-agentsmd規範虛擬環境與工具)
4. [啟動與 TUI 日常互動](#4-啟動與-tui-日常互動)
5. [Subagent（子代理）機制與自訂角色](#5-subagent子代理機制與自訂角色)
6. [專案權限與設定檔 (opencode.jsonc)](#6-專案權限與設定檔-opencodejsonc)
7. [非互動 CLI 模式 (opencode run)](#7-非互動-cli-模式-opencode-run)
8. [搭配 Herdr 終端多工工作台](#8-搭配-herdr-終端多工工作台)
9. [常用維護指令與疑難排解](#9-常用維護指令與疑難排解)

---

## 1. 安裝與確認版本

請依作業系統選擇一種方式安裝：

### macOS (Homebrew 推薦)
```bash
brew install anomalyco/tap/opencode-v2
```

### macOS / Linux 官方腳本
```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

### Node.js / npm
```bash
npm install -g @opencode/cli
```

安裝完成後，在 shell 檢查版本確認成功：
```bash
opencode --version
opencode --help
```

---

## 2. 設定 Provider 與選擇 Model（必備前置）

OpenCode 需要連接大語言模型提供商（Provider）才能運作。在正式開始 coding 前，請先完成認證與模型選擇。

### 方式 A：在 TUI 互動介面中設定（最直覺）

啟動 `opencode` 後，在對話框內輸入斜線指令（不要在一般 shell 執行）：

1. **連接 Provider**：
   ```text
   /connect
   ```
   畫面上會列出支援的提供商（如 Anthropic、OpenAI、Google、OpenRouter、Groq 或本地 Ollama 等）。選取後依提示輸入 API Key 或透過瀏覽器完成登入授權。

2. **切換模型 (Model)**：
   ```text
   /models
   ```
   可搜尋並切換目前 Session 想使用的模型。不同模型在推理能力、代碼品質與 Token 費用上各有優勢。

### 方式 B：在 Shell CLI 中直接管理

如果不進 TUI，也可在終端機命令列直接操作：

```bash
# 登入並連接 provider
opencode auth login

# 查看目前已綁定的 provider 狀態
opencode auth list

# 列出所有可用的模型清單
opencode models
```

---

## 3. 在你的專案中建立 AGENTS.md（規範虛擬環境與工具）

> [!IMPORTANT]
> **進行任何專案開發時，第一步請務必在該專案根目錄建立 `AGENTS.md`！**  
> OpenCode 在啟動時，會自動搜尋並讀取目前專案目錄下的 `AGENTS.md` 作為最高協作準則（System Context）。  
> 如果你的專案內沒有放入這份檔案，Agent 就缺乏專案導航與規範約束，容易發生：
> 1. 自作主張使用全域 Python，甚至污染或破壞系統環境。
> 2. 誤用傳統的 `pip install`，而不是現代化的專案虛擬環境管理工具。
> 3. 寫出不符合團隊習慣或未經驗證的程式碼。

### 虛擬環境與套件管理規範（以 uv 為例）

在 Python 專案中，必須明確約束 Agent 使用的虛擬環境與套件管理工具：

- **嚴格規範工具**：本專案統一採用 **`uv`** 管理虛擬環境與相依性。
- **安裝主要套件**：一律使用 `uv add <套件名稱>`，**嚴禁直接使用 `pip install`**。
- **安裝開發相依**：測試或 Linter 工具使用 `uv add --dev <套件名稱>`。
- **執行指令**：所有程式與測試一律透過 `uv run <指令>` 執行（例如 `uv run python main.py` 或 `uv run pytest`）。

### 可直接套用的 `AGENTS.md` 範本

當你建立自己的新專案或整理既有專案時，請在該**專案根目錄**建立 `AGENTS.md`，貼入以下內容作為協作基礎：

```markdown
# 專案協作規範 (AGENTS.md)

## 1. 基本溝通原則
- 一律使用繁體中文回覆。
- 回答保持精確簡練，修改檔案前先說明思考邏輯與預計改動。
- 修改代碼後主動執行測試或 Linter 驗證，並核對 `git diff`。

## 2. Python 虛擬環境與套件管理 (uv)
- 本專案採用 **uv** 作為虛擬環境與套件管理器。
- **套件安裝**：一律使用 `uv add <套件名稱>`，嚴禁使用 `pip install`。
- **開發相依**：測試、格式化工具使用 `uv add --dev <套件名稱>`。
- **執行指令**：所有 Python 程式與測試必須透過 `uv run` 執行：
  - 執行程式：`uv run python <entry_point.py>`
  - 執行測試：`uv run pytest`
  - 執行 linter：`uv run ruff check .`

## 3. Git 與版本控制
- 嚴禁直接將未驗證的代碼 commit 到 `main` 分支。
- 若需要多任務平行開發，請使用 `git worktree` 在 `.worktrees/` 下建立獨立工作目錄。
- 變更完成後列出異動清單，供人類確認。
```


---

## 4. 啟動與 TUI 日常互動

### 啟動進入專案

進入專案根目錄後啟動 OpenCode：

```bash
cd /path/to/your-project
opencode
```

亦可直接帶入路徑：`opencode /path/to/your-project`。

### 第一次對話驗收

在 OpenCode 對話框輸入以下提示，確認它能正確讀取專案與 `AGENTS.md`：

```text
請讀取專案的 @AGENTS.md 與目錄結構，說明本專案使用的虛擬環境工具與套件安裝方式。
先只做說明，不修改任何檔案。
```

### TUI 指令與快捷鍵速查

OpenCode 使用 `Ctrl+X` 作為 **Leader Key**（先按 `Ctrl+X` 放開，再按後續按鍵），以避免與終端機環境衝突。指令依使用情境劃分為三大層級：

#### 1. 常用操作（每天必用）

| 功能 | 操作方式 | 說明 |
| :--- | :--- | :--- |
| **換模型 (Switch Model)** | `/models` 或 `Ctrl+X` → `M` | 開啟模型清單，快速搜尋並切換當前 Session 的模型 |
| **引入檔案脈絡** | 輸入 `@檔案名稱` | 模糊搜尋並將檔案內容掛載到提示中（如 `@AGENTS.md`） |
| **提示換行** | `Ctrl+J` 或 `Shift+Enter` | 輸入多行文字而不立即發送 |
| **撤銷上一步 (Undo)** | `/undo` 或 `Ctrl+X` → `U` | 還原 Agent 上一步的所有代碼修改與對話（可連續多次復原） |
| **重做 (Redo)** | `/redo` 或 `Ctrl+X` → `R` | 重做被 `/undo` 撤銷的修改 |
| **中斷 / 暫停任務** | 按 `Esc`（或連按兩次） | 立即中止執行；中斷後可直接在輸入框補充漏掉的要求再按 `Enter` |
| **離開 OpenCode** | `/exit`（別名 `/quit`、`/q`）或 `Ctrl+X` → `Q` | 退出 TUI 互動介面回到 Shell |

#### 2. 一般用途（Provider、推理強度與 Session 管理）

| 功能 | 操作方式 | 說明 |
| :--- | :--- | :--- |
| **換 Provider** | `/connect` | 新增、切換或重新綁定模型提供商（如 Anthropic、OpenAI、Google 等）與 API Key |
| **切換推理強度** | 按 `Ctrl+T` 或輸入 `/variants` | 切換模型思考強度（如 `low` / `medium` / `high` / `max`），依任務難度調配推理預算 |
| **開啟新工作階段** | `/new`（別名 `/clear`）或 `Ctrl+X` → `N` | 建立全新對話（當前 Session 會自動保存於歷史中） |
| **切換歷史 Session** | `/sessions`（別名 `/resume`）或 `Ctrl+X` → `L` | 瀏覽並切換回到過去的對話歷史 |
| **直接執行 Shell 指令** | 開頭輸入 `!` | 直接在終端執行命令（如 `!git status`、`!uv run pytest`） |
| **指令面板** | 輸入 `/` 或按 `Ctrl+P` | 開啟完整的模糊搜尋指令選單 |

#### 3. 進階使用（上下文調優與深度協作）

| 功能 | 操作方式 | 說明 |
| :--- | :--- | :--- |
| **顯示/隱藏思考過程** | `/thinking` | 切換是否在介面中展開顯示模型內部的思考推導過程 |
| **壓縮對話 (Compact)** | `/compact`（別名 `/summarize`）或 `Ctrl+X` → `C` | 自動摘要先前對話，釋放 Context Window 空間避免爆 Token |
| **提示排入佇列** | `Ctrl+X` 再按 `Enter` | 當 Agent 正在執行任務時，將下一段提示暫存排隊 |
| **開啟外部編輯器** | `/editor` 或 `Ctrl+X` → `E` | 使用本機 `$EDITOR`（如 Vim、VSCode 等）撰寫長篇複雜 Prompt |
| **側邊快速提問** | `/btw <問題>` | 利用當前上下文快速詢問臨時問題，不寫入主對話歷史紀錄 |
| **切換工具執行細節** | `/details` 或 `Ctrl+X` → `D` | 切換是否顯示底層 Tool Call 的詳細輸入與輸出內容 |
| **匯出對話紀錄** | `/export` | 將目前對話完整導出為 Markdown 格式檔 |

### 💡 實戰情境與解決方案（新手常見盲點）

簡單的操作查閱上方表格即可，但以下幾種開發中常見的「突發情境」，建議採用對應的最佳解法：

#### 情境一：Agent 正在執行，突然發現漏交代需求（想中斷或補話）
* **痛點**：看到 Agent 已經在讀寫檔案或跑命令，只能乾等它做完再重來嗎？
* **解決方案**：
  1. **先按 `Esc` 中斷，輸入後按 `Enter`（最推薦、最穩妥）**：
     直接按 **`Esc`**（或連按兩次），Agent 會立刻暫停動作並將焦點還給輸入框。此時從容輸入漏掉的需求（例如：*「剛才中斷是因為還要加上……請連同剛才的進度一起完成」*），按 **`Enter`** 送出即可接續執行。
  2. **不停下直接插話（Steering）**：
     不按 Esc，直接在下方打字並按 **`Enter`**。OpenCode 會在下一個工具執行的空檔即時吸收提示，動態修正方向。
  3. **排隊等目前任務結束（Queueing）**：
     打完字後按 **`Ctrl+X`** 再按 **`Enter`**，該指令會暫存在佇列中，等當前任務收尾後自動接續執行。

#### 情境二：剛 Commit 完才發現漏掉檔案或細節
* **痛點**：剛讓 Agent 建立了 Commit，才發現少改了一個設定，不想產生零碎難看的修復 Commit。
* **解決方案**：
  不需要手動 reset 或開新 commit，直接在 OpenCode 輸入：
  ```text
  剛才的 commit 漏掉了 X 內容，請幫我修改後，使用 git commit --amend 合併進前一個 commit。
  ```
  Agent 會自動修改檔案、加入暂存並以 `--amend` 乾淨地併入前一筆提交紀錄。

#### 情境三：Agent 越改越糟或改錯方向（如何安全復原）
* **痛點**：Agent 誤解了架構，動了許多檔案，手動改回來費時費力。
* **解決方案**：
  1. 按 **`Esc`** 中斷當前動作。
  2. 輸入 **/undo**（或快捷鍵 `Ctrl+X` → `U`），一鍵還原 Agent 上一步的所有代碼修改與對話（可連續多次執行）。
  3. 在終端以 `!git status` 核對確認檔案已乾淨復原。

#### 情境四：對話太長、Agent 開始健忘或反應變慢（Context 肥大）
* **痛點**：同一個 Session 處理過多任務，Token 消耗過大且模型容易漏掉規範。
* **解決方案**：
  輸入 **/compact**（或快捷鍵 `Ctrl+X` → `C`），OpenCode 會自動提煉摘要前段對話，騰出 Context Window 空間；若已進入全新任務，建議輸入 **/new** 開啟新對話（舊紀錄隨時可用 `/sessions` 找回）。


### 高效 Prompt 原則（目標、範圍、驗收）

撰寫提示時，提供明確的三要素能大幅提升 Agent 的成功率：

```text
請新增使用者登入 API 的單元測試。
範圍：只修改 tests/test_auth.py，不要改動業務代碼。
工具：使用 uv run pytest 執行測試。
驗收：所有測試必須 pass，並回報覆蓋率。
```

---

## 5. Subagent（子代理）機制與自訂角色

OpenCode 具備原生健全的 **Agent 與 Subagent（子代理）體系**。它能幫助你將複雜龐大的開發任務拆解給不同專業角色的子代理處理，徹底解決單一模型負擔過重與 Token 浪費的問題。

### 什麼是 Primary Agent vs. Subagent？

| 角色層級 | 定義與切換方式 | 執行環境與優勢 | 代表內建角色 |
| :--- | :--- | :--- | :--- |
| **Primary Agent（主代理）** | 你在對話框中直接互動的主助手。在 TUI 中按下 **`Tab`** 鍵可直接在主代理間切換。 | 共享主對話的上下文。擁有全域視角，負責推進主體開發任務。 | **Build**（預設全能開發，具讀寫與 Shell 權限）<br>**Plan**（唯讀分析規劃，預設需詢問授權） |
| **Subagent（子代理）** | 由主代理自動委派或由人類手動呼叫的專職助手。 | **在獨立的子工作階段（Child Session）中執行**！大範圍搜尋、龐大 Log 分析都不會灌爆主對話的 Context Window。 | **Explore**（快速唯讀專案探索）<br>**Scout**（外部文件與依賴查詢）<br>**General**（通用多步驟任務） |

### 為什麼一定要用 Subagent？（三大核心優勢）

1. **上下文隔離（Context Window 永不肥大）**：
   子代理在獨立的 Child Session 運作，它在背後翻閱了數十個檔案、看了數千行日誌，**完成後只把精簡結論帶回主對話**，主對話永遠保持輕盈與高精準度。
2. **極致省錢與高速（模型分工最佳化）**：
   你可以讓主代理使用昂貴頂級的模型，而將單純的代碼檢索、格式審查子代理綁定便宜又快速的模型（如 Muse Spark 或 NVIDIA Nemotron 的免費版），省下大筆 API 費用！
3. **安全圍欄（獨立權限控制）**：
   子代理可以單獨設定權限（例如設定 `edit: deny`，保證此子代理永遠只讀，絕不意外篡改任何代碼）。

### 如何呼叫 Subagent？

1. **手動以 `@` 標記直接召喚**：
   在提示輸入框中輸入 `@子代理名稱` 即可直接指派工作：
   ```text
   @explore 專案中負責處理使用者登入與 JWT 驗證的邏輯寫在哪個檔案？
   @reviewer 幫我檢視目前暫存區的 git diff，指出潛在的邊界錯誤與安全性問題。
   ```
2. **主代理自動派遣（Automatic Delegation）**：
   在一般的開發對話中，若你交代需要全面檢索專案或探索架構，主代理會根據各子代理的 `description` 專長，**自動派發子代理在背景執行**，完成後自動吸收報告接續編程。

### 如何自訂專屬 Subagent？（實戰範例）

OpenCode 採用直覺的 **Markdown + YAML Frontmatter** 來定義 Agent。你可以將它放在專案的 `.opencode/agents/` 目錄（專案專屬），或放在 `~/.config/opencode/agents/`（全域通用）。

#### 範例一：只讀代碼品質審查員 (`.opencode/agents/reviewer.md`)
建立檔案 `.opencode/agents/reviewer.md`：

```markdown
---
description: 負責審查近期變更或 Git Diff 的代碼品質、資安漏洞與邊界條件，只讀不修改檔案
mode: subagent
model: opencode-go/muse-spark-1.3-contributor
temperature: 0.1
permissions:
  - action: edit
    resource: "*"
    effect: deny
---

你是一位嚴格的資深 Code Reviewer 子代理。
請檢視提供的代碼改動或 Git Diff，重點關注：
1. 是否有未處理的 Null/None 例外、資源洩漏或邊界條件錯誤。
2. 是否有 SQL 注入、XSS 或未過濾輸入等安全風險。
3. 程式碼風格與架構是否符合專案 AGENTS.md 規範。

請條列式依嚴重程度（Critical / Warning / Info）輸出改進建議。嚴禁修改任何檔案。
```

#### 範例二：自動化測試助手 (`.opencode/agents/tester.md`)
建立檔案 `.opencode/agents/tester.md`：

```markdown
---
description: 專門執行單元測試、分析錯誤日誌並修復測試案例
mode: subagent
temperature: 0.2
---

你是一位自動化測試工程師子代理。
你的職責是：
1. 嚴格遵循專案根目錄的 AGENTS.md 規範，使用 `uv run pytest` 執行測試。
2. 分析失敗案例的 Stack Trace，定位出錯誤原因。
3. 補充覆蓋邊界情況的測試案例，確保測試全部通過。
```

#### Subagent Frontmatter 參數速查

| 參數 | 型態與可選值 | 說明 |
| :--- | :--- | :--- |
| `description` | 字串（**必填**） | 簡短描述此代理的專長。主代理會依此描述判斷何時自動委派任務給它！ |
| `mode` | `subagent` / `primary` / `all` | `subagent` 代表僅作為子代理；`primary` 代表可按 `Tab` 鍵切換的主代理。 |
| `model` | 模型 ID（選填） | 指定此子代理專用的 LLM 模型。若未指定，則自動繼承呼叫它的主代理模型。 |
| `temperature` | 浮點數（0.0 ~ 1.0） | 調整推導嚴謹度。代碼分析、測試建議設定為 `0.1` ~ `0.2`。 |
| `permissions` | 權限清單（選填） | 為此子代理設立安全邊界（如 `edit`、`shell` 的 `allow` / `ask` / `deny`）。 |

---

## 6. 專案權限與設定檔 (opencode.jsonc)

為了防止 Agent 誤執行危險指令（例如刪除重要檔案或未經授權的外部連線），可使用設定檔進行權限控管。

### 權限安全設定範例

在專案根目錄建立 `opencode.jsonc`（或全域 `~/.config/opencode/opencode.jsonc`）：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    // 預設讀取完全允許
    { "action": "read", "resource": "*", "effect": "allow" },
    // 編輯檔案與執行 shell 指令前必須經人類確認
    { "action": "edit", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "*", "effect": "ask" },
    // 安全無害的指令可直接允許自動執行
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "git diff *", "effect": "allow" },
    { "action": "shell", "resource": "uv run pytest *", "effect": "allow" }
  ]
}
```

> [!NOTE]
> 權限規則由上而下解析，**最後符合的規則優先**。`allow`（自動執行）、`ask`（詢問人類）、`deny`（直接禁止）。

### 設定檔職責分工

| 設定檔案 | 放置位置 | 主要職責 |
| :--- | :--- | :--- |
| `AGENTS.md` | 專案根目錄 | 自然語言撰寫的專案開發規範、虛擬環境與協作憲法 |
| `opencode.jsonc` | 專案根目錄 | 專案級工具權限圍欄、MCP Server 連接與模型覆寫 |
| `.opencode/agents/*.md` | 專案目錄 | 專案專屬的自訂 Agent / Subagent 定義檔（Markdown + YAML） |
| `.opencode/commands/*.md` | 專案目錄 | 專案專屬的自訂 Slash Command（例如 `/code-review`） |
| `~/.config/opencode/cli.json` | 家目錄 | 全域 TUI 介面主題、快捷鍵自訂 |

---

## 7. 非互動 CLI 模式 (opencode run)

除了進入 TUI 互動介面，OpenCode 也支援直接在 Shell 執行單次任務，非常適合寫入自動化腳本或 CI/CD：

```bash
# 執行單次任務並直接在終端輸出結果
opencode run "請用繁體中文檢查 @README.md 的連結是否正確"

# 針對特定檔案下達指令
opencode run --file main.py "優化這段程式碼的效能並加上型別標註"

# 延續上一次的對話進度
opencode run --continue "為剛才修改的函式補上單元測試"

# 輸出 JSON 格式供其他腳本解析
opencode run --format json "檢查專案是否有未符合 PEP8 的代碼"
```

---

## 8. 搭配 Herdr 終端多工工作台

當你需要同時處理多個任務、在背景持續執行 Agent，或是將終端機畫面分割（例如一邊讓 OpenCode 寫代碼、另一邊跑伺服器或測試）時，建議搭配 **Herdr** 使用。

### 8.1 安裝 OpenCode 官方整合
在終端機 shell 執行：
```bash
herdr integration install opencode
```
這會自動為 OpenCode 加入狀態通知外掛，讓 Herdr 的分頁與狀態欄能即時顯示 Agent 是否處於「工作中」或「等待使用者回應」。

### 8.2 進階操作與工作流
關於 Herdr 的分頁管理、窗格切割以及多 Agent 平行任務協同，請參考專門的 [Herdr 整合教學](../herdr/opencode-integration.md)。

---

## 9. 常用維護指令與疑難排解

### 常用管理指令速查

| 指令 | 說明 |
| :--- | :--- |
| `opencode auth list` | 檢查目前所有已設定的 Provider 連線狀態 |
| `opencode models` | 列出所有可用模型 ID 與資訊 |
| `opencode session list` | 列出目前專案的歷史對話 Sessions |
| `opencode mcp list` | 檢查已啟用的 MCP (Model Context Protocol) 伺服器 |
| `opencode debug config` | 診斷並列出目前載入的所有設定來源 |
| `opencode upgrade` | 自動升級 OpenCode CLI 至最新版本 |

### 常見問題排解 (Troubleshooting)

1. **找不到 `opencode` 指令**：
   - 重新啟動終端機，確認安裝目錄在 `$PATH` 變數中。macOS/Linux 可執行 `which opencode` 檢查路徑。
2. **模型連線失敗或報錯 401/429**：
   - 輸入 `/connect` 重新確認 API Key 是否過期、餘額是否充足，或使用 `opencode auth list` 檢查登入授權。
3. **Agent 嘗試使用 `pip` 而非 `uv`**：
   - 確認專案根目錄是否有 `AGENTS.md`，並在對話開始時輸入 `@AGENTS.md` 提醒它遵循規範。
4. **升級 CLI 後新功能未生效**：
   - OpenCode V2 採用背景服務機制。升級後請以 `opencode service restart` 重啟背景服務。
