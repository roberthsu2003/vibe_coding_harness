# 終端機 AI 開發入門

這是給剛開始用終端機開發的人看的操作手冊：從安裝工具、理解 AI coding agent，到用 Git 管理平行工作的程式版本。內容以實際操作為主，逐步帶你建立一套可以重複使用的終端機工作流程。


## Harness：AI coding agent

Harness 在這個 repo 指能直接操作專案的 AI coding agent 及其工作規則、工具與權限設定。它不只是回答問題，也能讀寫專案檔案、執行終端指令，並根據結果繼續修正。

### Harness 核心的五大職責

| 核心職責 | 領域 / 英文 | 說明與主要功能 |
| :--- | :--- | :--- |
| **工具連接與環境控制** | Tools & MCP | 提供檔案讀寫、終端機執行、Git 操作以及 MCP (Model Context Protocol) 伺服器介接能力，把大腦與真實開發環境連接起來。 |
| **上下文治理與持久化** | Context & State Management | 自動載入專案規範（如 AGENTS.md、架構設定）、過濾過大檔案或 lockfile 避免爆 token，並維護 session 狀態與對話交接（Handoff）。 |
| **權限約束與安全圍欄** | Constrain & Permissions | 透過設定檔（如 opencode.json）定義哪些操作可以直接執行（auto-run）、哪些需要人類確認（ask），防止危險指令破壞系統。 |
| **自動化驗證與修正迴圈** | Verify & Self-Correction | 代碼生成後自動掛載測試或 Linter 執行，並把失敗日誌餵回給模型修復，無需人類來回複製貼上終端機錯誤。 |
| **多 Agent 協同與分工** | Agent Orchestration | 支援主代理（Supervisor）與子代理（Subagent）拆分規劃、撰寫與評審（Auto-review）任務，避免單一模型包辦全部而失控。 |


### OpenCode

OpenCode 是可在終端機中執行的開源 AI coding agent，也是本 repo 目前的主要範例；它能讀寫專案檔案、修改程式並自動執行指令。完整的安裝、CLI 操作與設定請參考 [OpenCode 操作指南](opencode/README.md)。


## ADE：管理多個 agent 工作階段

ADE 是 **Agentic Development Environment** 的縮寫，可理解為以 agent 工作流程為中心的開發環境。這是正在發展中的工具類別；不同專案可能是 TUI、桌面程式或其他介面，因此本 repo 會介紹實際功能，不把它限定成單一介面或已定型的標準。

### Herdr

Herdr 是終端機內的 agent multiplexer，可用 workspace、tab 和 pane 管理 agent 與 shell，隨時查看狀態並重新連回工作階段。完整的安裝與操作請參考 [Herdr 操作指南](herdr/README.md)。

## 終端機工具

### Yazi

Yazi 是終端機內的檔案管理器，可用鍵盤瀏覽目錄、預覽檔案並快速管理路徑。完整的安裝與操作請參考 [Yazi 操作指南](yazi/README.md)。


### Git 與 worktree：同一個 repo 的多個工作目錄

Git 與 `git worktree` 是 AI coding agent 平行開發與任務隔離的核心機制，能讓多個 agent 同時在不同目錄處理各自的分支任務。詳細概念、目錄規劃與操作步驟請參考 [Git 與 Worktree 操作指南](git/README.md)。

## 目錄規劃

```text
.
├── README.md                 # 導覽、分類與新手學習路徑
├── opencode/                 # OpenCode 安裝、操作與設定
├── herdr/                    # Herdr 安裝、操作與 agent 整合
├── yazi/                     # Yazi 安裝、操作與外掛
└── git/                      # Git、branch、worktree 與 agent 平行開發流程
```

每個工具的專屬操作放在自己的資料夾；README 保留總覽、工具間的關係和學習順序。遇到共通概念（例如 Git、終端機路徑、shell）則集中在共用資料夾，讓新人能先理解再照著工具指南操作。

