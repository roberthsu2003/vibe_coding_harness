# 📚 參考：指令速查與疑難排解

> 📚 參考　｜　[章節首頁](README.md)

本頁以 Git 2.55 實測為準。

> 遇到錯誤時，最簡單的做法是把訊息貼給 AI：「我看到這個錯誤，請說明原因，先不要修改任何檔案。」

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
| 看有哪些被忽略的檔案 | `git status --ignored` | 任何地方 |
| 預覽要合併的 commit | `git log main..<分支> --oneline` | 母目錄 |
| 合併進 main | `git merge <分支>` | ⚠️ **母目錄** |
| 把 main 同步進分支 | `git merge main` | worktree |
| 放棄進行中的合併 | `git merge --abort` | 合併所在的位置 |
| 復原剛完成、還沒 push 的合併 | `git reset --merge ORIG_HEAD` | 母目錄 |
| 復原已 push 的合併 | `git revert -m 1 HEAD` | 母目錄 |
| 移除 worktree | `git worktree remove <路徑>` | 母目錄 |
| 刪除已合併的分支 | `git branch -d <分支>` | 母目錄 |
| 清掉失效的 worktree 紀錄 | `git worktree prune` | 母目錄 |

---

## 2. 疑難排解

Git 的訊息會依介面語言顯示英文或中文，兩種都列出來方便你搜尋。

| 錯誤訊息或狀況 | 原因與解法 |
| :--- | :--- |
| `'main' is already used by worktree at`<br>`「main」已被位於…的工作區使用` | 同一條分支不能同時在兩個 worktree 使用。最常見的是在 worktree 裡想切換到 main 合併，請回母目錄再合併 |
| `contains modified or untracked files, use --force`<br>`包含修改或未追蹤的檔案，使用 --force 刪除` | worktree 裡還有未 commit 的改動。先 commit 或確認不要了，再移除。**不要沒看內容就加 `--force`** |
| `cannot delete branch … used by worktree`<br>`無法刪除被位於…的工作區使用的分支` | worktree 還在。先移除 worktree，再刪除分支 |
| `the branch … is not fully merged`<br>`分支…沒有完全合併` | 分支還有 commit 沒合併。先合併，**不要**直接用 `-D` |
| `is a missing but already registered worktree`<br>`是個遺失但已註冊的工作區` | 資料夾被刪了但紀錄還在。先執行 `git worktree prune`，見[情境 B](05-scenarios.md#情境-b不小心刪掉了-worktree-資料夾) |
| `CONFLICT`<br>`衝突（內容）`；`git status` 裡的 `both modified`／`雙方修改` | 合併衝突，見 [04 合併與衝突](04-merge-conflict.md#4-處理衝突) |
| `Already up to date`／`已經是最新的`，但改動沒回來 | 這次合併之前可能被 revert 過，見[合併完才發現不對](04-merge-conflict.md#6-合併完才發現不對) |
| `git merge` 後跳出編輯器 | 正在確認合併訊息，不是當機。nano 按 `Ctrl+X`；Vim 輸入 `:wq` 按 `Enter` |
| 新 worktree 跑不起來、少了 `.env` | 被忽略的檔案不會帶過去，見[情境 C](05-scenarios.md#情境-c新的-worktree-跑不起來) |
| 移除 worktree 後 `.env` 不見了 | 被忽略的檔案會直接刪除，不會警告。移除前先用 `git status --ignored` 檢查 |
| 新 worktree 裡沒有 `.gitignore` | `.gitignore` 還沒 commit。回母目錄 commit 後，在 worktree 裡 `git merge main` |
| `git status` 出現 `.worktrees/` | `.gitignore` 沒有寫 `.worktrees/`，加上即可 |
| 已經把 `.worktrees/` commit 進去了 | 加入 `.gitignore` 後執行 `git rm -r --cached .worktrees/`，再 commit（不會刪掉磁碟上的檔案） |
| 手動刪掉資料夾後 `worktree list` 還看得到，後面標示 `prunable` | 執行 `git worktree prune` |
| 建立 worktree 時出現 `inferring '--orphan'`<br>`推測為「--orphan」` | 專案還沒有任何 commit，先做第一次 commit 再建立 |
