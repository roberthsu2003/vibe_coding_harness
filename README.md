# 終端機 AI 開發入門

這個 repo 是給剛開始用終端機開發的人看的操作手冊：從安裝工具、理解 AI coding agent，到用 Git 管理平行工作的程式版本。內容以實際操作為主，逐步帶你建立一套可以重複使用的終端機工作流程。

## 這個 repo 怎麼分類？

| 分類 | 負責什麼 | 目前範例 |
| --- | --- | --- |
| Harness（AI coding agent） | 讓 AI 讀取專案、修改檔案、執行指令，並在規則與權限內完成任務 | OpenCode；之後可加入 Claude Code、Codex CLI、Antigravity CLI |
| ADE（Agentic Development Environment） | 管理終端中的多個 agent 工作階段、工作區與執行狀態 | Herdr；可評估 AGTx、Termio |
| 終端機工具 | 提升檔案瀏覽、版本管理等日常操作效率 | Yazi、Git |

這些名稱是為了讓新手理解工具在工作流程中的角色，不代表每個專案都採用完全相同的分類。Harness 負責「agent 如何工作」；ADE 負責「如何安排和觀察多個工作階段」；終端工具則補足檔案瀏覽與版本管理。

## 建議學習順序

1. 熟悉終端機基本操作與資料夾路徑。
2. 安裝並使用一個 AI coding agent，先從 OpenCode 開始。
3. 學會 Git 的基本概念：狀態、差異、提交與分支。
4. 用 Git worktree 為不同任務建立獨立工作目錄。
5. 再使用 Herdr 等 ADE 管理多個 agent 工作階段。
6. 依需求安裝 Yazi，並讓 AI agent 協助設定外掛與預覽工具。

## Harness：AI coding agent

Harness 在這個 repo 指能直接操作專案的 AI coding agent 及其工作規則、工具與權限設定。它不只是回答問題，也能讀寫專案檔案、執行終端指令，並根據結果繼續修正。

### OpenCode

OpenCode 是本 repo 目前的主要範例。安裝、CLI 操作、專案指示與設定都集中在 [opencode/](opencode/)；請從 [OpenCode 操作指南](opencode/README.md) 開始。

之後新增 Claude Code、Codex CLI 或 Antigravity CLI 時，建議各自建立專屬資料夾，放置該工具的安裝、操作、專案規則與設定方式。跨工具共通的 Git 或終端機內容則留在共用章節，避免重複維護。

## ADE：管理多個 agent 工作階段

ADE 是 **Agentic Development Environment** 的縮寫，可理解為以 agent 工作流程為中心的開發環境。這是正在發展中的工具類別；不同專案可能是 TUI、桌面程式或其他介面，因此本 repo 會介紹實際功能，不把它限定成單一介面或已定型的標準。

### Herdr

Herdr 是終端機內的 agent multiplexer，可用 workspace、tab 和 pane 管理 agent 與 shell，查看工作狀態，並在離開後重新連回工作階段。它負責管理工作空間與工作階段；實際撰寫程式的仍是你在其中啟動的 OpenCode、Claude Code 等 agent。

Herdr 的安裝與操作請看 [herdr/README.md](herdr/README.md)，進階內容包含 [CLI](herdr/cli.md)、[OpenCode 整合](herdr/opencode-integration.md)與[更新紀錄](herdr/updates.md)。

### 其他 ADE 候選

- [AGTx](https://github.com/fynnfluegge/agtx)：以「coding agents 的黑板」為定位，支援多種 coding agent。搜尋時 GitHub 顯示約 1.7k stars，是目前值得優先評估的熱門候選。
- [Termio](https://github.com/termio-sh/termio)：定位為 terminal-first ADE，支援多種 CLI agent；可以觀察它是否適合作為 Herdr 的補充或比較對象。

GitHub stars 和功能都會變動。新增正式教學前，先確認專案仍有維護、安裝方式可用，並實際走過一次新手流程。

## 終端機工具

### Yazi：終端機檔案管理器

Yazi 是終端機內的檔案管理器，可用鍵盤瀏覽目錄及預覽檔案。安裝和基本操作請看 [yazi/README.md](yazi/README.md)。

Yazi 的外掛、預覽器和相依工具可能需要逐一設定。本 repo 的教學會示範如何請 AI coding agent 檢查環境、依官方說明安裝及設定，再由使用者確認結果；開始前先讓 agent 列出它預計執行的命令，遇到系統套件或權限變更時逐項檢視。

### Git 與 worktree：同一個 repo 的多個工作目錄

Git 是 AI 開發工作流程的重要基礎：它讓你檢查 agent 改了什麼、保存一個可回復的版本，也能把不同任務分開處理。`git worktree` 可讓同一個 Git repo 同時有多個工作目錄，各自切換分支，不需要為每個任務重新 clone 一份 repo。

本 repo 建議新手把 worktree 放在目前 repo 根目錄下的 `.worktrees/`，並把這個目錄加入 `.gitignore`。這樣工作目錄集中在專案旁邊，又不會被當成專案內容提交。若團隊有統一的工作目錄規範，也可以改放到 repo 外的專用資料夾。

```text
my-project/                 # 主要工作目錄（clone）
├── .git/
├── .gitignore              # 忽略 .worktrees/
├── src/
└── .worktrees/
    ├── feature-login/      # feature/login 分支的獨立工作目錄
    └── fix-header/         # fix/header 分支的獨立工作目錄
```

建立範例：

```bash
mkdir -p .worktrees
git worktree add .worktrees/feature-login -b feature/login
git worktree list
```

`.worktrees/` 是每個 repo 的本機工作資料夾，不要把它加入 Git 版本控制。worktree 使用完後，先確認改動已提交或已妥善保存，再用 `git worktree remove .worktrees/feature-login` 移除工作目錄。詳細教學之後可整理在 `git/` 資料夾，涵蓋 branch、worktree、agent 平行工作、衝突處理與清理流程。

## 目錄規劃

```text
.
├── README.md                 # 導覽、分類與新手學習路徑
├── opencode/                 # OpenCode 安裝、操作與設定
├── herdr/                    # Herdr 安裝、操作與 agent 整合
├── yazi/                     # Yazi 安裝、操作與外掛
└── git/                      # 建議新增：Git、branch、worktree 與協作流程
```

每個工具的專屬操作放在自己的資料夾；README 保留總覽、工具間的關係和學習順序。遇到共通概念（例如 Git、終端機路徑、shell）則集中在共用資料夾，讓新人能先理解再照著工具指南操作。
