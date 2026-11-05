# 07　實戰情境

> ★★★ 深入　｜　[← 06 Worktree 完整流程](06-worktree-lifecycle.md)　｜　[章節首頁](README.md)　｜　📚 [指令速查與疑難排解](reference.md)

**這一站你會學到**：八種在 AI 開發中常見的狀況，以及最省事的處理方式。

| 主題 | 情境 |
| :--- | :--- |
| **Branch** | [A. AI 直接改在 main 上](#情境-aai-直接改在-main-上)　｜　[B. 切換分支被擋下](#情境-b切換分支被擋下)　｜　[C. 刪錯分支](#情境-c刪錯分支) |
| **Worktree** | [D. 緊急修 bug](#情境-d功能做到一半突然要緊急修-bug)　｜　[E. 誤刪 worktree](#情境-e不小心刪掉了-worktree-資料夾)　｜　[F. 新 worktree 跑不起來](#情境-f新的-worktree-跑不起來)　｜　[H. 搭配 Herdr](#情境-h搭配-herdr同時指揮多個-ai) |
| **兩者都會遇到** | [G. Commit 漏了檔案](#情境-gai-剛-commit-完才發現漏了檔案) |

---

## 情境 A：AI 直接改在 main 上

> 老闆要換首頁大圖。你說完需求才發現忘了開分支，AI 已經直接改在 main 上了。

先看改動有沒有 commit，兩種救法不一樣。

**還沒 commit：** 改動還沒有跟著 main 被存下來，開新分支時會一起帶過去。

```text
剛才的改動不小心做在 main 上，還沒 commit。請開一條新分支 feature/hero，把這些改動帶過去並 commit，然後確認 main 沒有變動。
```

**已經 commit、還沒 push：**

```text
剛才的 commit 不小心做在 main 上，還沒 push。請把它移到一條新分支 feature/hero，讓 main 回到改動之前。動手前先告訴我會移動哪些 commit，等我同意。
```

> [!WARNING]
> **已經 push 了，就不要退回 main**，否則會和 GitHub 上的版本對不起來。請告訴 AI 已經 push 了，改用新的 commit 抵銷，做法和[復原已 push 的合併](03-merge-conflict.md#6-合併完才發現不對)類似。

## 情境 B：切換分支被擋下

> 你請 AI 改首頁標語，改到一半想切去看菜單分支，Git 拒絕切換：

```text
error: Your local changes to the following files would be overwritten by checkout:
	index.html
Please commit your changes or stash them before you switch branches.
```

```text
錯誤: 您對下列檔案的本機修改將被簽出動作覆蓋：
	index.html
請在切換分支前提交或貯存您的修改。
```

這是 Git 在保護你還沒 commit 的改動。對 AI 說：

```text
切換分支被擋下了。請告訴我還沒 commit 的改動是什麼，建議我該 commit、先暫存還是放棄，等我決定再處理。
```

> 如果改動已經告一段落，直接 commit 最簡單，不容易忘記。

## 情境 C：刪錯分支

> 上週刪掉 `experiment/dark-theme`，今天老闆說：「那個深色主題，客人好像滿喜歡的。」或者你剛才強制刪除時，刪錯了分支。

已經 commit 的內容通常還救得回來，越早處理越好：

```text
我想救回被刪除的 experiment/dark-theme 分支。請從刪除訊息或 Git 的操作紀錄（reflog）找出它最後一個 commit，用它重新建立分支，建立前先讓我確認內容。
```

> ⚠️ 沒有 commit 過的改動救不回來。Git 也會定期清理沒有分支指向的 commit，時間拖太久就可能找不到。

## 情境 D：功能做到一半，突然要緊急修 bug

> 會員登入做到一半，老闆打來：「客人一登入，網站就當機！」

**以前的做法**：把改到一半的檔案先藏起來（`git stash`），修完再拿回來，常常發生衝突。

**用 worktree**：原本的資料夾完全不動，對母目錄的 AI 說：

```text
我要緊急修登入當機的 bug。請從 main 建立一個新的 worktree 來修，分支叫 hotfix/auth-crash，放在 .worktrees/hotfix-auth，需要的 .env 和套件也準備好。
```

然後開新視窗，用 `opencode .worktrees/hotfix-auth` 進去讓 AI 修 bug，commit 後回母目錄合併。

## 情境 E：不小心刪掉了 worktree 資料夾

> 你覺得 `.worktrees/` 裡的檔案太亂，順手刪掉了 `feature-login`，才想起登入還沒做完。

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

## 情境 F：新的 worktree 跑不起來

> 主資料夾的網站跑得好好的，新 worktree 卻一啟動就出現找不到模組、缺少環境變數。

這通常是被忽略的檔案沒有帶過來（見 [05 站](05-worktree-structure.md#3-什麼隔離了什麼還是共用)）。對 worktree 裡的 AI 說：

```text
這個 worktree 跑不起來。請比對母目錄，看是不是少了 .env 或還沒安裝套件，然後幫我補齊。
```

## 情境 G：AI 剛 commit 完，才發現漏了檔案

> AI 做完會員登入並 commit，你一看才發現測試檔沒有放進去。

不需要再多一個「補檔案」的 commit，直接請 AI：

```text
剛才的 commit 漏掉了 tests/test_login.py，請把它加進來，合併進前一個 commit。
```

> ⚠️ 這個做法（`git commit --amend`）只適合**還沒 push** 的 commit。已經 push 的 commit 改用新的 commit 補上。

## 情境 H：搭配 Herdr，同時指揮多個 AI

> 老闆想同時推出會員登入和線上付款，你想一個人管兩個 AI。

| Herdr 分頁 | 位置 | 做什麼 |
| :--- | :--- | :--- |
| 分頁 1 | 母目錄 | 維護 main、最後合併 |
| 分頁 2 | `.worktrees/feature-login` | OpenCode 寫登入功能 |
| 分頁 3 | `.worktrees/feature-pay` | 另一個 AI 寫付款功能 |

看 Herdr 側欄的狀態燈號（🟡 工作中、🔴 等你回應、🟢 做完了），一個人就能同時管好幾個 AI。

> 想讓主管 AI 自動完成這整套流程？見 [Herdr 動手練習第 5 關](../herdr/practice/05-parallel-worktrees/README.md)。

---

## ✅ 自我檢查

- [ ] 發現 AI 改在 main 上時，知道先確認有沒有 commit、有沒有 push
- [ ] 知道切換分支被擋下時，Git 在保護什麼
- [ ] 知道刪錯分支後，什麼救得回來、什麼救不回來
- [ ] 能用 worktree 處理「做到一半要修 bug」
- [ ] 知道刪掉 worktree 資料夾後，哪些內容救得回來
- [ ] 知道新 worktree 跑不起來時先檢查什麼
- [ ] 知道 `--amend` 只適合還沒 push 的 commit

---

## 進階（選修）：自己打指令

```bash
# 情境 A：改動還沒 commit，帶到新分支
git switch -c feature/hero
git add .
git commit -m "feat: 更換首頁大圖"

# 情境 A：已經 commit、還沒 push，移到新分支（這裡以移動 1 個 commit 為例）
git branch feature/hero                # 先讓新分支指向目前的 commit
git reset --keep HEAD~1                # main 退回 1 個 commit

# 情境 C：救回刪除的分支
git reflog                             # 找出分支最後一個 commit 的編號
git branch experiment/dark-theme <commit 編號>

# 情境 D：建立修 bug 用的 worktree
git worktree add .worktrees/hotfix-auth -b hotfix/auth-crash main
cp .env .worktrees/hotfix-auth/        # 有 .env 才需要

# 情境 E：清掉失效的紀錄，再用原本的分支重建
git worktree prune
git worktree add .worktrees/feature-login feature/login
```

> 情境 C：刪除分支時，訊息裡的 `(was a035bc3)` 就是 commit 編號，有留著的話不用查 reflog。

> 情境 E 如果沒先執行 `prune`，重建時會出現 `missing but already registered worktree`。

> 🎉 完成 Branch 與 Worktree 章節！遇到問題時查閱 [指令速查與疑難排解](reference.md)。
