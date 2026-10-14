# Herdr 終端多工操作指南

## 導覽目錄

1. [安裝與確認版本](#1-安裝與確認版本)
2. [核心概念：Workspace、Tab 與 Pane](#2-核心概念workspace-tab-與-pane)
3. [啟動與日常鍵盤操作速查](#3-啟動與日常鍵盤操作速查)
4. [整合 AI Coding Agent（狀態辨識與連動）](#4-整合-ai-coding-agent狀態辨識與連動)
5. [實戰情境與解決方案（新手常見盲點）](#5-實戰情境與解決方案新手常見盲點)
6. [非互動 CLI 與背景工作階段管理](#6-非互動-cli-與背景工作階段管理)
7. [常用維護指令與疑難排解](#7-常用維護指令與疑難排解)

---

## 1. 安裝與確認版本

請依作業系統選擇對應方式安裝：

### macOS (Homebrew 推薦)
```bash
brew install herdr
```

### macOS / Linux 官方安裝腳本
```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

安裝完成後，在 shell 檢查版本確認成功：
```bash
herdr --version
herdr --help
```

---

## 2. 核心概念：Workspace、Tab 與 Pane

Herdr 是專為 AI coding agent 設計的終端多工工作台（Agent Multiplexer）。它採用三層結構管理你的開發環境：

| 層級名稱 | 概念定義 | AI 開發中的實際用途 |
| :--- | :--- | :--- |
| **Workspace（工作區）** | 一個獨立的專案或任務背景 | 一個專案目錄（如 `vibe_coding_harness`），或一個 Git Worktree |
| **Tab（分頁）** | 工作區內的一組終端版面 | 分頁 1 進行主功能開發、分頁 2 跑測試伺服器、分頁 3 執行檔案管理 |
| **Pane（窗格）** | 真正執行 shell、Agent 或程式的子視窗 | 左邊執行 OpenCode 撰寫代碼，右邊監控 `git diff` 變更 |
| **Agent 狀態** | 窗格內 AI Agent 的即時運作情況 | 標籤列即時提示 Agent 是否正在「工作中」或「等待人類批准」 |

> [!TIP]
> **滑鼠完全可用**：初學者可以直接用滑鼠點選窗格切換焦點、點擊上方分頁切換、拖曳分隔線調整大小，或按滑鼠右鍵開啟分割選單。

---

## 3. 啟動與日常鍵盤操作速查

### 啟動進入 Herdr

進入專案目錄後啟動 Herdr：

```bash
cd /path/to/your-project
herdr
```
`herdr` 會自動建立或連回預設的背景工作階段。

### Prefix Key 說明
Herdr 預設採用 **`Ctrl+B`** 作為 **Prefix** 鍵（先按下 `Ctrl+B` 放開，再按下後續指令鍵）。

#### 1. 常用操作（每天必用）

| 功能 | 操作方式 | 說明 |
| :--- | :--- | :--- |
| **向右分割窗格** | `prefix+v` | 垂直分割出右側終端窗格（適合左邊跑 Agent，右邊看 Git） |
| **向下分割窗格** | `prefix+-` | 水平分割出下方終端窗格（適合下方跑測試或 Server） |
| **切換窗格焦點** | `prefix+h/j/k/l` 或方向鍵 | 在左／下／上／右窗格之間移動游標（亦可直接滑鼠點擊） |
| **新增分頁** | `prefix+c` | 在當前工作區建立全新分頁（Tab） |
| **切換分頁** | `prefix+n` / `prefix+p` | 切換至「下一個 (Next)」或「上一個 (Previous)」分頁 |
| **直達指定分頁** | `prefix+1` ～ `prefix+9` | 直接切換至第 1 到第 9 個分頁 |
| **暫離介面 (Detach)** | `prefix+q` | 離開 Herdr 回到外層 Shell，**所有背景程式與 Agent 保持持續運行** |

#### 2. 一般用途（版面微調與導覽）

| 功能 | 操作方式 | 說明 |
| :--- | :--- | :--- |
| **放大／還原窗格 (Zoom)** | `prefix+z` | 將當前窗格放大至全螢幕，再按一次即可復原原有多窗格排列 |
| **關閉當前窗格** | `prefix+x` | 關閉游標所在的窗格（或在 shell 中直接輸入 `exit`） |
| **工作區樹狀導覽** | `prefix+w` | 開啟工作區與分頁清單，視覺化切換不同的 Session |
| **查閱快捷鍵清單** | `prefix+?` | 開啟即時快捷鍵說明彈窗，確認目前生效的鍵位 |

#### 3. 進階使用（滾動與環境自訂）

| 功能 | 操作方式 | 說明 |
| :--- | :--- | :--- |
| **滾動／查看歷史輸出** | `prefix+[` | 進入檢視模式，可用 `PgUp`/`PgDn` 或方向鍵向上翻閱長篇日誌 |
| **重新命名分頁** | `prefix+,` | 為當前分頁自訂名稱（例如 `server`、`agent-auth`） |
| **重新命名工作區** | `prefix+$` | 為當前工作區命名，方便在多專案間辨識 |

---

## 4. 整合 AI Coding Agent（狀態辨識與連動）

Herdr 最強大的功能之一是能主動感知窗格內的 Agent 執行狀態。分頁與窗格標籤會即時顯示狀態標記：

| Agent 狀態標籤 | 意義 | 開發者應對方式 |
| :--- | :--- | :--- |
| `working` | Agent 正在讀取檔案、推導思考或執行終端指令 | 正常等待，或做其他事情 |
| `blocked` | Agent 遇到需要人類授權或回答問題的互動界面 | **重要**！請切換回該窗格確認並給予批准 |
| `idle` | Agent 或 Shell 處於空閒狀態 | 可以交付下一個新任務 |
| `done` | 任務剛完成回到待命狀態，但你尚未檢視該窗格 | 切換回該窗格驗收成果 |
| `unknown` | 尚未安裝整合或無法識別狀態 | 檢查是否已安裝對應 Agent 的官方整合外掛 |

### 安裝 OpenCode 官方整合
在終端機執行：
```bash
herdr integration install opencode
```
安裝後，Herdr 會自動獲得 OpenCode 的原生狀態回報。詳細流程請參閱 [搭配 OpenCode 整合教學](opencode-integration.md)。

---

## 5. 實戰情境與解決方案（新手常見盲點）

日常使用查閱表格即可，但在多工開發時，以下幾種「典型情境」是掌握 Herdr 的關鍵技巧：

#### 情境一：下班或切換環境，如何讓 Agent 繼續跑而不中斷？
* **痛點**：平時關閉終端機或 SSH 斷線，正在執行的長任務就會被迫中斷；不知道如何安全退出。
* **解決方案**：
  使用 **`prefix+q`（Detach）**！
  按完後介面會立即退出回到一般 Shell，但 Herdr 的背景伺服器、正在寫 code 的 Agent 與跑中的 Server **完全不會中斷**。隨時在終端輸入 `herdr`，就能原封不動重連回先前的畫面。

#### 情境二：一邊讓 Agent 寫 code，一邊即時查看改動（標準雙窗格流）
* **痛點**：Agent 在背景默默改了好多檔案，不知道它有沒有改歪，一直切換視窗很繁瑣。
* **解決方案**：
  1. 啟動 Herdr 後，在預設窗格執行 `opencode`。
  2. 按 **`prefix+v`** 水平向右切出第二個窗格。
  3. 在右側窗格輸入 `git diff` 或 `git status --short`，一邊監督 Agent 操作，一邊隨時檢查改動。

#### 情境三：同時跑 Agent、開發伺服器與單元測試（分頁專注流）
* **痛點**：終端機視窗散落在桌面各處，測試輸出、Server 日誌與 Agent 提示混在一起難以管理。
* **解決方案**：
  善用分頁（Tab）分類職責：
  - **Tab 1（命名為 agent）**：按 `prefix+c` 建立，專門啟動 OpenCode 處理程式碼。
  - **Tab 2（命名為 test）**：專門執行 `uv run pytest -f` 持續測試。
  - **Tab 3（命名為 server）**：專門啟動本地 Web/API Server。
  利用 **`prefix+1`、`prefix+2`、`prefix+3`** 在不同任務間瞬間切換，桌面維持乾淨俐落。

#### 情境四：電腦重開機或意外關閉，如何找回工作區？
* **痛點**：電腦重啟後視窗全空，不確定之前的 Agent 進度還在不在。
* **解決方案**：
  Herdr 會持續保存工作區佈局結構。重開機後進入專案執行 `herdr`，會自動重建先前的分頁與窗格配置；接著在 Agent 窗格中輸入 `/sessions`（以 OpenCode 為例），即可一秒找回並續接上次的任務進度。

---

## 6. 非互動 CLI 與背景工作階段管理

除了透過 TUI 介面操作，Herdr 也提供了強大的 Shell 指令供自動化或快速管理：

```bash
# 列出目前背景所有的 Active Workspaces 與狀態
herdr list

# 重新連接到指定名稱的工作區
herdr attach vibe_coding_harness

# 建立新工作區而不立即進入
herdr workspace create --name feature-login

# 終止指定工作區及其底下的所有程序
herdr kill vibe_coding_harness
```

更多指令參數請參閱 [CLI 操作指南](cli.md)。

---

## 7. 常用維護指令與疑難排解

### 常用維護指令速查

| 指令 | 說明 |
| :--- | :--- |
| `herdr --version` | 檢查目前安裝的 Herdr 版本 |
| `herdr server status` | 檢查 Herdr 背景管理服務的運作狀態 |
| `herdr server restart` | 重啟 Herdr 背景服務（升級後套用新版本時使用） |
| `herdr upgrade` | 自動檢查並升級 Herdr CLI 至最新版 |

### 常見問題排解 (Troubleshooting)

1. **找不到 `herdr` 指令**：
   - 重新載入 shell 設定檔（例如 `source ~/.zshrc`），並確認安裝路徑（如 `/opt/homebrew/bin` 或 `~/.local/bin`）在系統環境變數 `$PATH` 中。
2. **快捷鍵按了沒反應**：
   - 請注意 **Prefix 鍵不是連按**：按下 `Ctrl+B` 後必須先放開，然後再按後續的英文字母鍵（例如 `c` 或 `v`）。亦可隨時按 `prefix+?` 檢查當前生效的鍵位。
3. **Agent 狀態一直顯示 `unknown`**：
   - 請確認已在該環境中執行 `herdr integration install opencode`。若版本曾更新，請依說明執行 `herdr server restart`。
4. **離開 Herdr 時誤關閉了程式**：
   - 請記得平時離開請使用 **`prefix+q`（Detach）**，不要直接關閉終端機視窗或輸入 `exit`。
