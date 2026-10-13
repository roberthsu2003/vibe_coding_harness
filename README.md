1. **Harness（駕馭核心）**：讓 AI 模型具備動手能力的控制與執行骨幹（以 OpenCode 為代表）。
2. **ADE（代理開發環境）**：當前最新流行的 TUI 工具，專為多 Agent 調度與終端開發打造的現代化工作台（以 Herdr 為代表）。
3. **工具（終端輔助）**：終端高效率檔案管理與預覽工具（以 Yazi 為代表）。

## Harness

### Harness 是什麼？

你可以把 **AI 模型想像成一匹精力充沛的「駿馬」**，而 **Harness（原意即為馬具、輓具）就是套在它身上的「馬鞍與韁繩」**。

過去你可能遇過這種情況：請 AI 幫忙改程式，它只在對話框給出一段建議，你得手動把程式碼貼進專案、自己執行測試，遇到報錯後再把錯誤訊息貼回去——這就像對著一匹未套鞍具的野馬喊話，空有強大力量卻難以直接為你所用。

**Harness 的核心價值，就是讓你能夠「全權掌控並駕馭這匹馬」：**
- **握緊韁繩（規範與權限）**：設定專案規則與操作邊界，確保模型朝著正確方向前進，不隨意脫韁亂跑。
- **配戴裝備（工具與環境）**：把模型、專案檔案與終端指令串接在一起，讓它不只會「想」，還能直接動手讀檔、改檔與執行指令。
- **掌控步伐（回饋與修正）**：在同一個工作流程中查看執行結果，遇到錯誤時能即時拉回韁繩並嘗試修正。

換句話說：**模型（馬）提供強大的前電動能，而 Harness（馬鞍與韁繩）則賦予你全權控制的能力，讓這股力量能精準且受控地奔向專案目標。**

### OpenCode

**OpenCode** 是一款在終端環境中運行的開源 AI Coding Agent，也是本專案介紹的核心 Harness 代表。它負責將 AI 模型的智慧轉化為實際動手能力，串接專案檔案、終端命令與各式工具，讓 AI 能夠自主讀檔、修改程式碼、執行指令並修復錯誤。

關於 OpenCode 的完整安裝步驟、常用 CLI 指令、專案指示與進階設定，請參閱專案內的 [opencode/ 資料夾](opencode/)（或閱讀 [OpenCode 操作指南](opencode/README.md)）。

#### 為什麼說 OpenCode 是 Harness？

