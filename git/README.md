# Git 與 Worktree：AI Agent 平行開發指南

Git 是 AI 開發工作流程的重要基礎：它讓你檢查 agent 改了什麼、保存可回復的版本，並將不同任務分開處理。搭配 `git worktree`，同一個 Git repo 可以同時擁有多個獨立的工作目錄，各自切換分支，不需要為每個任務重新 clone 整個專案。

---

## 1. 為什麼 AI Coding 需要 Worktree？

當你同時讓多個 AI coding agent 處理不同任務時：
- **避免互相干擾**：每個 agent 在各自的獨立目錄中讀寫檔案，不會發生檔案被覆蓋或編輯衝突。
- **節省磁碟空間**：所有 worktree 共用同一個 `.git` 物件資料庫，省去重複 clone 的時間與空間。
- **無縫切換與審查**：可以在主目錄維持穩定代碼，在個別 worktree 中讓 agent 進行實驗或功能開發。

---

## 2. 建議目錄結構

建議將 worktree 集中放在專案根目錄下的 `.worktrees/`，並加入 `.gitignore`，這樣目錄結構清楚又不會誤提交：

```text
my-project/                 # 主要工作目錄（clone）
├── .git/
├── .gitignore              # 忽略 .worktrees/
├── src/
└── .worktrees/
    ├── feature-login/      # feature/login 分支的獨立工作目錄
    └── fix-header/         # fix/header 分支的獨立工作目錄
```

> [!TIP]
> 記得在專案根目錄的 `.gitignore` 中加入 `.worktrees/`，避免本機工作目錄被提交進版本控制。

---

## 3. 常用操作指令

### 3.1 建立 Worktree

建立存放目錄，並建立新分支與對應工作目錄：

```bash
# 確保存放目錄存在
mkdir -p .worktrees

# 建立 feature/login 分支並掛載到 .worktrees/feature-login
git worktree add .worktrees/feature-login -b feature/login
```

### 3.2 檢視現有的 Worktree

列出目前所有的工作目錄及其對應分支：

```bash
git worktree list
```

輸出範例：
```text
/path/to/my-project                    abc1234 [main]
/path/to/my-project/.worktrees/feature-login  def5678 [feature/login]
```

### 3.3 讓 Agent 在 Worktree 中工作

進入該目錄後啟動 AI Agent（例如 OpenCode）：

```bash
cd .worktrees/feature-login
opencode
```

Agent 的所有讀寫、執行與 Git 操作都會完全隔離在這個目錄中。

### 3.4 完成任務與清理 Worktree

當功能完成、代碼已 commit 並 merge 回主分支後，即可移除工作目錄：

```bash
# 安全移除指定 worktree
git worktree remove .worktrees/feature-login

# 整理已過期的 worktree 參照
git worktree prune
```

---

## 4. 最佳實踐與注意事項

1. **先 commit 再清理**：在執行 `git worktree remove` 前，請務必確認分支上的進度已提交或推送。
2. **不要手動用 `rm -rf` 刪除**：手動刪除目錄會留下 Git 的中繼狀態紀錄，建議優先使用 `git worktree remove`。若已不小心手動刪除，請執行 `git worktree prune` 修理中繼狀態。
3. **搭配 Herdr 分頁**：在 Herdr 的不同 tab/pane 開啟不同 worktree，就能在一個終端機介面中同時監督多個 agent 的工作進度。
4. **Commit 漏改時善用 Amend**：若 Agent 剛建立 commit 卻發現漏加了檔案或內容，可直接請 Agent「修改後使用 `git commit --amend` 合併進前一個 commit」，避免產生零碎的修復紀錄，保持版本歷史整潔。

