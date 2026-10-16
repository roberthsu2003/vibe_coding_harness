# 📚 參考：指令速查與疑難排解

> 📚 參考　｜　[章節首頁](README.md)

本頁以 Git 2.55 實測為準。

---

## 1. 指令速查

| 想做的事 | 指令 | 在哪裡執行 |
| :--- | :--- | :--- |
| 建立 worktree 和新分支 | `git worktree add <路徑> -b <新分支>` | 母目錄 |
| 用現有分支建立 worktree | `git worktree add <路徑> <現有分支>` | 母目錄 |
| 列出所有 worktree | `git worktree list` | 任何地方 |
| 我在哪個資料夾？ | `git rev-parse --show-toplevel` | 任何地方 |
| 我在哪個分支？ | `git branch --show-current` | 任何地方 |
| 是母目錄還是 worktree？ | `git rev-parse --git-dir` | 任何地方 |
| 預覽要合併的 commit | `git log main..<分支> --oneline` | 母目錄 |
| 合併 | `git merge <分支>` | ⚠️ **母目錄** |
| 放棄合併 | `git merge --abort` | 母目錄 |
| 移除 worktree | `git worktree remove <路徑>` | 母目錄 |
| 刪除已合併的分支 | `git branch -d <分支>` | 母目錄 |
| 清掉失效的 worktree 紀錄 | `git worktree prune` | 母目錄 |

---

## 2. 疑難排解

| 錯誤訊息或狀況 | 原因與解法 |
| :--- | :--- |
| `fatal: '...' is already used by worktree at '...'`<br>（中文：「已被位於…的工作區使用」） | 同一條分支不能同時在兩個 worktree 使用。最常見的是在 worktree 裡想切換到 main 合併——請 `cd` 回母目錄再 `git merge` |
| `git status` 出現 `.worktrees/` | `.gitignore` 沒有寫 `.worktrees/`，加上即可 |
| 已經把 `.worktrees/` commit 進去了 | 加入 `.gitignore` 後執行 `git rm -r --cached .worktrees/`，再 commit（不會刪掉磁碟上的檔案） |
| `git worktree remove` 被拒絕 | worktree 裡還有未 commit 的改動。先 commit 或確認不要了，再移除 |
| `git branch -d` 出現 `not fully merged` | 分支還有 commit 沒合併。先合併，**不要**直接用 `-D` |
| 手動刪掉資料夾後 `worktree list` 還看得到 | 執行 `git worktree prune` |
| 合併時出現 `CONFLICT` | 見 [04 合併與衝突](04-merge-conflict.md#4-處理衝突) |
