# 05　實戰情境

> ★★★ 深入　｜　[← 04 合併與衝突](04-merge-conflict.md)　｜　[章節首頁](README.md)　｜　📚 [指令速查與疑難排解](reference.md)

**這一站你會學到**：五種在 AI 開發中常見的情況，以及最省事的處理方式。

---

## 情境 A：功能做到一半，突然要緊急修 bug

**以前的做法**：把改到一半的檔案先藏起來（`git stash`），修完再拿回來，常常發生衝突。

**用 worktree**：原本的資料夾完全不動，對母目錄的 AI 說：

```text
我要緊急修登入當機的 bug。請從 main 建立一個新的 worktree 來修，放在 .worktrees/ 底下，需要的 .env 和套件也準備好。
```

然後開新視窗，用 `opencode .worktrees/hotfix-auth` 進去讓 AI 修 bug，commit 後回母目錄合併。

## 情境 B：不小心刪掉了 worktree 資料夾

先別慌，看你的工作有沒有 commit 過：

| 內容 | 還在嗎 |
| :--- | :--- |
| ✅ 已經 commit 的 | **還在**，它們存在分支上 |
| ❌ 沒有 commit 的 | **救不回來**，所以做完一段就要 commit |

對母目錄的 AI 說：

```text
我不小心刪掉 .worktrees/feature-login 資料夾了。請清掉失效的 worktree 紀錄，再用原本的分支把它重新建立回來。
```

不需要這個 worktree 了，就只要說「請清掉失效的 worktree 紀錄」。

> 下次要刪除時，請 AI「移除這個 worktree」，不要直接刪資料夾。

## 情境 C：新的 worktree 跑不起來

出現找不到模組、缺少環境變數這類錯誤時，通常是被忽略的檔案沒有帶過來（見 [02 站](02-structure.md#3-什麼隔離了什麼還是共用)）。對 worktree 裡的 AI 說：

```text
這個 worktree 跑不起來。請比對母目錄，看是不是少了 .env 或還沒安裝套件，然後幫我補齊。
```

## 情境 D：AI 剛 commit 完，才發現漏了檔案

不需要再多一個「補檔案」的 commit，直接請 AI：

```text
剛才的 commit 漏掉了 tests/test_login.py，請把它加進來，合併進前一個 commit。
```

> ⚠️ 這個做法（`git commit --amend`）只適合**還沒 push** 的 commit。已經 push 的 commit 改用新的 commit 補上。

## 情境 E：搭配 Herdr，同時指揮多個 AI

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
- [ ] 知道刪掉 worktree 資料夾後，哪些內容救得回來
- [ ] 知道新 worktree 跑不起來時先檢查什麼
- [ ] 知道 `--amend` 只適合還沒 push 的 commit

---

## 進階（選修）：自己打指令

```bash
# 情境 A：建立修 bug 用的 worktree
git worktree add .worktrees/hotfix-auth -b hotfix/auth-crash main
cp .env .worktrees/hotfix-auth/        # 有 .env 才需要

# 情境 B：清掉失效的紀錄，再用原本的分支重建
git worktree prune
git worktree add .worktrees/feature-login feature/login
```

> 情境 B 如果沒先執行 `prune`，重建時會出現 `missing but already registered worktree`。

> 🎉 完成 Git Worktree 章節！遇到問題時查閱 [指令速查與疑難排解](reference.md)。
