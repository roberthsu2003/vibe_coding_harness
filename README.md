# 終端機 AI 開發入門

這是給剛開始用終端機開發的人看的操作手冊：從安裝工具、理解 AI coding agent，到用 Git 管理平行工作的程式版本。內容以實際操作為主，逐步帶你建立一套可以重複使用的終端機工作流程。


## AI coding agent 與 Harness

AI coding agent 由模型和 Harness 組成。Harness 把模型接上真實的開發環境，讓 AI 不只回答問題，還能讀寫專案檔案、執行終端指令，並根據結果繼續修正。想深入了解，請參考 [Harness 是什麼](harness.md)。

### OpenCode

OpenCode 是可在終端機中執行的開源 AI coding agent，也是本 repo 目前的主要範例；它能讀寫專案檔案、修改程式並自動執行指令。

完整的安裝、CLI 操作與設定請參考 [OpenCode 操作指南](opencode/README.md)。


### Antigravity CLI (agy)

Antigravity CLI (`agy`) 是 Google Antigravity 的終端機代理介面，能直接在命令列中與多代理（Subagents）協同工作、執行自動化任務、使用工作空間自訂規則與外掛（Plugins/Skills）。

完整的安裝、CLI 操作與設定請參考 [Antigravity CLI 操作指南](agy/README.md)。


## Git：Branch 與 Worktree

Branch（分支）與 Worktree 是 AI coding agent 平行開發與任務隔離的核心機制。透過 Branch 劃分功能與實驗，搭配 `git worktree` 讓同一個專案同時擁有數個獨立的工作資料夾，多個 agent 即可在各自的分支上平行修改與驗證程式，互不干擾。

教材以咖啡店網站的故事貫穿，從單一 AI 用 Branch，一路學到多個 AI 用 Worktree 同時開發。詳細概念、目錄規劃與操作步驟請參考 [Branch 與 Worktree 操作指南](worktree/README.md)。


## ADE：管理多個 agent 工作階段

ADE 是 **Agentic Development Environment** 的縮寫，可理解為以 agent 工作流程為中心的開發環境。這是正在發展中的工具類別；不同專案可能是 TUI、桌面程式或其他介面，因此本 repo 會介紹實際功能，不把它限定成單一介面或已定型的標準。

### Herdr

Herdr 是終端機內的 agent multiplexer，可用 workspace、tab 和 pane 管理 agent 與 shell，隨時查看狀態並重新連回工作階段。完整的安裝與操作請參考 

[Herdr 操作指南](herdr/README.md)。

## 終端機工具

### Yazi

Yazi 是終端機內的檔案管理器，可用鍵盤瀏覽目錄、預覽檔案並快速管理路徑。完整的安裝與操作請參考 

[Yazi 操作指南](yazi/README.md)。


### Glow

Glow 是終端機內的 Markdown 渲染與閱讀工具，能將 AI 產出的規格文件、README 與日誌直接在終端內呈現出精美的排版與語法高亮，無需切換瀏覽器或圖形編輯器。完整的安裝與操作請參考 

[Glow 操作指南](glow/README.md)。