OpenCode 的推理與回答主要來自它連接的 AI 模型；OpenCode 則負責把模型接到你的專案與工具。從這個角度看，我們可以把它理解成一種 coding agent harness。[OpenCode 官方介紹](https://opencode.ai/v2/docs/)

可以用五件事來理解它的工作：

| 它幫忙處理什麼？ | 用口語說 | 小例子 |
| --- | --- | --- |
| 連接工具 | 讓 AI 有工具可以動手 | 讀取程式、修改檔案、執行終端指令；也能透過 MCP 接上額外工具 |
| 整理工作脈絡 | 告訴 AI 現在做什麼、要遵守什麼 | 讀取 `AGENTS.md` 裡的專案規則，管理對話紀錄，對話太長時整理重點 |
| 管理權限 | 決定哪些事能做、哪些要先問 | 允許讀檔，但修改檔案或執行某些指令前，需要你確認 |
| 檢查與修正 | 讓 AI 看得到自己做完的結果 | 依任務執行測試，把失敗訊息交回模型，再嘗試修正 |
| 分工 | 需要時讓不同 agent 負責不同任務 | 主 agent 處理修改，子 agent 協助檢查問題 |

這五點是方便理解的整理方式；測試要依專案與任務安排，分工也要依需求使用，不代表每次都會自動發生。工具與脈絡功能見官方 [Tools](https://opencode.ai/v2/docs/tools/)、[Instructions](https://opencode.ai/v2/docs/instructions/) 與 [Compaction](https://opencode.ai/v2/docs/compaction/)；權限與分工見 [Permissions](https://opencode.ai/v2/docs/permissions/) 與 [Agents](https://opencode.ai/v2/docs/agents/)。

#### 一個小例子：請 AI 改按鈕文字

假設你正在做一個網站，想把「登入」按鈕改成「會員登入」。你可以在 OpenCode 裡說：

```text
請把首頁的「登入」按鈕改成「會員登入」。
保留原本的樣式與功能，修改後執行相關測試，並告訴我結果。
```

這時可以這樣理解整個過程：

1. **模型判斷怎麼改**：找出相關頁面與按鈕，決定需要修改哪裡。
2. **OpenCode 提供動手的工具**：讓模型能讀檔、提出修改，並依權限設定執行。
3. **工具把結果傳回來**：如果專案有相關測試，就執行測試；失敗時，模型可以根據錯誤再調整。
4. **你檢查成果**：看修改差異與測試結果，確認文字和功能都符合需求。

這是示意流程。實際步驟會依專案、提示與權限設定改變；專案沒有測試時，也要清楚回報哪些部分尚未驗證。

## ADE

**ADE（Agentic Development Environment，代理開發環境）** 是目前軟體開發領域最新流行的工作模式與 TUI（Terminal User Interface）工具。

如果說傳統 IDE（如 VS Code）是以「人手動寫程式碼、AI 偶爾在側邊欄輔助補齊」為中心，那麼 **ADE 則是以「AI Agent 自主執行任務、人負責宏觀調度與邊界審批」為核心所打造的終端開發環境**。

### 為什麼 ADE 是最新流行的 TUI 工具？
- **輕量極速**：以終端機（TUI）為基礎，沒有肥大 GUI 的負擔，在本地終端或遠端伺服器都能毫秒級啟動與切換。
- **多工 Agent 視圖調度**：專門為同時間跑多個 Agent 或工作階段設計，輕鬆分工不同任務。
- **沉浸式狀態掌握**：提供直觀的即時指示器，清楚看到每個 Agent 正在「思考」、「執行動作」還是「等待你的權限確認」。

### Herdr：專為 Coding Agent 打造的 ADE 終端環境
在這個架構中，**Herdr** 就是代表性的 ADE 工具：
- 它就像工作桌上的終端主管：左側窗格跑 OpenCode 讓 Agent 撰寫或修改程式，右側窗格即時看測試日誌或 Git 差異。
- 具備狀態指示器（Status indicator），讓你一眼掌握各個 Agent 的工作狀態，誰在忙、誰需要你確認一目了然。
- 支援背景執行與 Detach，即使斷線或切換其他任務，Agent 依然在背景持續工作。[Herdr Agents 文件](https://herdr.dev/docs/agents/)

## 工具

在純終端（TUI / ADE）的工作流程中，除了 Agent 之外，高效率的終端輔助工具必不可少，而核心工具就是 **Yazi**。

### Yazi：終端極速檔案管理器
**Yazi** 是一款以 Rust 開發的現代化終端檔案管理器（TUI File Manager）：
- **非同步與極致流暢**：採用全非同步事件驅動設計，在大型專案或萬級目錄間導航、搜尋完全不卡頓。
- **免切視窗的預覽體驗**：直接在終端內預覽程式碼語法高亮、Markdown 乃至圖片，支援鍵盤快捷操作。
- **完美協同 ADE 工作流**：在 Herdr 的獨立窗格或分頁常駐 Yazi，讓你隨時穿梭專案檔案、一鍵複製絕對路徑並餵給 OpenCode 處理，全程不需離開終端機。

## 開始操作

**最近上網查核：2026-10-13（Asia/Taipei）**。本次依官方文件整理；未在本機安裝工具或實際呼叫模型。文件是一份查核當日的快照，後續更新方式見各工具的更新紀錄。

| 領域 | 工具 | 用途 | 閱讀入口 |
| --- | --- | --- | --- |
| **Harness** | OpenCode CLI | 在專案中與 AI 對話、分析與修改程式、執行非互動任務 | [OpenCode 操作指南](opencode/README.md) |
| **ADE** | Herdr | 管理終端工作區、分頁與窗格，觀察 coding agent 狀態 | [Herdr 操作指南](herdr/README.md) |
| **工具** | Yazi | 在終端機用鍵盤瀏覽檔案、預覽文件與複製路徑 | [Yazi 安裝與簡單操作](yazi/README.md) |
| **整合實作** | OpenCode + Herdr | 在 Herdr 窗格中執行 OpenCode，加入狀態與 session 整合 | [整合實作](herdr/opencode-integration.md) |

建議先完成 OpenCode 的第一次對話，再學習 Herdr 的分割窗格與 detach，最後設定整合。

## 文件結構

```text
vibe_coding_harness/
├── README.md
├── opencode/
│   ├── README.md                # 安裝、對話、常用 CLI 與排錯
│   ├── configuration.md         # 專案指示、權限、自訂命令
│   └── updates.md               # 來源與更新紀錄
├── herdr/
│   ├── README.md                # 安裝、介面、快捷鍵、持續執行
│   ├── cli.md                   # 工作區、窗格、agent CLI
│   ├── opencode-integration.md  # OpenCode 整合與實作
│   └── updates.md               # 發行版本、來源與更新紀錄
└── yazi/
    └── README.md                # 一段 prompt 安裝、簡單操作與 Herdr 分頁
```

## 版本與指令

本 repo 的 OpenCode 教學統一採 [V2 官方文件](https://opencode.ai/v2/docs/)，包含安裝、操作、設定與整合。

Herdr 的指南採 [官方文件](https://herdr.dev/docs/)，另記錄 stable 與 preview 的差異。實際可用旗標以讀者安裝版本的 `--help` 為準；上游文件可能先於 stable binary 更新。

範例中的 `/path/to/project`、模型 ID 與 session ID 必須換成自己的值。文件只記錄人工查核，不會自動每日更新。
