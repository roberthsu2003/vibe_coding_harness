# 05　實戰情境

> ★★★ 深入　｜　[← 04 合併與衝突](04-merge-conflict.md)　｜　[章節首頁](README.md)　｜　📚 [指令速查與疑難排解](reference.md)

**這一站你會學到**：四種在 AI 開發中常見的情況，以及最省事的處理方式。

---

## 情境 A：功能做到一半，突然要緊急修 bug

**以前的做法**：`git stash` 把改到一半的檔案先藏起來，修完再拿回來，常常發生衝突。

**用 worktree**：原本的資料夾完全不動，另開一個 worktree 修 bug：

```bash
git worktree add .worktrees/hotfix-auth -b hotfix/auth-crash
cd .worktrees/hotfix-auth
opencode          # 讓 AI 修 bug，commit 後回母目錄合併
```

## 情境 B：不小心用 `rm -rf` 刪掉了 worktree 資料夾

`git worktree list` 還是會列出它。執行：

```bash
git worktree prune
```

Git 會自動清掉「資料夾已經不存在」的 worktree 紀錄。

> 正確的刪除方式是 `git worktree remove .worktrees/名稱`，Git 會一併處理紀錄。

## 情境 C：AI 剛 commit 完，才發現漏了檔案

不需要再多一個「補檔案」的 commit，直接請 AI：

```text
剛才的 commit 漏掉了 tests/test_login.py，請把它加進來，用 git commit --amend 合併進前一個 commit。
```

> ⚠️ `--amend` 只適合**還沒 push** 的 commit。已經 push 的 commit 改用新的 commit 補上。

## 情境 D：搭配 Herdr，同時指揮多個 AI

| Herdr 分頁 | 位置 | 做什麼 |
| :--- | :--- | :--- |
| 分頁 1 | 母目錄 | 維護 main、最後合併 |
| 分頁 2 | `.worktrees/feature-login` | OpenCode 寫登入功能 |
| 分頁 3 | `.worktrees/feature-pay` | 另一個 AI 寫付款功能 |

看 Herdr 側欄的狀態燈號（🟡 工作中、🔴 等你回應、🟢 做完了），一個人就能同時管好幾個 AI。

> 想讓主管 AI 自動完成這整套流程？見 [Herdr 動手練習第 5 關](../herdr/practice/05-parallel-worktrees/README.md)。

---

## ✅ 自我檢查

- [ ] 能用 worktree 處理「做到一半要修 bug」
- [ ] 知道 `git worktree prune` 什麼時候用
- [ ] 知道 `--amend` 只適合還沒 push 的 commit

> 🎉 完成 Git 與 Worktree 章節！遇到問題時查閱 [指令速查與疑難排解](reference.md)。
